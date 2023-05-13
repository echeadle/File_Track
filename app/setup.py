#!/usr/bin/env python3

import os


dirs = ['ansible_collections','node_modules','google-cloud-sdk', 'go', 'VirtualBox VMs','anaconda3','snap','env','venv','temp', '.testdir', 'goodir']


os.mkdir('test_file_track')
for dir in dirs:
    os.mkdir(f"./test_file_track/{dir}")

with open('./test_file_track/readme.txt', 'w') as f:
    f.write('Create a new text file!')

with open('./test_file_track/goodir/areadme.txt', 'w') as f:
    f.write('Create a new text file!')

with open('./test_file_track/.testdir/do_not_read_me.txt', 'w') as f:
    f.write('Create a new text file!')
