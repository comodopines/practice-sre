#!/usr/bin/python
import re, sys

file_name=sys.argv[1]
try:
  with open(file_name, 'r') as f:
    for line in f:
      # a@b.com a@b.c.com.uk.gov. a-zA-z0-9_-.
      emails = re.findall(r'([\w\-\.]+@([\w\-]+\.){1,2}\w+)', line)
      #email = re.sub(r' ', '', line)
      #print('---->',emails)
      for email in emails:
        print(email[0])
except:
  print("File can't be read")
