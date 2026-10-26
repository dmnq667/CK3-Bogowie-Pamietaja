# Bogowie pamiętają 0.1.7: oprawa wydarzeń

Wszystkie tła powstały WYŁĄCZNIE z oryginalnych prac dostarczonych przez użytkownika.
Nie wygenerowano ani nie zastąpiono żadnej ilustracji grafiką zewnętrzną.

## Lista teł

### Gromnica (zimowe ognie)
- `bp_gromnica_01.dds` ← `01-gromnica-01.jpg`
- `bp_gromnica_02.dds` ← `gromnica-02.jpg`

### Tydzień Welesa (mrok / ogień / następstwa)
- `bp_weles_02.dds` ← `02-siedem-nocy-02.jpg`
- `bp_weles_03.dds` ← `02-siedem-nocy-03.jpg`
- `bp_weles_04.dds` ← `02-siedem-nocy-04.jpg`

### Wiosenny Nowy Rok (poranek / noc)
- `bp_spring_01.dds` ← `03-Wiosenny-Nowy-Rok-01.jpg`
- `bp_spring_02.dds` ← `03-Wiosenny-Nowy-Rok-02.jpg`

### Jare Gody (Marzanna)
- `bp_jare_01.dds` ← `04-Jare-Gody-01.jpg`

### Gaik / Turzyca (gaj i zieleń)
- `bp_gaik_01.dds` ← `05-gaik-turzyca-01.jpg`
- `bp_gaik_02.dds` ← `05-gaik-turzyca-02.jpg`
- `bp_gaik_03.dds` ← `05-gaik-turzyca-03.jpg`

### Dziady wiosenne (głosy przodków)
- `bp_dziady_01.dds` ← `06-dziady-wiosenne-01.jpg`
- `bp_dziady_02.dds` ← `06-dziady-wiosenne-02.jpg`
- `bp_dziady_03.dds` ← `06-dziady-wiosenne-03.jpg`

### Stado (święto wspólnoty)
- `bp_stado_01.dds` ← `07-Stado-01.jpg`
- `bp_stado_02.dds` ← `07-Stado-02.jpg`
- `bp_stado_03.dds` ← `07-Stado-03.jpg`

### Noc Kupały (ognie i rzeka)
- `bp_kupala_01.dds` ← `08-Noc-Kupaly-01.jpg`
- `bp_kupala_02.dds` ← `08-Noc-Kupaly-02.jpg`
- `bp_kupala_03.dds` ← `08-Noc-Kupaly-03.jpg`

## Przypisanie do scen CK3

Wpisy poniżej odnoszą się do event IDs w modzie, a nie do nowych identyfikatorów wydarzeń.

### bp_announcement

- `bp_announcement.1001` → `gromnica_02`
- `bp_announcement.1002` → `weles_03`
- `bp_announcement.1003` → `spring_01`
- `bp_announcement.1004` → `jare_01`
- `bp_announcement.1005` → `gaik_01`
- `bp_announcement.1006` → `dziady_01`
- `bp_announcement.1007` → `stado_03`
- `bp_announcement.1008` → `kupala_01`
- `bp_announcement.9901` → `gromnica_02`
- `bp_announcement.9905` → `gaik_01`
- `bp_announcement.9906` → `dziady_01`
- `bp_announcement.9907` → `stado_03`
- `bp_announcement.9908` → `kupala_01`

### bp_gromnica

- `bp_gromnica.1001` → `gromnica_02`
- `bp_gromnica.1002` → `gromnica_01` przy `has_character_flag = bp_gromnica_fire`, `gromnica_02` domyślnie

### bp_weles

- `bp_weles.2001` → `weles_04`
- `bp_weles.2002` → `weles_03`
- `bp_weles.2003` → `weles_03` przy `has_character_flag = bp_weles_dynasty_blood`, `weles_04` domyślnie
- `bp_weles.2004` → `weles_03`
- `bp_weles.2005` → `weles_03`
- `bp_weles.2006` → `weles_02`
- `bp_weles.2007` → `weles_04`
- `bp_weles.2008` → `weles_04`
- `bp_weles.2010` → `weles_02`

