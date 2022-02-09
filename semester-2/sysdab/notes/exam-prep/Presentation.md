# Presentation
## Individual
### Ideas / notes
- Talk about atomic design
	- It was really nice to work with
	- Shortcomings in Vue
	- Problems with code duplication
	- Some members didn't do it at all
- Talk about shortcomings of the user test
	- Corona
	- Who did it.
- No design guide, apart from the Figma, which resulted in weird results in some places.

### Manus
Jeg vil gerne perspektivere lidt over hvordan projektet, og snakke specifikt om 2 områder. Den ene er vores projekt struktur og udvikling deraf, den anden er om en mangel på design guide.

#### Projekt struktur
- Vi satte os for at bruge Atomic Design til at udvikle vores applikation. 
- Det var lige ambitiøst nok da der var flere gruppe medlemmer der ikke var kendte med hvordan Vue.js fungerede, hvilket lagde et komplikations lag mere oven på. 
- Så der er flere steder hvor Atomic Design falder helt fra hinanden. 
- Derudover så lagde vi mærke til at der er mange steder hvor man virkelig skal ligge meget arbejde i at bruge den strategi, ihvertfald i Vue.js, som faktisk resulterede i en del kode duplikering, eller kæmpestore components, fordi et molecule, eller endnu være, organisms har så mange forskellige indstillinger at de tager kæmpe store mængder af data ind, som gør dem irreterende at arbejde med. 
- Der var også det problem at vi arbejde meget asynkront, så hvert gruppe medlem fik en eller flere sider de arbejdede på, hvilket nogen gange endte i at en komponent blev duplikeret eller lavet af en og brugt af en anden, så det var et rod, der kunne være fikset med bedre kommunikation.

- Der er også et problem med Vue.js, hvor man virkelig skal beslutte hvor man vil placere sin CSS. 
- Vi valgte at placere det i komponentent, for at lade den selv håndtere sin CSS, i en form for Seperation of Concerns. 
- Det havde den effekt at vi havde pænt meget kode duplikering i vores CSS. 
- Så der skal man enten flytte det ud så snart det duplikeres, hvilket ikke altid er lige nemt at lægge mærke til, eller helt håndtere det for sig selv, hvilket tilføjer sine egen komplikationer.

Overall var der en mangel på kommunikation, erfaring og overblik som gjorde at vores udviklede produkt ikke blev af den kvalitet vi ville have den.


#### Design guide
Vi aftalte aldrig rigtig en decideret design guide, altså et regelsæt for vores design.
Det betød at, og det kan i hind-sight ses i vores wireframe, at vi havde flere steder hvor designet ikke hører helt sammen. Vores farver er nogenlunde fulgte, men nogen steder bruger vi kort, nogen steder gør vi ikke, samme gælder for brug af skygger, mellemrum, flad eller ikke flad, font størrelse, farve, og generel typografi.

Det gør at ikke hele appen virker som om den hører sammen. Det faldt helt fra hinanden ved implementationen, pågrund af både det med components CSS, og mangel på CSS erfaring, som gør at visse sider ser helt anderledes ud. 

#### Til næste gang
- Bedre design guide
- Kommuniker aktivt om components, og beslut de hoved components der skal bruges og lav dem med det samme. Aftal en måde at lave dem på.

### Stikord
#### Projekt struktur
- Atomic design
- Mangel på erfaring, kompliceret
- Kode duplikering, da det er en tidskrævende strategi
- Asynkront arbejde
- CSS placering, kode duplikering
	- Komponent
	- Global

#### Design guide
- Vi havde ikke et regelsæt
- Kan ses i vores wireframe
- Typografi, og kort 
- Appen virker ikke som om den hører sammen

