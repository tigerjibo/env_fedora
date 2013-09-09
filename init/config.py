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
APP_DIR_NAME = 'app_package'
#NET_DRIVER_NAME this is the dell net dirver name
#if you don't want to install dell net dirver,you must comment the blow lines
#and give NET_DIRVER_NAME value NULL.
DRIVER_DIR_NAME     ='driver'
#NET_DRIVER_NAME    =''
#NET_DRIVER_VERSION =''
NET_DRIVER_NAME    = 'e1000e'
NET_DRIVER_VERSION = '1.9.5'
DRIVER_DIR = os.path.join(BASE,DRIVER_DIR_NAME)
NET_DRIVER_PATH = os.path.join(DRIVER_DIR,NET_DRIVER_NAME +'-' + NET_DRIVER_VERSION,'src')
APP_PACKAGE_DIR = os.path.join(BASE,APP_DIR_NAME)
