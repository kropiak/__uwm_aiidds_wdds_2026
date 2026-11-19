"""Przykładowy skrypt Pythona uruchamiany bezpośrednio z wiersza poleceń (terminala).

Uruchomienie z poziomu głównego katalogu repozytorium:
    uv run python modules/00_srodowisko_i_narzedzia/skrypt_startowy.py
lub z przekazaniem dodatkowych argumentów:
    uv run python modules/00_srodowisko_i_narzedzia/skrypt_startowy.py Olsztyn 2026
"""

import platform
import sys
from pathlib import Path


def wyswietl_informacje_o_srodowisku() -> None:
    """Wypisuje podstawowe informacje o interpreterze i systemie operacyjnym."""
    print("=== Informacje o środowisku wykonawczym ===")
    print(f"System operacyjny : {platform.system()} ({platform.release()})")
    print(f"Implementacja     : {platform.python_implementation()}")
    print(f"Wersja Pythona    : {sys.version.split()[0]}")
    print(f"Plik wykonywalny  : {sys.executable}")
    print(f"Katalog roboczy   : {Path.cwd()}")


def obsluz_argumenty_wejsciowe(argv: list[str]) -> None:
    """Pokazuje zawartość listy sys.argv przekazywanej z wiersza poleceń."""
    print("\n=== Argumenty wiersza poleceń (sys.argv) ===")
    print(f"Nazwa uruchamianego skryptu (argv[0]): {argv[0]}")
    pozostale = argv[1:]
    if pozostale:
        print(f"Przekazane argumenty ({len(pozostale)}): {pozostale}")
    else:
        print("Nie przekazano dodatkowych argumentów (uruchom skrypt dopisując słowa po spacji).")


if __name__ == "__main__":
    wyswietl_informacje_o_srodowisku()
    obsluz_argumenty_wejsciowe(sys.argv)
