#!/usr/bin/python

import string,random
import duffy

num_nodes = 1 + 1
nodes,ssid = duffy.get_nodes(num_nodes)

if len(nodes) != num_nodes:
  sys.exit("Could not acquire requested number of nodes")


# fc uses ssh to connect to libvirt server for live sessions
# this is done with pub/private keys, but password for the user is needed
# to install the public key the first time
username = "fcuser"
options = string.digits + string.letters + string.punctuation
pwd = ''.join(random.SystemRandom().choice(options) for _ in range(25))

prepare_user_cmd = "useradd -m {}; chpasswd <<< \"{}:{}\"".format(username,username,pwd)

prepare_git_cmd = """
sudo yum -q -y install git;
cd ~
git clone https://github.com/sk3r/fc-ci.git;
"""

try:
  # install git and prepare fc user on all nodes
  #FIXME do this async ...
  for n in nodes:
    duffy.ssh_execute(n,prepare_git_cmd)
    duffy.ssh_execute(n,prepare_user_cmd)
    duffy.ssh_execute(n,"echo {} > /root/libvirt_node_ip".format(nodes[0]))

  libvirt_node = duffy.ssh_execute_async(nodes[0],"cd ~/fc-ci; ./prepare_libvirt_node.sh")
  docker_node = duffy.ssh_execute_async(nodes[1],"cd ~/fc-ci; ./prepare_docker_node.sh") 

  docker_node.wait()
finally:
  duffy.release_nodes(ssid)

# FIXME we should likely return a value that indicates the status of the internal nodes
# so we might need to collect data from inside docker containers

