#!/usr/bin/bash

tee /etc/yum.repos.d/docker.repo <<-'EOF'
[dockerrepo]
name=Docker Repository
baseurl=https://yum.dockerproject.org/repo/main/centos/7/
enabled=1
gpgcheck=1
gpgkey=https://yum.dockerproject.org/gpg
EOF

# install docker
yum -y install docker-engine
systemctl start docker 

# install docker-compose
# FIXME might want to install it with pip later
curl -L https://github.com/docker/compose/releases/download/1.8.1/docker-compose-`uname -s`-`uname -m` > /usr/local/bin/docker-compose
chmod +x /usr/local/bin/docker-compose

# contents of /root/shared will be shared with every docker container
# we want to share distro_tests, so copy its contents there
cp -r ~/fc-ci/distro_tests/* /root/shared/

cd ~/fc-ci
/usr/local/bin/docker-compose up

