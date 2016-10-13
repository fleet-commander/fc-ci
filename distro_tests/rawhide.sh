#!/usr/bin/bash

echo "the ip of the libvirt node is available from here:"
cat /root/shared/libvirt_node_ip

echo "installing git and cloning fc-admin"
dnf -y install git
git clone https://github.com/fleet-commander/fc-admin

# compile and install fleet commander

echo "installing node.js, phantomjs, and casperjs"
cd ~
dnf -y install npm tar bzip2
npm install node.js
npm install phantomjs-prebuilt
npm install casperjs

# run some tests, for example 
# ./node_modules/casperjs/bin/casperjs test basic_settings.js

# report the status back to fpaste, etc.
