# Gniew i Łaska Bogów

Dawniej: **Bogowie Pamiętają**.

Mod do **Crusader Kings III** poświęcony słowiańskim bogom, obrzędom i cyklowi dwunastu świąt. Projekt niezależny od **The Weight of Words**.

## Aktualna wersja testowa: 0.4.1 DEV — znaczenie obrzędu i jego konsekwencje

**Każde z 12 świąt ma dokładnie dwa okna.** Pierwsze wyjaśnia sens obrzędu w wysokiej, zrozumiałej polszczyźnie i przyznaje +45 pobożności, -10 stresu oraz 90-dniowe błogosławieństwo. Drugie prowadzi do niebezpiecznej historii z możliwością zabójstwa, zemsty lub silnej nagrody. Dawne powiadomienia nie tworzą trzeciego okna.

Usunięto problem surowych identyfikatorów `bp_040_...` widocznych przy premiach i karach: **15 modyfikatorów i 4 efekty opinii** mają teraz nazwy i opisy PL/EN. Zachowano wszystkie 31 nowych ilustracji i trzy zatwierdzone objawienia bogów.

**[Pobierz aktualizator 0.4.1 DEV — test instalatora Windows PASS](https://github.com/dmnq667/CK3-Bogowie-Pamietaja/actions/runs/42565179434/artifacts/13651276740)**. Test skryptów potwierdza 12/12 dwustopniowych świąt, ale **działanie w grze CK3 wymaga sprawdzenia**. [Szczegóły, lista świąt i instalacja](docs/RELEASE_041_DWA_OKNA.md).

## Poprzednia wersja testowa: 0.4.0 DEV — przebudowana fabuła

Na gałęzi `feature/0.4.0-fabula-od-nowa` napisano od nowa wszystkie 12 historii świąt, wprowadzono krwawe decyzje, pamięć krzywd i późniejszą zemstę. Każde święto to jedna scena, dodatkowo może pojawić się zapowiedź. Dotychczasowe trzy osobiste objawienia bogów oraz 31 nowych grafik pozostały bez zmian.

[Poprawiona paczka 0.4.0 DEV — przetestowany instalator Windows](https://github.com/dmnq667/CK3-Bogowie-Pamietaja/actions/runs/42556994466) — **uwaga: nieprzetestowany w samej grze CK3**. [Bezpośredni link do poprawionego aktualizatora](https://github.com/dmnq667/CK3-Bogowie-Pamietaja/actions/runs/42556994466/artifacts/13648255623). Wcześniejszy instalator błędnie sprawdzał numer 0.3.0; problem został naprawiony i przetestowany na Windows PowerShell 5.1. Stara wersja 0.3.0 pozostaje na własnej gałęzi i w historii wydania. [Raport stanu i instrukcja instalacji](PROJECT_STATUS.md).

## Wcześniejsza produkcja: 0.3.0 DEV — gniew, łaska i nowe ilustracje

Na gałęzi `feature/0.3.0-gniew-i-laska` działa prototyp trzech interwencji bogów (Weles, Perun i Mokosz), pamięci najważniejszych czynów oraz premii za udział w wybranych świętach. Dostosowano sceny do osobistych objawień i przeredagowano ich polskie oraz angielskie teksty.

**Grafiki zaimportowane:** 31 tekstur DDS (28 świąt + 3 objawienia) i 31 źródeł zostało już zapisanych i zweryfikowanych na GitHubie. [Pobierz testowy aktualizator z GitHub Actions](https://github.com/dmnq667/CK3-Bogowie-Pamietaja/actions/runs/42506140283). Test w CK3 nadal oczekuje. Szczegóły: [raport importu](docs/IMPORT_GRAFIK_030.md).

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
