#coding: utf-8
import os
import socket
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
		self.co_serveur.send(msg_a_envoyer)
		msg_recu = self.co_serveur.recv(1024)
		print msg_recu.decode()


#On constr8t la connexion de la même manière, c'est-à-dire:
#AF_INET pour adresses internet
#SOCK_STREAM pour le protocole TCP
co_serveur = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#On utilise la méthode connect(), avec en paramètre les mêmes que bind()
co_serveur.connect((hote, port))
print "Connexion établie avec le serveur", hote,"sur le port",port

#On utilise la méthode recv() afin de recevoir la chaîne de bytes envoyée par send()
rcv_msg = co_serveur.recv(1024)			#1024 donc taille max du message de 1024 caractères
print rcv_msg
print ""

#On choisit un pseudo (et ce à chaque connexion)
pseudo = raw_input("Veuillez choisir un nom d'utilisateur: ")
co_serveur.send(pseudo.encode())
print co_serveur.recv(1024)


msg_a_envoyer = b""
while msg_a_envoyer != b"fin":
	print pseudo,">",
	msg_a_envoyer = raw_input(" ")
	msg_a_envoyer = msg_a_envoyer.encode()
	anotherThread = LeThread(co_serveur, msg_a_envoyer)
	anotherThread.start()

print "Fermeture de la connexion précédemment établie, au revoir"
co_serveur.close()



