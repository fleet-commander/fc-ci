yum -y install kvm libvirt qemu-kvm
systemctl start libvirtd

yum -y install openssh
systemctl start sshd
