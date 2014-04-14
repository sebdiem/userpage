Title: Démarrer un blog avec Pelican
Date: 2014-03-29 09:27
Category: Blogging
Tags: pelican
Author: Sébastien Diemer

Cela fait quelque temps maintenant que je voulais lancer un blog et c'est finalement cette [lecture](http://timkastelle.org/blog/2014/03/you-should-start-a-blog-right-now/) qui m'a convaincue... et plus particulièrement les points 3: "Blogging helps you turn your flow of idea into a stock of content" et 7: "Blogging helps you build your skills" qui sont pour moi de bonnes motivations.
J'ai eu l'occasion par le passé d'utiliser Wordpress et je songeais naturellement à m'orienter vers cette plateforme, jusqu'à ce que je lise [ceci](http://jakevdp.github.io/blog/2013/05/07/migrating-from-octopress-to-pelican/) qui m'a fait découvrir [Pelican](http://blog.getpelican.com), un générateur de sites statiques écrit en python.

La simplicité de mise en oeuvre est assez impressionante:

* pas de base de données: les articles sont écrits dans des fichiers texte dans un langage comme Markdown ou reStructuredText. Cela facilite les sauvegardes, migrations futures et j'en passe...
* pas besoin d'hébergeur, car le contenu statique peut être stocké directement sur des plateformes gratuites comme github
* les fichiers de configuration sont en python

Par ailleurs, de bons modules additionnels sont disponibles, dont un qui permet d'intégrer directement à un article un notebook ipython. Cela m'intéressait particulièrement car j'ai l'intention de publier ici les expérimentations que je peux faire en python, et les notebooks sont un moyen très pratique de diffusion!

Si pelican pêche sur un aspect, c'est peut être sur celui des thèmes disponibles. Il ne comprend que deux thèmes de base et je trouve les thèmes développés par la communauté disponibles actuellement pas très attrayants visuellement. Je recherchais pour ce blog un style très épuré, à l'image du thème [Whitespace](https://github.com/lucaslew/whitespace) d'Octopress. Je me suis tout d'abord orienté vers [pelican-mockingbird](https://github.com/wrl/pelican-mockingbird), qui propose quelque chose dans le même esprit, mais j'ai finalement opté pour [pelican-octopress-theme](https://github.com/duilio/pelican-octopress-theme). C'est un thème développé de façon très professionnelle, et même si le look de base est loin de ce que je recherchais, j'ai modifié les css à ma sauce pour obtenir le rendu que vous avez sous les yeux (largement inspiré de [Whitespace](https://github.com/lucaslew/whitespace)).

J'ai forké le thème [pelican-octopress-theme](https://github.com/duilio/pelican-octopress-theme) et mis en ligne ma propre version que vous pouvez bien sûr utiliser si elle vous plait! Les principales modifications par rapport au thème de base sont:

* suppression de la sidebar
* suppression du menu de navigation qui apparaissait sur les petits écrans. Cela suppose que le menu ne comporte pas trop d'éléments.
* suppression de l'image de fond et remplacement par un fond blanc
* largeur de base plus petite
* utilisation de police sans-serif uniquement

Dans un second temps, il faudrait que j'allège le css du site... Il est entièrement basé sur celui du thème pelican-octopress-theme, qui, s'il permet une très grande personnalisation, est quand même un peu lourd pour un site minimaliste comme celui-ci!

Enfin, j'ai ajouté un petit script qui réalise la traduction automatique du thème anglais dans la langue de son choix. Il suffit simplement de remplir un fichier `.txt` contenant les chaînes de caractères à traduire et le script effectue les remplacements dans les templates.

Les sources du thème sont disponibles [ici](https://github.com/sebdiem/pelican-octopress-theme).


