# Dutch profiles and package pages. Executed inside build.py's namespace after nl.py.
for _m in MASSEUSES:
    NLMAP[f"/dames/{_m[0]}/"] = f"/nl/dames/{_m[0]}/"
for _p in PACKAGES:
    NLMAP[f"/packages/{_p[1]}/"] = f"/nl/pakketten/{_p[1]}/"
ENMAP = {v: k for k, v in NLMAP.items()}
HAIR_NL = {"Blonde": "Blond", "Dark brunette": "Donkerbruin", "Brunette": "Bruin", "Black": "Zwart", "Platinum blonde": "Platinablond", "Dark curls": "Donkere krullen",
           "Light brown": "Lichtbruin", "Blonde curls": "Blonde krullen", "Auburn": "Kastanjerood", "Brunette with highlights": "Bruin met highlights",
           "Dark blonde": "Donkerblond", "Long braids": "Lange vlechten"}
TAGS_NL = {"mysterious": "mysterieus", "passionate": "passievol", "romantic": "romantisch", "playful": "speels", "natural": "natuurlijk"}

LOOK_NL = {
"bianca": ("Bianca is een blondine met een zachte, zonnige uitstraling, gefotografeerd in koningsblauw kant in een klassieke kamer met een witte schouw.", "Haar foto's hebben iets dromerigs en aanhankelijks: een masseuse die de tijd neemt en het oogcontact niet verliest."),
"olga": ("Olga draagt haar blonde haar lang en houdt van een elegante stijl: een transparante zwarte blouse, helder licht en geen detail te veel.", "Ze komt rustig en zelfverzekerd over, wat past bij de woorden natuurlijk en passievol waarmee ze wordt omschreven."),
"vicky": ("Vicky heeft lang, donker haar dat over haar schouders valt en een slank, strak figuur, te zien in ivoorkleurige kanten lingerie.", "Haar foto's zijn mysterieus en een beetje plagend: ze laat veel zien en houdt toch iets achter voor de ontmoeting."),
"adda": ("Adda heeft blond haar tot op haar taille en een gouden teint, en laat zich graag van achteren fotograferen in warm avondlicht.", "Haar stijl is ontspannen en zomers, meer strandvakantie dan studio."),
"alexandra": ("Alexandra is een brunette met zachte golven, gefotografeerd bij het raam in zwarte lingerie en kousen terwijl de zon ondergaat.", "Met haar 41 jaar heeft ze de rustige zekerheid van een vrouw die precies weet wat ze doet, en dat zie je op elke foto."),
"amanda": ("Amanda heeft lange platinablonde krullen en een klassiek pin-upfiguur, in gestreepte lingerie tegen vintage behang.", "Er zit een vleugje oud Hollywood in haar foto's, speels en elegant tegelijk."),
"anda": ("Anda is platinablond met een kort, nonchalant kapsel en draagt wit kant.", "Haar foto's zijn licht, zacht en een beetje engelachtig, met een ondeugende glimlach eronder."),
"cleopatra": ("Cleopatra heeft lang kastanjebruin haar in een staart en volle rondingen, te zien in zwarte lingerie en gestreepte kousen.", "Ze heeft de warme, zelfverzekerde uitstraling van een vrouw van 42 die ervan geniet bewonderd te worden."),
"denisa": ("Denisa combineert donker haar met rode lingerie en netkousen, gezeten op een witte vacht in een loft met houten wanden.", "Haar stijl is gedurfd en een tikje uitdagend, met het zelfvertrouwen dat daarbij hoort."),
"katy": ("Katy heeft donker haar tot op de schouders en een rond figuur, gefotografeerd voor een hoge spiegel in donkerblauwe lingerie.", "Ze spreekt Nederlands en Engels, en haar foto's hebben de ontspannen charme van het meisje van hiernaast."),
"lavinia": ("Lavinia heeft lang, steil donker haar en zachte rondingen, geknield op witte lakens in zwart kant.", "Haar uitstraling is natuurlijk en ongedwongen, precies zoals haar profiel haar omschrijft."),
"livana": ("Livana heeft donker haar en een slank figuur en poseert in zwarte lingerie in een kleurrijke kamer vol bloemen.", "Haar foto's zijn vrolijk en levendig, een beetje exotisch en nooit saai."),
"lora": ("Lora heeft lang, gitzwart haar en lange benen, uitgestrekt in rode lingerie en hoge hakken.", "Ze kijkt recht in de camera: direct, levendig en zeker van zichzelf."),
"noor": ("Noor heeft een bos lange zwarte golven en een strak, atletisch lichaam, gefotografeerd in zwarte lingerie tegen een egale muur.", "Haar foto's zijn puur en krachtig, zonder iets dat afleidt van de lijnen van haar figuur."),
"roxy": ("Roxy heeft lang donker haar en draagt een rode kanten body, staand in een deuropening met haar rug half naar de camera.", "Rood is duidelijk haar kleur, en haar foto's hebben een verleidelijke, licht geheimzinnige sfeer."),
"stephanie": ("Stephanie heeft lang donker haar en een speelse smaak in lingerie: zwart met witte kanten randjes.", "Een vinger op haar lippen en een twinkeling in haar ogen: haar foto's zijn ondeugend en vol humor."),
"brianna": ("Brianna heeft een hoofd vol donkere krullen, sprekende wenkbrauwen en warme bruine ogen, te zien in een natuurlijk portret van dichtbij.", "Het is een van de weinige portretten met een gezicht, open en direct, en dat zegt veel over haar zelfvertrouwen."),
"clarissa": ("Clarissa heeft lang zwart haar en een slank, sportief figuur, geknield op een witte bank in rode lingerie en zwarte hakken.", "Met negen foto's in haar galerij is ze niet verlegen, en haar poses zijn speels en atletisch."),
"miki": ("Miki heeft donker haar en een tenger figuur, liggend gefotografeerd bij een grote spiegel in zwarte lingerie en kousen.", "Haar foto's zijn intiem en een beetje dromerig, als een stil moment waar u toevallig binnenloopt."),
"roanna": ("Roanna heeft golvend blond haar en een slank, strak lichaam, in transparante zwarte lingerie in een klassiek interieur.", "Met 21 jaar is ze een van de jongsten van het team, met een frisse en zelfverzekerde uitstraling."),
"sophie": ("Sophie heeft lichtbruin haar met blonde highlights, gefotografeerd in een los wit overhemd en zachtroze kousen.", "Ze spreekt Engels, Italiaans en Spaans, en haar stijl is vrouwelijk en een beetje romantisch."),
"alee": ("Alee heeft donker, golvend haar en volle rondingen, te zien in zwarte kanten lingerie met jarretels.", "Haar foto's zijn warm en sensueel, met rijke kleuren en zacht licht."),
"alessia": ("Alessia heeft lang donker haar en een slank figuur, geknield op een bed in een zwarte beha in een stijlvolle hotelkamer.", "Haar look is modern en casual, alsof ze net thuis is en er de tijd voor neemt."),
"anely": ("Anely heeft donker haar en zachte rondingen, liggend op een bed in zwarte lingerie en hold-up kousen.", "Ze houdt van een lome, ontspannen pose, en haar foto's nodigen uit om het rustiger aan te doen."),
"angel": ("Angel heeft donker haar en draagt rood kant, uitgestrekt op een wit bed.", "Haar foto's zijn zacht en slaperig in de beste zin: een zondagochtend die de hele dag duurt."),
"annabel": ("Annabel heeft lang zwart haar en een sportief figuur en poseert in een wit topje en een verwassen spijkerbroek.", "Zij is de casual dame van het team: weinig make-up, geen poespas en een natuurlijk zelfvertrouwen."),
"ariel": ("Ariel heeft lange zwarte golven en opvallende make-up, gekleed in lingerie met luipaardprint en zwarte kousen.", "Glamoureus en gedurfd: ze is duidelijk niet bang om op te vallen."),
"celine": ("Celine draagt haar donkere haar opgestoken en heeft lange benen, staand gefotografeerd in een zwarte kanten body en kousen.", "Lang, beheerst en elegant, met de houding van een model."),
"cleo": ("Cleo heeft een strakke zwarte bob en een voorliefde voor speelse outfits met kniekousen.", "Haar foto's zijn ondeugend en vol humor, en ze houdt zichtbaar van een beetje theater."),
"dalya": ("Dalya heeft donker haar, draagt een bril en verkiest op haar foto's een spijkerbroek boven kant.", "De bril geeft haar een slimme, plagende blik die veel gasten onthouden."),
"denise": ("Denise heeft donker haar en zachte rondingen, achteroverleunend in zwart kant tegen een dieprode achtergrond.", "Haar foto's zijn sfeervol en sensueel, met de warme kleuren van een late avond."),
"ines": ("Ines heeft lang zwart haar en draagt zwarte lingerie met een parelchoker, gefotografeerd voor een gordijn met patroon.", "Een klassieke, vrouwelijke look met een vleugje burlesque."),
"ingrid": ("Ingrid heeft donker haar en het figuur van een danseres en poseert in zwarte lingerie en kousen met een dunne sluier boven haar hoofd.", "Er zit beweging in elke foto, luchtig en gracieus."),
"jeniffer": ("Jeniffer heeft lang donker haar en een gebruind, sportief lichaam, zittend in een zwart tweedelig setje.", "Haar stijl is ontspannen en zomers, met een makkelijke glimlach."),
"jenn": ("Jenn heeft donker haar en lange benen, van achteren gefotografeerd in een witte kanten body in een kamer vol kleur.", "Wit staat haar goed, en haar foto's voelen fris en elegant."),
"joy": ("Joy draagt haar donkere haar in een hoge staart en heeft een atletisch figuur, poserend in een rood topje.", "Sportief, energiek en trouw aan haar naam."),
"kim": ("Kim heeft donker haar, volle rondingen en een voorkeur voor rood: op de meeste foto's draagt ze een transparant rood topje.", "Haar look is gedurfd en zelfverzekerd, met een zachte glimlach die het geheel verzacht."),
"kimberly": ("Kimberly heeft lang, steil zwart haar tot op haar taille en draagt zachtroze kant.", "Met haar 35 jaar heeft ze een rustige, gracieuze uitstraling, en haar foto's horen bij de elegantste van de site."),
"lexi": ("Lexi heeft lang blond haar en draagt een zwarte kanten catsuit, van achteren gefotografeerd naast een rode fauteuil.", "Een rock-chic stijl, gedurfd en zelfverzekerd."),
"lisa": ("Lisa heeft een wolk van blonde krullen en een stralende lach, gekleed in een zwarte babydoll met rode details.", "Haar foto's zijn zonnig en open, en door haar krullen herkent u haar meteen."),
"mary": ("Mary heeft kastanjerood haar en een slank figuur, gefotografeerd tegen een rood gordijn in huidkleurige lingerie.", "Een beetje theatraal, met de warme tinten van een cabaret."),
"megan": ("Megan is een blondine die houdt van een chique, casual look: een oranje trui op een blauwfluwelen bank.", "Haar foto's voelen als een middag thuis, stijlvol en op haar gemak."),
"michelle": ("Michelle heeft zwart haar en houdt van een dramatische outfit: een zwart korset, netkousen en een cape.", "Ze spreekt Engels en Nederlands, en haar stijl is zelfverzekerd en theatraal."),
"nicole": ("Nicole heeft lang donker haar en een slank figuur, zittend op een witte bank in een zwarte body en hakken.", "Strak en modern, een look die niet zou misstaan in een designhotel."),
"pandora": ("Pandora heeft bruin haar met blonde highlights en draagt een zwarte halterbody met een diep decolleté.", "Haar blik in de camera is warm en direct, en ze zit zichtbaar lekker in haar vel."),
"raisa": ("Raisa heeft kort donker haar en draagt rood kant, liggend op witte lakens met een glimlach.", "Haar foto's zijn speels en uitnodigend, licht en ongecompliceerd."),
"vanessa": ("Vanessa heeft blond haar en lange benen, liggend op een bed in zwarte lingerie en hoge hakken.", "Elegant met een rebels randje, zoals de paarse hakken al verraden."),
"angella": ("Angella heeft donker krullend haar en draagt zwart kant, achteroverliggend op een bed met rozen.", "Ze spreekt Engels, Frans en Spaans, en haar foto's zijn romantisch en zacht."),
"bella": ("Bella heeft een lange bruine paardenstaart en een slank figuur, te zien in een zwart kanten topje en rokje tegen een witte achtergrond.", "Haar stijl is verzorgd en vrouwelijk, met een voorkeur voor kant."),
"catalina": ("Catalina heeft blond haar en volle rondingen, gekleed in felrode lingerie.", "Ze spreekt Engels, Portugees en Spaans, en haar foto's hebben een levendige, zonnige energie."),
"izabelle": ("Izabelle heeft heel lang donker haar en is als silhouet gefotografeerd tegen het licht van een raam.", "Ze spreekt vijf talen, en haar foto's houden iets mysterieus dat bij haar past."),
"lucy": ("Lucy is liggend gefotografeerd op een hotelbed in lila lingerie, ontspannen en zonder haast.", "Ze spreekt Engels en Spaans, en haar stijl is zacht en gemoedelijk."),
"lunnie": ("Lunnie draagt haar haar in lange vlechten, hoog opgebonden, en heeft een slank figuur; ze poseert in een gebloemd zomerjurkje en hakken.", "Haar look is fris en modieus, meer stadswandeling dan boudoir."),
"nina": ("Nina heeft lange, lichtbruine golven en is in zacht tegenlicht gefotografeerd in een zwarte beha.", "Met haar 42 jaar heeft ze een warme, natuurlijke schoonheid, en ze spreekt zowel Nederlands als Engels."),
"rosalie": ("Rosalie draagt haar blonde haar opgestoken en heeft een atletisch figuur, van achteren te zien in zwarte lingerie en hakken.", "Sportief en elegant, met de houding van iemand die graag in de sportschool komt."),
"adrianna": ("Adrianna heeft blond, opgestoken haar en combineert lingerie met een kort grijs jasje.", "Met haar 35 jaar heeft ze een zelfverzekerde, volwassen stijl met een vleugje rock-'n-roll."),
"alicia": ("Alicia heeft goudblond haar en een speels gevoel voor stijl, gefotografeerd in een witte blouse.", "Haar foto's zijn luchtig en plagend, en ze heeft duidelijk gevoel voor humor."),
"anna": ("Anna heeft lang blond haar en verschijnt met konijnenoren en zwart kant op een roze bank.", "Speels en flirterig: ze neemt zichzelf niet al te serieus."),
"annays": ("Annays draagt haar donkere haar opgestoken en is van achteren gefotografeerd in een zwarte netjurk.", "Haar foto's zijn gedurfd en zelfverzekerd, met oog voor detail."),
"arianna": ("Arianna is liggend gefotografeerd in een zwart korset, in een kamer met warm licht en dieprode tinten.", "Haar stijl is zwoel en rustig, gemaakt voor een lange avond."),
"eleni": ("Eleni heeft een zwarte bob met een rechte pony en draagt zwart kant en kousen.", "Een retrolook met een vleugje jaren twintig, elegant en onderscheidend."),
"ella": ("Ella heeft blond haar en heldere ogen en leunt achterover in een zwarte kanten body.", "Haar glimlach is open en uitnodigend, en haar foto's voelen spontaan."),
"ella-new": ("Ella New heeft lang blond haar en zachte rondingen, geknield in zwart kant bij een groot raam.", "Met haar 38 jaar heeft ze een rijpe, vrouwelijke charme en een rustige manier van poseren."),
"isabella": ("Isabella draagt haar blonde haar opgestoken en heeft een slank figuur, gefotografeerd in een eenvoudige zwarte beha.", "Een fris gezicht en een directe blik, met een natuurlijke, ongecompliceerde stijl."),
"julia": ("Julia heeft lang donker haar, opvallende make-up en een voorkeur voor zwart kant met lange mouwen.", "Haar foto's zijn glamoureus en een beetje gothic, met een sterke uitstraling."),
"lisanne": ("Lisanne heeft donker haar en draagt zwarte lingerie met overknee-laarzen.", "Gedurfd en stijlvol, met het zelfvertrouwen om het te dragen."),
"lolita": ("Ze heeft donker krullend haar en lange benen, van achteren gefotografeerd in zwarte lingerie en kousen tegen een witte muur.", "Haar foto's zijn grafisch en elegant: het draait om lijn en houding."),
"mihaela": ("Mihaela heeft donker haar en volle rondingen en poseert in lichtblauwe lingerie tegen een witte bakstenen muur.", "Het zachte blauw geeft haar foto's een frisse, zomerse sfeer."),
"mina": ("Mina heeft bruin haar en draagt rode lingerie, staand naast een hangmat in een kamer met donkere wanden.", "Ontspannen en een beetje bohemien, op haar plek in een informele omgeving."),
"nikki": ("Nikki heeft lang zwart haar en een lang, slank figuur, gekleed in een rode kanten body.", "Rechtop en met de blik in de lens: haar foto's zijn zelfverzekerd en opvallend."),
"sara": ("Sara heeft zwart haar en kiest voor een avondlook: een kort bronskleurig jurkje en hoge hakken.", "Zij is de meest geklede dame van het team, elegant genoeg voor elke hotelbar."),
"tania": ("Tania heeft blond haar en een gebruind figuur, geknield op een bank in zwarte lingerie.", "Haar foto's zijn warm en zonnig, met een ontspannen glimlach."),
"viky": ("Viky heeft lang zwart haar en is zittend op een stoel gefotografeerd in zwarte lingerie en kousen.", "Een klassieke boudoirstijl, beheerst en verleidelijk."),
}

