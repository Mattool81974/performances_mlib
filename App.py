from MLib import *

TAILLE=(700, 700)

fenetre=display.set_mode(TAILLE)
app = MFenetre(fenetre, "Mon app", afficherFps=True)
entree1 = MEntreeTexte((0, 0), (175, 50), app, texte="Test"*50, ligneMax=4, longueurMax=1000)
entree2 = MEntreeTexte((175, 0), (175, 50), app, texte="Test"*50, ligneMax=2, policeTaille=24, longueurMax=1000)
entree3 = MEntreeTexte((350, 0), (175, 50), app, texte="Test"*50, ligneMax=4, policeTaille=8, longueurMax=1000)
entree4 = MEntreeTexte((525, 0), (175, 50), app, texte="Test"*50, ligneMax=4, longueurMax=1000)
bouton1 = MBouton("Test", (0, 75), (175, 75), app)
bouton2 = MBouton("Test", (175, 75), (175, 75), app)
bouton3 = MBouton("Test", (350, 75), (175, 75), app)
bouton4 = MBouton("Test", (525, 75), (175, 75), app)
image = MImage("brutus.png", (0, 150), (700, 300), app, imageAlignement="CJ")
bordure1 = MBordure((0, 450), (700, 250), app, bordureCouleur=(0, 0, 0))
bordure2 = MBordure((50, 25), (600, 200), bordure1, bordureCouleur=(255, 0, 0))
bordure3 = MBordure((50, 25), (500, 150), bordure2, bordureCouleur=(0, 255, 0))
bordure4 = MBordure((50, 25), (400, 100), bordure3, bordureCouleur=(0, 0, 255))

while True:
    app.frame()
    display.flip()