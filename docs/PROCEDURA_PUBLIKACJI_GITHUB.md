# Standard publikacji modów CK3 na GitHubie

**Procedura produkcyjna uzgodniona 26.10.2026.** Obowiązuje dla projektów „Bogowie Pamiętają” i „The Weight of Words”, z osobnymi repozytoriami i historiami wydań.

## Zasada podstawowa

Przy dużej liczbie plików, zagnieżdżonych folderach albo zasobach binarnych **nie każ użytkownikowi ręcznie tworzyć katalogów i przesyłać plików po kolei**. Nie wymagaj Git for Windows, PowerShella ani lokalnego `git push` tylko po to, by opublikować mod.

Stosuj sprawdzony przebieg: **archiwum → bezpieczne części poniżej limitu przesyłania w przeglądarce → GitHub Actions → weryfikacja integralności → commit → oznaczenie wersji → aktualizacja statusu**.

## Gdy nie ma repozytorium

1. Sprawdź listę repozytoriów połączonego konta GitHub. Nie zakładaj, że brak wyniku wyszukiwania oznacza utratę projektu.
2. Jeśli repozytorium rzeczywiście nie istnieje i nie można utworzyć go połączonym narzędziem, użytkownik zakłada **puste, prywatne repozytorium** na github.com/new.
3. Po potwierdzeniu praw zapisu przez połączonego GitHuba, asystent tworzy pliki dokumentacji oraz workflow importowy. Użytkownik nie musi przygotowywać ścieżek katalogów moda.
4. Każdy mod ma osobne repozytorium; nie umieszczać jednego moda w repozytorium drugiego.

## Jednorazowy import dużej paczki

1. Na bazie zaakceptowanej paczki źródłowej zbuduj archiwum ZIP zawierające **relatywne ścieżki** potrzebnych źródeł, lokalizacji, zasobów DDS, źródłowych JPG i dokumentacji. Nie dokładaj przypadkowych katalogów tymczasowych ani danych osobistych.
2. Utwórz manifest `ścieżka → SHA-256`, policz SHA-256 całego archiwum i zapisz liczbę plików. Waliduj także oczekiwane katalogi i liczby zasobów dla konkretnego wydania.
3. Jeśli ZIP przekracza limit przeglądarki, podziel go na dwie lub więcej części, z których **każda ma mniej niż 25 MiB**. Nadaj jednoznaczne nazwy wersji, np. `BP020.part01` i `BP020.part02`.
4. Asystent publikuje przez połączonego GitHuba dedykowany plik `.github/workflows/import-...yml`. Workflow musi:
   - uruchamiać się dopiero po przesłaniu wymaganych części (lub ręcznie po upewnieniu się, że już tam są);
   - złożyć części w zadanej kolejności;
   - **przed rozpakowaniem** porównać SHA-256 ZIP z wartością wpisaną w workflow;
   - rozpakować do tymczasowego katalogu i skontrolować ścieżki oraz SHA-256 każdego pliku zgodnie z manifestem;
   - nie kopiować niczego do repozytorium w razie błędu walidacji;
   - odtworzyć drzewa źródeł i bezpiecznie usunąć wyłącznie przesłane tymczasowe części;
   - zapisać jeden commit bez wymuszania nadpisania cudzej historii i nadać oznaczenie wersji dopiero po udanym imporcie.
5. Użytkownik wykonuje **jedną czynność w przeglądarce**: na głównej stronie repozytorium używa `Add file → Upload files`, przeciąga wszystkie części i zatwierdza `Commit changes`. Nie rozpakowuje fragmentów ani nie klika każdego folderu.
6. Asystent sprawdza wynik importu i **samodzielnie odczytuje faktyczne drzewo GitHuba**. Porównuje je z manifestem, weryfikuje liczbę plików, wykrywa braki i sprawdza tag/commit.
7. Dopiero po udanym sprawdzeniu asystent zmienia `PROJECT_STATUS.md`, `CHANGELOG.md` i dokument potwierdzenia synchronizacji. Nie wolno nazywać przygotowanej paczki ani samego przesłania fragmentów „zakończoną publikacją”.

## Co jest specyficzne dla wersji 0.1.9

- Repo: `dmnq667/CK3-Bogowie-Pamietaja`
- Historyczny importer: `.github/workflows/import-bogowie-019.yml`
- Historyczne instrukcje: `IMPORT_GITHUB.md`
- Manifest: `IMPORT_MANIFEST_SHA256.json`
- Zakończony import: commit `d31a6809a21d0322d9bdd3ca4ce5250913305033`
- Tag: `v0.1.9-alpha`
- Sprawdzono na GitHubie 110/110 ścieżek manifestu; 32 DDS oraz 32 JPG są obecne.
- **Ten importer zawiera sumy kontrolne i nazwy części właściwe tylko dla 0.1.9. Nie należy używać go bez zmian dla nowej paczki.** Dla 0.2.0 lub kolejnego wydania przygotuj nowy importer i nowe sumy.

## Reguły aktualizacji i testów

- Małe tekstowe zmiany: zapisuj bezpośrednio połączonym GitHubem i kontroluj wynik.
- Duże zmiany i pliki binarne: importer paczki zgodnie z powyższą procedurą.
- Każdą wersję oznaczaj zgodnie ze stanem: ALPHA, RC, wydanie sprawdzone. **Walidacja plików nie jest testem w uruchomionym CK3.**
- Przed nowym wątkiem / przy wznowieniu pracy czytaj `README.md`, `PROJECT_STATUS.md`, `CHANGELOG.md`, tę procedurę i plan testów najnowszej wersji.
- Nie wymagaj od użytkownika odtwarzania historii całego projektu, jeśli stan jest już zapisany w repozytorium.
