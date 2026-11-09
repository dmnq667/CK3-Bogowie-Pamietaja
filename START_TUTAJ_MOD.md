# START TUTAJ — Gniew i Łaska Bogów / Produkcja MODÓW

**Aktualizacja: 9 listopada 2026.**
**Ważne dla kolejnych rozmów w projekcie:** przed jakąkolwiek kolejną zmianą w CK3 koniecznie przeczytać **[aktualny, szczegółowy stan projektu](https://github.com/dmnq667/CK3-Bogowie-Pamietaja/blob/feature/0.4.5-powrot-kalendarza-i-tel/docs/STATUS_MODU_2026-11-09.md)**. To jest kanoniczny dokument przejęcia prac. Nie opierać się tylko na nieaktualnym `PROJECT_STATUS.md` gałęzi `main`.

- **Repozytorium:** `dmnq667/CK3-Bogowie-Pamietaja`.
- **Stabilne `main`:** stare źródła 0.1.9 ALPHA; **nie nadpisywać kodem DEV przed zaliczeniem testów CK3**.
- **Aktywna gałąź DEV:** `feature/0.4.5-powrot-kalendarza-i-tel` (0.4.5 DEV, skrypty i test instalatora Windows PASS, gra NIEZATWIERDZONA).
- [Najnowsza paczka testowa 0.4.5](https://github.com/dmnq667/CK3-Bogowie-Pamietaja/actions/runs/42634924149/artifacts/13682642345).
- [Szczegóły wersji 0.4.5](https://github.com/dmnq667/CK3-Bogowie-Pamietaja/blob/feature/0.4.5-powrot-kalendarza-i-tel/docs/RELEASE_045_KALENDARZ_GRAFIKI.md).

## Obowiązkowa lista prac — zlecenie użytkownika, nadal OTWARTE

1. **Kalendarz i pauza:** porównać rzeczywiście działający mechanizm starszych wersji z `0.4.5`. Przywrócić automatyczne uruchamianie i faktyczne zatrzymanie czasu na **pierwszym** oknie. Nie zmieniać eksperymentalnie typu okien, nie dodawać toastów jako sztucznej pauzy. Test CK3 przy szybkości 5, zwłaszcza Gaik 30 IV → Dziady wiosenne 2 V. Nie oznaczać tego jako wykonane wyłącznie po walidatorze kodu.
2. **Sześć historii:** Stado (`bp_041.2107`), Noc Kupały (`2108`), Perun (`2109`), Plony (`2110`), Dziady jesienne (`2111`), Szczodre Gody (`2112`) losują dowolnego dorosłego dworzanina `random_courtier` i w części wariantów można go zabić bez sensownej winy. Przerobić **wszystkie** tak, by sprawca, pokrzywdzony i zemsta wynikały z faktycznych czynów/cech/relacji albo użyć wydarzenia bez fikcyjnego oskarżenia konkretnej osoby. Zachować odczuwalne konsekwencje — śmierć, stres, złoto, gniew bogów, zemstę.
3. **Kontrola 12 świąt:** tekst PL wysokiego rejestru, krótkie sensowne objaśnienie obrzędu i brutalne wydarzenie jako drugie okno, motywacje, cechy postaci, efekty gry, bilans stresu, odroczone skutki i właściwa grafika z 31 zaakceptowanych. Następnie kontrola w rzeczywistej grze CK3, **dopiero potem release**.

## Zasady niepodlegające negocjacji

- **12 świąt, wszystkie dotychczasowe daty i zatwierdzone grafiki** — bez podmian na inne obrazy.
- **Dokładnie dwa główne okna na święto**: edukacyjne przedstawienie i wynikający z historii czyn. Spotkania z Perunem, Welesem i Mokoszą jako dodatkowe wydarzenia o silnych skutkach.
- **Słowiańska polszczyzna wysokiego rejestru, bez niejasnych metafor i nielogicznych oskarżeń**.
- **Silne dodatnie i ujemne skutki, również śmierć władcy lub postaci, ale bez losowego zabijania niewinnych dworzan z fabularnego kapelusza**.
- Prace na osobnej gałęzi; nie publikować `main` do czasu testów w grze. Przy testach wersji instalator nadpisuje dotychczasowy mod z kopią, bez duplikatu.
- **Nie deklarować, że coś działa w CK3, jeśli przeprowadzono jedynie statyczną kontrolę GitHub Actions**.

Ten plik w `main` jest **stałym odsyłaczem między rozmowami**. Szczegółowy status pozostaje w gałęzi DEV. Jeśli następny wątek nie ma kontekstu, użytkownik może wskazać sam link do niniejszego pliku.
