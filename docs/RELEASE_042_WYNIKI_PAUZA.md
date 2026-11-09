# Gniew i Łaska Bogów 0.4.2 DEV — wyniki prób i automatyczna pauza

**Data:** 9 listopada 2026  
**Gałąź:** `feature/0.4.2-wyniki-i-pauza`  
**Weryfikacja CI:** [przebieg GitHub Actions #42573291604](https://github.com/dmnq667/CK3-Bogowie-Pamietaja/actions/runs/42573291604) — testy statyczne **PASS**, rzeczywista podmiana testowej instalacji na Windows PowerShell 5.1 **PASS**.  
**[Pobierz aktualizator 0.4.2 DEV](https://github.com/dmnq667/CK3-Bogowie-Pamietaja/actions/runs/42573291604/artifacts/13654395511)**.

## Zgłoszenie po teście 0.4.1

1. W Gaiku i Nocy Kupały ryzyko śmierci 25% nie powodowało żadnej czytelnej informacji o wyniku; przy przeżyciu gracz widział po prostu znikające okno.
2. Święta i inne wydarzenia pojawiały się bardzo blisko siebie, co skutkowało ucieczką albo nakładaniem się okien podczas biegu czasu.
3. Daty, dwa główne okna obrzędu i zaakceptowane grafiki należy zachować.

## Naprawa rozstrzygnięć

Każda z niebezpiecznych decyzji kończy się odtąd **czytelnym komunikatem w interfejsie** o wygranej albo przegranej, bez dodawania trzeciego okna wydarzenia. Zachowano rzeczywistą śmierć postaci CK3 i pierwotne prawdopodobieństwa.

| Wydarzenie | Śmierć | Przetrwanie | Wynik |
|---|---:|---:|---|
| Gaik — wejście między walczących | 25% | 75% | Zgon władcy lub 2 lata zwiększonej siły wojskowej |
| Noc Kupały — osobisty ratunek | 25% | 75% | Zgon władcy lub ratunek rzeczywistego dworzanina i łaska Mokoszy |
| Noc Kupały — wysłanie straży | 50% zgonu dworzanina | 50% ocalenia dworzanina | Osobny komunikat dla obu wyników |
| Święto Peruna — próba wojownika | 20% | 80% | Zgon albo 2-letnia wielka premia wojenna |
| Zemsta rodu — starcie z mścicielami | 30% | 70% | Zamach śmiertelny lub militarna przewaga i postrach |
| Ostateczna rozprawa z waśnią | 25% | 75% | Zgon albo pojednanie i 4-letnia premia |
| Bezpośredni gniew Peruna | 25% | 75% | Zgon albo 5-letnia niełaska |
| Bezpośredni gniew Welesa | 35% | 65% | Zgon albo 5-letnia dotkliwa klątwa |

Każdy z siedmiu śmiertelnych wariantów zapisuje w historii dynastii osobną informację o wyniku. W Nocy Kupały ocalony dworzanin otrzymuje pięcioletni znacznik uratowanego z powodzi. **Zmiany nie zmieniają rozkładu prawdopodobieństw.**

## Wymuszenie uwagi i kontrola tempa

Dokumentacja skryptów CK3 **nie udostępnia potwierdzonego parametru `pause = yes` w zwykłym `character_event`**. Zamiast dodawać niedziałającą instrukcję, mod wykorzystuje natywny system `message_filter_types` i `messages`:

- `bp_042_events_pause` — nowy filtr: `auto_pause = yes`, `always_show = yes`, `display = toast`;
- oba widoczne okna wszystkich 12 świąt emitują krótki komunikat przez ten filtr;
- osobiste objawienia Welesa, Peruna i Mokoszy, a także dwa wydarzenia zemsty, korzystają z tego samego rozwiązania;
- nawet wyniki ryzykownych prób wyświetlają się jako **krótkie komunikaty**, bez kolejnych przycisków.

Domyślne ustawienie filtra prosi silnik CK3 o **automatyczne zatrzymanie czasu po wyświetleniu komunikatu**. Jeśli gracz wcześniej zmienił ustawienia powiadomień, jego konfiguracja może nadpisać domyślną. W takim przypadku należy sprawdzić Ustawienia → Komunikaty → **Gniew i Łaska Bogów — zatrzymywanie czasu**.

**Istotne:** testy CI potwierdzają konfigurację filtra, a nie zachowanie pauzy w działającej grze. Taką próbę trzeba przeprowadzić w CK3.

## Co pozostało niezmienione

- **12 świąt, wszystkie oryginalne daty**, w tym święta występujące w odstępie kilku dni.
- **Dokładnie dwa główne okna**: krótka historia obrzędu i dar, następnie wydarzenie fabularne z wyborami.
- **31 zatwierdzonych grafik** i trzy osobiste objawienia bogów.
- Wszystkie dotychczasowe premie, klątwy, fabularne wybory, sądy i główne mechanizmy pamięci.
- Instalacja nadpisuje tę samą pozycję w launcherze; nie powstaje nowy mod.

## Testy

- Weryfikator `tools/validate_story_042.py` wykazał **7 wydarzeń ze śmiertelną próbą i 16 komunikatów wyniku**, 42 klucze lokalizacji w każdym języku, filtr pauzy i **12/12 świąt z dwoma oknami**.
- `tools/validate_gods_030.py` potwierdził zestaw 31 grafik i istniejące boskie objawienia.
- [GitHub Actions #42573291604](https://github.com/dmnq667/CK3-Bogowie-Pamietaja/actions/runs/42573291604): **SUCCESS**. Instalator na Windows nadpisał 0.4.1 i wykonał poprawną kopię zapasową.
- **Nie przeprowadzono testu rozgrywki CK3**; należy sprawdzić, czy komunikaty rzeczywiście zatrzymują czas i są czytelne po zmianie władcy.

## Instalacja

1. Pobierz [pakiet 0.4.2 DEV](https://github.com/dmnq667/CK3-Bogowie-Pamietaja/actions/runs/42573291604/artifacts/13654395511) z GitHub Actions.
2. Rozpakuj ZIP z pobranym artefaktem, następnie jego zawartość: `GNIEW_I_LASKA_BOGOW_0.4.2_DEV_NADPISZ.zip`.
3. Wyłącz CK3 i uruchom `AKTUALIZUJ_042.bat`.
4. Graj na **kopii zapisu**; przetestuj Gaik 30 kwietnia, Noc Kupały 20 czerwca i Święto Peruna.
5. Po otwarciu każdego okna sprawdź stan pauzy; po ryzykownym wyborze sprawdź komunikat i właściwą zmianę stanu postaci.

**Uwaga:** losowanie 25% jest niezależne. Przy kilku kolejnych próbach władca może za każdym razem przeżyć — samo przeżycie nie jest błędem, jeśli pojawia się prawidłowy komunikat.
