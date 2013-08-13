import os
from   config import IP_ADDRESS, NET_DRIVER_PATH,NET_DRIVER_NAME  

def install_netdriver():
    print 'intall net dirver...\n'
    s,o = getso("cd %s && make clean && make install && modprobe" % (NET_DRIVER_PATH,NET_DRIVER_NAME))
    handle(s,o)
    s,o = getso("ifconfig eth0 %s" %IP_ADDRESS)


def do():
    install_netdriver()
