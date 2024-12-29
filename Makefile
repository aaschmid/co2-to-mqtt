UDEV_FILE=99-holtek-co2.rules

install-debian :
	sudo apt-get install python-dev-is-python3 python3-paho-mqtt python3-yaml

install-dependencies :
	pip install --user -r requirements.txt

run :
	python3 monitor.py /dev/co2sensor

setup-udev :
	sudo cp $(UDEV_FILE) /etc/udev/rules.d/$(UDEV_FILE)
