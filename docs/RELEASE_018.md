# Bogowie pamietaja 0.1.8 ALPHA: dlug wobec Welesa

Data: 25.10.2026. To jest wersja do testowania na kopii kampanii CK3 1.20.1.2.

## Status poprzedniej wersji

Uzytkownik potwierdzil w rzeczywistej grze, ze wszystkie oryginalne tla 0.1.7 wyswietlaja sie prawidlowo. Nie modyfikowano tekstur, rejestru grafik, eventow zapowiadajacych swieta, harmonogramu ani plikow on_action.

## Rozwoj fabuly

- Cztery nowe wydarzenia Welesa: 2011 Imiona spod korzeni, 2012 Puste miejsce w spichlerzu, 2013 Dlug odziedziczony, 2014 To, co przyjela ziemia.
- Po wielkim darze Welesa kontrakt zapisuje sie na DYNASTII. Po 90-160 dniach istnieje zapowiedz wierzyciela 2010, a po dalszych 18-36 dniach pojawia sie realny wybor naprawy winy, publicznego wyznania prawdy albo odmowy. Odmowa prowadzi do kolejnego wydarzenia po 300-430 dniach.
- Sprawa moze powrocic przy Dziadach wiosennych, takze dla nowego wladcy tej samej dynastii, gdy posiadacz pierwotnego zobowiazania zmarl. Watek jest uruchamiany po wyborze rodzaju Wiedzy Przodkow. Stan nie zalezy wylacznie od flagi na postaci.
- W Ksieze Bogow > Weles jest strona Ksiegi dlugow z aktualnym statusem niezaplaconego lub rozliczonego zobowiazania. Otwieranie ksiag pozostaje bez oplat i nie udziela nagrod.
- Przy otwartym dlugu nowa decyzja Rozlicz dlug Welesa pozwala samodzielnie wezwac zerce (nie czesc swieta), z ograniczeniem do jednego razu na 90 dni. Dziala rowniez gdy potomek zmieni wiare. Nie sluzy do powtarzania wielkich blogoslawienstw.
- Weles nie przyzna drugiego wielkiego blogoslawienstwa przy nieuregulowanym dlugu. Nowa scena slabego daru wyjasnia ten warunek.
- Przy dawnej ofierze z czlonka dynastii pamiec o krwi jest trwalym znacznikiem dynastii; odmienny opis wystepuje przy odziedziczonym dlugu. Wiosenne swieta i Dziady odnosza sie do tej pamieci.
- Nowe konkretne skutki: przywrocone imiona i odrodzenie wybranej ziemi, dodatkowa wiedza po publicznym wyznaniu, cien wierzyciela na wladcy i kara gospodarcza na hrabstwie za uporczywa odmowe.
- [TEST] Bogowie pamietaja > Kolejne swieta > [TEST] Dlug Welesa: nowa strona do wywolywania scen bez czekania na miesiace. Tylko na kopii zapisu.

## Kompatybilnosc zapisow

Po aktualizacji z 0.1.7 otworz raz Ksiega Bogow. Jesli AKTUALNY wladca ma wciaz flage dlugu Welesa po dawnej wielkiej lasce, mechanizm przeniesie ja do dynastycznego rejestru. Sprawdzi takze pamiec dawnych ofiar z rodziny. Jesli oryginalna postac juz zmarla, a stara wersja nie zapisala dlugu na dynastii, danych o nim nie mozna wiarygodnie odzyskac wstecz.

Zadnej z 8 dat swiat, 20 tekstur DDS i materialow JPG, 8 automatycznych zapowiedzi, kalendarza ani bazowej funkcji pauzy nie zmieniono. Mod The Weight of Words pozostaje oddzielny i nietkniety.

## Kontrola

STATIC PASS: 84 eventy CK3 (w tym 6 nowych okien: 4 Weles, 1 Ksiega, 1 TEST), 452 poprawne klucze PL i 452 EN; sprawdzono nawiasy, cytowania, strukture, cele trigger_event, efekty fabularne, wszystkie 20 tekstur DDS i ich niezmienione bajty oraz dokladna zgodnosc kodu kalendarza z 0.1.7. Raport szczegolowy: docs/VALIDATION_018.json.

GAME TEST: NIE WYKONANO dla nowej fabuly 0.1.8. Dopiero CK3 potwierdzi zachowanie skryptow, dziedziczenia i tooltipow. To jest wczesna alfa, nie stabilne wydanie. Testuj na kopii zapisu. Jesli wystapi blad, przeslij screenshot oraz Documents/Paradox Interactive/Crusader Kings III/logs/error.log.