### bp_spring

- `bp_spring.3001` → `spring_01`
- `bp_spring.3002` → `spring_02`

### bp_jare

- `bp_jare.4001` → `jare_01`
- `bp_jare.4002` → `jare_01`
- `bp_jare.4003` → `jare_01`

### bp_gaik

- `bp_gaik.5001` → `gaik_01`
- `bp_gaik.5002` → `gaik_02`
- `bp_gaik.5003` → `gaik_03`

### bp_dziady

- `bp_dziady.6001` → `dziady_01`
- `bp_dziady.6002` → `dziady_02`
- `bp_dziady.6003` → `dziady_03`

### bp_stado

- `bp_stado.7001` → `stado_01`
- `bp_stado.7002` → `stado_02`

### bp_kupala

- `bp_kupala.8001` → `kupala_01`
- `bp_kupala.8002` → `kupala_02`
- `bp_kupala.8003` → `kupala_03`
- `bp_kupala.8004` → `kupala_01`
- `bp_kupala.8005` → `kupala_03`
- `bp_kupala.8006` → `kupala_02`

### bp_calendar

- `bp_calendar.8101` → `gromnica_02`
- `bp_calendar.8111` → `gromnica_01`
- `bp_calendar.8102` → `weles_03`
- `bp_calendar.8112` → `weles_03`
- `bp_calendar.8103` → `spring_01`
- `bp_calendar.8113` → `spring_02`
- `bp_calendar.8104` → `jare_01`
- `bp_calendar.8114` → `jare_01`

### bp_book

- `bp_book.0001` → `dziady_03`
- `bp_book.0002` → `weles_04`
- `bp_book.0003` → `spring_01`
- `bp_book.0005` → `gaik_02`
- `bp_book.0006` → `dziady_03`
- `bp_book.0007` → `dziady_02`
- `bp_book.0008` → `dziady_02`
- `bp_book.0009` → `gaik_02`
- `bp_book.0101` → `gromnica_02`
- `bp_book.0102` → `weles_03`
- `bp_book.0103` → `spring_01`
- `bp_book.0104` → `jare_01`
- `bp_book.0105` → `gaik_01`
- `bp_book.0106` → `dziady_02`
- `bp_book.0107` → `stado_01`
- `bp_book.0108` → `kupala_01`

## Konwersja

- Rozmiar tekstur: **1592 × 848 px**, zgodnie z bazowym rozmiarem scen wydarzeń CK3.
- Format: **DDS DXT1 (BC1)**, bez mipmap. Oryginalne JPG nie zostały zmienione.
- Konwersja: skalowanie Lanczos i niewielkie, centralne przycięcie dla formatu okna.
- Wpisy w `common/event_backgrounds/bp_slavic_holiday_backgrounds.txt` rejestrują tekstury.
- Sceny wykorzystują `override_background`; definicje `theme = diplomacy` i portrety CK3 pozostają.
- W wydarzeniach technicznych `[TEST]` oraz niezrealizowanym jeszcze wpisie o Perunie pozostawiono domyślną oprawę, by nie używać nieadekwatnej ilustracji.

## Test w grze

1. Na kopii zapisu włącz mod 0.1.7 i uruchom dowolną scenę testową Gromnicy oraz Welesa.
2. Sprawdź, czy pojawia się nowa grafika zamiast starej i czy portret postaci jest widoczny.
3. Przetestuj Stado i Noc Kupały, a następnie Księgę Bogów i Kronikę.
4. W razie pustego lub różowego tła zbierz `error.log` oraz zrzut ekranu.
5. Gdy wszystko działa, wybierzemy ostateczne kadrowanie w realnym oknie gry.
