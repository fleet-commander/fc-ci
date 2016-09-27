#!/usr/bin/python

# this file is based on 
# https://github.com/kbsingh/centos-ci-scripts/blob/master/build_python_script.py

import os
import json, urllib, subprocess 

url_base="http://admin.ci.centos.org:8080/Node/"

api_key=open(os.path.expanduser('~/duffy.key')).read().strip()

# get count of nodes from duffy
def get_nodes(count,ver="7",arch="x86_64"):
  get_nodes_url="{}get?key={}&ver={}&arch={}&count={}".format(url_base,api_key,ver,arch,count)
  res = urllib.urlopen(get_nodes_url).read()
  res = json.loads(res)

  ssid = res['ssid']
  nodes = res['hosts']
  print "duffy /Nodes/get result ssid = " + ssid
  return nodes,ssid

# release nodes for the current ssid
def release_nodes(ssid):
  print "releasing nodes for ssid " + ssid
  done_nodes_url="{}done?key={}&ssid={}".format(url_base,api_key, ssid)
  res = urllib.urlopen(done_nodes_url).read()

# execute cmd on host through ssh, synchronious 
def ssh_execute(host,cmd):
  ssh_prefix = "ssh -t -o UserKnownHostsFile=/dev/null -o StrictHostKeyChecking=no"
  cmd_template = "{} root@{} '{}'"
  
  cmd = cmd_template.format(ssh_prefix,host,cmd)
  return subprocess.call(cmd,shell=True)

# execute cmd on host, asynchronously
def ssh_execute_async(host,cmd):
  ssh_prefix = "ssh -t -o UserKnownHostsFile=/dev/null -o StrictHostKeyChecking=no"
  cmd_template = "{} root@{} '{}'"
  
  cmd = cmd_template.format(ssh_prefix,host,cmd)
  return subprocess.Popen(cmd,shell=True)
