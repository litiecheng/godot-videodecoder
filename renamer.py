#!/usr/bin/env python3
import os
import subprocess

def rename_files(prefix, changeto, tool_prefix, filenames):
    renamer_buffer = 'RENAMER_BUFFER_314159265358979'
    otool = tool_prefix + 'otool'
    install_name_tool = tool_prefix + 'install_name_tool'
    for filename in filenames:
        data = str(subprocess.check_output([otool,'-L',filename])).strip()
        val = map(lambda x: x[0], map(str.split,map(str.strip, data.strip().split('\n'))))
        val = list(val)[2:]

        to_change = {}
        for path in val:
            if path.startswith(prefix):
                to_change[path] = changeto+path[len(prefix):]

        for k,v in to_change.items():
            print(k, v, sep=' -> ')
            subprocess.call([install_name_tool,'-change',k,v,filename])


if __name__ == '__main__':
    from sys import argv
    name, prefix, changeto, tool_prefix = argv[0:4]
    filenames = argv[4:]
    rename_files(prefix, changeto, tool_prefix, filenames)
