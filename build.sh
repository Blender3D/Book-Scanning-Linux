#!/bin/sh

NAME="induction"
WORK_DIR="work"
INSTALL_DIR="install"

ARCH="`uname -m`"
FULLNAME="/opt/${NAME}-${ARCH}.iso"

PACKAGES="`cat packages.list`"
KVER_FILE="${WORK_DIR}/root-image/etc/mkinitcpio.d/kernel26.kver"

mkarchiso -v -D "${INSTALL_DIR}" -p "${PACKAGES}" create "${WORK_DIR}"

mkdir -p "${WORK_DIR}/iso/${INSTALL_DIR}/boot/${ARCH}"
cp "${WORK_DIR}/root-image/boot/System.map26" "${WORK_DIR}/iso/${INSTALL_DIR}/boot/${ARCH}/"
cp "${WORK_DIR}/root-image/boot/vmlinuz26" "${WORK_DIR}/iso/${INSTALL_DIR}/boot/${ARCH}/"

mkdir -p "${WORK_DIR}/iso/${INSTALL_DIR}/boot/${ARCH}/"
mkdir -p "${WORK_DIR}/iso/syslinux"
mkdir -p "${WORK_DIR}/iso/${INSTALL_DIR}/syslinux"

cp -r "${WORK_DIR}/root-image/boot" "${WORK_DIR}/iso/"
cp -r "boot-files/"* "${WORK_DIR}/iso/"
cp -r "boot-files/"* "${WORK_DIR}/iso/boot/"

cp -PR "${WORK_DIR}/root-image/usr/lib/syslinux/"*.c32 "${WORK_DIR}/iso/syslinux/"
cp -PR "${WORK_DIR}/root-image/usr/lib/syslinux/isolinux.bin" "${WORK_DIR}/iso/syslinux/"

sed "s|%ARCHISO_LABEL%|${NAME}|g" -i "${WORK_DIR}/iso/syslinux/syslinux.cfg"
sed "s|%INSTALL_DIR%|${INSTALL_DIR}|g" -i "${WORK_DIR}/iso/syslinux/syslinux.cfg"
sed "s|%ARCH%|${ARCH}|g;" -i "${WORK_DIR}/iso/syslinux/syslinux.cfg"

cp -PRrf "${WORK_DIR}/iso/syslinux/"* "${WORK_DIR}/iso/${INSTALL_DIR}/syslinux/"

mkinitcpio -v -c "mkinitcpio.conf" -b "${WORK_DIR}/root-image" -k "`cat ${KVER_FILE} | grep "^ALL_kver='" | sed "s|ALL_kver='||" | sed "s|'||"`" -g "${WORK_DIR}/iso/${INSTALL_DIR}/boot/${ARCH}/archiso.img"

cp -r "overlay" "${WORK_DIR}/"
sed "s|@ARCH@|${ARCH}|g" isomounts > "${WORK_DIR}/iso/${INSTALL_DIR}/isomounts"

mkarchiso -v -L "${NAME}" -D "${INSTALL_DIR}" -c "xz" iso "${WORK_DIR}" "${FULLNAME}"

#rm -rf "${WORK_DIR}" "${FULLNAME}"
