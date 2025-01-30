import pytest
from bs4 import BeautifulSoup

HTML_FILE = "index.html"
CSS_FILE = "style.css"

def read_html():
    """Beolvassa az HTML fájlt és BeautifulSoup objektummá alakítja."""
    with open(HTML_FILE, "r", encoding="utf-8") as f:
        return BeautifulSoup(f, "html.parser")

def read_css():
    """Beolvassa a CSS fájlt szövegként."""
    with open(CSS_FILE, "r", encoding="utf-8") as f:
        return f.read()

# ---- HTML szerkezet tesztelése ----
def test_container_exists():
    soup = read_html()
    assert soup.find("div", class_="container"), "Hiányzik a .container div"

def test_h1_exists():
    soup = read_html()
    assert soup.find("h1"), "Hiányzik a h1 elem"

def test_doboz_exists():
    soup = read_html()
    assert soup.find("div", class_="doboz"), "Hiányzik a .doboz div"

def test_p_exists():
    soup = read_html()
    assert soup.find("p"), "Hiányzik a p elem"

# ---- Szövegformázás tesztelése ----
def test_third_word_bold():
    soup = read_html()
    p = soup.find("p")
    assert p, "Hiányzik a p elem"
    words = p.text.split()
    assert len(words) >= 3, "A p elemben nincs legalább három szó"
    bold_words = [b.text for b in p.find_all("strong")]
    assert "dolor" in bold_words, "A harmadik szó nem félkövér ('dolor')"

# ---- CSS szabályok tesztelése ----
def test_container_background():
    css = read_css()
    assert "background-color: coral" in css, "A .container háttérszíne nem coral"

def test_container_margin():
    css = read_css()
    assert "margin: 10%" in css, "A .container külső margója nem 10%"

def test_container_padding():
    css = read_css()
    assert "padding: 20px 10px" in css, "A .container belső margója nem megfelelő"

def test_container_border():
    css = read_css()
    assert "border: 3px solid gold" in css, "A .container szegélye nem megfelelő"

def test_doboz_size():
    css = read_css()
    assert "width: 80px" in css and "height: 80px" in css, "A .doboz mérete nem 80x80px"

def test_doboz_background():
    css = read_css()
    assert "background-color: aqua" in css, "A .doboz háttérszíne nem aqua"

def test_doboz_float():
    css = read_css()
    assert "float: right" in css, "A .doboz nincs jobbra lebegtetve"

def test_doboz_margin():
    css = read_css()
    assert "margin-left: 10px" in css, "A .doboz bal margója nem 10px"

