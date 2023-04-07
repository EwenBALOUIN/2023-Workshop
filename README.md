

<p align='center'>
  
  <a href="#">
    <img src="https://img.shields.io/badge/Django-092E20?style=for-the-badge&logo=django&logoColor=green" />
  </a>&nbsp;&nbsp;
  <a href="#">
    <img src="https://img.shields.io/badge/Docker-2CA5E0?style=for-the-badge&logo=docker&logoColor=white" />        
  </a>&nbsp;&nbsp;
  <a href="#">
    <img src="https://img.shields.io/badge/VSCode-0078D4?style=for-the-badge&logo=visual%20studio%20code&logoColor=white" />        
  </a>&nbsp;&nbsp;
  
</p>

# Team-3-Workshop : NK CRM
### Authors : Anthony LEGRAND - Ewen BALOUIN - Thibault LEDANOIS - Manon JULIEN-KUENTZ

## Contexte 👋
Le monde de l’entrepreneuriat est de plus en plus plébiscité par les Français. Dans ce cadre, chaque nouvel entrepreneur doit réaliser du chiffre d'affaires et utiliser ou développer des compétences commerciales afin de vendre ses produits ou services.

Les techniques et workflows des commerciaux ne sont pas toujours évident pour tous, et l’utilisation d’outils de gestion de la relation client (GRC ou CRM en anglais) est souvent coûteuse à la fois en temps et en argent.

Il existe quelques CRM Open Source disponibles sur le net, mais ceux-ci sont complexes car disposent de trop nombreuses fonctionnalités.

Le but de ce projet va donc être de créer un CRM Open Source avec les fonctionnalités primaires uniquement, et qui devra être très facile à prendre en main.

Le but est de créer un CRM Open Source afin de simplifier la gestion de la relation client.


## Pré-requis 📦

- Docker
- Docker-compose

## Installation de l'environement dev 🏗️
Construire le conteneur
```sh
docker-compose build
```

Lancer le conteneur
```sh
docker-compose up
```

Accèder au conteneur
```sh
docker exec -it nkworkshop-web-1 sh
```

## Setup de Django 🐍
Réaliser les migrations de la base de données
```sh
python manage.py migrate
```

Créer un utilisateur admin
```sh
python manage.py createsuperuser
```


### Vous pouvez maintenant accèder à l'application sur l'URL : [http://localhost/:8000](http//localhost:8000) 🚀🚀🚀

---
## Documention fonctionnelle :

Elle se situe à la racine du dossier et se nomme [funct-specs.md](/funct-specs.md)