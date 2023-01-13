from TP5.tp5 import *
import random

articles = ('Pommes', 'Poires', 'Fraises', 'Bananes', 'Oranges', 'Clémentines', 'Endives', 'Laitues')
prix = (5.27, 7.12, 4.98, 3.46, 4.02, 5.27, 1.67, 2.78)
panier = dict(zip(articles, prix))
print(panier)

print("\nFonction getPrix :")
print(getPrix(panier, "Poires")) # Devrait afficher 7.12
print(getPrix(panier, "Clémentines")) # Devrait afficher 5.27
print(getPrix(panier, "Cerises")) # Devrait afficher 0.0

print("\nFonction getPrixTotal :")
print(getPrixTotal(panier)) # Devrait afficher 34.57

print("\nFonction afficherPanier :")
afficherPanier(panier)

print("\nFonction supprimerArticle :")
print(supprimerArticle(panier, 'fraises'))
afficherPanier(panier)
print(supprimerArticle(panier, 'Cerises'))

print("\nFonction ajouterArticle :")
ajouterArticle(panier, 'bananes', 2.3)
afficherPanier(panier)
ajouterArticle(panier, 'Cerises', 4.1)
afficherPanier(panier)

print("\nFonction getArticlePlusCher :")
panier = {"Pommes": 5.27, "Poires": 7.12, "Fraises": 4.98, "Bananes": 3.46, "Oranges": 4.02, "Clémentines": 5.27, "Endives": 1.67, "Laitues": 2.78}
print("Liste des articles les plus chers : ")
while len(panier)!=0:
    a = getArticlePlusCher(panier)
    print(f"{a:<20}: prix = {getPrix(panier, a)}")
    supprimerArticle(panier, a)
