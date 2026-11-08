# Gniew i Łaska Bogów — produkcyjna lista wydarzeń i grafik (0.3.0 DEV)

**Podstawa:** faktyczne skrypty gałęzi `feature/0.3.0-gniew-i-laska` i rejestr teł `bp_slavic_holiday_backgrounds.txt`.
**Status:** plan assetów i fabuły; nie oznacza gotowych grafik ani przepisanych scen.

## Zasada

- **Święto:** istniejąca grafika obrzędowa użytkownika; jeden krótki, jasny opis i premia za uczestnictwo.
- **Znak, wiadomość od żercy:** może korzystać z istniejącej grafiki; nowy kadr jest opcjonalny.
- **Bóg obecny osobiście, przemawia do władcy, ogłasza wyrok:** **nowa ilustracja sytuacyjna z widocznym bogiem**, zgodna ze sceną; wymaga spójnego tekstu wydarzenia.
- Wszystkie 32 dotychczasowe źródłowe JPG (w tym zatwierdzone trzy prace Peruna) pozostają nietknięte.
- Nie mylić: **obraz już przypisany** nie znaczy, że **obraz pasuje do nowego objawienia**.

## 1. Kalendarz: 12 świąt i tła zachowane

| Święto | Otwarcie wydarzenia | Zatwierdzone tła, bez zamiany | Produkcja |
| --- | --- | --- | --- |
| Gromnica | `bp_gromnica.1001` | `gromnica_01/02` | Zachować |
| Siedem Nocy Welesa | `bp_weles.2001` | `weles_02/03/04` | Zachować |
| Wiosenny Nowy Rok | `bp_spring.3001` | `spring_01/02` | Zachować |
| Jare Gody | `bp_jare.4001` | `jare_01` | Zachować |
| Gaik / Turzyca | `bp_gaik.5001` | `gaik_01/02/03` | Zachować |
| Dziady wiosenne | `bp_dziady.6001` | `dziady_01/02/03` | Zachować |
| Stado | `bp_stado.7001` | `stado_01/02/03` | Zachować |
| Noc Kupały | `bp_kupala.8001` | `kupala_01/02/03` | Zachować |
| Święto Peruna | `bp_perun.9101` | `perun_01/02/03` | Zachować 3 zatwierdzone |
| Dożynki | `bp_harvest.9201` | `harvest_01/02/03` | Zachować |
| Dziady jesienne | `bp_autumn.9301` | `autumn_01/02/03` | Zachować |
| Szczodre Gody | `bp_szczodre.9401` | `szczodre_01/02/03` | Zachować |

## 2. Priorytet A — ilustracje do wykonania pod konkretną scenę

**A01 — Weles. „Wyrok za dług”**  
Event `bp_weles.2020`, obecne tło `bp_scene_weles_03`. Scena: władca dwukrotnie odrzucił spłatę długu; Weles staje osobiście przed nim, żąda zapłaty albo przyjęcia wyroku; gracz może zginąć. **NOWA GRAFIKA WYMAGANA, jeśli Weles osobiście przemawia**. **WYMAGANA KOREKTA TEKSTU:** w obecnym opisie mówi żerca.

**A02 — Perun. „Próba odpowiedzialności”**  
Event `bp_perun.9110`, obecne tło `bp_scene_perun_03`. Scena: odmowa świętego obowiązku wobec wojów; Perun ukazuje się przy strażnicy wśród burzy i ogłasza warunki zadośćuczynienia lub wyzwania. Śmierć możliwa wyłącznie w świadomie wybranej śmiertelnej próbie. **NOWA GRAFIKA WYMAGANA, jeśli Perun osobiście przemawia**. **WYMAGANA KOREKTA TEKSTU:** obecnie komunikat przekazuje żerca.

**A03 — Mokosz. „Nieurodzaj i nowy siew”**  
Event `bp_spring.3010`, obecne tło `bp_scene_spring_02`. Scena: odmówiono pomocy wiosną; Mokosz objawia się na zniszczonych polach i żąda naprawienia szkody. **NOWA GRAFIKA WYMAGANA, jeśli Mokosz osobiście przemawia**. **WYMAGANA KOREKTA TEKSTU:** obecnie komunikat przekazuje żerca.

