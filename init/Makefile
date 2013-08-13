$(info ******************************************)
$(info *****Auto Install and Configure software***)
$(info **Author :JiBo Email:jibo.tiger@gmail.com**)

all: install_driver install_software env

install_dirver:
	@echo "install driver..."
	sudo python sudo_driver.py
install_software:
	@echo "Install all software..."
	sudo python sudo.py
env:
	@echo "Configure Software Environment.."
	python do.py
	sudo python sudo_env.py

