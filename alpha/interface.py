#coding: utf-8

import pygame
import os
from pygame.locals import *
os.system('clear')

class MenuGeneral:
	def __init__ (self, user, userSocket):
		self.fenetre = pygame.display.set_mode((640, 480), RESIZABLE)
		self.connectionActives = usersList
		self.utilisateur = user


class Fenetretchat:
	def __init__ (self, user, autreUser):
		self.fenetre = pygame.display.set_mode((640, 480))
		separateur = pygame.image.load("img/separateur.xcf").convert()
		self.pseudo = user.pseudo
		self.socketClient = user.socket
		self.numUser = user.numero
		self.numDeux = autreUser.numero
		self.socketDeux = autreUser.socket
		self.pseudoDeux = autreUser.pseudo
	def actualiser(self):
		self.fenetre.flip()
	def afficherImage(self, image, x, y):
		y = 480 - (480 - y)
		self.fenetre.blit(image, (x, y))
		actualiser()

#On initialise pygame


#On définit la variable principale, en gros la fenêtre pygame
#En paramètres: largeur et hauter de l'image, puis trucs optionnels

#l'instruction sert ici à charger une image dans une variable


#On applique la variable avec l'image à la fenêtre
#En paramètres, la variable et les coordonnées où coller.


#Pour actualiser la fenêtre pygame dans sa totalité


