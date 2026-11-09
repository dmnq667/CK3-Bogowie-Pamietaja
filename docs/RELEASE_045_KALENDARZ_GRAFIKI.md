# Gniew i Łaska Bogów — 0.4.5 DEV: powrót automatycznego kalendarza i grafik świąt

**Wersja:** `0.4.5-dev`, 9 listopada 2026.  
**Repozytorium:** `feature/0.4.5-powrot-kalendarza-i-tel`.  
**[Pobierz aktualizację 0.4.5 DEV](https://github.com/dmnq667/CK3-Bogowie-Pamietaja/actions/runs/42634924149/artifacts/13682642345)**.  
**GitHub Actions:** [przebieg #42634924149](https://github.com/dmnq667/CK3-Bogowie-Pamietaja/actions/runs/42634924149) — kontrola kodu **PASS**, test instalatora Windows 0.4.4→0.4.5 **PASS**.

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

## Jare Gody — usunięcie przypadkowych oskarżeń (nowa poprawka 0.4.5)

Po teście użytkownik zgłosił, że zdarzenie `bp_041.2104` losowo wskazywało młodą, cnotliwą i gorliwą cesarzównę jako napastniczkę. Kod rzeczywiście używał `random_courtier` z jedynymi warunkami `is_alive = yes`, `is_adult = yes`. Opcja `b` wykonywała realne `death = { killer = root death_reason = death_execution }` na tak wylosowanej osobie, mimo braku dowodów lub wcześniejszego czynu.

**Zmiany:**
- Usunięto losowanie dworzanina, fikcyjne oskarżenie i nieuprawnioną egzekucję postaci CK3.
- Zdarzenie dotyczy teraz dwóch faktycznie zwaśnionych grup zbrojnych; rana podczas święta jest wyraźnie opisana, a osobista historia władcy wpływa na fabułę.
- Jeśli dynastia wcześniej faktycznie przelewała krew (pamięć `bp_040_blood_ever_v040`), pojawiają się **krewni ofiar wcześniejszych rozkazów**. Jeśli wcześniej okazywano miłosierdzie (pamięć `bp_040_mercy_ever_v040`), starszyzna **przypomina o wyrokach łaski**. Inaczej opis uwzględnia odwagę, tchórzostwo lub zwykły konflikt o ziemię i przeprawę.
- Zachowano trzy możliwe rozstrzygnięcia: zapłata 90 złota za pokój; siłowe stłumienie bójki, postrach, łupy, tyrania i przyszła zemsta (bez zabijania przypadkowego dworzanina); odmowa sądu, **utrata prestiżu i trzyletnia waśń**, zamiast nieuzasadnionego bonusu prestiżu.
- Bez zmiany grafiki Jarych Godów ani liczby dwóch okien. Zmieniono teksty PL i EN.

## Komunikat `bp_042_trial_success_message_desc` — poprawiony

W poprzedniej wersji wysyłano 16 wyników jako generyczne wiadomości, nie nadając im wszystkich opisów w definicjach `common/messages`. Silnik wyświetlał surowy identyfikator. Obecnie każdy wariant śmierci/przeżycia ma osobny **nazwany typ komunikatu z własnym kluczem tytułu i opisu**, a brakujące teksty zapasowe są uzupełnione w polskiej i angielskiej lokalizacji.

**Kontrola regresji:** walidator wykazał brak losowego oskarżonego w Jarych Godach, 16 kompletów komunikatów, 12 świąt oraz prawidłowy Windows-update.

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
2. Pobierz [0.4.5 DEV](https://github.com/dmnq667/CK3-Bogowie-Pamietaja/actions/runs/42634924149/artifacts/13682642345) z GitHub Actions.
3. Rozpakuj pobrany ZIP, a następnie `GNIEW_I_LASKA_BOGOW_0.4.5_DEV_NADPISZ.zip` znajdujący się wewnątrz.
4. Uruchom `AKTUALIZUJ_045.bat`. Instalator **nadpisuje istniejący mod**, zachowuje kopię i nie dodaje nowej pozycji w launcherze.
5. Ustaw szybkość 5 i sprawdź **30 kwietnia — Gaik**, a następnie **2 maja — Dziady wiosenne**: pierwsze okno powinno pojawić się samoczynnie, bez klikania decyzji. Zapisz, czy w tej chwili zegar gry staje.
6. Zimą sprawdź **Szczodre Gody (od 21 grudnia)**: pierwsze okno z zimowym ogniskiem, drugie „Prawo gościny” z inną zatwierdzoną ilustracją, nie czarnym panelem.

Nie wolno traktować braku pauzy jako sprawy zakończonej, dopóki test w CK3 nie potwierdzi zachowania; nie modyfikowano ustawień globalnych samej gry.
