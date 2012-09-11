#!/bin/env python2

import os, shutil, sys, platform, subprocess, datetime, errno, glob, urllib2, pwd, grp

date = datetime.datetime.now()

iso_name = 'BSL'
iso_label = 'BOOK_SCANNING_LINUX_' + date
iso_version = date.strftime('%Y.%m.%d')
install_dir = 'book_scanning_linux'
arch = platform.machine()
work_dir = 'work'
out_dir = 'out'

verbose = '-v'

script_path = os.getcwd()

def install_packages(packages):
    return subprocess.check_call(['mkarchiso', verbose, '-w' work_dir, '-D', install_dir, '-p', ' '.join(packages), 'create'])


def download_file(url):
    return urllib2.urlopen(url).read()


def mkdir_p(path):
    try:
        os.makedirs(path)
    except OSError as exception:
        if exception.errno != errno.EEXIST:
            raise

# Base installation (root-image)
def make_basefs():
    install_packages(['base'])
    install_packages(['memtest86+', 'syslinux', 'mkinitcpio-nfs-utils', 'nbd', 'curl'])

# Additional packages (root-image)
def make_packages():
    packages = []

    with open('packages.all', 'r') as handle:
        for line in handle:
            line = line.strip()

            if not line or line.startswith('#'):
                continue

            packages.append(line)

    install_packages(packages)

def make_setup_mkinitcpio():
    hooks = ['archiso', 'archiso_shutdown', 'archiso_pxe_common', 'archiso_pxe_nbd', 'archiso_pxe_http', 'archiso_pxe_nfs', 'archiso_loop_mnt']

    hook_input_dir = '/lib/initcpio/hooks/'
    hook_output_dir = os.path.join(work_dir, 'root-image/lib/initcpio/hooks')
    hook_install_dir = os.path.join(work_dir, 'root-image/lib/initcpio/hooks/install')
    
    for hook in hooks:
        hook_path = os.path.join(hook_input_dir, hook)
        shutil.copy2(hook_path, hook_output_dir)
        shutil.copy2(hook_path, hook_install_dir)

    for source, destination in [
        ('/lib/initcpio/install/archiso_kms', os.path.join(work_dir, 'root-image/lib/initcpio/install')),
        ('/lib/initcpio/archiso_shutdown', os.path.join(work_dir, 'root-image/lib/initcpio')),
        ('/lib/initcpio/archiso_pxe_nbd', os.path.join(work_dir, 'root-image/lib/initcpio')),
        ('mkinitcpio.conf', os.path.join(work_dir, 'root-image/etc/mkinitcpio-archiso.conf'))
    ]:
        shutil.copy2(source, destination)

# Prepare ${install_dir}/boot/
def make_boot():
    source = os.path.join(work_dir, 'root-image')
    destination = os.path.join(work_dir, 'iso', install_dir, boot)

    mkdir_p(os.path.join(destination, arch))

    subprocess.check_call(['mkarchroot', '-n', '-r', 'mkinitcpio -c /etc/mkinitcpio-archiso.conf -k /boot/vmlinuz-linux -g /boot/archiso.img', source])

    for _source, _destination in [
        ('boot/archiso.img', os.path.join(arch, 'archiso.img')),
        ('boot/vmlinuz-linux', os.path.join(arch, 'vmlinuz')),
        ('boot/memtest86+/memtest.bin', 'memtest'),
        ('usr/share/licenses/common/GPL2/license.txt', 'memtest.COPYING')
    ]:
        shutil.move(os.path.join(source, _source), os.path.join(destination, _destination))

# Prepare /${install_dir}/boot/syslinux
def make_syslinux():
    src_syslinux = os.path.join(work_dir, 'root-image/usr/lib/syslinux')
    dst_syslinux = os.path.join(work_dir, 'iso', install_dir, 'boot/syslinux')
    
    mkdir_p(dst_syslinux)

    for config in glob.glob(os.path.join(script_path, 'syslinux/*.cfg')):
        with open(config, 'r') as handle:
            contents = handle.read()

        for search, replace in [
            ('%ARCHISO_LABEL%', iso_label),
            ('%INSTALL_DIR%', install_dir),
            ('%ARCH%', arch)
        ]:
            contents.replace(search, replace)

        with open(os.path.join(dst_syslinux, os.path.split(config)[-1]), 'w') as handle:
            handle.write(contents)

    for filename in glob.glob(os.path.join(src_syslinux, '*')):
        name = os.path.split(filename)[-1]
        basename, extension = os.path.splitext(name)

        if extension in ['.c32', '.com', '.0'] or basename == 'memdisk':
            shutil.copy2(filename, dst_syslinux)

    mkdir_p(os.path.join(dst_syslinux, 'hdt'))

    ids = download_file('http://pciids.sourceforge.net/v2.2/pci.ids').encode('zlib')
    
    with open(os.path.join(dst_syslinux, 'hdt/pciids.gz'), 'w') as handle:
        handle.write(ids)

    for filename in glob.glob(os.path.join(work_dir, 'root-image/lib/modules/*-ARCH/modules.alias')):
        with open(filename, 'r') as handle:
            contents = handle.read().encode('zlib')

        with open(os.path.join(dst_syslinux, 'hdt/modalias.gz'), 'w') as handle:
            handle.write(contents)