PKG_MORE_NL = {
    "amsterdam-tour": ("Amsterdam Tour & Massage | Stadstour met Gezelschap", "Amsterdam is op zijn mooist met iemand die de stad kent. Bij dit pakket brengt u het eerste deel van uw tijd buiten door en het tweede deel in uw hotelkamer.",
        [("Ontmoeting in uw hotel", "Uw masseuse ontmoet u in de lobby of op een plek die u in de chat afspreekt."), ("Samen de stad in", "Wandel door het oude centrum en langs de grachten, of maak een rondvaart. U bepaalt de route en het tempo."), ("Terug naar uw kamer", "Daarna gaat u terug naar uw hotel voor de erotische massage van uw keuze, met happy ending.")],
        ["Tickets voor een rondvaart of museum en eventuele drankjes onderweg betaalt u zelf.", "Vier uur is het minimum, zodat de tour en de massage geen van beide gehaast aanvoelen.", "Vertel ons in de chat wat u wilt zien, dan plannen wij de tijd met u."],
        [("Kan ik zelf de route kiezen?", "Ja. Vertel ons wat u wilt zien, bijvoorbeeld de grachten, de Jordaan of de Wallen, en wij plannen het met u."), ("Hoort de massage bij de vier uur?", "Ja. Het pakket duurt in totaal vier uur. U bepaalt hoe u de tijd verdeelt tussen de tour en de massage.")]),
    "dinner-date": ("Dinner Date & Erotische Massage | Avondpakket Amsterdam", "Sommige avonden verdienen meer dan een uur. Een dinner date geeft u de tijd om te praten, te lachen en elkaar te leren kennen voordat de massage begint, en dat maakt alles daarna beter.",
        [("Kies uw restaurant", "Kies een restaurant in Amsterdam of dineer in uw hotel. Uw masseuse ontmoet u daar, gekleed voor de gelegenheid."), ("Geniet samen van het diner", "Neem de tijd. Goed eten en een goed gesprek zijn het beste begin van de avond."), ("Sluit de avond af op uw kamer", "Na het diner gaat u naar uw hotel voor een rustige erotische massage naar keuze.")],
        ["De restaurantrekening betaalt u zelf.", "Drie uur is het minimum. Met vier uur hoeft u aan tafel niet op de klok te letten.", "Geef het restaurant en de tijd vooraf door, zodat uw masseuse zich passend kan kleden."],
        [("Kunnen jullie een restaurant aanbevelen?", "Wij denken graag mee. Vertel ons in de chat waar u verblijft en van welke keuken u houdt."), ("Wat draagt mijn masseuse naar het diner?", "Zij kleedt zich stijlvol en passend bij het restaurant dat u kiest. Heeft u een voorkeur, noem die dan in de chat.")]),
    "amsterdam-by-night": ("Amsterdam by Night | Drankje & Erotische Massage", "Geen trek, maar ook geen haast? Samen iets drinken is de makkelijkste manier om het ijs te breken. Tegen de tijd dat u naar boven gaat, voelt u zich al op uw gemak bij elkaar.",
        [("Ontmoeting bij een drankje", "In de bar van uw hotel of een cocktailbar in de buurt. U kiest de plek."), ("Ontspannen en kennismaken", "Eén of twee drankjes, geen programma, geen druk."), ("Uw massage", "Daarna gaat u naar uw kamer voor een sensuele of body to body massage.")],
        ["De drankjes betaalt u zelf.", "Twee uur is het minimum; voeg een uur toe als u graag de tijd neemt.", "Vaak op de dag zelf mogelijk, afhankelijk van de beschikbaarheid."],
        [("Kan ik dit voor vanavond boeken?", "Vaak wel. Stuur ons in de chat uw hotel en het tijdstip dat u in gedachten heeft, dan hoort u wie beschikbaar is."), ("Moeten we de deur uit voor het drankje?", "Nee. Veel gasten kiezen de bar van hun eigen hotel, of gewoon een drankje op de kamer.")]),
    "schiphol-stopover": ("Schiphol Stopover Pakket | Massage tussen Twee Vluchten", "Een lange overstap of een nacht in een luchthavenhotel hoeft geen verloren tijd te zijn. Uw masseuse komt naar uw hotel op of bij Schiphol, zodat u de stad niet in hoeft.",
        [("Stuur uw vluchttijden", "Vertel ons in de chat wanneer u landt en wanneer u weer weg moet."), ("Uw masseuse komt naar uw hotel", "Zij bezoekt hotels op Schiphol en in Hoofddorp en Aalsmeer."), ("Ontspannen voor uw vlucht", "Een uur massage en u stapt als een ander mens in uw volgende vliegtuig.")],
        ["Mogelijk in hotels op Schiphol, in Hoofddorp en in Aalsmeer.", "Boek zo vroeg mogelijk als u weinig tijd heeft.", "Extra tijd kost € 160 per uur."],
        [("Is één uur genoeg?", "Ja. Eén uur is genoeg voor een complete sensuele of full body massage. Heeft u meer tijd, dan kunt u een uur toevoegen."), ("Kan ik boeken voordat ik land?", "Ja, en dat raden wij aan. Stuur ons uw hotel en aankomsttijd, dan wordt uw masseuse rond uw vlucht ingepland.")]),
    "jetlag-relief": ("Jetlag Relief Massage | Massage na uw Vlucht", "Een lange vlucht laat sporen na: een stijve nek, zware benen en een hoofd dat niet uit wil. Dit pakket pakt eerst het lichaam aan en direct daarna het hoofd.",
        [("Aankomen en douchen", "Check in, neem een warme douche en laat ons weten dat u er klaar voor bent."), ("Eerste uur: full body massage", "Stevige, rustige strijkingen voor uw rug, nek, schouders en benen."), ("Tweede uur: sensuele afsluiting", "Het tempo zakt, de aanraking wordt lichter en de spanning verdwijnt helemaal.")],
        ["Twee uur in totaal.", "Vertel uw masseuse waar u de vlucht het meest voelt.", "De meeste gasten boeken dit op de dag van aankomst."],
        [("Helpt een massage tegen jetlag?", "Een massage ontspant spieren die urenlang stil hebben gezeten en helpt u tot rust te komen, waardoor u makkelijker op het juiste moment in slaap valt."), ("Kan ik dit laat op de avond boeken?", "Geef uw aankomsttijd door in de chat, dan kijken wij welke masseuse beschikbaar is.")]),
    "after-work": ("After Work Massage Amsterdam | 's Avonds in uw Hotel", "In Amsterdam voor uw werk? Na een dag vol vergaderingen, presentaties of een beurs is geen plan het beste plan. Laat uw masseuse naar u toe komen.",
        [("Eén bericht in de chat", "Uw hotel, de tijd en de massage waar u zin in heeft."), ("Wij bevestigen", "U hoort wie beschikbaar is en wat het tarief is."), ("Uw masseuse arriveert", "In uw hotel of thuis. U hoeft alleen de deur open te doen.")],
        ["Eén uur, met de mogelijkheid om te verlengen voor € 160 per uur.", "In uw hotel of thuis.", "Discreet van het eerste bericht tot het afscheid."],
        [("Hoe laat kan ik nog boeken?", "Geef het tijdstip door dat u in gedachten heeft. De beschikbaarheid laat op de avond verschilt per dag; u krijgt direct antwoord in de chat."), ("Kan ik ter plekke een uur bijboeken?", "Als uw masseuse tijd heeft, kunt u verlengen. Het extra-uurtarief is € 160.")]),
    "duo-deluxe": ("Duo Deluxe Pakket | Twee Masseuses, Twee Uur", "Eén masseuse is een verwennerij. Twee is een ervaring waar u nog lang over napraat, al is het maar met uzelf. Duo Deluxe geeft u twee masseuses voor twee volle uren.",
        [("Kies twee masseuses", "Kies uw favorieten uit de profielen, of laat ons een duo voorstellen dat goed op elkaar is ingespeeld."), ("Vier handen in één ritme", "Ze beginnen met een 4 hands massage waarin ze elkaar spiegelen."), ("Body to body met twee", "In het tweede deel wisselen ze elkaar af en werken ze samen, huid op huid.")],
        ["Twee masseuses voor twee uur.", "Het tarief hangt af van de twee masseuses die u kiest; vraag het in de chat.", "Boek vooruit, want beide masseuses moeten tegelijk vrij zijn."],
        [("Kan ik beide masseuses zelf kiezen?", "Ja. Noem beide namen in de chat. Is een van hen niet beschikbaar, dan stellen wij een alternatief voor."), ("Is twee uur nodig?", "Het is wat wij aanraden. Met twee masseuses valt er veel te beleven, en één uur is zo voorbij.")]),
    "tantra-ritual": ("Tantra Ritueel Pakket | Sessie van Twee of Drie Uur", "Een tantra massage heeft tijd nodig. In dit ritueel wordt niets gehaast: elke fase van de massage krijgt de aandacht die ze verdient.",
        [("Aankomen in het moment", "Het ritueel begint met ademhaling en rustige, aardende aanraking."), ("Langzame opbouw", "Het hele lichaam wordt gemasseerd, met lange strijkingen die lichter en sensueler worden."), ("De afsluiting", "De spanning wordt opgebouwd, losgelaten en opnieuw opgebouwd, tot de massage haar natuurlijke einde bereikt.")],
        ["Vanaf twee uur; drie uur is ideaal.", "Ervaring met tantra is niet nodig.", "Een rustige kamer en een telefoon op stil maken echt verschil."],
        [("Wat is het verschil met een gewone tantra massage?", "De lengte. Met twee of drie uur is de opbouw veel trager en de ervaring dieper."), ("Is een tantra ritueel geschikt voor beginners?", "Ja. Uw masseuse begeleidt u en u hoeft alleen uw ademhaling te volgen.")]),
    "bath-and-massage": ("Bad & Massage Pakket | Begin in Bad of onder de Douche", "Warm water is het beste begin van elke massage. Het ontspant uw spieren, maakt uw hoofd leeg en breekt het ijs op de meest natuurlijke manier.",
        [("Begin in het water", "Samen in bad, of onder een warme douche."), ("Afdrogen en gaan liggen", "Handdoeken op het bed, warme olie binnen handbereik."), ("Body to body massage", "Huid op huid, met langzame glijdende bewegingen van top tot teen.")],
        ["Twee uur in totaal.", "U heeft een hotelkamer of huis met een bad of een ruime douche nodig.", "Leg een paar extra grote handdoeken klaar."],
        [("Mijn kamer heeft alleen een douche. Is dat een probleem?", "Helemaal niet. Een ruime douche werkt net zo goed als een bad."), ("Moet ik iets meenemen?", "Alleen handdoeken. Vraag zo nodig een paar extra bij uw hotel.")]),
    "champagne-evening": ("Champagne-avond Pakket | Drie Uur met Champagne", "Voor een verjaardag, een gesloten deal of zomaar. Drie uur met champagne, goed gezelschap en een lange sensuele massage.",
        [("Open de fles", "Bestel champagne via uw hotel of neem uw eigen fles mee, en proost op de avond."), ("Neem de tijd", "Een gesprek, muziek, aardbeien. Er is geen schema."), ("Een lange sensuele massage", "De massage is over de avond verdeeld, met alle tijd die u nodig heeft.")],
        ["Drie uur in totaal.", "Champagne en hapjes bestelt en betaalt u zelf.", "Een hotelkamer met een zithoek maakt de avond compleet."],
        [("Is de champagne inbegrepen?", "Nee. U bestelt die via uw hotel of neemt die zelf mee, zodat u precies kunt kiezen wat u lekker vindt."), ("Kan ik de avond verlengen?", "Ja, als uw masseuse tijd heeft. Elk extra uur is € 160.")]),
    "couples-massage": ("Massage voor Stellen Amsterdam | Erotische Massage voor Twee", "Samen een erotische massage delen is een bijzondere ervaring voor een stel. U ontspant allebei, u geniet allebei en dat gevoel neemt u mee naar huis.",
        [("Vertel ons uw wensen", "Eén masseuse of twee, en waar u zich allebei prettig bij voelt."), ("Wij adviseren en bevestigen", "U hoort welke masseuses openstaan voor stellen en wat het tarief is."), ("Uw massage", "In uw hotel of thuis, naast elkaar of na elkaar.")],
        ["Voor stellen.", "Met één of twee masseuses.", "Alles wordt vooraf besproken, zodat er geen verrassingen zijn."],
        [("Bieden jullie massages voor stellen aan?", "Ja. Vertel ons in de chat dat u als stel boekt, dan selecteren wij masseuses die daar plezier in hebben."), ("Kunnen we tegelijk gemasseerd worden?", "Met twee masseuses wel. Met één masseuse bent u om de beurt, of verdeelt zij haar aandacht over u beiden.")]),
    "massage-lesson": ("Massageles voor Stellen Amsterdam | Samen Leren Masseren", "Een massage is na een avond voorbij. Weten hoe u er een geeft, gaat een leven lang mee. In deze les leert u van een ervaren masseuse hoe u elkaar masseert.",
        [("De basis", "Hoe u olie, druk en ritme gebruikt, en hoe u de ander op zijn of haar gemak stelt."), ("Oefenen op elkaar", "Eerst de een, dan de ander, terwijl uw masseuse uw handen begeleidt."), ("Sensueel maken", "De trage strijkingen en de opbouw die van een ontspannende massage een sensuele maken.")],
        ["Twee uur voor twee personen.", "In uw hotel of thuis.", "Een mooi cadeau voor een jubileum of een weekend Amsterdam."],
        [("Hebben we ervaring nodig?", "Nee. De les begint bij de basis en past zich aan uw tempo aan."), ("Kan dit ook voor één persoon?", "Ja. Laat het ons weten in de chat, dan passen wij de les aan.")]),
    "birthday-surprise": ("Verjaardagsverrassing | Erotische Massage Cadeau Geven", "Zoekt u een cadeau dat hij niet ziet aankomen? Elk van onze pakketten is als verrassing te boeken, voor een verjaardag, een vrijgezellenweekend of een feestelijk moment.",
        [("Kies een pakket", "Van één uur massage tot een dinner date of een duo."), ("Geef ons de gegevens", "De datum, het hotel of adres en de naam van de gelukkige."), ("Wij regelen de rest", "Discreet en in overleg met u.")],
        ["Elk pakket kan cadeau worden gegeven.", "Boek vooruit, zodat wij de verrassing kunnen plannen.", "Het tarief hangt af van het pakket dat u kiest."],
        [("Kan ik voor iemand anders betalen?", "Ja. Vertel ons in de chat dat het een cadeau is, dan leggen wij uit hoe het werkt."), ("Moet de jarige het weten?", "Dat bepaalt u. Bij een huisadres controleren wij altijd of het bezoek welkom is.")]),
}


