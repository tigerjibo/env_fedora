import os
from os.path import join as pjoin
from handle_error import handle
from commands import getstatusoutput as getso
from config   import HOST_NAME 
def reset_tftp():
    print 'reset tftp server...\n'
    s,o = getso("/etc/init.d/xinetd reload")
    handle(s,o)
    s,o = getso("service xinetd restart")
    handle(s,o)

def reset_nfs():
    print 'reset nfs server...\n'
    s,o = getso("exportfs -rv")
    handle(s,o)
    s,o = getso("service nfs restart")
    handle(s,o)


def do():
    reset_tftp()
    reset_nfs()
