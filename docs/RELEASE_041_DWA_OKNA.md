# Gniew i Łaska Bogów — 0.4.1 DEV: Dwa okna, dwa zadania

**Stan: poprawka przygotowana i sprawdzona automatycznie 9 listopada 2026.**  
**GitHub Actions:** [przebieg #42565179434](https://github.com/dmnq667/CK3-Bogowie-Pamietaja/actions/runs/42565179434) — testy skryptów **PASS**, próba rzeczywistej instalacji na Windows PowerShell 5.1 **PASS**.  
**[Pobierz aktualizator 0.4.1 DEV](https://github.com/dmnq667/CK3-Bogowie-Pamietaja/actions/runs/42565179434/artifacts/13651276740)**.

## Założenie wynikające z testu użytkownika

Dotychczasowy model 0.4.0 był dramaturgiczny, ale przedstawiał święta jedynie jako tło przypadkowych wyroków. Ponadto efekty `bp_040_oath_of_peace_modifier`, `bp_040_feud_curse_modifier`, `bp_040_blood_price_modifier` były widoczne w interfejsie w postaci technicznych identyfikatorów. **Obie sprawy zostały skorygowane w 0.4.1.**

Każde z dwunastu świąt składa się teraz z **dokładnie dwóch okien wyświetlanych kolejno**:
1. **Obrzęd.** Zrozumiałe objaśnienie nazwy, czasu i sensu święta. Udział daje **+45 pobożności, -10 stresu oraz 90-dniową premię tematyczną**. Bonus jest przyznawany tylko w tym oknie. Przyciski pierwszego okna są krótkie; dokładne wartości i nazwa daru pojawiają się w podpowiedzi CK3.
2. **Los władcy.** Dalsza część z realnym problemem, trudnymi wyborami, konsekwencjami i możliwością krwawego wyroku. Dotychczasowe mechanizmy boskich długów, ofiar, klątw i zemsty zostały zachowane.

Dawne opcjonalne zapowiedzi `bp_announcement.1001`–`1012` stały się **niewidocznymi przekaźnikami**; nie dodają trzeciego okna. Dotychczasowe wejścia z Kalendarza Bogów nadal kierują na te same identyfikatory `bp_gromnica.1001`, `bp_weles.2001` itd. Drugie sceny przeniesiono do `bp_041.2101`–`2112`. Odrębne, odłożone w czasie objawienia bogów i zemsty **nie liczą się do dwustopniowego obrzędu**; są osobnymi rozdziałami rozgrywki.

## Komplet dwunastu świąt

| Święto | Pierwsze okno: obrzęd i premia na 90 dni | Drugie okno: konflikt |
| --- | --- | --- |
| Gromnica | Ogień chroniący dom; Ochrona ognia | Komu pomóc podczas śnieżycy; los osad |
| Siedem Nocy Welesa | Wspomnienie zmarłych i pamięć przysiąg; Dostatek spod korzeni | Pakt z Welesem, więzień lub odmowa długu |
| Wiosenny Nowy Rok | Przygotowanie ziemi i ziarna; Błogosławieństwo siewu | Wojsko żąda zapasów potrzebnych na zasiew |
| Jare Gody | Równonoc, odejście zimy i pojednanie; Nowe więzi | Spór rodów, sąd i możliwość egzekucji |
| Gaik / Turzyca | Zielone gałązki i święty gaj; Ochrona gaju | Wyrąb i brutalny konflikt w gaju |
| Dziady wiosenne | Pamięć przodków i odziedziczone zobowiązania; Wiedza przodków | Roszczenie rodziny skrzywdzonej przez dawny wyrok |
| Stado | Wspólna uczta, rodzina i pojednanie; Zgoda w rodzinie | Krwawa bójka i spór o winę |
| Noc Kupały | Ognie, wianki i woda; Łaska miłości | Tonący dworzanin i śmiertelna próba ratunku |
| Święto Peruna | Dąb, wojowie i przysięga; Wojenny zapał | Złamana przysięga, egzekucja lub próba życia |
| Święto Plonów | Wdzięczność za zbiory i podział żywności; Pomyślność plonów | Podatki, głód i odpowiedzialność za krzywdę |
| Dziady jesienne | Pamięć o zmarłych i zadośćuczynienie; Mądrość przodków | Żywi świadkowie domagają się sprawiedliwości |
| Szczodre Gody | Powrót światła, wspólnota i gościnność; Szczodra gościnność | Prawo gościny, zdrada lub krwawy wyrok |

W przypadku świąt mających więcej niż jeden zatwierdzony obraz pierwsze i drugie okno korzystają z **różnych istniejących ilustracji**. Nie wykonano nowych grafik i nie przywrócono czterech odrzuconych wariantów.

## Usunięcie podkreślników

Dodano lokalizacje **15 nowych modyfikatorów** z `common/modifiers/bp_040_modifiers.txt` i **4 modyfikatorów opinii** z `common/opinion_modifiers/bp_040_opinions.txt` — każde oznaczenie ma nazwę i opis w języku polskim i angielskim. Zachowano wcześniej istniejące lokalizacje wszystkich jedenastu używanych premii obrzędowych.

Przykłady:
- `bp_040_oath_of_peace_modifier` → **Przysięga zgody**;
- `bp_040_feud_curse_modifier` → **Waśń bez pojednania**;
- `bp_040_blood_price_modifier` → **Cena przelanej krwi**.

## Zakres testów

- **12/12 PASS:** dokładnie dwie widoczne sceny na każde święto, z uwzględnieniem starych zapowiedzi;
- sprawdzona poprawność referencji do `bp_041.21xx`, nazw, polskich i angielskich opisów;
- sprawdzono komplet 19 nowych tłumaczeń efektów i 31 zatwierdzonych tekstur;
- instalator Windows 0.4.1 rzeczywiście nadpisał próbny mod 0.4.0 i wykonał jego kopię: **PASS**.

**Nie jest to potwierdzenie działania w samej grze CK3.** Do sprawdzenia w rozgrywce pozostaje otwieranie obu okien, właściwy moment naliczania premii, przypisanie rzeczywistej postaci w scenie wyroku, działanie efektów i `error.log`. Nie oznaczamy wersji jako stabilnej bez tego testu.

## Instalacja

1. Pobierz [poprawną paczkę 0.4.1 DEV](https://github.com/dmnq667/CK3-Bogowie-Pamietaja/actions/runs/42565179434/artifacts/13651276740).
2. Rozpakuj ZIP pobrany z GitHub Actions, następnie rozpakuj `GNIEW_I_LASKA_BOGOW_0.4.1_DEV_NADPISZ.zip` znajdujący się wewnątrz.
3. Wyłącz CK3.
4. Uruchom `AKTUALIZUJ_041.bat`. Instalator nadpisze obecną instalację moda, zachowując jej kopię. **Nie tworzy drugiego wpisu w launcherze.**
5. Wczytaj **kopię zapisu gry**, przetestuj Gromnicę, Jare Gody i Dziady wiosenne, zwróć uwagę na nazwy modyfikatorów, a potem pozostałe święta.

**Wersja 0.4.0 na poprzedniej gałęzi nie została nadpisana**. Repozytorium `main` pozostało nietknięte.
