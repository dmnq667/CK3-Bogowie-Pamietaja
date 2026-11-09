# Gniew i Łaska Bogów — 0.4.5 DEV: powrót automatycznego kalendarza i grafik świąt

**Wersja:** `0.4.5-dev`, 9 listopada 2026.  
**Repozytorium:** `feature/0.4.5-powrot-kalendarza-i-tel`.  
**[Pobierz aktualizację 0.4.5 DEV](https://github.com/dmnq667/CK3-Bogowie-Pamietaja/actions/runs/42632417532/artifacts/13682155682)**.  
**GitHub Actions:** [przebieg #42632417532](https://github.com/dmnq667/CK3-Bogowie-Pamietaja/actions/runs/42632417532) — kontrola kodu **PASS**, test instalatora Windows 0.4.4→0.4.5 **PASS**.

## Analiza źródła problemów

W początkowych wersjach (m.in. 0.1.9) ukryty, codzienny zegar `bp_announcement.1299` automatycznie sprawdzał **12 terminów świąt** i sam uruchamiał widoczne okna. W wersjach 0.4.x wszystkie dwanaście wywołań usunięto z jego `immediate`: pozostawiono głównie automatyczny sąd i ręczne decyzje. To była konkretna, przeoczona regresja funkcjonalności.

W eksperymentalnym 0.4.3 wprowadzono `type = letter_event` z `window = character_event`. Na screenie użytkownika (Szczodre Gody, „prawo gościny”) widać ciemny, pusty panel za postacią — mimo że `bp_scene_szczodre_01` jest poprawnym odwołaniem do rzeczywistego obrazu. **Nie brakowało materiałów graficznych:** wszystkie trzy pliki `bp_szczodre_01.dds`, `02.dds` i `03.dds` są obecne, mają poprawną sygnaturę DDS i znaczną zawartość. Wersja 0.4.4 przywróciła `character_event`; 0.4.5 zachowuje tę poprawkę.

## Wykonana zmiana

Ponownie włączono w istniejącym zegarze `bp_announcement.1299` obsługę wszystkich **12 świąt**. Zamiast starej zapowiedzi jako trzeciego okna bezpośrednio wywoływane jest **edukacyjne okno święta** — identyfikator `bp_<nazwa>.<numer>`. Jego przycisk uruchamia następnie istniejącą, brutalniejszą historię `bp_041.21xx`.

Każde wywołanie:
- jest sprawdzane codziennie w tej samej **oryginalnej dacie lub oknie kalendarza**;
- wymaga religii słowiańskiej i nieodbytego obrzędu;
- przed otwarciem okna zapisuje w dynastii znacznik `bp_<nazwa>_announced_v...` na 335 dni, aby uniknąć codziennego dublowania święta;
- nie tworzy dodatkowego komunikatu, trzeciego okna ani nowego obiektu UI;
- działa w starym, rozpoznawalnym `character_event`, zgodnym z przypisanymi tłami.

Zachowano sąd (obecny w zegarze 0.4.4), wszystkie 12×2 etapów, 16 tekstów rozstrzygnięć prób, niebezpieczne wybory, daty, 31 grafik i ich dotychczasowe przypisania.

## Szczodre Gody — kontrola grafiki

| Etap | Zdarzenie | Tło |
|---|---|---|
| 1. Przedstawienie obrzędu | `bp_szczodre.9401` | `bp_scene_szczodre_02` → `bp_szczodre_02.dds` |
| 2. Prawo gościny / opowieść | `bp_041.2112` | `bp_scene_szczodre_01` → `bp_szczodre_01.dds` |

Oba okna muszą być w grze wyświetlane jako normalne wydarzenia `character_event`. Osobno zachowano `bp_szczodre_03.dds` dla pozostałych scen.

## Walidacja

W `tools/validate_story_045.py` sprawdzono:
- dokładnie **12 automatycznych wywołań**, zabezpieczonych znacznikami sezonowymi;
- strukturę **12 świąt × 2 widoczne okna**, bez trzecich banerów;
- normalny typ okna 29 wydarzeń, bez starego, wadliwego `letter_event`;
- integralność trzech plików DDS Szczodrych Godów, poprawność ich odniesień w kodzie i dwóch wersji tła;
- 16 wyników ryzykownych prób, dotychczasowe grafiki oraz zasady kodu z wersji 0.4.4;
- instalację w PowerShell 5.1 na Windows i kopię przed nadpisaniem **PASS**.

**Ważne:** testy nie uruchamiają silnika CK3. Automatyczne wyświetlanie w terminie oraz **rzeczywista pauza gry** wymagają testu na komputerze użytkownika. Odnowienie pierwotnego łańcucha wydarzeń jest rzeczową naprawą regresji, ale nie wolno jeszcze nazywać go potwierdzoną poprawką pauzy.

## Instalacja

1. Zamknij grę i graj na kopii zapisu.
2. Pobierz [0.4.5 DEV](https://github.com/dmnq667/CK3-Bogowie-Pamietaja/actions/runs/42632417532/artifacts/13682155682) z GitHub Actions.
3. Rozpakuj pobrany ZIP, a następnie `GNIEW_I_LASKA_BOGOW_0.4.5_DEV_NADPISZ.zip` znajdujący się wewnątrz.
4. Uruchom `AKTUALIZUJ_045.bat`. Instalator **nadpisuje istniejący mod**, zachowuje kopię i nie dodaje nowej pozycji w launcherze.
5. Ustaw szybkość 5 i sprawdź **30 kwietnia — Gaik**, a następnie **2 maja — Dziady wiosenne**: pierwsze okno powinno pojawić się samoczynnie, bez klikania decyzji. Zapisz, czy w tej chwili zegar gry staje.
6. Zimą sprawdź **Szczodre Gody (od 21 grudnia)**: pierwsze okno z zimowym ogniskiem, drugie „Prawo gościny” z inną zatwierdzoną ilustracją, nie czarnym panelem.

Nie wolno traktować braku pauzy jako sprawy zakończonej, dopóki test w CK3 nie potwierdzi zachowania; nie modyfikowano ustawień globalnych samej gry.