# Prepare /isolinux
def make_isolinux():
    mkdir_p(os.path.join(work_dir, 'iso/isolinux'))

    with open(os.path.join(script_path, 'isolinux/isolinux.cfg'), 'r') as handle:
        contents = handle.read().replace('%INSTALL_DIR%', install_dir)

    with open(os.path.join(work_dir, 'iso/isolinux/isolinux.cfg'), 'w') as handle:
        handle.write(contents)

    for filename in ['isolinux.bin', 'isohdpfx.bin']:
        shutil.copy2(os.path.join(work_dir, 'root-image/usr/lib/syslinux/', filename), os.path.join(work_dir), 'iso/isolinux/')

def make_customize_root_image():
    shutil.copytree(os.path.join(script_path, 'root-image'), work_dir)

    os.chmod(os.path.join(work_dir, 'root-image/etc/sudoers.d'), 0750)
    os.chmod(os.path.join(work_dir, 'root-image/etc/sudoers.d/g_wheel'), 0440)

    path = os.path.join(work_dir, 'root-image/etc/')
    args = (pwd.getpwnam('root').pw_uid, pwd.getpwnam('root').pw_gid)
    chown = lambda root, f: os.chown(os.path.join(root, f), *args)

    for root, dirs, files in os.walk(path)):
        for f in dirs + files:
            chown(root, f)
            
    
    mkdir_p(os.path.join(work_dir, 'root-image/etc/pacman.d'))
    
    with open(os.path.join(work_dir, 'root-image/etc/pacman.d/mirrorlist'), 'w') as handle:
        mirrorlist = download_file('http://www.archlinux.org/mirrorlist/all/')
        mirrorlist.replace('#Server', 'Server')

        handle.write(mirrorlist)
    
    subprocess.check_call(['chroot', os.path.join(work_dir, 'root-image'), 'post-install'])


def make_lib_modules():
    shutil.move(os.path.join(work_dir, 'root-image/lib/modules'), os.path.join(work_dir, 'lib-modules'))

def make_usr_share():
    shutil.move(os.path.join(work_dir, 'root-image/usr/share'), os.path.join(work_dir, 'usr-share'))


# Process aitab
# args: $1 (core | netinstall)
def make_aitab():
    aitab = os.path.join(script_path, 'aitab')

    with open(aitab, 'r') as handle:
        contents = handle.read()
        contents.replace('%ARCH%', arch)

    with open(os.path.join(work_dir, 'iso', install_dir, 'aitab'), 'w') as handle:
        handle.write(contents)

# Build all filesystem images specified in aitab (.fs .fs.sfs .sfs)
def make_prepare():
    return subprocess.check_call(['mkarchiso', '-v', '-w', work_dir, '-D', install_dir, 'prepare'])

# Build ISO
# args: $1 (core | netinstall)
def make_iso():
    subprocess.check_call(['mkarchiso', '-v', '-w', work_dir, '-D', install_dir, 'checksum'])
    subprocess.check_call(['mkarchiso', '-v', '-w', work_dir, '-D', install_dir, '-L', iso_label, '-o', out_dir, 'iso', '{}-{}-{}.iso'.format(iso_name, iso_version, arch)])

def clean_single():
    return shutil.rmtree(work_dir)

build_steps = [
    make_basefs,
    make_packages,
    make_setup_mkinitcpio,
    make_boot,
    make_syslinux,
    make_isolinux,
    make_customize_root_image,
    make_lib_modules,
    make_usr_share,
    make_aitab,
    make_prepare,
    make_iso
]

if __name__ == '__main__':
    for step in build_steps:
        raw_input('FOO')
        step()