## 3. Priorytet B — pozostałe sceny boskie do rozstrzygnięcia po rewizji tekstów

| Event | Obecna treść / obraz | Decyzja |
| --- | --- | --- |
| `bp_weles.2003` | Weles mówi bezpośrednio spod korzeni dębu; obecne `weles_03/04` | **NOWA**, jeśli ukaże się osobiście; dotychczas może być głosem bez postaci |
| `bp_weles.2006` | Postać w gaju przemawia głosem Welesa i obiecuje dostatek; `weles_02` | **NOWA**: objawienie i skarbiec |
| `bp_jare.4002` | Mokosz osobiście wychodzi z mgły nad rzeką, przemawia i błogosławi ziemi; `jare_01` | **NOWA**: jawne objawienie Mokoszy |
| `bp_kupala.8004` | Mokosz stoi nad rzeką i przemawia, udzielając łaski; `kupala_01` | **NOWA**: inne objawienie Mokoszy |
| `bp_kupala.8003` | Z rzeki słychać głos Mokoszy, bóg niewidoczny; `kupala_03` | **STARA WYSTARCZA**, jeśli pozostanie głosem; nowa, gdy przyjmie postać |
| `bp_perun.9105` | Błogosławieństwo poprzez piorun i broń wojów; `perun_03` | **STARA WYSTARCZA**, jeśli Perun nie pojawia się osobiście |
| `bp_perun.9107` | Gniew przez pęknięty posąg i grzmot; `perun_03` | **STARA WYSTARCZA**, jeśli bóg nie pojawia się osobiście |
| `bp_autumn.9304` | Sąd cieni przodków i znak Welesa, bez osobistej postaci; `autumn_03` | **STARA WARUNKOWO**, osobny Weles tylko przy bezpośrednim objawieniu |
| `bp_judgement.1001` | Sąd Popiołu i Przysięgi, różne wyroki; `gromnica_02` | **STARA NA RAZIE**, odrębna scena jeśli bogowie zasiądą fizycznie do sądu |

## 4. Zdarzenia z tłem do zachowania / scalenia, bez nowych grafik na tym etapie

- **Gromnica:** `1001–1002` z istniejącymi tłami; `1003` techniczne ukryte.
- **Weles:** `2001–2002` ceremonie / wariant zachowany dla zapisów; `2004` wybór ofiary; `2005` instrukcja więźnia; `2007–2008` stare zakończenia; `2010` ukryte; `2011–2014` rozliczenie długu. Tła istnieją; *jeśli przebudowa sprawi, że bóg pojawi się osobiście — oznaczyć nową ilustrację*.
- **Wiosna:** `3001–3002`; grafiki istnieją.
- **Jare Gody:** `4001`, `4003`; grafika istnieje. `4002` → priorytet B.
- **Gaik:** `5001–5003`; grafiki istnieją.
- **Dziady wiosenne:** `6001–6003`; grafiki istnieją.
- **Stado:** `7001–7002`; grafiki istnieją.
- **Kupała:** `8001–8002`, `8005–8006`; grafiki istnieją. `8003–8004` → priorytet B.
- **Perun:** `9101–9104`, `9106`, `9108`; grafiki istnieją. `9105`, `9107` → priorytet B.
- **Dożynki:** `9201–9208`; grafiki istnieją, późniejsze sceny do scalania / skrócenia.
- **Dziady jesienne:** `9301–9303`, `9305–9308`; grafiki istnieją.
- **Szczodre Gody:** `9401–9408`; grafiki istnieją, późniejsze sceny do scalania / skrócenia.
- **Sąd I:** `bp_judgement.1001` jest aktualną sceną; `1002`, `1011–1015` pozostają dla zgodności z zapisami. Korzystają z wcześniejszych teł. Nie tworzyć nowych grafik dla etapów, które zostaną usunięte z widocznej sekwencji.

