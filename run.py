#!/usr/bin/python

import string,random
import duffy

num_nodes = 1 + 1
nodes,ssid = duffy.get_nodes(num_nodes)

if len(nodes) != num_nodes:
  sys.exit("Could not acquire requested number of nodes")

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
  for n in nodes:
    duffy.ssh_execute(n,prepare_git_cmd)
    duffy.ssh_execute(n,prepare_user_cmd)

  libvirt_node = duffy.ssh_execute_async(nodes[0],"cd ~/fc-ci; ./prepare_and_run_libvirt.sh;")
  docker_node = duffy.ssh_execute_async(nodes[1],"cd ~/fc-ci; ./prepare_and_run_docker.sh;")

  docker_node.wait()
finally:
  duffy.release_nodes(ssid)

# we should likely return a value that indicates the status of the internal nodes
# so we might need to collect data from inside docker containers

