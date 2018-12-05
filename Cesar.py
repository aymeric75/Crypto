#!/usr/bin/env python
# -*- coding: utf-8 -*- 

import string


# @fonction: demande à l'util. d'entrer un entier < 27
def Requete():

	mode=input('Entrez le décalage souhaité:')
	print('\n')
	while (type(mode) != int or mode>=27):
			mode=input('Erreur, réessayez:')
			print('\n')
	return mode



def Chiffrement(decalage):

	m = raw_input('Entrez une expression à chiffrer: ')
	print('\n')

	while (type(m) != str):
			m=input("Erreur, veuillez n'entrer que des lettres: ")
			print('\n')
	chiffre=''
	for i in range(len(m)):
		if m[i] == ' ':
			chiffre += ' '
		else:
			chiffre += string.ascii_lowercase[(string.ascii_lowercase.index(m[i]) + decalage)%26]

	return chiffre

	




if __name__ == '__main__':
	decal = Requete()
	resul = Chiffrement(decal)

	print "Voici l'expression chiffrée par Cesar: ", resul
	print('\n')





