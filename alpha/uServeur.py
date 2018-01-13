#coding: utf-8
import socket
import os
import sys
from threading import Thread, RLock


hote = ''
port = 12800
global indice_user
global userslist
global userSocket
userslist = []
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


class ClientThread(Thread):
	def __init__(self, socket, ip, port, indice_user):
		Thread.__init__(self)
		self.socket = socket
		self.ip = ip
		self.port = port
		self.numero = indice_user[0]
		print "Nouvelle connexion: utilisateur",indice_user[0]
		self.socket.send(b"Bonjour le peuple j'accepte la connexion")

	def run(self):
		user = "user"+str(self.numero)
		print self.ip, self.port
		print ""
		user = Users(self.socket.recv(1024).decode(), self.numero, self.socket, self.ip, self.port)
		self.socket.send(b"Tu es l'utilisateur "), self.socket.send(user.pseudo.encode()), self.socket.send(b" c'est cela ?")
		msg_recu = b""
		while msg_recu != b"fin":		#On continue tant que le client n'a pas dit fin
			if msg_recu == b"fin":
				break
			msg_recu = self.socket.recv(1024)
			msg_recu = msg_recu.decode()
			nouveauMessageThread = MessageThread(self.socket, user, msg_recu)
			nouveauMessageThread.start()
		indice_user[0] = indice_user[0] - 1
		if msg_recu == b"fin":
			print "L'utilisateur", user.pseudo, "est parti"
			userSocket[self.numero] = 0
			self.socket.close()



class MessageThread(Thread):
	def __init__(self, socket, user, message):
		Thread.__init__(self)
		self.socket = socket
		self.user = user
		self.message = message
	def run(self):
		print "fonction partager pour ", self.user.pseudo
		print "population actuelle: ", len(userSocket)
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
				self.socket.close()
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
def connexion_client(userslist):
	i = 0
	if userslist[i]:
		while userslist[i]:
			i = i+1
	userslist[i] = "user"+str(i)
	return i







#############FERMETURE DU SERVEUR
def fermer_serveur(main_co, client_co):
	print "Fermeture du serveur"
	client_co.close()
	main_co.close()
