# Application d'Authentification Flask (Formulaire d'authentification) 

-Cette application Flask fournit une interface web simple pour l'enregistrement et la connexion des utilisateurs. 
-Utilisation de SQLite comme système de gestion de base de données pour stocker les informations des utilisateurs et Flask pour servir l'application web.

## Fonctionnalités Techniques

- Flask : Un framework web léger en Python pour servir l'application web.
- SQLite : Une base de données embarquée qui stocke les informations des utilisateurs.
- Hashage de Mot de Passe : Utilisation de SHA-256 pour le hachage des mots de passe (sécurisé).
- Validation de Mot de Passe : Des contraintes pour assurer que les mots de passe sont suffisamment forts.


L'application est accessible à l'adresse http://localhost:5000.


## Utilisation

-Enregistrement d'un Nouvel Utilisateur :

Remplissez les champs du formulaire d'inscription.
Cliquez sur le bouton "Ajout Compte".
Un message de confirmation de la création du compte ou indiquera une erreur.

-Connexion d'un Utilisateur :

Entrez vos identifiants dans le formulaire de connexion.
Cliquez sur le bouton "OK".

Exemple d'un compte; 
Identifiant:Ramdani Chaimae
Mot de Passe:Etudiante@paris8

Un message vous accueillera si la connexion est réussie ou indiquera une erreur.

-Réinitialisation des Champs du Formulaire :
Cliquez sur le bouton "Réinitialiser" pour effacer les champs du formulaire.

##Sécurité
-Les mots de passe sont hachés avant d'être stockés dans la base de données.
-Les validations de mot de passe garantissent que les utilisateurs créent des mots de passe forts.
-Des requêtes paramétrées sont utilisées pour prévenir les injections SQL.
