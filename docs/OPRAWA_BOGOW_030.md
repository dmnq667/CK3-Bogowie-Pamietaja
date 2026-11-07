# Gniew i Łaska Bogów — oprawa boskich interwencji 0.3.0

## Reguła nadrzędna

**Nie zastępować żadnej z zatwierdzonych ilustracji dwunastu świąt** ani trzech przyjętych wizerunków Peruna. W repozytorium istnieją 32 oryginalne obrazy źródłowe użytkownika i ich konwersje do DDS. Nowe ilustracje powinny uzupełniać opowieść, nie redefiniować grafiki świąt.

## Stan produkcyjny

- Interwencja Welesa `bp_weles.2020`: na razie używa zatwierdzonego `bp_scene_weles_03`.
- Interwencja Peruna `bp_perun.9110`: na razie używa zatwierdzonego `bp_scene_perun_03`.
- Interwencja Mokoszy `bp_spring.3010`: na razie używa zatwierdzonego `bp_scene_spring_02`.
- **Nie stworzono nowych obrazów w tej partii**. Brak potrzeby podmieniania działających assetów tylko z powodu dodania fabuły.

## Dodatkowe kadry, jeśli okażą się potrzebne podczas testów

1. **Weles — wyrok za złamaną przysięgę**. Nocny święty gaj albo dworska komnata. Sam bóg jest obecny i groźny; widoczny symbol niespłaconego długu. Kadr ma opowiadać o konsekwencji dawnego czynu, a nie o ogólnym mroku.
2. **Perun — próba przed wojną**. Potężna burza, wojowie, broń złożona do przysięgi. Gniew boga odnosi się do ochrony wojów i złamanego obowiązku.
3. **Mokosz — osąd ziemi i plonów**. Przerażający kontrast między opuszczonym polem a możliwością nowego siewu. Bogini ma przypominać o odpowiedzialności za głód poddanych.

## Wymagania techniczne i spójność

- Przygotowywać ujęcia poziome, odpowiednie do okien wydarzeń CK3; bazowy rozmiar wykorzystywany w istniejących materiałach to **1592 × 848 px**.
- Zachować filmową, mroczną, słowiańską oprawę zgodną z oryginalnymi grafikami użytkownika — **ostateczna paleta, szczegóły twarzy bogów, sposób malowania i ich wygląd wymagają sprawdzenia oryginalnych obrazów**.
- Finalny format w grze: DDS DXT1 (BC1) bez mipmap, zgodnie z aktualnym pipeline'em dokumentacji artystycznej.
- Nie wpisywać promptu jako zatwierdzonego, dopóki nie zostanie odnaleziony jego dokładny zapis lub przeanalizowany materiał referencyjny. Użytkownik potwierdził, że taki prompt był wcześniej używany, ale nie ma jego dosłownej treści w tym dokumencie.
- Każdą dodatkową grafikę najpierw sprawdzić wizualnie, a dopiero potem podpiąć do nowego `bp_scene_...` i wydarzenia; używać istniejących grafik do czasu zatwierdzenia.

**Decyzja:** mechanikę i fabułę wdrażać teraz; nowe ilustracje tworzyć jako spójne rozszerzenie po porównaniu oryginalnych prac.
