# Import grafik do „Gniewu i Łaski Bogów” — 0.3.0 DEV

**Stan: pliki przygotowane, import czeka na użytkownika.** Materiał pochodzi z 28 nowych ilustracji świąt (`nowe.zip`), zatwierdzonych obrazów Welesa, Peruna i lustrzanej Mokoszy.

## Co jest gotowe

- 31 tekstur DDS 1592 × 848 px, kompresja DXT1/BC1, bez mipmap.
- 31 plików źródłowych: 28 JPG świąt i 3 wizerunki bogów.
- Jedno archiwum `Bogowie_030_GRAFIKI_IMPORT.zip` z **62 plikami** i indywidualnym manifestem SHA256.
- Całość rozdzielona na **trzy części do jednorazowego przesłania przez przeglądarkę**:
  - `BP030.part01` — 20 971 520 bajtów;
  - `BP030.part02` — 20 971 520 bajtów;
  - `BP030.part03` — 13 883 631 bajtów.
- **SHA256 składanego archiwum:** `bd9fe6725f27e61af632cad613f9d1aa03799b073d3cee47d2f037233c18b0b7`.
- Workflow: `.github/workflows/import-grafiki-030.yml`, który waliduje archiwum, importuje materiały i buduje instalator z kontrolą sum.

## Jedna czynność użytkownika, bez instalacji Git

1. Pobierz **wszystkie trzy** części `BP030.part01`, `BP030.part02`, `BP030.part03` udostępnione przez asystenta.
2. Otwórz repozytorium w GitHubie i przejdź na gałąź **`feature/0.3.0-gniew-i-laska`** (nie `main`).
3. W głównym katalogu wybierz **Add file → Upload files** i przeciągnij **razem trzy pliki** (nie rozpakowuj, nie zmieniaj nazw).
4. Zatwierdź **Commit changes** na tej samej gałęzi.
5. Workflow powinien sprawdzić całe archiwum i wszystkie pliki, nadpisać 28 tekstur starego stylu, dodać 3 nowe obrazy bogów, usunąć 4 nieużywane stare warianty DDS, a następnie przygotować artefakt `Gniew-i-Laska-Bogow-0.3.0-DEV-NADPISZ` w zakładce Actions.
6. Dopiero po sprawdzeniu faktycznego zakończenia workflow i pobraniu aktualizatora **wyłącz CK3**, rozpakuj aktualizator i uruchom `AKTUALIZUJ_030.bat`. Instaluje się w miejscu dotychczasowego moda i tworzy kopię bezpieczeństwa, nie drugi wpis w launcherze.

## Ważne zastrzeżenia

- **Przed udanym importem nie instalować gałęzi 0.3.0**: skrypty odwołują się do trzech jeszcze nieobecnych na GitHubie DDS.
- Automatyczna walidacja struktur i sum plików **nie dowodzi**, że zdarzenia działają w CK3. Na pierwszym teście korzystać z kopii zapisu, monitorować `error.log` i zachowanie wydarzeń.
- Nie używać dawnego workflow `import-bogowie-019.yml`, przeznaczonego wyłącznie dla 0.1.9 i `main`.
- Nie zastępować czterech brakujących wariantów dawnymi obrazami. Ich klucze tła przekierowano na inne ilustracje z nowej serii.
- Nie zmieniać nazwy żadnej części ani nie przesyłać ich do `main`.
