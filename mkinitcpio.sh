#!/bin/sh

NAME="induction"
WORK_DIR="work"
INSTALL_DIR="install"

ARCH="`uname -m`"
FULLNAME="/opt/${NAME}-${ARCH}.iso"

PACKAGES="`cat packages.list`"
KVER_FILE="${WORK_DIR}/root-image/etc/mkinitcpio.d/kernel26.kver"

mkinitcpio -v -c "mkinitcpio.conf" -b "${WORK_DIR}/root-image" -k "`cat ${KVER_FILE} | grep "^ALL_kver='" | sed "s|ALL_kver='||" | sed "s|'||"`" -g "${WORK_DIR}/iso/${INSTALL_DIR}/boot/${ARCH}/archiso.img"

rm -f "${FULLNAME}"

./mkarchiso -v -L "${NAME}" -D "${INSTALL_DIR}" -c "xz" iso "${WORK_DIR}" "${FULLNAME}"
