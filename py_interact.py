#!/usr/bin/env python

from subprocess import Popen, PIPE, STDOUT
from time import sleep, time
from threading import Thread
import sys

try:
    from Queue import Queue, Empty
except ImportError:
    from queue import Queue, Empty
    
class PyInteract(object):

    def __init__(self, process, *args):
        self._process = [process]
        self._process += [x for x in args]
        ON_POSIX = 'posix' in sys.builtin_module_names
        self._sub = Popen(  self._process,
                            stdin=PIPE,
                            stdout=PIPE,
                            stderr=STDOUT,
                            bufsize=1,
                            close_fds=ON_POSIX,
                         )
        self._q = Queue()
        self._t = Thread(target=PyInteract._enqueue_output, args=(self._sub.stdout,self._q))
        self._t.daemon = True
        self._t.start()

    def interact(self, input, buffer_timeout=.1, max_timeout=0, newline=True):
        try:
            self._sub.stdin.write(input)
            if newline:
                self._sub.stdin.write('\n')
            self._sub.stdin.flush()
        except IOError:
            return ''
        output = ''
        received_output = False
        last_time = time()
        while True:
            try:
                line = self._q.get_nowait()
                output += line
                received_output = True
                last_time = time()
            except Empty:
                if received_output and time() - last_time > buffer_timeout:
                    return output
                if max_timeout > 0 and time() - last_time > max_timeout:
                    return output

    def is_alive(self):
        return self._sub.poll() is None

    def status_code(self):
        return self._sub.returncode

    @staticmethod
    def _enqueue_output(out, queue):
        for line in iter(out.readline, b''):
            queue.put(line)
        out.close()

if __name__ == '__main__':
    if len(sys.argv) < 2 or sys.argv[1] == '-h' or sys.argv[1] == '--help':
        print "Usage: %s command [options]" % (sys.argv[0])
    else:
        p = PyInteract(*sys.argv[1:])
        while p.is_alive():
            i = raw_input('> ')
            res = p.interact(i, max_timeout=1)
            if res:
                print res

