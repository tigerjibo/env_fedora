import os
#PROJECT_FOLDER is the project folder name
PROJECT_FOLDER = 'env_fedora'
HOME = os.environ['HOME']
HOST_NAME =  (HOME.split('/'))[2]
CONFIG = 'CV_Linux'
BASE = os.path.join(HOME, CONFIG)
ENV_URL = os.path.join(HOME,PROJECT_FOLDER,'config')
#EMBED_WORK is the nfs server share  dirname
EMBED_WORK = 'Embbed_work'
#use to generate ssh public key
EMAIL = 'jibo@edan.com'
#IP_ADDRESS 
IP_ADDRESS = '192.168.21.107'
#NET_DRIVER_NAME this is the dell net dirver name
DRIVER_DIR         ='driver'
NET_DRIVER_NAME    = 'e1000e'
NET_DRIVER_VERSION = '1.9.5'
NET_DRIVER_PATH = os.path.join(BASE,DRIVER_DIR,NET_DRIVER_NAME +'-' + NET_DRIVER_VERSION,'src')