Inne sceny techniczne (Księga Bogów, kalendarz, ogłoszenia, testy) nie wymagają nowych portretów bogów tylko dlatego, że istnieją jako osobne eventy.

## 5. Wspólny workflow Magnific

**Exact legacy prompt: NIEODZYSKANY.** Dokumentacja potwierdza istniejące źródłowe grafiki użytkownika i styl mroczny, historyczno-słowiański; nie zawiera dosłownego promptu. **Nie nazywać poniższych promptów oryginalnymi.**

W Magnific za każdym razem podawać **rzeczywistą zatwierdzoną pracę referencyjną z `source_artwork/`** (nie generować wyłącznie na podstawie opisów) i tekst:
> Match the uploaded reference image's exact painterly technique, palette, lighting, brushwork, atmospheric depth, character realism and historical Slavic material culture. Maintain a cohesive visual series for a dark medieval Slavic mythology narrative game. Cinematic wide environmental storytelling composition for a Crusader Kings III event illustration. One clear dramatic moment, fully visible deity, believable medieval architecture and garments, practical light sources, no modern items, no text, no lettering, no logos, no UI, no borders. Preserve space and contrast for the game's character portraits and overlay.

**PROMPT A01 / WELES** — reference: `02-siedem-nocy-03.jpg` or `02-siedem-nocy-04.jpg`.  
> A direct manifestation of Veles, ancient Slavic deity of the underworld, debts and sacred oaths, confronting a medieval Slavic ruler inside a dark wooden throne hall. Veles is unmistakably visible as a commanding supernatural figure with archaic woodland and underworld symbolism, his presence emerging through roots, damp black earth and cold shadow. A sacrificial knife lies on the floor beside a record of the unpaid oath. The ruler faces him, fearful but able to choose. Flickering ritual fire, witnesses held back in darkness, the terrible moment before a divine verdict; dignified, emotionally intense, specific scene, not generic fantasy combat.

**PROMPT A02 / PERUN** — reference: `09-perun-01.jpg` (zatwierdzony Perun, nadrzędny dla wyglądu boga).  
> Perun, the mighty Slavic god of thunder and sacred warrior oaths, appears physically before a medieval Slavic ruler and his warriors at a timber watchtower. Storm clouds explode over an ancient sacred oak; one bolt of lightning reveals Perun as a towering divine warrior whose features, clothing and weapons closely match the provided approved Perun reference. The ruler has neglected his duty to protect his warriors, and the god demands a public oath of restitution. Warriors kneel beside shields and spears; broken watchtower timbers, wet earth, rain and lightning. Clear confrontation, solemn dread and martial grandeur, no triumphal victory pose.

**PROMPT A03 / MOKOSZ** — reference: `03-Wiosenny-Nowy-Rok-02.jpg` (lub druga zatwierdzona grafika Mokoszy, jeśli występuje).  
> Mokosh, the ancient Slavic goddess of earth, life, fertility and the harvest, visibly manifests before a medieval Slavic ruler at the boundary of barren spring fields. Starving villagers stand behind the ruler with empty baskets of seed. Mokosh is solemn, powerful and stern, not a gentle fairy; one hand rests on dark, cracked soil, and faint signs of new growth appear only near her fingertips. Her gaze condemns the ruler's refusal to provide seed while offering one final chance to repair the wrong. Cold spring morning, damp Slavic countryside, emotionally charged encounter, restrained supernatural atmosphere, grounded historical material culture.

**PROMPT B01 / WELES — DAR I DŁUG** — reference `02-siedem-nocy-02.jpg`.  
> Veles visibly manifests beneath the roots of an ancient sacred oak in a Slavic grove, showing a medieval ruler a hidden ancestral treasure. The gift of wealth is magnificent, but the god's expression and an unbroken ritual oath indicate a future debt. This is a negotiation with a powerful deity, not a celebration. Weathered wooden shrines, wet roots, dark earth, restrained gold highlights, dawn fog; clear focus on Veles, ruler and opened treasury.

