# Konfiguracja środowiska pracy (Pre-work: Windows / macOS / Linux)

Na zajęciach korzystamy z interpretera **Python 3.14**, menedżera środowisk i pakietów **`uv`**, edytora **Visual Studio Code** (z rozszerzeniami *Python* oraz *Jupyter*) oraz systemu kontroli wersji **Git**.

Wykonaj poniższe kroki przed pierwszym spotkaniem. Na początku pierwszego zjazdu przeznaczamy 30–45 minut na wspólne sprawdzenie konfiguracji i rozwiązanie ewentualnych problemów.

---

## 1. Instalacja narzędzia Git

> **Dokumentacja oficjalna:** [https://git-scm.com/doc](https://git-scm.com/doc)

### Windows
1. Pobierz instalator **Git for Windows** ze strony [https://git-scm.com/download/win](https://git-scm.com/download/win) (64-bit Setup). Pakiet zawiera m.in. terminal **Git Bash** oraz **Git Credential Manager**.
2. Uruchom instalator i przejdź przez kolejne kroki, pozostawiając domyślne ustawienia.

### macOS
1. Otwórz aplikację **Terminal** (`Cmd + Spacja` → wpisz `Terminal`).
2. Uruchom polecenie installing Xcode Command Line Tools:
   ```bash
   xcode-select --install
   ```
   lub zainstaluj Git przez menedżer pakietów [Homebrew](https://brew.sh/):
   ```bash
   brew install git
   ```

### Linux
- **Ubuntu / Debian:** `sudo apt update && sudo apt install -y git`
- **Fedora:** `sudo dnf install -y git`
- **Arch Linux:** `sudo pacman -S git`

### Weryfikacja instalacji Git (wszystkie systemy)
Otwórz terminal (na Windows: **Git Bash** lub **PowerShell**) i wpisz:
```bash
git --version
```

---

## 2. Instalacja menedżera `uv` oraz interpretera Python 3.14

> **Dokumentacja oficjalna `uv`:** [https://docs.astral.sh/uv/](https://docs.astral.sh/uv/)  
> **Dokumentacja Python 3.14:** [https://docs.python.org/3.14/using/index.html](https://docs.python.org/3.14/using/index.html)

Narzędzie `uv` potrafi samodzielnie pobrać oficjalną dystrybucję CPython 3.14 i utworzyć odizolowane środowisko wirtualne `.venv` wraz z pakietami (`pandas >= 3.0`, `matplotlib`, `seaborn`, `jupyter`).

### Windows (PowerShell)
```powershell
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
```
Po zakończeniu instalacji **zamknij i otwórz ponownie** okno terminala, a następnie zainstaluj Pythona 3.14:
```powershell
uv python install 3.14
```

### macOS / Linux (Terminal)
```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```
Po zakończeniu instalacji **zamknij i otwórz ponownie** terminal, a następnie zainstaluj Pythona 3.14:
```bash
uv python install 3.14
```

---

## 3. Instalacja Visual Studio Code i rozszerzeń

> **Dokumentacja VS Code + Python:** [https://code.visualstudio.com/docs/python/python-tutorial](https://code.visualstudio.com/docs/python/python-tutorial)

1. Pobierz i zainstaluj **Visual Studio Code** ze strony [https://code.visualstudio.com/](https://code.visualstudio.com/).
2. Otwórz widok **Extensions** (`Ctrl+Shift+X` na Windows/Linux, `Cmd+Shift+X` na macOS).
3. Zainstaluj dwa oficjalne rozszerzenia:
   - **Python** (`ms-python.python`)
   - **Jupyter** (`ms-toolsai.jupyter`)

---

## 4. Pobranie materiałów kursu i synchronizacja środowiska `.venv`

W terminalu przejdź do katalogu, w którym przechowujesz projekty, sklonuj repozytorium i uruchom `uv sync`:

```bash
git clone <ADRES_REPOZYTORIUM_KURSU>
cd __uwm_aiids_2026
uv sync
```

Polecenie `uv sync`:
- odczyta plik [pyproject.toml](pyproject.toml),
- utworzy lokalne środowisko wirtualne w podkatalogu `.venv` oparte na **Pythonie 3.14**,
- zainstaluje `pandas >= 3.0.0`, `matplotlib`, `seaborn`, `jupyter`, `ipykernel`, `requests` oraz narzędzia deweloperskie (`pytest`, `ruff`).

---

## 5. Sprawdzenie działania w VS Code

1. W VS Code wybierz `File → Open Folder...` i otwórz główny katalog repozytorium.
2. Otwórz notatnik `modules/00_srodowisko_i_narzedzia/02_wprowadzenie_do_jupyter.ipynb`.
3. W prawym górnym rogu notatnika kliknij **Select Kernel** → **Python Environments...** → wybierz środowisko **`.venv (Python 3.14.x)`**.
4. Uruchom kolejne komórki skrótem `Shift + Enter`.
