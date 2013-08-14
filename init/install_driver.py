import os
from commands import getstatusoutput as getso
from handle_error import handle
from config import IP_ADDRESS, NET_DRIVER_PATH, NET_DRIVER_NAME  

def install_netdriver():
    print 'intall NET Driver...\n'
    
    s,o = getso("cd %s && make clean && make install && modprobe %s  " %(NET_DRIVER_PATH,NET_DRIVER_NAME))
    handle(s,o)
    
    s,o = getso("ifconfig eth0 %s " %IP_ADDRESS)
    handle(s,o)

def do():
    install_netdriver()
