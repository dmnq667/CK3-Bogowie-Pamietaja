# Bogowie pamiętają 0.1.6 ALPHA: poprawki interfejsu i kalendarza

## Zgłoszenie
- Na ekranie decyzji Stada przycisk pokazywał `bp_stado_decision_confirm`.
- W wymaganiach pojawiał się różowy błąd `[BUG: 'has_variable' missing localization NOT_has_variable_trigger]`.
- Noc Kupały informowała tylko ikonką "Dostępna decyzja", bez pauzy. Również nowe święta mogą nie być zaplanowane, gdy mod dodano do trwającego zapisu po 1 stycznia.

## Poprawki 0.1.6
1. Dodano 4 brakujące potwierdzenia przycisków w PL i EN oraz jawne `confirm_text`.
2. Przeniesiono warunek `nie odprawiono w bieżącym sezonie` z widocznych `is_valid`/Wymagań do niewidocznego `is_shown`. Zrealizowany obrzęd znika z Decyzji do kolejnego sezonu, pozostaje do odczytu w Księdze i Kronice. Usunięto przyczynę różowego `[BUG]`.
3. Mechanizm zapowiedzi zmieniono: po inicjacji przez standardowy roczny on_action, po rozpoczęciu nowej kampanii, przez kwartalny fallback albo otwarcie Księgi Bogów, **jeden niewidoczny event na gracza** sprawdza datę **raz na dzień**, we wszystkich 8 okresach. Otwiera właściwy *widoczny* `character_event`, a nie toast/alert decyzji. Wpisy lat przestępnych obsługuje bez liczenia przesunięć.
4. Jeśli wersję zainstalowano w środku kampanii, otwarcie Księgi Bogów uruchamia licznik kolejnego dnia. Mod nie próbuje odtwarzać minionych świąt.
5. Pozostawiono poprzednie definicje wydarzeń i kalendarza do obsługi zdarzeń już zakolejkowanych w zapisach. Usunięto jedynie automatyczne tworzenie starych harmonogramów (nie wolno ręcznie kasować eventów z zapisu).
6. Poprawiono 2 literówki w zapowiedziach.

## Zastrzeżenie
W prawidłowo uruchomionym CK3 zwykłe wydarzenie wymagające decyzji zazwyczaj pauzuje grę. **Nie dodano nieudokumentowanego `pause_game` ani zmian w plikach vanilla GUI.** Wpływ innych modów oraz ustawień wiadomości trzeba zweryfikować w grze. Kontrola skryptów NIE zastępuje testu CK3 1.20.1.2.

## Szybki test
1. Rozpakuj ZIP, uruchom `PRZYGOTUJ_NA_H.bat` po wykonaniu kopii zapisu kampanii.
2. Po włączeniu moda wejdź raz w **Decyzje -> Księga Bogów**. Zapisz grę, a następnie uruchom ją na normalnej prędkości.
3. W oknie 20–23 czerwca, jeśli obrzędu jeszcze nie odprawiono, poczekaj do następnego dnia. Powinien ukazać się **pełny modal zapowiedzi Nocy Kupały** (a nie tylko ikonka). Sprawdź ikonę pauzy u góry mapy.
4. Otwórz Stado w maju/czerwcu, upewnij się, że przycisk ma polski napis i brak różowych komunikatów w wymaganiach. Po odprawieniu obrzędu nie powinien pojawić się ponownie w tym sezonie.
5. W trybie debug można użyć `[TEST] -> Zapowiedzi -> Noc Kupały`, aby od razu zobaczyć pełen popup. Taki ręczny test **nie sprawdza** automatycznej zapowiedzi.
6. Jeśli modal nie przyjdzie po następnym dniu, prześlij `Documents\Paradox Interactive\Crusader Kings III\logs\error.log` wraz z datą w grze i listą modów.

**Status wydania:** Statycznie sprawdzone, **NIEPRZETESTOWANE W URUCHOMIONYM CK3**.
