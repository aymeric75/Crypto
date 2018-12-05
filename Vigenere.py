#!/usr/bin/env python
# -*- coding: utf-8 -*- 

import string

def Requete():

	mode=raw_input('Entrez la clés secrète:')
	print('\n')
	while (type(mode) != str or len(mode)>6):
			mode=raw_input('La clés secrète doit être composé de max 6 lettres uniquement , veuillez réessayer:')
			print('\n')
	return mode





def Chiffrement(cles):

	m = raw_input('Entrez une expression à chiffrer: ')
	print('\n')

	while (type(m) != str):
			m=raw_input("Erreur, veuillez n'entrer que des lettres: ")
			print('\n')
	chiffre=''
	j=0
	for i in range(len(m)):

		if m[i] == ' ':
			chiffre += ' '
			j-=1

		else:
			rang = (string.ascii_lowercase.index(cles[j]) + string.ascii_lowercase.index(m[i]) ) % 26

			chiffre += string.ascii_lowercase[rang]

		j+=1
		j=j%len(cles)
		
		

			


	return chiffre



#def Dechiffrement(cles):




if __name__ == '__main__':
	cle = Requete()
	resul = Chiffrement(cle)

	print "Voici l'expression chiffrée par Vigenere: ", resul
	print('\n')

