# LifeGame
**Jeu de la vie de Conway en Python.**   
Lancement :

```
    python -m venv venv
    pip install -r requirements.txt
    jupyter lab
```

Ouvrir main.ipynb   

```
from src.board import Board
from src.entity import Entity

t0 = Board((30, 60), Entity.canon(), offset = (2, 10))
t0.plot()
t0.animate(n_max=100)
```
