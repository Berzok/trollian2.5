#coding: utf-8
import os
import socket
from interface import *
from threading import Thread
os.system('clear')

hote = "localhost"
port = 12800



class LeThread(Thread):
	def __init__(self, co_serveur, msg_a_envoyer):
		Thread.__init__(self)
		self.co_serveur = co_serveur
		self.msg_a_envoyer = msg_a_envoyer
	def run(self):
		if self.msg_a_envoyer == b"fin":
			self.co_serveur.send(self.msg_a_envoyer)
			self.co_serveur.close()
			print "Fermeture de la connexion précédemment établie, au revoir"
		else:
			self.co_serveur.send(self.msg_a_envoyer)
			msg_recu = self.co_serveur.recv(1024)
			print msg_recu.decode()


#On constr8t la connexion de la même manière, c'est-à-dire:
#AF_INET pour adresses internet
#SOCK_STREAM pour le protocole TCP
co_serveur = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#On utilise la méthode connect(), avec en paramètre les mêmes que bind()
co_serveur.connect((hote, port))


#On utilise la méthode recv() afin de recevoir la chaîne de bytes envoyée par send()
rcv_msg = co_serveur.recv(1024)			#1024 donc taille max du message de 1024 caractères
if int(rcv_msg) == 1:
	print "Erreur. Connexion impossible."
else:
	print "Connexion établie avec le serveur", hote,"sur le port",port
print ""

#On choisit un pseudo (et ce à chaque connexion)
pseudo = raw_input("Veuillez choisir un nom d'utilisateur: ")

#On envoie le pseudo du client au serveur
co_serveur.send(pseudo.encode())


#On reçoit le message du serveur qui nous dit coucou
print co_serveur.recv(1024)



#On reçoit la usersList de la part du serveur
listeUtilisateurs = []
#while True:
#	listeUtilisateurs.append() = co_serveur.recv(1024).decode()


msg_a_envoyer = b""
while msg_a_envoyer != b"fin":
	print pseudo,">",
	msg_a_envoyer = raw_input(" ")
	msg_a_envoyer = msg_a_envoyer.encode()
	anotherThread = LeThread(co_serveur, msg_a_envoyer)
	anotherThread.start()


rcv_msg = co_serveur.recv(1024)
if int(rcv_msg) == 1:
	print "Erreur."
else:
	print "Fermeture de la connexion précédemment établie. Au revoir."
	co_serveur.close()