def card(m, eager=False):
    if L != "nl":
        return _card_en(m, eager)
    slug, name, age, langs, city = m
    sub_l = " · ".join(x for x in (str(age), nl_langs(langs) or city) if x)
    im = img(m, eager=eager).replace("erotic masseuse in Amsterdam", "erotische masseuse in Amsterdam")
    return f'<li class="card"><a href="/nl/dames/{slug}/">{im}<span class="card-b"><strong>{E(name)}</strong><span>{E(sub_l)}</span></span></a></li>'


def pkg_card_nl(p, h="h3"):
    pid, photo = p[1], p[5]
    name, dur, price, d = PKG_NL[pid]
    return (f'<li class="pkg" id="{pid}">{pic(photo, name, 600, 400)}<div class="pkg-b"><p class="pkg-m"><span>{E(dur)}</span><strong>{E(price)}</strong></p>'
            f'<{h}>{E(name)}</{h}><p>{E(d)}</p><p><a class="btn btn-sm" href="/nl/contact/" data-chat>Boek dit pakket</a> '
            f'<a class="link" href="/nl/pakketten/{pid}/">Meer over {E(name)}</a></p></div></li>')


def build_nl2():
    global L
    L = "nl"
    urls = []
    mchips = "".join(f'<li><a href="{NLMAP[f"/{s}/"]}">{E(n)}</a></li>' for s, n, _ in MASSAGES_NL) + '<li><a href="/nl/happy-ending-massage/">Happy ending massage</a></li>'
    top = [("/nl/pakketten/dinner-date/", "Dinner Date & Erotische Massage"), ("/nl/pakketten/amsterdam-tour/", "Amsterdam Tour & Massage"), ("/nl/pakketten/duo-deluxe/", "Duo Deluxe"),
           ("/nl/pakketten/schiphol-stopover/", "Schiphol Stopover"), ("/nl/pakketten/", "Alle pakketten")]
    topchips = "".join(f'<li><a href="{u}">{E(t)}</a></li>' for u, t in top)
    k = len(MASSEUSES)
    for idx, m in enumerate(MASSEUSES):
        slug, name, age, langs, city = m
        nlang = nl_langs(langs)
        ll = nlang.rsplit(", ", 1) if nlang else []
        p1 = [f"{name} is {age} jaar en is een van de erotische masseuses van Erotic Massage Amsterdam.",
              f"Maak kennis met {name}, {age} jaar, een van de masseuses die u via Erotic Massage Amsterdam kunt boeken.",
              f"{name} ({age}) hoort bij het team van Erotic Massage Amsterdam.",
              f"{name}, {age} jaar, is een van de masseuses van Erotic Massage Amsterdam."][idx % 4]
        if ll:
            p1 += f" Ze spreekt {' en '.join(ll)}."
        if city:
            p1 += f" Haar standplaats is {city}."
        tags = [TAGS_NL.get(t, t) for t in TAGS.get(slug, [])]
        if tags:
            p1 += f" Haar stijl is {' en '.join(tags)}."
        visit = [f"{name} bezoekt u in uw hotel of thuis. U kunt haar boeken voor de massages op onze massagepagina, van een sensuele massage tot een body to body massage.",
                 f"Zoals al onze masseuses komt {name} naar u toe: naar uw hotelkamer of uw huisadres. Kies de massage die u aanspreekt op onze massagepagina.",
                 f"Een massage met {name} vindt plaats waar u verblijft, in uw hotel of thuis. Op onze massagepagina ziet u uit welke massages u kunt kiezen."][idx % 3]
        book = f"Wilt u {name} boeken? Noem haar naam in de chat, samen met uw locatie en het gewenste tijdstip. Is zij niet beschikbaar, dan stellen wij een alternatief voor en beslist u."
        look = LOOK_NL[slug]
        facts = {"Leeftijd": str(age)}
        if nlang:
            facts["Talen"] = nlang
        if city:
            facts["Standplaats"] = city
        facts["Haar"] = HAIR_NL.get(LOOK[slug][0], LOOK[slug][0])
        for kx, vx in EXTRA.get(slug, {}).items():
            if kx == "Height":
                facts["Lengte"] = vx
            elif kx == "Eyes":
                facts["Ogen"] = "Bruin" if vx == "Brown" else vx
        dl = "".join(f"<div><dt>{E(a)}</dt><dd>{E(b)}</dd></div>" for a, b in facts.items())
        n = COUNTS.get(slug, 0)
        base = f"/images/masseuses/{slug}-erotic-massage-amsterdam"
        gal = ""
        if n > 1:
            items = "".join(f'<li><a href="{base}-{i}.jpg"><img src="{base}-{i}-400.jpg" alt="{E(name)}, foto {i}" loading="lazy" decoding="async"></a></li>' for i in range(1, n + 1))
            gal = f'<section class="sec"><div class="wrap"><h2>Foto\'s van {E(name)}</h2><ul class="gal">{items}</ul></div></section>'
        rest = "".join(card(MASSEUSES[(idx + j) % k]) for j in range(1, 9))
        im = img(m, eager=True, sizes="(max-width:48rem) 90vw, 420px").replace("erotic masseuse in Amsterdam", "erotische masseuse in Amsterdam")
        inner = (f'<section class="sec"><div class="wrap prof"><div class="prof-img">{viewer(m)}</div>'
                 f'<div class="prose"><h2>Over {E(name)}</h2>{"".join(f"<p>{E(x)}</p>" for x in (p1, look[0], look[1], visit, book))}<dl class="facts">{dl}</dl>'
                 f'<p><a class="btn" href="/nl/contact/" data-chat>Boek {E(name)}</a> <a class="link" href="/nl/prijzen/">Bekijk prijzen</a></p>'
                 f'<h2>Massages met {E(name)}</h2><ul class="chips">{mchips}</ul><h2>Pakketten met {E(name)}</h2><ul class="chips">{topchips}</ul></div></div></section>'
                 f'<section class="sec sec-alt"><div class="wrap"><h2>Meer masseuses</h2><ul class="cards">{rest}</ul>'
                 f'<p class="center"><a class="link" href="/nl/masseuses/">Bekijk alle masseuses</a></p></div></section>')
        bits = [f"{name} ({age}) is masseuse bij Erotic Massage Amsterdam."]
        if nlang and len(nlang) < 30:
            bits.append(f"Ze spreekt {nlang}.")
        bits.append(f"Hotel- en thuisbezoek. Boek {name} via de chat.")
        lead = " · ".join(x for x in (f"{age} jaar", nlang, city) if x) + " · Hotel- en thuisbezoek"
        urls.append(sub(f"/nl/dames/{slug}/", f"{name} ({age}) | Masseuse bij Erotic Massage Amsterdam", " ".join(bits), name, lead, inner,
                        [("Onze masseuses", "/nl/masseuses/")], og_image=f"{SITE}{base}-card.jpg"))

    # package pages
    for p in PACKAGES:
        g, pid, _, _, _, photo, _, _ = p
        name, dur, price, d = PKG_NL[pid]
        p_title, intro, flow, know, pq = PKG_MORE_NL[pid]
        pq = pq + [("Wat kost dit pakket?", (f"{name} kost {price.lower()} ({dur.lower()}) in Amsterdam, Schiphol, Haarlem en Hoofddorp. " if "€" in price else f"Het tarief voor {name} hangt af van uw keuzes. ") + "Elk extra uur is € 160 en wij bevestigen uw tarief in de chat voordat u boekt."),
                   ("Hoe boek ik?", "Open de chat, vertel ons welk pakket u wilt, uw hotel of adres, de datum en tijd en de masseuse van uw keuze. Wij bevestigen alles voordat het definitief is.")]
        fh, fs = faq_block(pq, f"Vragen over {name}")
        steps = "".join(f"<li><h3>{E(t)}</h3><p>{E(x)}</p></li>" for t, x in flow)
        related = [x for x in PACKAGES if x[0] == g and x[1] != pid] + [x for x in PACKAGES if x[0] != g][:2]
        rel = "".join(f'<li><a href="/nl/pakketten/{x[1]}/">{E(PKG_NL[x[1]][0])}</a></li>' for x in related)
        inner = (f'<section class="sec"><div class="wrap split"><div class="split-img">{pic(photo, name, 600, 400, eager=True)}</div>'
                 f'<div class="prose"><p class="pkg-m"><span>{E(dur)}</span><strong>{E(price)}</strong></p><h2>{E(name)}</h2><p>{E(d)}</p><p>{E(intro)}</p>'
                 f'<p><a class="btn" href="/nl/contact/" data-chat>Boek dit pakket</a> <a class="link" href="/nl/pakketten/">Alle pakketten</a></p></div></div></section>'
                 f'<section class="sec sec-alt sec-c"><div class="wrap"><h2>Zo werkt het</h2><ol class="steps">{steps}</ol></div></section>'
                 f'<section class="sec"><div class="wrap narrow prose"><h2>Goed om te weten</h2><ul class="ticks">{"".join(f"<li>{E(x)}</li>" for x in know)}</ul>'
                 f'<h2>Kies uw massage</h2><p>Elk pakket bevat een erotische massage naar keuze, met een happy ending. Lees meer over elke massage:</p><ul class="chips">{mchips}</ul></div></section>'
                 f'{fh}{cta(f"Boek {name} via de chat. Wij bevestigen masseuse, tijd en tarief voordat u boekt.")}'
                 f'<section class="sec"><div class="wrap"><h2>Kies uw masseuse</h2><ul class="cards">{"".join(card(m) for m in MASSEUSES[:10])}</ul><p class="center"><a class="link" href="/nl/masseuses/">Bekijk alle masseuses</a></p>'
                 f'<h2 class="mt">Meer pakketten</h2><ul class="chips">{rel}<li><a href="/nl/pakketten/">Alle pakketten</a></li></ul></div></section>')
        p_desc = (d[:150].rsplit(" ", 1)[0] + "…") if len(d) > 155 else d
        svc = {"@context": "https://schema.org", "@type": "Service", "name": name, "serviceType": "Erotische massage pakket", "description": d,
               "provider": {"@id": SITE + "/#org"}, "areaServed": {"@type": "City", "name": "Amsterdam"}, "url": f"{SITE}/nl/pakketten/{pid}/"}
        urls.append(sub(f"/nl/pakketten/{pid}/", p_title, p_desc, name, f"{dur} · {price}", inner, [("Pakketten", "/nl/pakketten/")], [svc, fs]))
    L = "en"
    return urls


