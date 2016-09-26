sudo yum -y install kvm libvirt qemu-kvm
sudo systemctl start libvirtd

sudo yum -y install openssh
sudo systemctl start sshd
