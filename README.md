# LifeGame
**Jeu de la vie de Conway en Python.**   
Lancement :

```
    python -m venv venv
    pip install -r requirements.txt
    jupyter lab
```

Ouvrir main.ipynb   
Initialiser un instant initial

```
t0 = Board(20, [[2, 6], [2, 5], [2, 4], [1, 4], [0, 5]])
```


Pour afficher le tableau initial :
```
t0.plot(**kwargs)
```

Pour enregistrer l'animation en .gif
```
t0.animate()
```