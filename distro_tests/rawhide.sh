#!/usr/bin/bash

echo "the ip of the libvirt node is available from here:"
cat /root/shared/libvirt_node_ip

dnf -y install git
git clone https://github.com/fleet-commander/fc-admin
cd fc-admin
echo "do some tests, build admin, whatever"
ls
