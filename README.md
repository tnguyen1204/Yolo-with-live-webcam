# Yolo-with-live-webcam : Goal and how to use it
This repo is using YoloV8 on your live webcam
In order to use it : 
1. Clone the repo
2. On a terminal _pip install -r requirements.txt_
3. And then _python webcam_yolo.py_
4. Enjoy :)

# MEMO
### Environnement virtuel
* Ouvrir un terminal windows 
* Créer l'env virt appelé "venv": _python -m venv venv_
* Activer "venv" l'env virt : _venv\Scripts\activate_
* Telecharger toutes les dépendances d'un "Requirements.txt" : _pip install -r requirements.txt_
* Lancer VSCode : _code ._
* Désactiver "venv" l'env virt : _deactivate_
* Arreter les dépendances : _pip freeze > requirements.txt_
* Pour installer les dépendances sur un autre env virtuel : _pip install -r requirements.txt_

### GitHub
#### Exemple théorique
* Cloner le git initial : git clone https://github.com/tnguyen1204/Yolo-with-live-webcam
* Copier coller les nouveaux fichiers dans le dossier du repo créer dans l'étape précédente
* Se placer dans le fichier qu'on vient de cloner : cd Yolo-with-live-webcam
* git init  # Initialisez le dépôt Git
* git add .  # Ajoutez tous les fichiers au dépôt
* git commit -m "Initial commit"  # Faites un commit avec un message
* git remote add origin https://github.com/votre_nom_utilisateur/mon_projet.git  # Ajou# tez l'URL de votre dépôt GitHub
* git push -u origin master  # Poussez vos commits vers GitHub

#### Exemple réel : 
C:\Users\TheoN\Desktop\YOLO GIT - Copie>git clone https://github.com/tnguyen1204/Yolo-with-live-webcam
Cloning into 'Yolo-with-live-webcam'...
remote: Enumerating objects: 3, done.
remote: Counting objects: 100% (3/3), done.
remote: Total 3 (delta 0), reused 0 (delta 0), pack-reused 0
Receiving objects: 100% (3/3), done.

C:\Users\TheoN\Desktop\YOLO GIT - Copie>ls
'ls' n’est pas reconnu en tant que commande interne
ou externe, un programme exécutable ou un fichier de commandes.
C:\Users\TheoN\Desktop\YOLO GIT - Copie>cd Yolo-with-live-webcam

C:\Users\TheoN\Desktop\YOLO GIT - Copie\Yolo-with-live-webcam>git add requirements.txt
fatal: pathspec 'requirements.txt' did not match any files

C:\Users\TheoN\Desktop\YOLO GIT - Copie\Yolo-with-live-webcam>git add requirements.txt

C:\Users\TheoN\Desktop\YOLO GIT - Copie\Yolo-with-live-webcam>git status
On branch main
Your branch is up to date with 'origin/main'.

Changes to be committed:
  (use "git restore --staged <file>..." to unstage)
        new file:   requirements.txt

Untracked files:
  (use "git add <file>..." to include in what will be committed)
        webcam_yolo.py


C:\Users\TheoN\Desktop\YOLO GIT - Copie\Yolo-with-live-webcam>git add webcam_yolo.py

C:\Users\TheoN\Desktop\YOLO GIT - Copie\Yolo-with-live-webcam>g
it status
On branch main
Your branch is up to date with 'origin/main'.

Changes to be committed:
  (use "git restore --staged <file>..." to unstage)
        new file:   requirements.txt
        new file:   webcam_yolo.py


C:\Users\TheoN\Desktop\YOLO GIT - Copie\Yolo-with-live-webcam>g
it commit -m "Test fonctionnel"
[main 18fe011] Test fonctionnel
 2 files changed, 36 insertions(+)
 create mode 100644 requirements.txt
 create mode 100644 webcam_yolo.py

C:\Users\TheoN\Desktop\YOLO GIT - Copie\Yolo-with-live-webcam>g
it push origin main
Enumerating objects: 5, done.
Counting objects: 100% (5/5), done.
Delta compression using up to 16 threads
Compressing objects: 100% (4/4), done.
Writing objects: 100% (4/4), 1.59 KiB | 812.00 KiB/s, done.
Total 4 (delta 0), reused 0 (delta 0), pack-reused 0 (from 0)
To https://github.com/tnguyen1204/Yolo-with-live-webcam
   dc36c2d..18fe011  main -> main

### Ouvrir flux vidéo de la webcam
 
import cv2

cap = cv2.VideoCapture(0)  # 0 pour la première webcam, 1 pour la deuxième, etc.

if not cap.isOpened():
    print("Erreur : Impossible d'ouvrir la webcam")
    exit()

while True:
    # Lire une frame
    ret, frame = cap.read()

    # Vérifier si la lecture a réussi
    if not ret:
        print("Erreur : Impossible de lire la frame")
        break

    # Afficher la frame
    cv2.imshow('Webcam', frame)

    # Quitter la boucle si l'utilisateur appuie sur 'q'
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()

