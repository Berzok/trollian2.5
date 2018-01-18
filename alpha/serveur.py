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
	(client_socket, (ip, port)) = main_co.accept()		#Quelqu'un se connecte
	userSocket[indice_user[0]] = client_socket
	
	#On envoie un 0 au client pour lui dire que tout va bien
	client_socket.send(b"0")
	
	#On créé l'utilisateur d'indice correspondant, puis on constr8t sa classe associée
	user = "user" + str(indice_user[0])
	user = Users(client_socket.recv(1024).decode(), indice_user[0], client_socket, ip, port)
	
	#On append la usersList de l'utilisateur qui vient de se connecter
	usersList.append(user)
	
	#On créé le Thread d'envoi la usersList au client en question
#	for elth, valeur in enumerate(usersList):
#		listeUtilisateurs = usersList[elth].envoyerGens(usersList)
#	for elth, valeur in enumerate(listeUtilisateurs):
#		usersList[elth].socket.send(listeUtilisateurs[elth])
	indice_user[0] = indice_user[0]+1
	
	
	
	nouveauThread = ClientThread(client_socket, ip, port, indice_user, user)
	nouveauThread.start()


if msg_recu == b"fin":
	fermer_serveur(main_co, client_co)
