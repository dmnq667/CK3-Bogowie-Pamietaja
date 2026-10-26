# Kontrola statyczna: Sąd Popiołu i Przysięgi 0.2.0 DEV

**Stan:** PASS statyczny, test silnika CK3: NIE PRZEPROWADZONO.  
**Źródło:** gałąź `feature/0.2.0-gromnica-dual-duty`.  
**Reguła wydania:** bez połączenia do `main` przed zaakceptowaniem wyników testu 0.1.9 i uruchomieniem 0.2.0.

## Potwierdzenia

- Siedem unikalnych identyfikatorów: `bp_judgement.1001`, `1002`, `1011`–`1015`; wszystkie wewnętrzne połączenia wskazują istniejące wydarzenia.
- Nowe definicje `scripted_triggers` i `scripted_effects`, ich odwołania oraz nawiasy bloków mają potwierdzoną spójność.
- 42 nowe klucze fabularne Sądu I i kompletna karta kroniki Welesa. Polska i angielska lokalizacja mają po 741 unikalnych kluczy całego moda na etapie kontroli; brak duplikatów i brakujących odwołań dotyczących sądu. Zachowane prefiksy BOM.
- Cechę `bp_gods_mark_1_v020` zdefiniowano w `common/traits` i powiązano z unikatową ikoną `gfx/interface/icons/traits/bp_gods_mark_1_v020.dds`. Ikona: DDS, 64×64 px, BC3/DXT5, 4224 bajty.
- Trzy oddzielne roczne modyfikatory: +5 dyplomacji; +5 intrygi oraz +10 naturalnego postrachu; +5 wiedzy. Odrębne premie nie są sumowane równocześnie podczas pojedynczego wyroku.
- Sąd nie zawiera efektu `add_gold`; jedyna planowana nagroda +1500 złota pozostaje w przyszłym Sądzie II.
- Ochrona zarówno ognia, jak i mieszkańców Gromnicy jest rejestrowana osobnym znacznikiem. Sąd rozpatruje także ścieżki Welesa: prawdę, odmowę, ofiarę, łaskę, kłamstwo i oczekującego więźnia.
- Krwawa ofiara ma celowo wyższy priorytet niż łagodne rozstrzygnięcie, nawet jeżeli władca wykonał oba obowiązki Gromnicy.
- Do uruchamiania wykorzystano istniejący strażnik kalendarza, bez drugiego własnego cyklu zdarzeń.
- Blokada sądu ma zasięg dynastyczny i chroni przed wielokrotnym wywołaniem w jednym obiegu. Przyznanie nagrody zapisuje wynik bieżącej postaci oraz ostatni historyczny wyrok rodu, odczytywany w Księdze Bogów.
- Wersja stable `main` nadal ma `descriptor.mod` w wersji `0.1.9-alpha`; gałąź rozwojowa ma `0.2.0-dev`.

## Scenariusze wymagające testu w rzeczywistym CK3

| ID | Ścieżka | Oczekiwany wynik | Stan |
| --- | --- | --- | --- |
| C01 | Ogień → osady; Weles → prawda | Światło dla żywych, +5 dyplomacji, cecha | NIE TESTOWANO |
| C02 | Osady → ogień; Weles → łaska więźnia | Światło dla żywych, +5 dyplomacji, cecha | NIE TESTOWANO |
| C03 | Ogień i osady; Weles → krwawa ofiara | Słowo dane ziemi, +5 intrygi i +10 naturalnego postrachu | NIE TESTOWANO |
| C04 | Pomoc osadom; Weles → świadoma odmowa ceny | Granica ofiary, +5 wiedzy | NIE TESTOWANO |
| C05 | Zaniedbanie Gromnicy lub kłamstwo / ucieczka u Welesa | Gdy bogowie milczą, brak nowej cechy | NIE TESTOWANO |
| C06 | Niewybrany jeszcze więzień albo prośba o czas | Niedopełniona cena, nie wyrok winy | NIE TESTOWANO |
| C07 | Sąd I z nowym długiem Welesa | Zachowany dług, bez automatycznej kary za sam pakt | NIE TESTOWANO |
| C08 | Odmowa przyjęcia znaku po pozytywnym wyroku | Brak nowej premii, nie cofanie wcześniejszej cechy | NIE TESTOWANO |
| C09 | Przełom roku, ponowne wywołanie, sukcesja, zapis/odczyt | Brak dublowania bieżącego rozstrzygnięcia i premii | NIE TESTOWANO |
| C10 | Księga Bogów, rozdział Welesa, po roku | Bieżący wynik i archiwalna pamięć rodu rozróżnione | NIE TESTOWANO |
| C11 | Wyłączenie nowej gałęzi, powrót do 0.1.9 | Brak zmian w starym źródle, test na osobnym zapisie | NIE TESTOWANO |
| C12 | Instalacja 0.2.0 w środku cyklu lub bez dawnych decyzji | Brak fałszywego odtworzenia nieznanych wyborów | NIE TESTOWANO |

## Co można automatycznie sprawdzać

- Skrypt repozytorium: `tools/validate_first_court_020.py`.
- Workflow: `.github/workflows/validate-first-court-020.yml`, generuje raport JSON i archiwum deweloperskie.
- **Nie oznaczać joba jako wykonany/pomyślny bez odczytu rzeczywistego przebiegu na GitHub Actions.**
- Silnik CK3, warstwa UI, powiązania DDS z grafią i działanie z innymi modami wymagają uruchomienia gry. Nie są wynikiem walidacji statycznej.
