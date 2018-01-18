#coding: utf-8
import socket
import os
import sys
from threading import Thread, RLock


hote = ''
port = 12800
global indice_user
global usersList
global userSocket
usersList = []
userSocket = []
for loop in range(50):
	userSocket.append(0)
indice_user = [0]


class Users:
	def __init__(self, name, numero, socket, ip, port):
		self.pseudo = name
		self.socket = socket
		self.ip = ip
		self.port = port
		self.numero = numero
	def envoyerGens(self, usersList):
		envoi = []
		arret = 0
		for elth, valeur in enumerate(usersList):
			print valeur
			envoi.append(valeur)
		return envoi


class ActualiserGensThread(Thread):
	def __init__(self, user, usersList):
		Thread.__init__(self)
#		self.user.




class ClientThread(Thread):
	def __init__(self, socket, ip, port, indice_user, user):
		Thread.__init__(self)
		self.socket = socket
		self.ip = ip
		self.port = port
		self.numero = indice_user[0]
		self.user = user
		print "Nouvelle connexion: utilisateur",indice_user[0]
		self.socket.send(b"Bonjour le peuple j'accepte la connexion")

	def run(self):
		print self.ip, self.port
		print ""
		msg_recu = b""
		while msg_recu != b"fin":		#On continue tant que le client n'a pas dit fin
			if msg_recu == b"fin":
				break
			msg_recu = self.socket.recv(1024)
			msg_recu = msg_recu.decode()
			if msg_recu == b"fin":
				break
			print "longueur de usersList:", len(usersList)
			nouveauMessageThread = MessageThread(self.socket, self.user, msg_recu)
			nouveauMessageThread.start()
		indice_user[0] = indice_user[0] - 1
		if msg_recu == b"fin":
			print "L'utilisateur", self.user.pseudo, "est parti"
			userSocket[self.numero] = 0
			self.socket.close()
			return



class MessageThread(Thread):
	def __init__(self, socket, user, message):
		Thread.__init__(self)
		self.socket = socket
		self.user = user
		self.message = message
	def run(self):
		print "fonction partager pour ", self.user.pseudo
		print "population actuelle: ", len(usersList)
		print ""
		self.message = "["+self.user.pseudo+"] " + self.message
		textLog = open('logtext.txt', 'w')
		textLog.write(self.message)
		textLog.close()
		i = 0
		for i in range(0, len(userSocket)):
			textLog = open('logtext.txt', 'r')
			try:
				userSocket[i].send(textLog.readline())
				textLog.close()
			except:
				pass
			if i == len(userSocket):
				break



##############CONSTRUCTION DU SERVEUR AVEC LES SOCKETS
#On construit la connexion principale:
#AF_INET pour les adresses internet
#SOCK_STREAM pour le protocole TCP
#Bind va lier main_co avec deux paramètres, un nom d'hôte et un port de connexion
#Listen est le max de connexion simultanées sans être acceptées
def init_serv():
	main_co = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	main_co.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
	main_co.bind((hote, port))
	return main_co


############NOUVEAU CLIENT CONNECTÉ







#############FERMETURE DU SERVEUR
def fermer_serveur(main_co, client_co):
	print "Fermeture du serveur"
	client_co.close()
	main_co.close()
