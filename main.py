#!/usr/bin/env python

from py_interact import PyInteract
import sys

def main(argv):
    gdb = PyInteract('gdb', '-q', *argv[1:])
    while gdb.is_alive():
        inpu = raw_input('> ')
        print gdb.interact(inpu, max_timeout=1)

if __name__ == '__main__':
    main(sys.argv)
