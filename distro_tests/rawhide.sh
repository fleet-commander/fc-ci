#!/usr/bin/bash

echo "the ip of the libvirt node is available from here:"
cat /root/shared/libvirt_node_ip

dnf -y install git
git clone https://github.com/fleet-commander/fc-admin
cd fc-admin

cd ~
dnf -y install npm tar bzip2

echo "installing node.js, phantomjs, and casperjs"
npm install node.js
npm install phantomjs-prebuilt
npm install casperjs

ls -la
cd ./node_modules/
ls -la
