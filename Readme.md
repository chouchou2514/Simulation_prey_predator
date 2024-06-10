# Projet informatique S4
**Marie Epinat** & **Cécilia Prétot**  
Projet : Modèle de simulation Proies/Prédateurs  
Bibliothèques à importer :   
- `Matplotlib`  
- `Numpy`

Code organisé en classe avec la Programmation Orientée Objet.  
Chaque fichier est une classe, le fichier « simulation » contient la classe simulation ainsi que le ‘main’ : c’est le fichier qu’il faut exécuter. Le fichier « Read me » est un rapport sur le projet. Le fichier « constante » est un fichier regroupant toutes les paramètres utiles à la recherche de l’équilibre du système.  
Le but du projet : Obtenir un équilibre entre 3 populations : l’herbe, les lapins et les loups. Les trois populations doivent vivre ensemble sans que leurs effectifs ne tendent vers 0 ou l’infini.  
Notre écosystème est doté des 3 populations : l’herbe pousse à une certaine vitesse et se fait manger une proportion de sa pousse lorsque les lapins se nourrissent. Les animaux se déplacent et perdent de l’énergie. Les animaux de la même espèce se reproduisent s’ils ont assez d’énergie et l’âge minimum requis. Nos animaux se nourrissent si leur énergie est trop faible et qu’ils sont sur une case où se trouvent de la nourriture. Nos animaux meurent si leur énergie devient trop faible ou si leur âge est trop avancé (ou bien mangé dans le cas des lapins).  
Les extensions : Notre environnement est doté d’une rivière et de terriers. La rivière n’est pas accessible aux animaux qui doivent la contourner pour accéder à l’autre coté de la rive. Les terriers sont des cases où les lapins peuvent se cacher : ces cases sont inaccessibles aux loups. Les loups savent chasser : si un lapin se retrouve proche d’un loup, le loup va se déplacer vers le lapin.  
Les limites : Notre programme ne correspond pas parfaitement à la réalité. La simulation ne prend pas en compte le sexe des animaux. De plus, les animaux peuvent se reproduisent autant de fois que les conditions d’âge et de faim leurs permettent.  
