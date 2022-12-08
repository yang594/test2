#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import subprocess
import sys

def main(token, git_url):
    cmd = 'git init'
    subprocess.call(cmd, shell=True)

    cmd = 'git add .'
    subprocess.call(cmd, shell=True)

    cmd = 'git commit -m "just test baits"'
    subprocess.call(cmd, shell=True)

    
    cmd = 'git config --global user.name "superyangbb@163.com"'
    subprocess.call(cmd, shell=True)

    cmd = 'git config --global user.email "superyangbb@163.com"'
    subprocess.call(cmd, shell=True)

    cmd = 'git remote remove origin'
    subprocess.call(cmd, shell=True)

    cmd = 'git remote add origin https://{}@{}'.format(token, git_url)
    subprocess.call(cmd, shell=True)

    cmd = 'git push -u origin master -f'
    print(subprocess.call(cmd, shell=True))


if __name__ == '__main__':
    token = sys.argv[1]
    git_url = sys.argv[2]
    print(token, git_url)
    main(token, git_url)
