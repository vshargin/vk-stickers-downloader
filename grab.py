#!/usr/bin/env python3

import os, sys
import yaml
import requests
from itertools import count

def download_file(url, filename, chunk_size=256):
  r = requests.get(url, stream=True)
  with open(filename, 'wb') as fd:
    for chunk in r.iter_content(chunk_size):
      fd.write(chunk)


def usage(preface=""):
  print((preface+"""
grab.py config.yml [OPTIONS]

Config file example:
    otto:
      - https://vk.com/images/stickers/346/512.png
      - https://vk.com/images/stickers/347/512.png
      - https://vk.com/images/stickers/348/512.png
      - ...

    # For your convenience, you can use special 'range' objects:
    foxy: {range: [233, 264]}
    # This would work for VK stickers only, for now.
    # Both left and right ends are inclusive.
""").strip())


def main():
  if len(sys.argv) < 2:
    usage()
    sys.exit(1)

  cfg = yaml.load(open(sys.argv[1]))

  if len(sys.argv) >= 3:
    generator = ((name, cfg[name]) for name in sys.argv[2:])
  else:
    generator = cfg.items()

  for pack_name, pack in generator:
    if 'range' in pack:
      rs, re = pack['range'][0:2]
      fmt = pack['range'][2] if len(pack['range']) > 2 else "https://vk.com/images/stickers/{}/512.png"
      urls = ["https://vk.com/images/stickers/{}/512.png".format(i)
              for i in range(rs, re+1)]
    elif isinstance(pack, list):
      urls = pack
    else:
      usage("Incorrect pack definition: {}".format(pack_name))
      sys.exit(1)

    os.makedirs(pack_name, exist_ok=True)

    for i, url in zip(count(), urls):
      filename = "%s/%s.png" % (pack_name, str(i))
      download_file(url, filename)

if __name__ == "__main__":
  main()
