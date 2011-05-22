all:
	pyuic4 -i 2 -o gui.py gui.ui
	pyrcc4 -o resources_rc.py resources.qrc
	python2 main.py

clean:
	rm -f *.pyc
