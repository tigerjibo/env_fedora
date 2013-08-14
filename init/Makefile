$(info ******************************************)
$(info *****Auto Install and Configure software***)
$(info **Author :JiBo Email:jibo.tiger@gmail.com**)

all:    install_software env install_driver

install_software:
	@echo "Install all software..."
#sudo python sudo.py
env:
	@echo "Configure Software Environment.."
	python do.py
	sudo python sudo_env.py

install_driver:
	@echo "install driver..."
	sudo python sudo_driver.py

