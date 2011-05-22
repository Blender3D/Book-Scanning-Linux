#!/bin/sh

NAME="induction"
WORK_DIR="work"
INSTALL_DIR="install"

ARCH="`uname -m`"
FULLNAME="/opt/${NAME}-${ARCH}.iso"

mkdir -p "${WORK_DIR}/iso/${INSTALL_DIR}/boot/${ARCH}"
cp -f "${WORK_DIR}/root-image/boot/System.map26" "${WORK_DIR}/iso/${INSTALL_DIR}/boot/${ARCH}/"
cp -f "${WORK_DIR}/root-image/boot/vmlinuz26" "${WORK_DIR}/iso/${INSTALL_DIR}/boot/${ARCH}/"

mkdir -p "${WORK_DIR}/iso/${INSTALL_DIR}/boot/${ARCH}/"
mkdir -p "${WORK_DIR}/iso/syslinux"
mkdir -p "${WORK_DIR}/iso/${INSTALL_DIR}/syslinux"

cp -rf "${WORK_DIR}/root-image/boot" "${WORK_DIR}/iso/"
cp -rf "boot-files/"* "${WORK_DIR}/iso/"
cp -rf "boot-files/"* "${WORK_DIR}/iso/boot/"

cp -PRf "${WORK_DIR}/root-image/usr/lib/syslinux/"*.c32 "${WORK_DIR}/iso/syslinux/"
cp -PRf "${WORK_DIR}/root-image/usr/lib/syslinux/isolinux.bin" "${WORK_DIR}/iso/syslinux/"

sed "s|%ARCHISO_LABEL%|${NAME}|g" -i "${WORK_DIR}/iso/syslinux/syslinux.cfg" -i "${WORK_DIR}/iso/boot/syslinux/syslinux.cfg"
sed "s|%INSTALL_DIR%|${INSTALL_DIR}|g" -i "${WORK_DIR}/iso/syslinux/syslinux.cfg" -i "${WORK_DIR}/iso/boot/syslinux/syslinux.cfg"
sed "s|%ARCH%|${ARCH}|g;" -i "${WORK_DIR}/iso/syslinux/syslinux.cfg" -i "${WORK_DIR}/iso/boot/syslinux/syslinux.cfg"

cp -PRrf "${WORK_DIR}/iso/syslinux/"* "${WORK_DIR}/iso/${INSTALL_DIR}/syslinux/"
cp -PRrf "${WORK_DIR}/iso/syslinux/"* "${WORK_DIR}/iso/boot/syslinux/"

rm -Rf "${WORK_DIR}/overlay/"
rm -f ${FULLNAME}

cp -r "overlay" "${WORK_DIR}/"

mkarchiso -v -f -L "${NAME}" -D "${INSTALL_DIR}" -c "xz" iso "${WORK_DIR}" "${FULLNAME}"
