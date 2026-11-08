# Gniew i Łaska Bogów

Dawniej: **Bogowie Pamiętają**.

Mod do **Crusader Kings III** poświęcony słowiańskim bogom, obrzędom i cyklowi dwunastu świąt. Projekt niezależny od **The Weight of Words**.

## Aktualna produkcja: 0.3.0 DEV — gniew, łaska i nowe ilustracje

Na gałęzi `feature/0.3.0-gniew-i-laska` działa prototyp trzech interwencji bogów (Weles, Perun i Mokosz), pamięci najważniejszych czynów oraz premii za udział w wybranych świętach. Dostosowano sceny do osobistych objawień i przeredagowano ich polskie oraz angielskie teksty.

**Uwaga:** komplet 31 nowych tekstur DDS został przygotowany i zweryfikowany lokalnie, ale nie jest jeszcze zaimportowany do repozytorium. Bez tej paczki nie należy uruchamiać wersji 0.3.0. Importer i instalator znajdują się na gałęzi rozwojowej; szczegóły w [instrukcji importu](docs/IMPORT_GRAFIK_030.md).

Test CK3: **nie wykonany**. Stabilna wersja 0.1.9 na `main` pozostała bez zmian.

## Wcześniejsza wersja 0.2.0 DEV: pierwszy sąd

Na tej gałęzi zaimplementowano **Sąd Popiołu i Przysięgi**: siedem scen, pięć rozstrzygnięć, pamięć Gromnicy i Welesa, jedną trwałą rozwijaną cechę z własną ikoną DDS, silne roczne premie, polskie i angielskie teksty oraz kartę Księgi Bogów. **Kontrola statyczna PASS; test działania w CK3 oczekuje.** Wydanie `v0.1.9-alpha` na `main` pozostaje bez zmian.

- [Szczegóły wersji DEV](docs/RELEASE_020_DEV_SAD_I.md)
- [Raport i lista prób w CK3](docs/VALIDATION_020_SAD_I.md)
- [Automatyczny walidator](tools/validate_first_court_020.py)
- [Szkic fabularny i przyjęte rozstrzygnięcia](docs/SAD_I_POPIOLU_I_PRZYSIEGI_020_KONCEPCJA.md)

## Stan projektu
- Wersja źródłowa: **0.1.9 ALPHA**, 12 świąt.
- 131 identyfikatorów wydarzeń, 32 tekstury DDS, lokalizacje polskie i angielskie według dokumentacji wydania.
- Walidacja statyczna wydania: PASS; test w uruchomionej grze: **jeszcze niepotwierdzony**.

## Dokumentacja
- [Status produkcji](PROJECT_STATUS.md)
- [Historia wydań](CHANGELOG.md)
- [Odtwarzanie i instalacja](RESTORE.md)
- [Standard publikacji przez GitHub Actions](docs/PROCEDURA_PUBLIKACJI_GITHUB.md)
- [Wieczorna sesja testowa 0.1.9](docs/SESJA_TESTOWA_019.md)
- [Szczegółowy plan testów](docs/PLAN_TESTOW_019.md)
- [Projekt na kolejną wersję: Cztery Sądy Bogów](docs/PROJEKT_CZTERY_SADY_BOGOW_020.md) (koncepcja, jeszcze bez zmian w mechanice)

Źródłowa paczka 0.1.9 i grafiki są zachowane w archiwum produkcyjnym. **Źródła v0.1.9 ALPHA i zasoby zostały zaimportowane i zweryfikowane sumami SHA-256**. Wyniki testów w grze nie są jeszcze potwierdzone. Zobacz [stan synchronizacji](SYNC_STATUS.md).

## Zasady
Po każdej zmianie aktualizujemy status, historię i wyniki testów. Nie mieszamy projektu z `CK3-The-Weight-of-Words`. Grafiki pozostają materiałami autora, bez automatycznego udzielenia licencji innym osobom.
