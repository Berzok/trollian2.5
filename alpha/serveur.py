#coding: utf-8
import os
import socket
import sys
sys.path.append("~/Documents/pythonNetwork/")
from uServeur import *
os.system('clear')

#On constr8t la connexion principale
main_co=init_serv()

while True:
	main_co.listen(5)
	(client_socket, (ip, port)) = main_co.accept()
	userSocket[indice_user[0]] = client_socket
	nouveauThread = ClientThread(client_socket, ip, port, indice_user)
	indice_user[0] = indice_user[0]+1
	nouveauThread.start()


if msg_recu == b"fin":
	fermer_serveur(main_co, client_co)
