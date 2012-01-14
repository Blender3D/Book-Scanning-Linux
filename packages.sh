#!/bin/bash

set -e -u

for package in $(grep -v ^# packages.aur); do
    mkdir $package
    cd $package
    wget http://aur.archlinux.org/packages/$package/$package.tar.gz
    tar -xf $package.tar.gz
    cd $package
    makepkg
    cd ../..
    cp $package/$package/*.tar.xz ./packages/
    rm -Rf $package
done

cd ./packages
repo-add induction.db.tar.gz *.pkg.tar.xz
cd ..
