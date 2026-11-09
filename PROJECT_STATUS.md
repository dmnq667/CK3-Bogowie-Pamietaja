# Stan produkcji: Gniew i Łaska Bogów

## 0.4.0 DEV — przebudowa fabuły, 9 listopada 2026

**Wersja testowa zbudowana na osobnej gałęzi** `feature/0.4.0-fabula-od-nowa`. [Zakończony build #42555294029](https://github.com/dmnq667/CK3-Bogowie-Pamietaja/actions/runs/42555294029), status **SUCCESS**. **Nie była testowana w uruchomionym CK3.**

### Wykonane w kodzie

- Wymieniono wszystkie **12 głównych wydarzeń świątecznych** na niezależne, jednookienkowe sceny o realnych stawkach. Ograniczono wszystkie automatyczne łańcuchy świąt: **12/12 PASS, maksymalnie 2 okna wraz z zapowiedzią**.
- Napisano **107 kluczy fabularnych lokalizacji PL i EN**, w tym warianty charakterologiczne: `brave`, `craven`, `compassionate`, `callous`; alternatywne opisy dla wydarzeń z istniejącą postacią i pamięcią krwi.
- Nowe konsekwencje: prawdziwa śmierć wybranego z rzeczywiście istniejących dworzan, śmierć władcy po świadomym podjęciu ryzyka, 12 nowych modyfikatorów statusu i prowincji, 4 opinie, pamięć łaski i krzywdy w dynastii.
- Dodatkowe **2 odroczone wydarzenia rodowej zemsty** `bp_040.5001` i `bp_040.5002` (miesiące i rok po decyzji); losowanie wypadków i zamachów, rodzinne konsekwencje.
- Zachowano **31 zatwierdzonych DDS** bez podmieniania starymi grafikami. Objawienia osobiste A01 Weles, A02 Perun i A03 Mokosz nadal istnieją i są powiązane z istotnymi wyborami.
- Weles może udzielić -100 stresu i 250 złota za dług spłacany po miesiącach; jego sąd ma nowy opis adekwatny do paktu. Wybór prawdziwego więźnia pozostaje interakcją, ale jego egzekucja nie uruchamia dawnych kaskad.
- Perun osobiście powraca po uchylaniu się od przysięgi, Mokosz rozlicza ziarno zabrane poddanym.
- **Pierwszy rytualny sąd** jest obecnie niewidocznym rozliczeniem czynów i automatycznie zapisuje rezultat zamiast otwierać kolejne, abstrakcyjne okno. Pozostawiono rozwijaną cechę i istniejącą Księgę Bogów.
- Zastąpiono dawną decyzję „Zmień dar dla Welesa” decyzją rezygnacji bez dodatkowych okien.
- Dodano kontrolę struktury i lokalizacji (`tools/validate_story_040.py`), audyt długości okien oraz **aktualizator Windows nadpisujący ten sam mod z kopią bezpieczeństwa**.

### Nadal wymagające testu / rozwinięcia

- Test w CK3 1.20: rzeczywisty wybór dworzanina, dostępność wszystkich opcji, `death`, przekazanie władzy następcy, działanie przy różnych stanach wojny i bez dworzan, sprawdzenie `error.log`.
- Balans: częstość krwawej zemsty, stres przy charakterach, wielkość premii i faktyczny wpływ modyfikatorów na prowincje.
- Pełna kampania wieloletnia na kopii zapisu oraz kontrola starszych zapisów z wydarzeniami 0.3.0 zaplanowanymi już w kolejce. **Stare ID pozostały dla kompatybilności, choć główny kalendarz nie otwiera starych kaskad.**
- Docelowa przebudowa wszystkich czterech sądów i Księgi Bogów, jeśli po testach nadal będzie potrzebna.

### Testowa instalacja

[GitHub Actions: pobierz artefakt 0.4.0 DEV](https://github.com/dmnq667/CK3-Bogowie-Pamietaja/actions/runs/42555294029). Najpierw rozpakuj pobrany artefakt ZIP, potem zawarty w nim `GNIEW_I_LASKA_BOGOW_0.4.0_DEV_NADPISZ.zip`; wyłącz CK3 i uruchom `AKTUALIZUJ_040.bat`. Skrypt tworzy kopię dotychczasowej instalacji i nadpisuje jej pliki. **Testuj na kopii sejwa.** Nie instaluj równolegle 0.3.0 i 0.4.0.

## Poprzednie ustalenia (0.3.0 i wcześniejsze)

**Aktualizacja:** 08.11.2026  
**Wersja produkcyjna:** 0.3.0 DEV na `feature/0.3.0-gniew-i-laska`.  
**Import grafik ZAKOŃCZONY:** 31 nowych DDS i 31 obrazów źródłowych są w repozytorium na tej gałęzi; zakończony [GitHub Actions run #42506140283](https://github.com/dmnq667/CK3-Bogowie-Pamietaja/actions/runs/42506140283) uzyskał status SUCCESS. Instalator 0.3.0 DEV jest dostępny jako artefakt tego uruchomienia. Test wewnątrz CK3 nadal niewykonany.

## Faktycznie wykonane w 0.3.0 DEV

- Weles `2020`, Perun `9110`, Mokosz `3010`: osobne interwencje z wyborami, konsekwencjami i opisami różnymi dla cech postaci.
- Weles może uśmiercić władcę po świadomie podjętym ryzyku (prototyp 35%); Perun również (prototyp 25%).
- Wszystkie trzy sceny mają nowe identyfikatory teł; polskie i angielskie opisy mówią o widocznym, osobiście przemawiającym bogu.
- Wybrane święta dają natychmiastową premię, a dziedziczone zmienne zapamiętują działania przy Gromnicy i ofiarę Welesa.
- Przeredagowano otwarcia wszystkich 12 świąt. **Całościowa redakcja pozostałej lokalizacji trwa.**
- Sprawdzono 28 świątecznych i 3 boskie ilustracje; przygotowano 31 DDS 1592×848 DXT1, bez czterech starych wariantów; w kodzie przekierowano brakujące tła do nowych odpowiedników.
- Przeprowadzono automatyczny import bez udziału użytkownika: Magnific → GitHub Actions → 31 zweryfikowanych DDS oraz 31 obrazów źródłowych. Wygenerowano instalator Windows nadpisujący istniejący mod z kopią zapasową.

**Czego NIE wykonano:** uruchomienia moda w grze, sprawdzenia `error.log`, pełnej redakcji tekstów, weryfikacji ikony cechy w CK3.

## Dotychczasowa historia 0.1.9 / 0.2.0


**Aktualizacja:** 26.10.2026  
**Wersja:** 0.1.9 ALPHA, 12 świąt  
**Stan GitHub:** PEŁNA SYNCHRONIZACJA ŹRÓDEŁ, TESTY W CK3 OCZEKUJĄ.

## Potwierdzony import GitHub

- Import automatyczny ukończono commitem `d31a6809a21d0322d9bdd3ca4ce5250913305033`.
- Utworzono tag odtwarzalnej wersji źródeł: `v0.1.9-alpha`.
- Archiwum importowe przeszło kontrolę SHA-256; importer zweryfikował indywidualnie 110 plików na podstawie `IMPORT_MANIFEST_SHA256.json`.
- Dodatkowa kontrola listy plików w repozytorium: **110/110 ścieżek manifestu obecnych**, bez braków.
- Repozytorium zawiera 64 pliki w `Bogowie_Pamietaja/`, w tym 16 plików wydarzeń i 32 tekstury DDS; ponadto 32 oryginalne JPG w `source_artwork/` oraz 13 dokumentów wydania w `docs/`. Są również dokumenty służące do prowadzenia repozytorium.
- Wcześniejsze instrukcje o brakujących plikach lub oczekującym imporcie w archiwalnych komunikatach nie są już aktualne.

**Uwaga:** sprawdzenie integralności archiwum i obecności plików nie zastępuje uruchomienia moda w Crusader Kings III.

## Materiał źródłowy

- Archiwum wyjściowe: `Bogowie_Pamietaja_v0.1.9_ALPHA_12_SWIAT(1).zip`
- SHA-256 archiwum wyjściowego: `98ac06b79946907fe36fb01d3a3d10c5a6ab5da24b9bd103fdce26ab4e66a9f4`
- SHA-256 archiwum importowego: `8b7d33b7d40b47c81041273abc9705fb13272cfbd066af427e366d7f0b9be7e6`
- Szczegóły: [SYNC_STATUS.md](SYNC_STATUS.md), [IMPORT_MANIFEST_SHA256.json](IMPORT_MANIFEST_SHA256.json)

## Kolejny etap produkcji

1. Sprawdzić działanie w bieżącej wersji CK3 oraz `error.log`, uwzględniając zgodność z innymi modami.
2. Przetestować cykl roczny wszystkich 12 świąt i warunki wywoływania wydarzeń.
3. Zweryfikować wybory i skutki: Perun (wojna/pokój), dług Welesa, Mokosz, Dziady jesienne i Szczodre Gody.
4. Sprawdzić lokalizacje PL/EN, 32 tekstury DDS i dopasowanie ilustracji.
5. Zapisać potwierdzone wyniki testów i błędy w repozytorium przed wydaniem następnej wersji.

## Procedury i bieżące testy

- [Standard importu przez GitHub Actions](docs/PROCEDURA_PUBLIKACJI_GITHUB.md): stosować przy większych paczkach, żeby nie wymagać ręcznego przesyłania katalogów.
- [Wieczorna sesja testowa 0.1.9](docs/SESJA_TESTOWA_019.md): przygotowana, nie została jeszcze przeprowadzona.
- Nowy mechanizm do wersji 0.2.0: [Cztery Sądy Bogów](docs/PROJEKT_CZTERY_SADY_BOGOW_020.md). **Zatwierdzony przez autora podział 2 / 4 / 3 / 3**, czyli sądy po 2., 6., 9. i 12. święcie. **Tylko drugi sąd, po Dziadach wiosennych, może warunkowo przyznać +1500 złota w ostatecznym rozliczeniu minionego roku, maksymalnie raz na rok obrzędowy.** Ten sam władca może otrzymać premię w następnych latach, po ponownym spełnieniu warunków. Pozostałe sądy bez nagrody pieniężnej, z konsekwencjami fabularnymi i możliwym rozwojem cechy. **To projekt, bez zmian w skryptach 0.1.9.**
- **Sąd I 0.2.0, zakodowany na gałęzi roboczej:** [opis wydania DEV](https://github.com/dmnq667/CK3-Bogowie-Pamietaja/blob/feature/0.2.0-gromnica-dual-duty/docs/RELEASE_020_DEV_SAD_I.md). Siedem wydarzeń, pięć wyników (w tym nierozstrzygnięta przysięga), jedna trwała cecha „Znak Pierwszego Ognia” z ikoną DDS 64×64, trzy jednoroczne premie +5 dyplomacji / +5 intrygi i +10 naturalnego postrachu / +5 wiedzy, zapis skutków do przyszłego Sądu II, Księga Bogów i tłumaczenia PL/EN. Nazwy wszystkich czterech podstawowych rozstrzygnięć i jedna wspólna rozwijana cecha zatwierdzone przez autora. **Kontrole skryptów i lokalizacji: PASS statycznie; uruchomienie CK3 i CI GitHub Actions: wymagają weryfikacji.** Brak 1500 złota w Sądzie I. Opis testów i automatyczne pakowanie w workflow na gałęzi 0.2.0.
- Stabilnej bazy 0.1.9 nie zmieniać przed wieczornymi testami i uzgodnieniem mechaniki.

## Zasady

GitHub jest źródłem stanu produkcji. Każde wydanie wymaga historii zmian, stanu testów i oznaczenia wersji. Nie mieszać z `CK3-The-Weight-of-Words`.

