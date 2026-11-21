# Moduł 1 (cz. 1): Praktyczny warsztat Git oraz język znaczników Markdown

> **Oficjalna dokumentacja referencyjna:**
> - Dokumentacja systemu Git: [https://git-scm.com/doc](https://git-scm.com/doc)
> - Książka *Pro Git* (S. Chacon, B. Straub — rozdz. 1–3): [https://git-scm.com/book/pl/v2](https://git-scm.com/book/pl/v2)
> - GitHub Docs — *Get started with Git*: [https://docs.github.com/en/get-started/using-git/about-git](https://docs.github.com/en/get-started/using-git/about-git)
> - GitHub Docs — *Basic writing and formatting syntax (Markdown)*: [https://docs.github.com/en/get-started/writing-on-github/getting-started-with-writing-and-formatting-on-github/basic-writing-and-formatting-syntax](https://docs.github.com/en/get-started/writing-on-github/getting-started-with-writing-and-formatting-on-github/basic-writing-and-formatting-syntax)
> - Markdown Guide: [https://www.markdownguide.org/basic-syntax/](https://www.markdownguide.org/basic-syntax/)

---

## Efekty uczenia się

Po zrealizowaniu tego warsztatu potrafisz:
- wyjaśnić, czym jest system kontroli wersji i jak przepływają zmiany między katalogiem roboczym, poczekalnią (*staging area*), repozytorium lokalnym i serwisem GitHub,
- skonfigurować tożsamość i podstawowe parametry narzędzia Git na swoim komputerze (Windows, macOS, Linux),
- utworzyć lokalne repozytorium, rejestrować zmiany za pomocą `git add` oraz `git commit`, a także badać historię zmian poleceniami `git status`, `git diff` oraz `git log`,
- cofać niezatwierdzone zmiany (`git restore`) i wykluczać pliki ze śledzenia za pomocą pliku `.gitignore`,
- tworzyć kompletną, estetyczną dokumentację projektu w języku **Markdown** na przykładzie spójnego pliku `README.md` dla naszego kursu,
- opublikować lokalne repozytorium w serwisie GitHub (`git remote`, `git push`),
- tworzyć, przełączać i scalać gałęzie (*branches*: *fast-forward merge* oraz *merge commit*) i odczytywać graf historii (`git log --graph`).

---

## Lista kontrolna przed startem

Upewnij się, że masz przygotowane:
1. Konto w serwisie [https://github.com/](https://github.com/) (zalecane włączenie uwierzytelniania dwuskładnikowego 2FA).
2. Zainstalowane narzędzie **Git** (zgodnie z [SETUP.md](../../SETUP.md)). Na systemie Windows zalecamy korzystanie z terminala **Git Bash** (instalowanego razem z *Git for Windows*), dzięki czemu wszystkie polecenia terminalowe wyglądają identycznie na Windows, macOS oraz Linux.
3. Zainstalowany edytor **Visual Studio Code**.

---

## 1. Dlaczego używamy systemu kontroli wersji?

### Wprowadzenie
System kontroli wersji (**VCS — *Version Control System***) rejestruje pełną historię zmian w plikach projektu. Pozwala sprawdzić, kto, kiedy i dlaczego zmienił dany fragment kodu lub analizy, bezpiecznie wrócić do wcześniejszej działającej wersji oraz współpracować z innymi osobami bez wzajemnego nadpisywania swojej pracy (i bez tworzenia plików `analiza_v1.ipynb`, `analiza_v2_final.ipynb`, `analiza_v2_ostateczna.ipynb`).

W przeciwieństwie do starszych systemów, które zapisywały jedynie różnice tekstowe między plikami, **Git przechowuje historię jako serię migawek (*snapshots*)** całego projektu, identyfikowanych unikalnym skrótem kryptograficznym (40-znakowy hash SHA-1).

Git utrzymuje Twoje pliki w trzech lokalnych strefach, a każda zmiana przemieszcza się od lewej do prawej strony poniższego schematu:

```text
Working directory  --git add-->  Staging area  --git commit-->  Local repository  --git push-->  GitHub
(katalog roboczy:                (poczekalnia / indeks:         (historia wersji                 (zdalna kopia
 Twoje pliki na dysku)            co trafi do kolejnego          na Twoim komputerze              w chmurze)
                                  commita)                       w katalogu .git)
```

> **Ważne rozróżnienie:** **Git** to program działający lokalnie na Twoim komputerze (nawet bez dostępu do internetu). **GitHub** to zewnętrzny serwis internetowy służący do przechowywania kopii repozytoriów Git w chmurze i współpracy zespołowej.

---

## 2. Jednorazowa konfiguracja początkowa (`git config`)

> **Dokumentacja:** [https://git-scm.com/book/pl/v2/Pierwsze-kroki-Wst%C4%99pna-konfiguracja-Gita](https://git-scm.com/book/pl/v2/Pierwsze-kroki-Wst%C4%99pna-konfiguracja-Gita)

### Wprowadzenie
Zanim utworzysz pierwszy punkt zapisu (*commit*), musisz przedstawić się narzędziu Git. Twoje imię, nazwisko oraz adres e-mail są trwale zapisywane w metadanych każdego commita. Ponadto ustawimy domyślną nazwę głównej gałęzi na `main`, wskażemy VS Code jako domyślny edytor komunikatów oraz ujednolicimy zachowanie polecenia `git pull`.

Flaga `--global` zapisuje ustawienia w Twoim profilu użytkownika w systemie operacyjnym (obowiązują dla wszystkich projektów na Twoim koncie). Gdybyś pracował na współdzielonym koncie laboratoryjnym, użyłbyś flagi `--local` wewnątrz konkretnego repozytorium.

### Przykład 2.1 — Konfiguracja tożsamości i domyślnych opcji
Otwórz terminal (**Git Bash** na Windows lub **Terminal** na macOS/Linux) i wykonaj poniższe polecenia, podstawiając własne dane:

```bash
git config --global user.name "Jan Kowalski"
git config --global user.email "twoj-email-z-githuba@example.com"
git config --global init.defaultBranch main
git config --global core.editor "code --wait"
git config --global pull.rebase false
```

### Przykład 2.2 — Weryfikacja zapisanej konfiguracji
Sprawdź wszystkie aktywne ustawienia wraz ze ścieżką pliku konfiguracyjnego, z którego pochodzą:

```bash
git config --list --show-origin
```

> **Uwaga o znakach końca linii (`CRLF` vs `LF`):**  
> System Windows kończy wiersze tekstu dwoma znakami `CRLF` (`\r\n`), natomiast systemy macOS i Linux pojedynczym znakiem `LF` (`\n`). Instalator *Git for Windows* domyślnie ustawia opcję `core.autocrlf` na `true`, automatycznie konwertując znaki końca linii przy zapisie i odczycie, aby repozytorium pozostało spójne między różnymi systemami operacyjnymi. Możesz to sprawdzić poleceniem `git config --get core.autocrlf`. Komunikat ostrzegawczy *„LF will be replaced by CRLF”* podczas `git add` jest całkowicie niegroźny.

### Ćwiczenie 1.1 — Konfiguracja własnego środowiska Git
1. Wykonaj powyższe komendy `git config --global` ze swoim prawdziwym imieniem, nazwiskiem oraz adresem e-mail powiązanym z kontem GitHub.
2. Uruchom `git config --list --show-origin` i upewnij się, że `user.name`, `user.email` oraz `init.defaultBranch=main` są widoczne na liście.

---

## 3. Twoje pierwsze repozytorium lokalne (`init`, `status`, `add`, `commit`, `diff`, `log`)

> **Dokumentacja:** [https://git-scm.com/book/pl/v2/Podstawy-Gita-Pierwsze-repozytorium-Gita](https://git-scm.com/book/pl/v2/Podstawy-Gita-Pierwsze-repozytorium-Gita)

### Wprowadzenie
Nowe repozytorium lokalne inicjalizujemy poleceniem `git init`. Tworzy ono ukryty podkatalog `.git`, w którym Git przechowuje bazę obiektów, indeks oraz historię commitów (nigdy nie edytuj plików wewnątrz `.git` ręcznie!).

Każdy plik w katalogu roboczym może znajdować się w jednym z głównych stanów:
- **Untracked (nieśledzony)** — nowy plik, o którego istnieniu Git jeszcze nie pamięta w historii,
- **Modified (zmodyfikowany)** — plik śledzony, którego zawartość na dysku różni się od ostatniego commita,
- **Staged (w poczekalni)** — plik zgłoszony poleceniem `git add` do zapisania w najbliższym commicie.

### Przykład 3.1 — Utworzenie folderu projektu i inicjalizacja repozytorium
W terminalu przejdź do swojego katalogu domowego (lub katalogu projektów) i utwórz nowy folder ćwiczeniowy `wds-git-lab`:

```bash
cd ~
mkdir wds-git-lab
cd wds-git-lab
git init
```

### Przykład 3.2 — Utworzenie pierwszego pliku i sprawdzenie stanu (`git status`)
Utwórzmy plik `README.md` z tytułem naszego projektu i sprawdźmy reakcję Gita:

```bash
echo "# Wprowadzenie do Data Science — moje repozytorium" > README.md
git status
```
Git poinformuje, że znajdujesz się na gałęzi `main`, nie ma jeszcze żadnych commitów, a plik `README.md` ma status **Untracked files**.

### Przykład 3.3 — Dodanie pliku do poczekalni (`git add`) i pierwszy commit (`git commit`)
Przenosimy plik do poczekalni (*Staging area*) i utrwalamy pierwszą migawkę w historii:

```bash
git add README.md
git status
git commit -m "Add README with course title"
```

### Przykład 3.4 — Modyfikacja pliku i podgląd różnic (`git diff` vs `git diff --staged`)
Dopiszmy drugi wiersz do `README.md` i porównajmy zmiany przed oraz po wykonaniu `git add`:

```bash
echo "Repozytorium utworzone podczas zajęć z Wprowadzenia do Data Science." >> README.md
git status
git diff
```
Polecenie `git diff` (bez flag) pokazuje różnice między **katalogiem roboczym** a **poczekalnią** (zmiany, których jeszcze nie dodałeś przez `git add`). Dodajmy teraz zmianę do poczekalni:

```bash
git add README.md
git diff
git diff --staged
```
Zauważ, że po `git add` zwykłe `git diff` nie zwraca już nic, natomiast `git diff --staged` pokazuje dokładnie to, co czeka w poczekalni na najbliższy commit! Zatwierdźmy zmianę i obejrzyjmy historię:

```bash
git commit -m "Describe the purpose of the repository"
git log
git log --oneline
```

**Zasady pisania dobrych komunikatów commitów (*Good commit messages*):**
- Używaj trybu rozkazującego (np. *Add notes file* / *Dodaj plik z notatkami*, a nie *Added* czy *Dodano*).
- Pierwsza linia powinna być zwięzła (do ok. 50 znaków) i jasno mówić, **co** robi dany commit.
- Jeden commit powinien odpowiadać **jednej spójnej, logicznej zmianie**.

### Ćwiczenie 1.2 — Śledzenie nowego pliku i historia zmian
1. W katalogu `wds-git-lab` utwórz drugi plik o nazwie `notes.txt` zawierający trzy wiersze tekstu o tym, czego oczekujesz po kursie *Wprowadzenie do Data Science*.
2. Sprawdź `git status`, dodaj plik do poczekalni (`git add notes.txt`) i wykonaj commit z czytelnym komunikatem.
3. Otwórz `notes.txt` w VS Code (`code notes.txt`), zmodyfikuj jeden z wierszy, zapisz plik i sprawdź różnicę poleceniem `git diff`.
4. Dodaj zmianę do poczekalni i wykonaj kolejny commit. Sprawdź za pomocą `git log --oneline`, czy Twoja historia liczy już co najmniej **4 commity**.

---

## 4. Język znaczników Markdown — budowa spójnego dokumentu `README.md` dla kursu

> **Dokumentacja:** [https://www.markdownguide.org/basic-syntax/](https://www.markdownguide.org/basic-syntax/) oraz [https://www.markdownguide.org/extended-syntax/](https://www.markdownguide.org/extended-syntax/)

### Wprowadzenie
**Markdown** to lekki język znaczników stworzony po to, aby pisać zwykły tekst, który jest czytelny sam w sobie, a jednocześnie może być automatycznie renderowany do estetycznego dokumentu HTML (na GitHubie, w VS Code oraz w komórkach tekstowych Jupyter Notebooka).

Zamiast uczyć się znaczników w oderwaniu od praktyki, **zbudujemy teraz krok po kroku jeden kompletny, spójny dokument `README.md`** będący oficjalną wizytówką Twojego repozytorium na przedmiocie *Wprowadzenie do Data Science*.

Otwórz plik `README.md` ze swojego repozytorium `wds-git-lab` w edytorze VS Code:
```bash
code README.md
```
Otwórz obok podgląd na żywo w VS Code skrótem **`Ctrl+Shift+V`** (na macOS: `Cmd+Shift+V`) lub kliknij ikonę lupy na pasku zakładek edytora (*Open Preview to the Side*).

---

### Krok 4.1 — Nagłówki (`#`), akapity i miękkie przełamanie wiersza

#### Wprowadzenie
- **Nagłówki** tworzymy znakiem `#` powtórzonym od 1 do 6 razy (odpowiedniki `<h1>`–`<h6>` w HTML). Po znaku `#` zawsze stawiamy spację! Alternatywnie podkreślenie tekstu w kolejnej linii znakami `===` daje nagłówek 1. poziomu, a `---` nagłówek 2. poziomu.
- **Nowy akapit (paragraf)** wymaga pozostawienia **jednej pustej linii** pomiędzy blokami tekstu. Zwykłe naciśnięcie `Enter` bez pustej linii zostanie złączone w jeden ciągły akapit.
- **Miękkie przełamanie linii (*soft break*, `<br>`)** bez odstępu akapitowego uzyskujemy, wstawiając **dwie spacje** na samym końcu wiersza przed naciśnięciem `Enter`.

#### Przykład 4.1 — Sekcja tytułowa i metryczka naszego dokumentu kursu
```markdown
# Wprowadzenie do Data Science — Portfolio Studenta

Dokumentacja repozytorium ćwiczeniowego ze studiów podyplomowych.  
Prowadzący: dr inż. Krzysztof Ropiak  
Rok akademicki: 2026/2027

## 1. O projekcie

W tym repozytorium gromadzę skrypty w języku Python 3.14 oraz notatniki Jupyter realizowane w ramach przedmiotu.
```

#### Ćwiczenie 1.3 (Markdown — Krok 1)
Zastąp zawartość swojego pliku `README.md` powyższą strukturą nagłówków i metryczką (uzupełniając ją o własne imię i nazwisko z miękkim przełamaniem linii — dwie spacje na końcu wiersza). Sprawdź w podglądzie `Ctrl+Shift+V`, czy wiersze metryczki wyświetlają się jeden pod drugim bez pustego odstępu akapitowego.

---

### Krok 4.2 — Wyróżnienia tekstu (`*`, `**`, `***`) oraz bloki cytowania (`>`)

#### Wprowadzenie
- *Kursywa* (`<em>`): pojedyncze gwiazdki `*tekst*` lub podkreślenia `_tekst_`.
- **Pogrubienie** (`<strong>`): podwójne gwiazdki `**tekst**` lub podkreślenia `__tekst__`.
- ***Pogrubiona kursywa***: potrójne gwiazdki `***tekst***` lub zagnieżdżenie `_*tekst*_`.
  *(Uwaga: nie wstawiaj spacji bezpośrednio po znaku otwierającym ani przed zamykającym, np. `** błąd **` wyłączy formatowanie!)*
- **Blok cytowania (`>`):** rozpoczęcie wiersza od znaku `>` tworzy wyróżniony blok cytatu lub uwagi (można go zagnieżdżać podwójnym `>>`).

#### Przykład 4.2 — Rozbudowa sekcji „O projekcie” w naszym dokumencie
```markdown
Głównym celem przedmiotu jest opanowanie **solidnych podstaw języka Python** oraz narzędzi pracy analityka danych, takich jak *Jupyter Notebook*, *Git* oraz biblioteka ***pandas 3.0***.

> Zasada przewodnia kursu (PEP 20 — *The Zen of Python*):
> „Readability counts. Explicit is better than implicit.”
```

#### Ćwiczenie 1.4 (Markdown — Krok 2)
Dopisz do swojego `README.md` akapit wykorzystujący **pogrubienie**, *kursywę* oraz ***pogrubioną kursywę***, a pod nim umieść dwuwierszowy blok cytowania (`>`).

---

### Krok 4.3 — Listy punktowane, numerowane, zagnieżdżone oraz listy zadań (`- [x]`)

#### Wprowadzenie
- **Listy punktowane:** wiersze zaczynające się od `-`, `*` lub `+` (dobra praktyka: trzymaj się jednego wybranego znaku w całej liście, np. `-`).
- **Listy numerowane:** wiersze zaczynające się od `1.`, `2.` itd.
- **Listy zagnieżdżone:** każdy kolejny poziom zagnieżdżenia poprzedzamy wcięciem o szerokości **4 spacji** (lub wyrównaniem do pierwszego znaku tekstu punktu nadrzędnego).
- **Listy zadań (*Task lists / Checkboxes*):** `- [x]` oznacza zadanie wykonane, a `- [ ]` zadanie oczekujące na realizację.

#### Przykład 4.3 — Sekcja „Stos technologiczny i postęp nauki” w naszym dokumencie
```markdown
## 2. Wykorzystywane narzędzia i postęp prac

### 2.1. Narzędzia w projekcie
1. Środowisko wykonawcze i pakiety:
   - interpreter **CPython 3.14**,
   - menedżer pakietów i środowisk wirtualnych **uv**,
   - biblioteki analityczne:
     - `pandas` (>= 3.0),
     - `matplotlib` oraz `seaborn`.
2. Narzędzia deweloperskie:
   - edytor **Visual Studio Code**,
   - system kontroli wersji **Git** oraz serwis **GitHub**.

### 2.2. Status realizacji modułów
- [x] Moduł 0: Konfiguracja środowiska pracy i Jupyter Notebook
- [x] Moduł 1: Warsztat Git, Markdown oraz standard PEP 8
- [ ] Moduł 2: Typy danych, operatory i łańcuchy znaków
- [ ] Moduł 3: Kolekcje w języku Python
```

#### Ćwiczenie 1.5 (Markdown — Krok 3)
Dodaj do swojego `README.md` sekcję `## 2. Wykorzystywane narzędzia i postęp prac` zawierającą listę zagnieżdżoną (minimum 2 poziomy) oraz listę zadań z polami wyboru `- [x]` i `- [ ]`.

---

### Krok 4.4 — Wyróżnianie kodu w linii (`` ` ``) oraz bloki kodu (```` ``` ````)

#### Wprowadzenie
- **Kod w linii (*inline code*):** pojedyncze odwrócone apostrofy (*backticks*, klawisz pod `Esc`), np. `` `git status` ``, `` `pyproject.toml` ``.
- **Wielowierszowe bloki kodu (*fenced code blocks*):** potrójne odwrócone apostrofy ```` ``` ```` przed i po fragmencie kodu. Dopisanie nazwy języka tuż po otwierających znakach (np. ```` ```bash ````, ```` ```python ````, ```` ```json ````) włącza kolorowanie składni właściwe dla danej technologii.

#### Przykład 4.4 — Sekcja „Instrukcja uruchomienia” w naszym dokumencie
````markdown
## 3. Szybki start (Uruchomienie środowiska)

Aby odtworzyć środowisko wirtualne `.venv` na podstawie pliku `pyproject.toml`, wykonaj w terminalu:

```bash
git clone https://github.com/twoj-login/wds-git-lab.git
cd wds-git-lab
uv sync
```

Przykładowy kod weryfikujący wersję biblioteki `pandas` w Pythonie 3.14:

```python
import pandas as pd

print(f"Zainstalowana wersja pandas: {pd.__version__}")
```
````

#### Ćwiczenie 1.6 (Markdown — Krok 4)
Dopisz do swojego `README.md` sekcję `## 3. Szybki start` zawierającą co najmniej dwa wyróżnienia kodu w linii (`` `...` ``) oraz dwa wielowierszowe bloki kodu: jeden z podświetlaniem `bash` i jeden z podświetlaniem `python`.

---

### Krok 4.5 — Tabele z wyrównaniem kolumn, linki, linie poziome i wzory LaTeX

#### Wprowadzenie
- **Tabele:** kolumny rozdzielamy pionową kreską `|`, a wiersz nagłówkowy oddzielamy od danych wierszem myślników `---`. Dwukropki w wierszu separatora sterują wyrównaniem tekstu w kolumnie:
  - `:---` — wyrównanie do lewej (domyślne),
  - `:---:` — wyśrodkowanie,
  - `---:` — wyrównanie do prawej (zalecane dla kolumn liczbowych).
- **Linki:** `[tekst wyświetlany](https://adres-url)`. Możesz też używać ścieżek względnych do innych plików w repozytorium, np. `[Notatki](notes.txt)`.
- **Obrazki:** `![tekst alternatywny](ścieżka/do/obrazka.png)` (taka sama składnia jak link, ale poprzedzona wykrzyknikiem `!`).
- **Linia pozioma:** trzy myślniki `---` lub trzy gwiazdki `***` w osobnej linii (pamiętaj o pustej linii powyżej!).
- **Wzory matematyczne LaTeX** (obsługiwane w Jupyterze, VS Code i na GitHubie): wewnątrz zdania `$...$` lub w osobnym bloku `$$...$$`.

#### Przykład 4.5 — Sekcja „Podręczna ściągawka i przydatne odnośniki” w naszym dokumencie
```markdown
## 4. Podręczna tabela komend i dokumentacja

| Narzędzie | Polecenie | Zastosowanie | Liczba kroków |
| :--- | :--- | :--- | ---: |
| Git | `git status` | Sprawdzenie stanu plików w katalogu roboczym | 1 |
| Git | `git commit -m "..."` | Zapisanie nowej migawki w historii lokalnej | 2 |
| uv | `uv sync` | Synchronizacja pakietów z plikiem `pyproject.toml` | 1 |

Wzór na średnią arytmetyczną używany w modułach analitycznych:

$$\bar{x} = \frac{1}{n} \sum_{i=1}^{n} x_i$$

---

### Przydatne linki
- [Oficjalna dokumentacja Python 3.14](https://docs.python.org/3.14/)
- [Dokumentacja biblioteki pandas](https://pandas.pydata.org/docs/)
- [Moje notatki z kursu](notes.txt)
```

#### Ćwiczenie 1.7 (Markdown — Krok 5 i zatwierdzenie w Git)
1. Uzupełnij swój plik `README.md` o sekcję 4 zawierającą tabelę (minimum 3 wiersze, z wyrównaniem ostatniej kolumny do prawej strony `---:`), wzór matematyczny, linię poziomą `---` oraz 3 linki (w tym link względny do pliku `notes.txt`).
2. Sprawdź kompletny wygląd dokumentu w podglądzie VS Code (`Ctrl+Shift+V`).
3. Zapisz plik, sprawdź różnice poleceniem `git diff`, a następnie dodaj `README.md` do poczekalni i zatwierdź zmianę:
   ```bash
   git add README.md
   git commit -m "Complete course README documentation in Markdown"
   ```

---

## 5. Cofanie zmian (`git restore`) oraz ignorowanie plików (`.gitignore`)

> **Dokumentacja:**
> - Cofanie zmian: [https://git-scm.com/book/pl/v2/Podstawy-Gita-Cofanie-zmian](https://git-scm.com/book/pl/v2/Podstawy-Gita-Cofanie-zmian)
> - Ignorowanie plików (`.gitignore`): [https://git-scm.com/docs/gitignore](https://git-scm.com/docs/gitignore)

### Wprowadzenie
Podczas codziennej pracy często zdarza się, że:
1. Wprowadzisz przypadkową zmianę w pliku i chcesz szybko przywrócić jego zawartość z ostatniego commita (`git restore <plik>`).
2. Dodasz plik za wcześnie do poczekalni (`git add`) i chcesz go z niej wycofać bez utraty zmian w samym pliku (`git restore --staged <plik>`).
3. W folderze projektu pojawiają się pliki tymczasowe, dzienniki zdarzeń (`*.log`), pobrane środowisko wirtualne (`.venv/`), pamięć podręczna kodu bajtowego (`__pycache__/`) lub ukryte punkty kontrolne notatników (`.ipynb_checkpoints/`), które **nigdy nie powinny trafić do repozytorium Git**. Do ich automatycznego wykluczania służy plik tekstowy o nazwie **`.gitignore`**.

### Przykład 5.1 — Odrzucenie niezatwierdzonej zmiany w katalogu roboczym (`git restore`)
Dopiszmy błędny wiersz do pliku `notes.txt`, sprawdźmy `git status` i cofnijmy modyfikację:

```bash
echo "Przypadkowy błędny wpis" >> notes.txt
git status
git diff
git restore notes.txt
git status
```
> **Ostrzeżenie:** Polecenie `git restore <plik>` bezpowrotnie nadpisuje niezatwierdzone zmiany w tym pliku stanem z ostatniego commita! Używaj go rozważnie.

### Przykład 5.2 — Wycofanie pliku z poczekalni (`git restore --staged`)
```bash
echo "Kolejna robocza notatka" >> notes.txt
git add notes.txt
git status
git restore --staged notes.txt
git status
git restore notes.txt
```

### Przykład 5.3 — Utworzenie i przetestowanie pliku `.gitignore`
Utwórz w katalogu `wds-git-lab` plik `.gitignore` zawierający reguły dla plików tymczasowych oraz typowych artefaktów Pythona i Jupytera:

```gitignore
*.log
temp/
.venv/
__pycache__/
.ipynb_checkpoints/
```

Przetestujmy działanie reguł, tworząc plik `debug.log` oraz katalog `temp/` z plikiem tymczasowym:

```bash
echo "debug output" > debug.log
mkdir temp
echo "tymczasowe dane" > temp/scratch.txt
git status
```
Zauważ, że ani `debug.log`, ani folder `temp/` nie pojawiają się na liście nieśledzonych plików — Git całkowicie je ignoruje! Widoczny jest natomiast sam plik `.gitignore`, który należy dodać do repozytorium:

```bash
git add .gitignore
git commit -m "Add .gitignore for logs, temp files and Python environment"
```

> **Co zrobić, jeśli plik został już wcześniej zatwierdzony w commicie, a dopiero potem dopisaliśmy go do `.gitignore`?**  
> Reguły `.gitignore` działają wyłącznie na pliki nieśledzone (*untracked*). Aby przestać śledzić plik bez usuwania go z dysku, używamy polecenia:
> ```bash
> git rm --cached nazwa_pliku
> ```

### Ćwiczenie 1.8 — Praktyka z `.gitignore` i `git restore`
1. Dopisz do pliku `.gitignore` regułę ignorującą pliki z rozszerzeniem `*.tmp`.
2. Utwórz plik `test.tmp` (`echo "test" > test.tmp`) i upewnij się za pomocą `git status`, że Git go ignoruje.
3. Zatwierdź zmodyfikowany plik `.gitignore` nowym commitem.

---

## 6. Publikacja repozytorium w serwisie GitHub (`git remote`, `git push`)

> **Dokumentacja:** [https://docs.github.com/en/migrations/importing-source-code/using-the-command-line-to-import-source-code/adding-locally-hosted-code-to-github](https://docs.github.com/en/migrations/importing-source-code/using-the-command-line-to-import-source-code/adding-locally-hosted-code-to-github)

### Wprowadzenie
Dotychczas wszystkie Twoje commity znajdują się wyłącznie na dysku Twojego komputera. Aby zabezpieczyć pracę w chmurze i udostępnić ją prowadzącemu, połączymy lokalne repozytorium z nowym zdalnym repozytorium (*remote*) w serwisie GitHub.

### Przykład 6.1 — Utworzenie zdalnego repozytorium i pierwsze wypchnięcie (`git push`)
1. Zaloguj się na [https://github.com/](https://github.com/) i kliknij przycisk **New repository** (ikona `+` w prawym górnym rogu).
2. Jako nazwę wpisz `wds-git-lab`.
3. **Bardzo ważne:** **NIE** zaznaczaj opcji *Add a README file*, *Add .gitignore* ani *Choose a license* — Twoje lokalne repozytorium ma już własną historię commitów i plik `README.md`, więc zdalne repozytorium na starcie musi być całkowicie puste. Kliknij **Create repository**.
4. Skopiuj adres HTTPS swojego nowego repozytorium i wykonaj w terminalu:

```bash
git remote add origin https://github.com/<twoj-login-github>/wds-git-lab.git
git branch -M main
git push -u origin main
```

- `origin` to standardowa, umowna nazwa wskazująca na główne zdalne repozytorium.
- Flaga `-u` (`--set-upstream`) wiąże Twoją lokalną gałąź `main` ze zdalną gałęzią `origin/main`, dzięki czemu przy kolejnych zmianach wystarczy wpisać krótkie `git push` lub `git pull`.
- Podczas pierwszego `git push` otworzy się okno przeglądarki (**Git Credential Manager**) z prośbą o autoryzację konta GitHub.
  > **Uwaga (Windows):** Jeśli zamiast okna przeglądarki terminal poprosi o wpisanie hasła tekstowego, przerwij operację (`Ctrl + C`), wykonaj komendę `git config --global credential.helper manager` i ponów `git push -u origin main`.

5. Odśwież stronę swojego repozytorium na GitHubie — zobaczysz swoje pliki, historię commitów oraz sformatowany dokument `README.md`!

---

## 7. Gałęzie i scalanie zmian (*Branches and Merging*)

> **Dokumentacja:** [https://git-scm.com/book/pl/v2/Ga%C5%82%C4%99zie-Gita-Czym-jest-ga%C5%82%C4%85%C5%BA](https://git-scm.com/book/pl/v2/Ga%C5%82%C4%99zie-Gita-Czym-jest-ga%C5%82%C4%85%C5%BA)

### Wprowadzenie
**Gałąź (*branch*)** w systemie Git to lekki, ruchomy wskaźnik wskazujący na konkretny commit. Gałęzie pozwalają bezpiecznie przetestować nowy pomysł, napisać nowy moduł analizy lub rozwinąć funkcjonalność bez naruszania stabilnej zawartości głównej gałęzi `main`. Gdy praca na gałęzi bocznej jest gotowa, **scalamy (*merge*)** ją z powrotem do `main`.

Przygotujmy najpierw prosty plik `shopping.md` na gałęzi `main` w naszym repozytorium `wds-git-lab`:

```bash
echo "# Lista zakupów projektu" > shopping.md
git add shopping.md
git commit -m "Add shopping list"
```

---

### 7.1. Scalanie typu *Fast-Forward* (gdy `main` nie posunął się do przodu)

#### Przykład 7.1 — Utworzenie gałęzi, zmiana i scalenie *fast-forward*
Sprawdźmy listę gałęzi, a następnie jednym poleceniem `git switch -c` utwórzmy nową gałąź `feature/fruits` i przełączmy się na nią:

```bash
git branch
git switch -c feature/fruits
```

Dodajmy pozycję do pliku `shopping.md`, zatwierdźmy zmianę (flaga `-a` w `git commit -am` automatycznie dodaje do poczekalni wszystkie zmodyfikowane pliki, które były już wcześniej śledzone przez Gita) i wyświetlmy graf historii:

```bash
echo "- jabłka" >> shopping.md
git commit -am "Add apples"
git log --oneline --graph --all --decorate
```

Wróćmy teraz na gałąź `main` i sprawdźmy zawartość pliku `shopping.md` **przed** scaleniem:

```bash
git switch main
cat shopping.md
```
Zauważ, że na gałęzi `main` nie ma jeszcze wpisu `- jabłka`! Pliki w Twoim katalogu roboczym dynamicznie zmieniają swoją zawartość podczas przełączania gałęzi. Scalmy teraz zmiany z `feature/fruits` do bieżącej gałęzi (`main`) i usuńmy niepotrzebną już gałąź boczną:

```bash
git merge feature/fruits
git log --oneline --graph --all --decorate
git branch -d feature/fruits
```
Ponieważ na gałęzi `main` nie pojawiły się w międzyczasie żadne inne commity, Git po prostu przesunął wskaźnik `main` do przodu na commit z gałęzi `feature/fruits`. Taki mechanizm nosi nazwę **Fast-forward**.

---

### 7.2. Scalanie z commitem scalającym (*Three-way merge / Merge commit*)

#### Przykład 7.2 — Niezależne zmiany na dwóch gałęziach i ich połączenie
Sprawdźmy teraz sytuację, w której praca toczy się równolegle na obu gałęziach (w różnych plikach lub różnych sekcjach):

```bash
git switch -c feature/drinks
printf "\n## Napoje\n\n- woda\n" >> shopping.md
git commit -am "Add drinks section"

git switch main
echo "Lista przygotowana na wyjazd weekendowy." > weekend_info.md
git add weekend_info.md
git commit -m "Add weekend info file"
```

Sprawdźmy przed scaleniem, jak wygląda rozwidlony graf historii:
```bash
git log --oneline --graph --all --decorate
```

Teraz, będąc na gałęzi `main`, scalmy gałąź `feature/drinks`:
```bash
git merge feature/drinks
```
Git otworzy edytor VS Code z domyślnym komunikatem commitu scalającego (`Merge branch 'feature/drinks'`). Zapisz plik i zamknij kartę edytora w VS Code, aby dokończyć scalanie, a następnie ponownie obejrzyj graf:

```bash
git log --oneline --graph --all --decorate
git branch -d feature/drinks
```
Zobaczysz dwie ścieżki historii łączące się we wspólnym commicie scalającym (*merge commit*).

### Ćwiczenie 1.9 — Samodzielna praca z gałęziami
1. Utwórz i przełącz się na nową gałąź `feature/vegetables` (`git switch -c feature/vegetables`).
2. Dopisz trzy warzywa do pliku `shopping.md` i wykonaj commit.
3. Przełącz się na gałąź `main` (`git switch main`), scal gałąź `feature/vegetables` (`git merge feature/vegetables`), usuń gałąź boczną (`git branch -d feature/vegetables`) i wypchnij całą historię na GitHuba (`git push`).

---

## Dla chętnych / Wyzwanie (opcjonalne): Rozwiązywanie konfliktów scalania (*Merge Conflicts*)

Konflikt scalania pojawia się wtedy, gdy dwie gałęzie zmieniły **dokładnie te same linie w tym samym pliku** i Git nie może automatycznie zdecydować, którą wersję zachować. Jest to całkowicie normalna sytuacja w pracy zespołowej.

Wywołajmy konflikt celowo krok po kroku:

```bash
# 1. Tworzymy gałąź feature/water i zmieniamy wiersz "- woda" na "- woda kokosowa"
git switch -c feature/water
# Otwórz shopping.md w VS Code, zamień "- woda" na "- woda kokosowa" i zapisz plik
git commit -am "Prefer coconut water"

# 2. Wracamy na main i w tym samym miejscu zmieniamy "- woda" na "- woda gazowana"
git switch main
# Otwórz shopping.md w VS Code, zamień "- woda" na "- woda gazowana" i zapisz plik
git commit -am "Prefer sparkling water"

# 3. Próbujemy scalić gałąź feature/water do main
git merge feature/water
```

Git zatrzyma proces scalania z komunikatem `CONFLICT (content): Merge conflict in shopping.md`. Sprawdź `git status`, a następnie otwórz plik `shopping.md` w VS Code. Zobaczysz znaczniki konfliktu:

```text
<<<<<<< HEAD
- woda gazowana
=======
- woda kokosowa
>>>>>>> feature/water
```
- Fragment pomiędzy `<<<<<<< HEAD` a `=======` pochodzi z Twojej bieżącej gałęzi (`main`).
- Fragment pomiędzy `=======` a `>>>>>>> feature/water` pochodzi z dołączanej gałęzi (`feature/water`).

**Jak rozwiązać konflikt?**  
W VS Code kliknij jedną z opcji nad konfliktem (*Accept Current Change*, *Accept Incoming Change* lub *Accept Both Changes*) albo zredaguj tekst ręcznie tak, aby brzmiał np. `- woda (kokosowa, gazowana)` i **nie zawierał żadnych znaczników `<<<`, `===`, `>>>`**. Następnie zapisz plik i sfinalizuj scalanie:

```bash
git add shopping.md
git commit -m "Resolve merge conflict in water preference"
git branch -d feature/water
```
*(Wskazówka: gdybyś w trakcie konfliktu chciał całkowicie przerwać scalanie i wrócić do stanu sprzed `git merge`, użyj komendy `git merge --abort`.)*

---

## 8. Rozwiązywanie najczęstszych problemów (Troubleshooting)

| Problem / Komunikat błędu | Rozwiązanie |
| :--- | :--- |
| `Please tell me who you are` | Pominąłeś konfigurację tożsamości. Uruchom komendy `git config --global user.name` oraz `user.email` z Sekcji 2. |
| `src refspec main does not match any` | W repozytorium nie wykonano jeszcze żadnego commita lub gałąź ma inną nazwę. Wykonaj pierwszy commit i uruchom `git branch -M main`. |
| `remote origin already exists` | Zdalny adres został już wcześniej dodany. Sprawdź go przez `git remote -v`, a w razie potrzeby podmień: `git remote set-url origin <NOWY_URL>`. |
| `failed to push some refs` | Repozytorium na GitHubie zawiera commity, których nie masz lokalnie (np. zaznaczyłeś *Add README* na GitHubie). Wykonaj `git pull --rebase=false origin main` (lub skonsultuj z prowadzącym). |
| `CONFLICT (content)` | Otwórz plik ze znacznikami konfliktu w VS Code, wybierz docelową treść, usuń znaczniki `<<<`/`===`/`>>>`, a następnie wykonaj `git add <plik>` i `git commit`. |
| Utknąłem w trakcie nieudanego scalania | Sprawdź podpowiedź w `git status` lub wycofaj scalanie poleceniem `git merge --abort`. |
| Otworzył się edytor z komunikatem merge i nie wiem co zrobić | Zapisz plik (`Ctrl+S`) i zamknij kartę pliku w VS Code — Git automatycznie dokończy commit scalający. |

---

## 9. Podręczna ściągawka komend Git (*Command Cheat Sheet*)

| Polecenie | Przeznaczenie |
| :--- | :--- |
| `git init` | Utworzenie nowego repozytorium lokalnego w bieżącym katalogu |
| `git clone <URL>` | Pobranie kopii istniejącego repozytorium zdalnego na dysk |
| `git status` | Sprawdzenie stanu plików w katalogu roboczym i poczekalni |
| `git add <plik>` / `git add .` | Dodanie zmian z pliku (lub wszystkich zmian) do poczekalni (*staging area*) |
| `git commit -m "opis"` | Zapisanie zmian z poczekalni jako nowego commita w historii |
| `git commit -am "opis"` | Dodanie zmodyfikowanych plików śledzonych i wykonanie commita w jednym kroku |
| `git diff` / `git diff --staged` | Podgląd zmian niezatwierdzonych w poczekalni / czekających w poczekalni |
| `git log --oneline --graph --all --decorate` | Wyświetlenie zwięzłego grafu historii wszystkich gałęzi |
| `git restore <plik>` | Odrzucenie niezatwierdzonych zmian w pliku w katalogu roboczym |
| `git restore --staged <plik>` | Wycofanie pliku z poczekalni bez usuwania zmian z dysku |
| `git remote add origin <URL>` | Powiązanie lokalnego repozytorium ze zdalnym repozytorium na GitHubie |
| `git push -u origin main` | Pierwsze wysłanie lokalnej gałęzi `main` na serwer GitHub |
| `git pull` / `git fetch` | Pobranie i scalenie zmian z serwera / samo pobranie bez scalania |
| `git branch` | Wyświetlenie listy lokalnych gałęzi |
| `git switch <gałąź>` | Przełączenie się na istniejącą gałąź |
| `git switch -c <gałąź>` | Utworzenie nowej gałęzi i natychmiastowe przełączenie się na nią |
| `git merge <gałąź>` | Scalenie wskazanej gałęzi do aktualnie aktywnej gałęzi |
| `git branch -d <gałąź>` | Usunięcie scalonej już gałęzi |
| `git merge --abort` | Przerwanie trwającego scalania w razie konfliktu |

### Interaktywne gry i symulatory do samodzielnego treningu Git:
- [https://learngitbranching.js.org/](https://learngitbranching.js.org/) — wizualny symulator gałęzi i operacji Git w przeglądarce,
- [https://ohmygit.org/](https://ohmygit.org/) — gra open-source ucząca działania Gita,
- [https://gitimmersion.com/](https://gitimmersion.com/) — przewodnik krok po kroku po komendach Gita.
