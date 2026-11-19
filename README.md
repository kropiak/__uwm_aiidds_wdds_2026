# Wprowadzenie do data science

**Prowadzący:** dr inż. Krzysztof Ropiak (`krzysztof.ropiak@uwm.edu.pl`)  
**Wymiar zajęć:** 30 godzin dydaktycznych  
**Środowisko techniczne:** Python **3.14**, `uv`, Visual Studio Code (+ rozszerzenia *Python* oraz *Jupyter*), Git, `pandas >= 3.0`, `matplotlib`, `seaborn`.

---

## 1. Organizacja zajęć oraz praca z materiałami

1. Przed pierwszym zjazdem wykonaj konfigurację środowiska opisaną krok po kroku w pliku [SETUP.md](SETUP.md) (instrukcje dla systemów **Windows, macOS oraz Linux**).
2. Materiały podzielone są na logiczne moduły w katalogu `modules/`. W katalogu `solutions/` znajdują się wersje notatników z przykładowymi rozwiązaniami wszystkich ćwiczeń.
3. Każdy moduł zbudowany jest według stałego rytmu dydaktycznego:
   - **Wprowadzenie teoretyczne** wraz z odnośnikami do oficjalnej dokumentacji Pythona 3.14 (`https://docs.python.org/3.14/`), dokumentów PEP (`https://peps.python.org/`) oraz dokumentacji bibliotek,
   - **Atomowe przykłady** (jedna koncepcja = jedna krótka komórka kodu z omówieniem),
   - **Ćwiczenie powtórzeniowe** wykonywane bezpośrednio po przykładach,
   - **Sekcje opcjonalne („Dla chętnych / Wyzwanie”)** dla osób posiadających wcześniejsze doświadczenie programistyczne.

---

## 2. Struktura modułów

| Moduł | Katalog | Zakres tematyczny |
| :--- | :--- | :--- |
| **Moduł 0** | `modules/00_srodowisko_i_narzedzia/` | Interpreter CPython 3.14, IDE (VS Code, PyCharm), uruchamianie kodu z plików `.py` i REPL, środowiska wirtualne (`venv`, `pip`, PyPI, PEP 440 oraz nowoczesny `uv`), wprowadzenie do narzędzia Jupyter Notebook |
| **Moduł 1** | `modules/01_git_markdown_pep8/` | Praktyczny warsztat Git (inicjalizacja, `add`, `commit`, `diff`, `log`, `restore`, `.gitignore`, GitHub, gałęzie i scalanie), język Markdown na bazie budowy dokumentacji projektu, historia języka Python, proces PEP (PEP 20, PEP 8) |
| **Moduł 2** | `modules/02_typy_danych_i_operatory/` | Operatory (arytmetyczne, przypisania, porównania, logiczne, tożsamości, przynależności, bitowe, `:=`), typy liczbowe (`int`, `float`, `Decimal`), typ `str` (indeksowanie, *slicing*, metody) oraz formatowanie napisów (f-stringi, sekwencje sterujące, Unicode) |
| **Moduł 3** | `modules/03_kolekcje/` | Struktury danych: `list`, `dict`, `tuple`, `set` oraz sekwencja `range` (mutowalność, operacje *in-place*, rozpakowywanie, operacje mnogościowe, alokacja pamięci i złożoność) |
| **Moduł 4** | `modules/04_warunki_i_petle/` | Instrukcje warunkowe `if/elif/else`, dopasowanie wzorców `match/case` (PEP 622/634), pętle `for` oraz `while`, `enumerate`, `zip`, `break`, `continue`, standardowe wejście/wyjście (`input`, `sys.stdin`/`stdout`) |
| **Moduł 5** | `modules/05_funkcje_comprehensions_moduly/` | Wyrażenia *comprehensions* (`list`, `dict`, `set`), definiowanie własnych funkcji (`def`, argumenty pozycyjne, domyślne, nazwane, `*args`, `**kwargs`, zasięg LEGB, docstringi), tworzenie własnych modułów `.py` i pakietów (`__init__.py`, `__all__`) |
| **Moduł 6** | `modules/06_pliki_i_wyjatki/` | Obsługa plików tekstowych (`open`, menedżer kontekstu `with`, kodowania znaków, `pathlib.Path`), hierarchia i obsługa wyjątków (`try/except/else/finally`), serializacja `json` oraz pliki `csv` (`reader`, `writer`, `DictReader`, `DictWriter`) |
| **Moduł 7** | `modules/07_programowanie_obiektowe/` | Klasa i obiekt, klasa bazowa `object`, `isinstance`/`issubclass`, konstruktor `__init__`, atrybuty i metody, dziedziczenie i `super()`, przesłanianie metod, metody specjalne (`__str__`, `__repr__`, `__eq__`, `__mul__`, `__getitem__` z obsługą `slice`), kompozycja obiektów, `@property`, `@dataclass` |
| **Moduł 8** | `modules/08_pandas_podstawy/` | Podstawy analizy danych w `pandas >= 3.0`: `Series`, `DataFrame`, mechanizm *Copy-on-Write*, wczytywanie i inspekcja danych, selekcja (`loc`, `iloc`, maski logiczne, `isin`), czyszczenie braków i duplikatów, grupowanie `groupby` |
| **Moduł 9** | `modules/09_wizualizacja_wstep/` | Zasygnalizowanie możliwości wizualizacji danych w `matplotlib` (`Figure`, `Axes`, `savefig`) oraz `seaborn` (`histplot`, `boxplot`, `scatterplot`, `countplot`) |
| **Projekt** | `modules/10_projekt_eda/` | Wymagania i szablon zaliczeniowego mini-projektu EDA (realizowanego poza godzinami zajęć) |

---

## 3. Literatura i dokumentacja

1. **Oficjalna dokumentacja Python 3.14:** [https://docs.python.org/3.14/](https://docs.python.org/3.14/)
2. **Indeks dokumentów PEP (Python Enhancement Proposals):** [https://peps.python.org/](https://peps.python.org/)
3. **Dokumentacja narzędzia `uv`:** [https://docs.astral.sh/uv/](https://docs.astral.sh/uv/)
4. **Dokumentacja `pandas` (3.x):** [https://pandas.pydata.org/docs/](https://pandas.pydata.org/docs/)
5. **Dokumentacja `matplotlib` oraz `seaborn`:** [https://matplotlib.org/stable/](https://matplotlib.org/stable/), [https://seaborn.pydata.org/](https://seaborn.pydata.org/)
6. **Pro Git (S. Chacon, B. Straub):** [https://git-scm.com/book/pl/v2](https://git-scm.com/book/pl/v2)
7. **Mark Lutz**, *Python. Wprowadzenie (Learning Python)*, Helion / O'Reilly.
8. **Real Python Tutorials:** [https://realpython.com/](https://realpython.com/)
