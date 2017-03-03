#!/usr/bin/env python
# coding:utf-8
from __future__ import with_statement, print_function
import os
import re
import subprocess
import sys


def system(*args, **kwargs):
    kwargs.setdefault('stdout', subprocess.PIPE)
    proc = subprocess.Popen(args, **kwargs)
    out, err = proc.communicate()
    return out


def main():
    modified = re.compile('^[AM]+\s+(?P<name>.*\.ts$)', re.MULTILINE)
    files = system('git', 'status', '--porcelain').decode("utf-8")
    files = modified.findall(files)

    tempdir = os.popen('pwd').read()
    for name in files:
        filename = os.path.join(tempdir, name)
        filepath = os.path.dirname(filename)

        if not os.path.exists(filepath):
            os.makedirs(filepath)
        with open(filename, 'w') as f:
            system('git', 'show', ':' + name, stdout=f)

        args = ['tslint']
        args.append('--type-check')
        args.append(name)
        args = ' '.join(args)
        output = os.popen(args).read()
        if output:
            print(output.decode("utf-8"),)
            print(output)
            sys.exit(1)


if __name__ == '__main__':
    main()
