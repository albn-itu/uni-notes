# First presentation

## Relations issue

PT så har vores objekter af typen relation det problem af de

1. I nogen tilfælde bliver tegnet uden deres indre tegnet rigtigt, hvilket resulterer i at nogle af dem såsom Tietgen kollegiet ikke har huller i.
2. Samtidig så er der et problem med at store relations bestående af flere ydre ways ikke tegnes i den rigtige rækkefølge hvilket resulterer i nogle artifakter såsom inder og sydhavnen hvor den ene har en linje der går på tværs og en anden der mangler en ø.

Vi vil fikse dem med respektivt at bruge fillRule, og ved på en eller anden måde at beregne den rigtige rækkefølge, denne er stadig work in progress.



## RTree

Vi har implementeret et Rtræ for kun at tegne de elementer der kan ses når man har zoomet og pannet mappet, det er for at gøre applikation langt hurtigere, da tegning af elementer er en relativt langsom process. Vi har valgt at bruge et R-træ i modsætning til et KD-træ,

1. Fordi KD-træet var langt langsommere i queryes, dog ikke i building i vores test
2. Fordi R-træet supporterer multi dimensionelle elementer, hvor KD-træet er tiltænkt punkter.

Vores R-træ specifikt er et R*-træ som inkluderer nogle flere kriterier og en ny måde at søge på, hvilket betyder at træet ofrer noget bygnings tid, men vinder i query tid, hvilket er rigtigt godt for det her formål. Derudover så bruger vi en metode kaldet STR (Sort-Tile-Recursive) bulk loading som bygger træet bottom first og dermed vinder en hel masse i bygnings tid, hvilket faktisk betyder at den også tager den rekord fra KD-træet



- Implementeret for at gøre applikation hurtigere ved transform (zoom, pan)
- Tegning er langsom
- Vi valgte r-træ fordi
  - Fordi KD-træet var langt langsommere i queryes, dog ikke i building i vores test
  - Fordi R-træet supporterer multi dimensionelle elementer, hvor KD-træet er tiltænkt punkter.
- R*-træ
  -  ofrer noget bygnings tid, men vinder i query tid
  - STR (Sort-Tile-Recursive) bulk loading som bygger træet bottom first
    - tager den rekord fra KD-træet.
- Vi har kunnet tegne hele Danmark