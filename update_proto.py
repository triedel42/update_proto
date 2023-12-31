#!/usr/bin/env python3
import os
import os.path
import subprocess
import getpass

from sys import argv, platform


bin_cproto = None
if platform.startswith('darwin'):
	bin_cproto = '/Users/' + getpass.getuser() + '/homebrew/bin/cproto'
else: #if platform.startswith('linux')
	bin_cproto = '/usr/bin/cproto'

assert os.path.exists(bin_cproto), 'cproto not found'


def update_proto(header) -> bool:
    cfile = header.replace('.h', '.c')
    did_something = False
    inside_proto = False
    lines_new = []
    for line in open(header).read().splitlines(True):
        if '$$proto_end$$' in line:
            if inside_proto:
                lines_new.append('\n')
            inside_proto = False
        if not inside_proto:
            lines_new.append(line)
        if '$$proto_start$$' in line:
            lines_new.append('\n')
            if not inside_proto:
                lines_new.extend(subprocess.run(f'{bin_cproto} {cfile}'.split(' '),
                        capture_output=True, text=True).stdout.splitlines(True))
            inside_proto = True
            did_something = True

    assert not inside_proto, 'Did not find both $$proto_start$$ and $$proto_end$$'
    open(header, 'w').write(''.join(lines_new))
    return did_something


if __name__ == '__main__':
    assert len(argv) >= 2, 'Not enough args'

    for header in argv[1:]:
        assert header.endswith('.h'), 'Arg is not a .h file'
        res = update_proto(header)
        msg = 'Updated ' + header
        msg += ' (No $$proto_start$$ and $$proto_end$$)' if not res else ''
        print(msg)
