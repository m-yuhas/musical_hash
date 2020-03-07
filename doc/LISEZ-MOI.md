# Hashage Musicale
## Introduction
Tout comme l'algorithme «[Random Art](https://github.com/calmh/randomart)»
fournit une méthode pour visualiser les clés RSA, l'hachage musicale fournit
une méthode pour «visualiser» la sortie d'une fonction de hachage comme
l'audio.  Génère une mélodie unique pour chaque valeur de hachage que peut être
exportée comme fichier wave, fichier midi, ou une liste des notes en la
notation ABC.

## Lancement Rapide
* Clonez ce dépôt:

```
git clone https://github.com/m-yuhas/musical_hash.git
```

* Construisez le paquet:

```
python setup.py sdist
```

* Installez le paquet dans l'environment virtuel voulu:

```
python -m pip install musical_hash-x.y.z.tar.gz
```

* Dans une console Python, importez le paquet:

```python
>>> import musical_hash
```

* Construisez l'objet hachage musicale:

```python
>>> hash = musical_hash.MusicalHash(b'Hello World!', 'md5')
```

* Exportez l'hachage comme une fichier wave dans la tonalité de A mineur pentatonique:

```python
>>> hash.wave('hash.wav', key=musical_hash.A_PENTATONIC_MINOR)
```

* Ou, exportez comme une fichier midi:

```python
>>> hash.midi('hash.mid', key=musical_hash.A_PENTATONIC_MINOR)
```

## Documentation de l'IPA
Pour la documentation complète, [cliquez ici](api_documentation.md).
Actuellement la documentation est seulement disponible en anglais.

## Théorie d'Operation
Dans la musique classique il y a douze demi-tones dans une octave. La première
note de l'octave subséquente est la première harmonique de l'octave précédente.
Ainsi nous allons considérer une octave singulière comme l'univers des toutes
les notes disponible pour «visualiser» une séquence d'octets.  La majorité
des compositions musicales sont écrits dans une tonalité spécifique, laquelle
est une inclusion des toutes les notes possibles.  Dans une octave singulière,
chaque tonalité a un nombre de notes fini, alors si nous considerons la
séquence d'octets comme un nombre entier, nous pouvons trouver la
représentation de cet entier dans une base laquelle est égale au nombre de
notes dans la tonalité.  Ensuite nous signons chaque chiffre de cette
représentation une note musicale.  Ce paquet aussi comprend beaucoup de
tonalités diatonique et pentatonique comme constantes.

## Dépendances
Ce paquet seulement supporte Python version 3.5 et plus.  Ce paquet devrait
pouvoir être exécuté dans toute système POSIX aussi bien que Windows 7 et plus.

Les suivants paquets Pypi sont requis:
* mido
* numpy
* wavio

## Comment Contribuer
Suggestions et «pull requests» sont bienvenus.  Si trouvez un bug et vous
n'avez pas le temps à le régler vous-même, s'il vous plaît ouvrez un problème.
Aussi, je ne suis pas un experte à la théorie de la musique; si vous trouvez
une erreur avec la façon j'ai appelé une tonalité ou un terme musical, s'il
vous plaît dites-moi ainsi je peux apprendre.

## Tâches Futures
- Faire une hachage que comprend accords pour diminuer la longueur de la
    mélodie et augmenter l'unicité perçue de chaque hachage.

## Voyez Aussi
Initialement je pensais que j'étais la seule personne avec cette idée, mais
après de je l'avais implémenté j'ai trouvé le
[dépôt](https://github.com/jmaclean/musical-hash) de cet homme. Alors
vérifiez-le si vous voulez voir une autre implémentation de le même concept.