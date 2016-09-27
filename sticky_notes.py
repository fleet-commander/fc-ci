#!/usr/bin/bash

# a simple python wrapper for posting to (primarily) fedorapaste

import requests

def post(paste_data,paste_lang="text",paste_expire="0",api_submit="true",mode="json",url="http://paste.fedoraproject.org/"):
  data = {
  'paste_data': paste_data,
  'paste_lang': paste_lang,
  'api_submit': api_submit,
  'mode': mode,
  'paste_expire': paste_expire
  }

  return requests.post(url,data=data)
