# Copyright (C) 2003-2007  Robey Pointer <robeypointer@gmail.com>
#
# This file is part of paramiko.
#
# Paramiko is free software; you can redistribute it and/or modify it under the
# terms of the GNU Lesser General Public License as published by the Free
# Software Foundation; either version 2.1 of the License, or (at your option)
# any later version.
#
# Paramiko is distributed in the hope that it will be useful, but WITHOUT ANY
# WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR
# A PARTICULAR PURPOSE.  See the GNU Lesser General Public License for more
# details.
#
# You should have received a copy of the GNU Lesser General Public License
# along with Paramiko; if not, write to the Free Software Foundation, Inc.,
# 59 Temple Place, Suite 330, Boston, MA  02111-1307  USA.


import socket
import sys
from paramiko.py3compat import u

# windows does not have termios...
try:
    import termios
    import tty
    has_termios = True
except ImportError:
    has_termios = False


def interactive_shell(chan,request):
    windows_shell(chan,request)



# thanks to Mike Looijmans for this code
def windows_shell(chan,request):
    import threading

    sys.stdout.write("Line-buffered terminal emulation. Press F6 or ^Z to send EOF.\r\n\r\n")
        
    def writeall(sock):
        while True:
            data = sock.recv(256)
            if not data:
                sys.stdout.write('\r\n*** EOF ***\r\n\r\n')
                sys.stdout.flush()
                break
#             sys.stdout.write(data)
            request.websocket.send(data)
#             sys.stdout.flush()
        
    writer = threading.Thread(target=writeall, args=(chan,))
    writer.start()
        
    try:
        while True:
#             d = sys.stdin.read(1)
#             if not d:
#                 break
#             chan.send(d)
            for message in request.websocket:
                if not message:
                    break
                chan.send(message)
    except EOFError:
        # user hit ^Z or F6
        pass