**PROMPT B02 / MOKOSZ — JARE GODY** — reference `04-Jare-Gody-01.jpg`.  
> During Slavic spring equinox rites beside a river, Mokosh appears in person across a misty meadow before a ruler who has protected his people. The Marzanna effigy drifts away in the background. Plants spring from the wet soil beneath the goddess's steps; she raises a hand in an unmistakable blessing of the land. The goddess is clearly visible, solemn and regal, the villagers remain far behind, misty dawn, delicate but potent natural miracle.

**PROMPT B03 / MOKOSZ — KUPAŁA** — reference `08-Noc-Kupaly-01.jpg`.  
> At dawn after the Slavic Kupala night, Mokosh stands visibly on the opposite bank of a river, addressing a ruler beside dying ritual bonfires. Three seeds fall from the goddess's hand onto the water and begin to sprout. Flower wreaths float on the river, summer mist and warm ember light meet the first sunrise. A profound, serious blessing after the ruler aided the living, with the deity clearly visible, distinct from spring equinox imagery.

## 6. Format, nazwy i instalacja

- Plan: **1592 × 848** jako ostateczny kadr CK3; wygenerować większy oryginał o proporcji zbliżonej do **1.877:1**, zostawić zapas na bezpieczne przycięcie.
- Zachować kolorystykę i styl według oryginału referencyjnego, nie własnej nowej palety.
- Nazewnictwo źródeł np. `god_weles_2020_v01.png`, `god_perun_9110_v01.png`, `god_mokosh_3010_v01.png`; na etapie wyboru nie nadpisywać dawnych JPG ani DDS.
- Po akceptacji dodać DDS do `gfx/interface/illustrations/event_scene/`, zarejestrować osobne `bp_scene_...` i przypisać konkretny event. W CK3 zweryfikować kadr oraz portrety.
- Przed podpięciem A01/A02/A03 **przepisać narrację** tak, by przemawiał widoczny bóg; dziś w tych scenach przemawia żerca.

**To jest plan produkcyjny do wykonania grafik w Magnific, nie informacja o gotowych obrazach.**

## Zatwierdzenie Welesa — 8 listopada 2026

- **A01 / `bp_weles.2020`: GRAFIKA ZATWIERDZONA PRZEZ UŻYTKOWNIKA.** Jest to konkretny przesłany obraz ciemnej sali: potężny Weles po prawej, z długimi czarnymi włosami i brodą, w ciemnej futrzanej szacie, po lewej klęczący ukoronowany władca; chłodne niebiesko-czarne światło, świece, mgła i wilgotna posadzka. **Nie zastępować go kolejną generacją.**
- Nazwa bieżącego pliku przesłanego w rozmowie: `image(20261108-155952).png` (nazwa robocza konwersacji). **Plik nie został jeszcze dodany do repozytorium** i nie jest podłączony do CK3. Należy go zachować, a przy etapie instalacyjnym przygotować DDS, zarejestrować tło i sprawdzić w grze.
- Obraz A01 jest **wzorcem monumentalnego naturalizmu** dla pozostałych osobistych objawień; nie należy kopiować dosłownie sylwetki Welesa na innych bogów.
- **Perun i Mokosz pozostają do wykonania** pod sceny A02/A03. Do Magnific przekazywać zatwierdzony Weles A01 jako **referencję stylu i skali**, a charakterystyczny dotychczasowy wizerunek konkretnego boga jako osobną referencję postaci, jeśli narzędzie umożliwia jej wskazanie.
- Oprawa: fotorealistyczny, mroczny, naturalistyczny kadr filmowy; boska postać zdecydowanie przewyższa człowieka, ale zachowuje wiarygodną anatomię i powagę. Bez komiksowości i przesadnych efektów CGI.
- Należy zsynchronizować tekst `2020` z osobistym objawieniem Welesa przed podłączeniem obrazu. Aktualny tekst nadal odwołuje się do żercy.
