# CSS0402

* Szerző: Sallai András
* Copyright © 2014, Sallai András
* Szerkesztve: 2014-2024
* Licenc: CC BY-SA 4.0
* Web: https://szit.hu

## Feladat

1. Hozz létre egy `container` osztályú divet.
2. A divben legyen egy `h1` cím.
3. A cím után egy `doboz` osztályú div.
4. A doboz után egy 60 szóból álló `p` elem.
5. A `style.css` fájl segítségével formázd a kinézetet az alábbiak szerint:
   - A `.container` legyen coral színű, 10% külső margóval, 20px felső-alsó és 10px oldalsó belső margóval.
   - A `.container` szegélye 3px solid gold.
   - A `.doboz` legyen 80x80 px méretű, aqua háttérszínnel, jobbra lebegtetve, 10px bal margóval.
   - A `h1` legyen nagybetűs és talpatlan betűtípusú.
   - A `p` elem szövege legyen sorkizárt, a harmadik szó (`dolor`) legyen **félkövér**.

## Ellenőrzés
Használj `pytest`-et az automatikus ellenőrzéshez. Futtatás:
```sh
pytest test_webpage.py
