# coding:utf-8
from __future__ import with_statement, print_function
import os
import re
import shutil
import subprocess
import sys
import tempfile


def system(*args, **kwargs):
    kwargs.setdefault('stdout', subprocess.PIPE)
    proc = subprocess.Popen(args, **kwargs)
    out, err = proc.communicate()
    return out


def main():
    modified = re.compile('^[AM]+\s+(?P<name>.*\.ts$)', re.MULTILINE)
    files = system('git', 'status', '--porcelain').decode("utf-8")
    files = modified.findall(files)

    tempdir = tempfile.mkdtemp()
    for name in files:
        filename = os.path.join(tempdir, name)
        filepath = os.path.dirname(filename)

        if not os.path.exists(filepath):
            os.makedirs(filepath)
        with open(filename, 'w') as f:
            system('git', 'show', ':' + name, stdout=f)

    args = ['tslint']
    # if select_codes and ignore_codes:
    #     print(u'Error: select and ignore codes are mutually exclusive')
    #     sys.exit(1)
    # elif select_codes:
    #     args.extend(('--select', ','.join(select_codes)))
    # elif ignore_codes:
    #     args.extend(('--ignore', ','.join(ignore_codes)))
    # args.extend(overrides)
    # args.append('.')
    # output = system(*args, cwd=tempdir)
    # shutil.rmtree(tempdir)
    # if output:
    #     print(u'PEP8 style violations have been detected.  Please fix them\n'
    #           'or force the commit with "git commit --no-verify".\n')
    #     print(output.decode("utf-8"),)
    #     sys.exit(1)


if __name__ == '__main__':
    main()
