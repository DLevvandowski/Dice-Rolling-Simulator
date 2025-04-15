# Dice Rolling Simulator

## Opis projektu
Dice Rolling Simulator to projekt w Pythonie, który symuluje rzuty kostkami do 
gry. Użytkownik może wybrać liczbę kostek oraz ich typ (np. sześciościenne, 
ośmiościenne itp.), a program losowo generuje wyniki dla każdej z nich. Wynik
jest przedstawiony w postaci wykresu słupkowego w pliku `dice_simulation.html`

## Funkcjonalności
- Symulacja rzutu różnymi typami kostek (np. D6, D8, D20).
- Możliwość wyboru liczby kostek do rzutu.
- Przyjazny interfejs tekstowy.
- Obsługa niestandardowych typów kostek poprzez plik `die.py`.

## Wymagania
- Python 3.8 lub nowszy
- Zainstalowane biblioteki:
    - `plotly`

## Jak uruchomić
1. Sklonuj repozytorium:
    ```bash
    git clone https://github.com/DLevvandowski/Dice-Rolling-Simulator.git
    ```
2. Przejdź do katalogu projektu:
    ```bash
    cd Dice-Rolling-Simulator
    ```
3. Uruchom skrypt:
    ```bash
    python Dice_Rolling_Simulator.py
    ```

## Przykład użycia
Po uruchomieniu programu użytkownik zostanie zapytany o liczbę kostek, ich typ 
oraz liczbe rzutów. Wyniki rzutów zostaną wyświetlone na ekranie.

## Struktura projektu
- `Dice_Rolling_Simulator.py`: Główny skrypt obsługujący logikę programu.
- `die.py`: Moduł definiujący klasy i funkcje związane z różnymi typami kostek.