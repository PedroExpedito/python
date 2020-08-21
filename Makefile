all:
	cython --embed -o keylogger.c keylogger.py
	tcc -Os -I /usr/include/python3.8/ keylogger.c -lpython3.8 -o build/keylogger
run:
	python3 keylogger.py

