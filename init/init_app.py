from commands import getstatusoutput as getso
from handle_error import handle
from config import APP_PACKAGE_DIR
SUFFIX = "rpm"

def do():
    fd = open("app.txt")
    files = fd.readlines()
    fd.close()

    cmd = "rpm -ivh  "

    for p in files:
        p = p.strip()
        if p:
            s=p.split(" ")[0]
            t=p.split(" ")[1]
            f = s+'-'+t
            install = cmd + APP_PACKAGE_DIR + '/'  + f +'.'+SUFFIX         
            print install + '\n'
            s,o = getso(cmd)
#    handle(s,o)
        else:
            continue
