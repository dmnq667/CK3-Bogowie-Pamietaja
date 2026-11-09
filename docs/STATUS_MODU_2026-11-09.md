# GNIEW I ŁASKA BOGÓW — JEDEN STAN PRODUKCJI
**Data:** 2026-11-09 (Europe/Warsaw)  
**Źródło prawdy:** repozytorium `dmnq667/CK3-Bogowie-Pamietaja`, gałąź `feature/0.4.5-powrot-kalendarza-i-tel`.  
**Status:** 0.4.5 DEV; testy kodu i instalatora Windows są zielone, **mod nie został zatwierdzony po teście w CK3**.  
**[Ostatni zielony build GitHub Actions](https://github.com/dmnq667/CK3-Bogowie-Pamietaja/actions/runs/42634924149)** · **[Paczka 0.4.5 DEV](https://github.com/dmnq667/CK3-Bogowie-Pamietaja/actions/runs/42634924149/artifacts/13682642345)**.

## Co ustalono i czego nie zmieniamy
- Robocza nazwa gry/moda: **Gniew i Łaska Bogów** (oryginalnie **Bogowie pamiętają**).
- **12 świąt** według dotychczasowych terminów i **31 zatwierdzonych grafik** bez wymieniania oryginałów.
- Dokładnie **dwa główne okna na święto**: (1) sens obrzędu, korzyść za udział, (2) dynamiczna, niebezpieczna fabuła o konsekwencjach.
- Osobiste spotkania z Perunem, Welesem i Mokoszą są dodatkowymi opowieściami, nie kolejnym bezsensownym klikaniem w świętach.
- Język: **wysoki rejestr, zrozumiała polszczyzna, słowiański, mroczny klimat**, bez bezsensownych metafor i niedomkniętych wątków.
- Istotne wyniki obejmują śmierć władcy/postaci, potężne premie i kary, stres, zemstę, winę, pamięć dawnych decyzji.
- Dopuszczony rozwój poza 0.4.5 tylko po rozpoznaniu błędu, bez losowych eksperymentów z typem UI; należy nadpisywać istniejący mod i zachować możliwość powrotu.

## Stan faktyczny kodu 0.4.5

| Moduł | Wykonane w kodzie | Nadal do potwierdzenia |
|---|---|---|
| Kalendarz 12 świąt | Przywrócono w `bp_announcement.1299` 12 automatycznych wywołań; bez dodatkowego banera; znacznik sezonowy | Czy otwiera pierwsze okno automatycznie w terminie i nie dubluje okien |
| Dwa okna i święta | 12 okien edukacyjnych + 12 fabularnych | Działanie przy dużej prędkości i sąsiednich terminach (np. Gaik 30.04 i Dziady 02.05) |
| Pauza CK3 | Starsze wersje użytkownika zatrzymywały grę; próby 0.4.2 (`toast + auto_pause`) i 0.4.3 (`letter_event`) zawiodły. 0.4.4 wrócił do `character_event`, 0.4.5 to zachowuje | **Pauza na pierwszym oknie NIE JEST NAPRAWIONA ANI POTWIERDZONA** |
| Szczodre Gody | Wszystkie 3 DDS istnieją; `bp_041.2112` wskazuje `bp_scene_szczodre_01`, pierwsze okno `bp_scene_szczodre_02` | W grze wystąpiło czarne tło; sprawdzić po przywróceniu `character_event` |
| Wyniki prób | 16 oddzielnych definicji komunikatów (plus fallback), w tym 25% śmierci / 75% przeżycia | Czy tekst rzeczywiście wyświetla się bez surowych identyfikatorów |
| Jare Gody | Z `bp_041.2104` usunięto `random_courtier`, fikcyjne oskarżenie i egzekucję losowej cesarzówny; tekst zależy od czynów rodu oraz charakteru władcy | Sprawdzić scenę w grze |
| Pozostałe sceny | Zasady 0.4.0–0.4.5 częściowo działają | **Sześć scen nadal losuje przypadkowego dorosłego dworzanina**: Stado `2107`, Noc Kupały `2108`, Perun `2109`, Plony `2110`, Dziady jesienne `2111`, Szczodre Gody `2112`. W **pięciu** wylosowana postać może zostać stracona. Przyczyny i motywacje NIE są jeszcze powiązane ze zdarzeniami rzeczywiście zaszłymi w grze. |
| Dodatkowa zemsta | Kod `bp_040_blood_events.txt` także losuje dworzanina jako stronę zdarzenia | Uwiarygodnić powiązania osobiste i dynastię |
| Assety | 31 zatwierdzonych obrazów w repo, oryginały zachowane | CK3 musi wyświetlić faktyczne tła w każdej scenie |

## Historia wydań — co oznaczają wersje
- `main`: **0.1.9-alpha**, stara baza, **nie aktualny dev**.
- `0.4.0 DEV`: próba ostrego, krwawego przebudowania wszystkich fabuł.
- `0.4.1 DEV`: rozdzielenie każdego święta na dwa okna, poprawki lokalizacji premii/kar.
- `0.4.2 DEV`: komunikaty po śmiertelnych próbach; **nieudane zatrzymywanie czasu za pomocą toastów**.
- `0.4.3 DEV`: eksperyment `letter_event`; **nie zatrzymywał gry**, dodatkowo regresja grafiki/komunikatu.
- `0.4.4 DEV`: cofnięcie eksperymentu i przywrócenie standardowych okien, **bez poprawionej pauzy**.
- `0.4.5 DEV`: przywrócony oryginalny automatyczny kalendarz, poprawione Jare Gody, kompletne komunikaty wyników, standardowe okna. **GitHub Actions #42634924149: oba testy PASS**.

## Co zrobić dalej — w tej kolejności
1. **Zamrozić mnożenie wersji i zmian w fabule**. Przetestować 0.4.5 na **kopii zapisu**: najpierw Gaik→Dziady, potem Szczodre Gody, komunikaty o wynikach i Jare Gody. Nie oznaczać pauzy jako naprawionej bez rzeczywistego testu.
2. **Odzyskać pauzę z rzeczywiście działającej wcześniejszej implementacji**. Porównać uruchamianie wydarzeń, sposób rejestracji on_action, ustawienia gry/modów i logi z konkretną wersją, zamiast zgadywać parametry.
3. **Naprawić sześć pozostałych scen z losowym dworzaninem**, analogicznie do Jarych Godów: winni, ofiary i przysięgi muszą wynikać z cech, stosunków i wcześniejszych działań. Osobno przejrzeć `bp_040_blood_events.txt`. Nie kasować krwawych konsekwencji, lecz nadać im sens.
4. Następnie wykonać pełny **przegląd jakości 12 fabuł**: wydarzenie, motywacja, postać, wybór, stres, nagroda/kara, odroczony skutek i poprawny obraz. Jedna zweryfikowana wersja po całym przeglądzie.
5. Dopiero po przetestowaniu w CK3 zaktualizować `main` i przygotować publikację. Sam zielony GitHub Actions **nie wystarcza**.

## Uwaga o rozmowie
Użytkownik zgłosił, że niektóre wiadomości i screeny znikają z interfejsu ChatGPT. Nie ma technicznej kontroli nad widokiem rozmowy z poziomu repozytorium; ten plik jest trwałym punktem odniesienia przy nowym wątku w projekcie „Produkcja MODÓW”.
