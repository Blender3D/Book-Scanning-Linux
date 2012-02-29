all:
	bash ./packages.sh
	sudo bash ./build.sh build single netinstall

aur:
	bash ./packages.sh

iso:
	sudo bash ./build.sh build single netinstall
