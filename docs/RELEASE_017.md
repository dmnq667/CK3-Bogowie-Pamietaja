# Bogowie pamiętają: wydanie 0.1.7 ALPHA, oprawa wydarzeń

**25 października 2026.** Kontynuacja rzeczywiście testowanej w grze wersji **0.1.6-alpha**.

## Zakres

- Zachowano mechanikę ośmiu świąt i automatyczne zapowiedzi z pauzą, które użytkownik przetestował w CK3.
- Zachowano wszystkie 78 definicji wydarzeń i wszystkie 403 właściwe klucze lokalizacji w każdym języku (dodatkowo po jednym nagłówku `l_polish:` / `l_english:`). Poprzednia statystyka 404 obejmowała nagłówek pliku.
- Zachowano pełną treść decyzji, skutków, dat, interakcji i on_actions bit w bit.
- Wykorzystano 20 oryginalnych ilustracji dostarczonych przez użytkownika, 2 z Gromnicy, 3 z Tygodnia Welesa, 2 z marcowego Nowego Roku, 1 z Jarych Godów, 3 z Gaiku, 3 z Dziadów, 3 ze Stada i 3 z Kupały.
- Wygenerowano 20 tekstur CK3 DDS DXT1 1592×848, bez mipmap i bez modyfikowania plików JPG.
- Do 67 istniejących, widocznych okien dodano `override_background` (łącznie 69 bloków; w dwóch wydarzeniach obraz zmienia się zależnie od flagi). Tła zapowiedzi, scen i stron Kroniki są ze sobą spójne.
- Dołączono `common/event_backgrounds/bp_slavic_holiday_backgrounds.txt` definiujący osobne nazwy zasobów, bez nadpisywania oryginalnych definicji CK3.
- Wszystkie oryginalne obrazy dołączono w katalogu `source_artwork` poza głównym folderem instalacyjnym moda.
- Instalator na H: nadal wykonuje kopie bezpieczeństwa i nie dotyka The Weight of Words, a przed instalacją weryfikuje istnienie wszystkich 20 DDS.

## Walidacja

**Statyczna: PASS.** Sprawdzono dekodowanie DDS, nagłówki DXT1, rozdzielczość, integralność JPG (SHA-256), unikatowe identyfikatory rejestru, kompletność odwołań w 67 wydarzeniach, poprawność nawiasów, nienaruszony kod 0.1.6 po odjęciu nowych pól oprawy, parzystość lokalizacji, strukturę instalatora. Wynik znajduje się w `docs/VALIDATION_017.json`.

**Test w silniku CK3: BRAK.** Tylko gra potwierdzi, czy definicje niestandardowych teł są załadowane, czy portrety nie zakrywają ważnych obiektów i czy wymagana jest korekta kadru. Na pierwszym teście uruchomić 0.1.7 na kopii save.

## Zalecany scenariusz testu

1. Rozpakować cały ZIP. Wykonać `PRZYGOTUJ_NA_H.bat`. Kopia poprzedniej wersji trafi do `H:\codex\_CK3_backups`.
2. Włączyć w CK3 tylko `Bogowie pamietaja - The Gods Remember`, najlepiej na kopii zapisu. Start gry powinien działać jak w 0.1.6.
3. W trybie debug wywołać zapowiedź Gromnicy i Welesa. Sprawdzić, czy tło jest czytelne i portret nadal widoczny.
4. Z [TEST] otworzyć Gaik, Dziady, Stado i Noc Kupały, przeglądając także ich kolejne sceny.
5. Sprawdzić Księgę Bogów i zapisy statusów, ponieważ część jej stron ma teraz tematyczne tła.
6. Sprawdzić, czy wszystkie sceny nadal pauzują grę oraz czy wybory nie tracą konsekwencji.
7. W razie błędu przesłać `error.log`, datę rozgrywki, zrzut ekranu i aktywne mody.

**Nie rozszerzano scenariuszy fabularnych ani nowych świąt.** Kolejne cztery święta (Perun, Plony, Dziady jesienne, Szczodre Gody) pozostają do zaplanowania i wdrożenia po stabilizacji grafiki 0.1.7.