def viewer(m):
    """Large main photo with a strip of thumbnails; swipe, arrows or tap a thumbnail."""
    slug, name = m[0], m[1]
    nl = L == "nl"
    n = max(COUNTS.get(slug, 0), 1)
    base = f"/images/masseuses/{slug}-erotic-massage-amsterdam"
    word = "erotische masseuse in Amsterdam" if nl else "erotic masseuse in Amsterdam"
    slides = "".join(
        f'<img src="{base}-{i}.jpg" alt="{E(name)}, {word}{"" if i == 1 else (" – foto " if nl else " – photo ") + str(i)}" '
        f'{"fetchpriority=" + chr(34) + "high" + chr(34) if i == 1 else "loading=" + chr(34) + "lazy" + chr(34) + " decoding=" + chr(34) + "async" + chr(34)}>'
        for i in range(1, n + 1))
    if n == 1:
        return f'<div class="pv"><div class="pv-main">{slides}</div></div>'
    thumbs = "".join(
        f'<li><button type="button" data-pv="{i - 1}"{" class=" + chr(34) + "on" + chr(34) if i == 1 else ""} aria-label="{"Foto" if nl else "Photo"} {i}">'
        f'<img src="{base}-{i}-400.jpg" alt="" loading="lazy" decoding="async"></button></li>' for i in range(1, n + 1))
    return (f'<div class="pv" data-pv-root><div class="pv-main" tabindex="0" aria-label="{"Foto" + chr(39) + "s van" if nl else "Photos of"} {E(name)}">{slides}</div>'
            f'<button type="button" class="pv-nav pv-prev" data-pv-step="-1" aria-label="{"Vorige foto" if nl else "Previous photo"}">‹</button>'
            f'<button type="button" class="pv-nav pv-next" data-pv-step="1" aria-label="{"Volgende foto" if nl else "Next photo"}">›</button>'
            f'<ul class="pv-thumbs">{thumbs}</ul></div>')
