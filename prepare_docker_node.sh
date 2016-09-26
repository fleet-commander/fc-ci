sudo tee /etc/yum.repos.d/docker.repo <<-'EOF'
[dockerrepo]
name=Docker Repository
baseurl=https://yum.dockerproject.org/repo/main/centos/7/
enabled=1
gpgcheck=1
gpgkey=https://yum.dockerproject.org/gpg
EOF

sudo yum -y install docker-engine
sudo systemctl start docker 

# this machine (docker node) will have some shared files in /root/shared
# we want these to be available to every docker container
# the folder ./fc-ci/distro_tests will be mounted inside the contaienrs, so we
# copy the shared files there
cp -r /root/shared/ ~/fc-ci/distro_tests

cd ~/fc-ci
sudo docker-compose up
