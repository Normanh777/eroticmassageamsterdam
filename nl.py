# Dutch version (/nl/) + language-aware layout. Executed inside build.py's namespace.
L = "en"
NLMAP = {"/": "/nl/", "/our-masseuses/": "/nl/masseuses/", "/services/": "/nl/massages/", "/prices/": "/nl/prijzen/", "/packages/": "/nl/pakketten/",
         "/other-cities/": "/nl/locaties/", "/bookings/": "/nl/boeken/", "/contact/": "/nl/contact/", "/happy-ending-massage/": "/nl/happy-ending-massage/",
         "/sensual-massage/": "/nl/sensuele-massage/", "/tantra-massage/": "/nl/tantra-massage/", "/body-2-body-massage/": "/nl/body-to-body-massage/",
         "/4-hands-massage/": "/nl/4-hands-massage/", "/thai-massage/": "/nl/thaise-massage/", "/full-body-massage/": "/nl/full-body-massage/"}
for _s, _n in CITIES:
    NLMAP[f"/{_s}/"] = "/nl/erotische-massage-" + _s.replace("erotic-massage-", "") + "/"
ENMAP = {v: k for k, v in NLMAP.items()}
LANG_NL = {"English": "Engels", "Dutch": "Nederlands", "Spanish": "Spaans", "Italian": "Italiaans", "French": "Frans", "Portuguese": "Portugees"}
MASSAGES_NL = [
    ("sensual-massage", "Sensuele massage", "Langzame, vloeiende strijkingen met warme olie. Rustig, aandachtig en diep ontspannend vanaf de eerste aanraking."),
    ("tantra-massage", "Tantra massage", "Een aandachtig ritueel voor het hele lichaam, met ademhaling, rust en een langzaam opbouwende spanning."),
    ("body-2-body-massage", "Body to body massage", "Uw masseuse gebruikt haar hele lichaam om het uwe te masseren, huid op huid met warme olie."),
    ("4-hands-massage", "4 hands massage", "Twee masseuses in hetzelfde ritme. Dubbele aandacht en een gevoel dat moeilijk te beschrijven is."),
    ("thai-massage", "Thaise massage", "Traditionele rek- en druktechnieken die spanning losmaken, afgesloten met een sensuele aanraking."),
    ("full-body-massage", "Full body massage", "Een complete massage van schouders tot voeten, die de stress van reizen en lange dagen wegneemt."),
]


def P(path):
    return NLMAP.get(path, path) if L == "nl" else path


def nl_langs(s):
    return ", ".join(LANG_NL.get(x, x) for x in s.split(", ")) if s else s


def header():
    nl = L == "nl"
    ms = MASSAGES_NL if nl else MASSAGES
    massages = "".join(f'<li><a href="{P(f"/{s}/")}">{E(n)}</a></li>' for s, n, _ in ms)
    lab = ["Masseuses", "Massages", "Prijzen", "Pakketten", "Locaties", "Boeken"] if nl else ["Masseuses", "Massages", "Prices", "Packages", "Locations", "Bookings"]
    other = (ENMAP if nl else NLMAP).get(CUR_PATH, "/" if nl else "/nl/")
    sw = f'<a class="lang" href="{other}" hreflang="{"en" if nl else "nl"}" lang="{"en" if nl else "nl"}">{"English" if nl else "Nederlands"}</a>'
    return f"""<a class="skip" href="#main">{"Naar de inhoud" if nl else "Skip to content"}</a>
<header class="hdr">
<div class="wrap hdr-in">
<a class="logo" href="{P("/")}" aria-label="{BRAND} – home">{LOGO_MARK}<span class="logo-t"><span>Erotic Massage</span><small>Amsterdam</small></span></a>
<input type="checkbox" id="nav-t" class="nav-t" aria-hidden="true" tabindex="-1">
<label for="nav-t" class="burger" aria-label="Menu"><span></span></label>
<nav class="nav" aria-label="{"Hoofdmenu" if nl else "Main"}">
<ul>
<li><a href="{P("/our-masseuses/")}">{lab[0]}</a></li>
<li class="has-sub"><a href="{P("/services/")}">{lab[1]}</a><ul class="sub">{massages}</ul></li>
<li><a href="{P("/prices/")}">{lab[2]}</a></li>
<li><a href="{P("/packages/")}">{lab[3]}</a></li>
<li><a href="{P("/other-cities/")}">{lab[4]}</a></li>
<li><a href="{P("/bookings/")}">{lab[5]}</a></li>
<li class="lang-li">{sw}</li>
</ul>
</nav>
<a class="btn btn-sm hdr-cta" href="{P("/contact/")}" data-chat>Direct contact</a>
</div>
</header>"""


_footer_en = footer


def footer():
    if L != "nl":
        return _footer_en()
    col = lambda title, items: f'<nav aria-label="{E(title)}"><h2>{E(title)}</h2><ul>' + "".join(
        f'<li><a href="{u}">{E(t)}</a></li>' for u, t in items) + "</ul></nav>"
    return f"""<footer class="ftr">
<div class="wrap ftr-grid">
<div><p class="logo">{LOGO_MARK}<span class="logo-t"><span>Erotic Massage</span><small>Amsterdam</small></span></p>
<p>Erotische massage bij u in het hotel of thuis, in Amsterdam en omgeving. Discreet, persoonlijk en geregeld via de chat.</p>
<p><a class="btn btn-sm" href="/nl/contact/" data-chat>Direct contact</a></p></div>
{col("Massages", [(P(f"/{s}/"), n) for s, n, _ in MASSAGES_NL] + [("/nl/happy-ending-massage/", "Happy ending massage"), ("/nl/nuru-massage/", "Nuru massage"), ("/nl/massages/", "Alle massages")])}
{col("Locaties", [(P(f"/{s}/"), f"Erotische massage {n}") for s, n in CITIES[:9]] + [("/nl/locaties/", "Alle locaties")])}
{col("Informatie", [("/nl/over-ons/", "Over ons"), ("/nl/masseuses/", "Onze masseuses"), ("/nl/prijzen/", "Prijzen"), ("/nl/pakketten/", "Pakketten"), ("/nl/boeken/", "Boeken"), ("/nl/contact/", "Contact"), ("/", "English")])}
</div>
<div class="wrap ftr-base"><p>© {date.today().year} {BRAND} · Licentienr. D18.000305</p><p><a href="/nl/privacy/">Privacy</a> · <a href="/nl/voorwaarden/">Voorwaarden</a> · 18+ · Alleen voor volwassenen</p></div>
</footer>"""


_page_en = page
CUR_PATH = "/"


def page(path, title, desc, body, schema, og_image=None):
    global CUR_PATH
    CUR_PATH = path
    url = _page_en(path, title, desc, body, schema, og_image)
    out = os.path.join(DIST, path.strip("/"), "index.html")
    doc = open(out, encoding="utf-8").read()
    pair = (path, NLMAP[path]) if path in NLMAP else (ENMAP[path], path) if path in ENMAP else None
    if pair:
        alt = (f'<link rel="alternate" hreflang="en" href="{SITE}{pair[0]}">\n<link rel="alternate" hreflang="nl" href="{SITE}{pair[1]}">\n'
               f'<link rel="alternate" hreflang="x-default" href="{SITE}{pair[0]}">\n')
        doc = doc.replace('<meta name="robots"', alt + '<meta name="robots"', 1)
    if L == "nl":
        doc = doc.replace('<html lang="en">', '<html lang="nl">', 1).replace('content="en_GB"', 'content="nl_NL"', 1).replace('"inLanguage":"en"', '"inLanguage":"nl"')
    open(out, "w", encoding="utf-8").write(doc)
    return url


_cta_en = cta


def cta(text=None, label="Direct contact"):
    if L != "nl":
        return _cta_en(text) if text else _cta_en()
    text = text or "Klaar om te boeken? Vertel ons in de chat waar u verblijft, wanneer u wilt en wat uw wensen zijn."
    return (f'<section class="sec band">{pic("massage-candles-stones", "", 1000, 400, cls="band-bg")}<div class="wrap narrow center-box"><p class="cta-t">{E(text)}</p>'
            f'<p><a class="btn" href="/nl/contact/" data-chat>{E(label)}</a> <a class="link" href="/nl/prijzen/">Bekijk prijzen</a></p></div></section>')


_card_en = card


def card(m, eager=False):
    if L != "nl":
        return _card_en(m, eager)
    slug, name, age, langs, city = m
    sub_l = " · ".join(x for x in (str(age), nl_langs(langs) or city) if x)
    im = img(m, eager=eager).replace("erotic masseuse in Amsterdam", "erotische masseuse in Amsterdam")
    return f'<li class="card"><a href="/dames/{slug}/">{im}<span class="card-b"><strong>{E(name)}</strong><span>{E(sub_l)}</span></span></a></li>'


def nl_price(label):
    return label.replace("2 hours", "2 uur").replace("3 hours", "3 uur").replace("6 hours", "6 uur")


def price_table_nl(rows):
    def loc(n):
        return f'<a href="{NLMAP[f"/{CITY_SLUG[n]}/"]}">{E(n)}</a>' if n in CITY_SLUG else E(n)
    return ('<div class="tbl"><table><caption class="vh">Tarieven per locatie</caption><thead><tr><th scope="col">Locatie</th>'
            '<th scope="col">Prijs</th><th scope="col">Extra uur</th></tr></thead><tbody>' + "".join(
                f'<tr><th scope="row">{loc(n)}</th><td>{E(nl_price(p))}</td><td>{E(x)}</td></tr>' for n, p, x in rows) + "</tbody></table></div>")


def sub_nl(path, title, desc, h1, lead, inner, trail, schema=None, og_image=None):
    return sub(path, title, desc, h1, lead, inner, trail, schema, og_image)


# ------------------------------------------------------------------ content
NL_FAQ_HOME = [
    ("Hoe boek ik een erotische massage in Amsterdam?", "Open de chat op deze website en kies live chat, WhatsApp of Telegram. Vertel ons waar u verblijft, welk tijdstip u prettig vindt en welke massage of masseuse u in gedachten heeft. Wij bevestigen alles voordat het definitief is."),
    ("Komt de masseuse naar mijn hotel?", "Ja. Onze masseuses bezoeken hotels en privéadressen in Amsterdam en omgeving, waaronder Schiphol, Hoofddorp en Haarlem. Andere steden vindt u op de prijzenpagina."),
    ("Kan ik zelf een masseuse kiezen?", "Ja. Bekijk de profielen, kies de masseuse die u aanspreekt en noem haar naam in de chat. Is zij niet beschikbaar, dan stellen wij een alternatief voor en beslist u."),
    ("Is de service discreet?", "Discretie is het uitgangspunt van elke boeking. Uw gegevens worden alleen gebruikt om uw afspraak te regelen en worden niet gedeeld."),
    ("Bieden jullie een happy ending massage aan?", "Ja. Een happy ending hoort bij al onze erotische massages, of u nu kiest voor een sensuele, tantra of body to body massage."),
    ("Wat kost een erotische massage?", "Het tarief hangt af van uw locatie. In Amsterdam, Schiphol, Haarlem en Hoofddorp is het tarief € 160 en elk extra uur is € 160. Alle locaties staan op de prijzenpagina."),
]

NL_MASSAGE = {
    "sensual-massage": ("Sensuele Massage Amsterdam | Bij u in Hotel of Thuis", "Sensuele massage Amsterdam",
        "Een langzame, aandachtige massage met warme olie, bij u in het hotel of thuis in Amsterdam.",
        "Sensuele massage in Amsterdam bij u in het hotel of thuis. Langzame strijkingen met warme olie door een masseuse naar keuze. Discreet, boeken via de chat.",
        [("Wat is een sensuele massage?", ["Bij een sensuele massage draait alles om tempo en aandacht. Uw masseuse werkt met lange, vloeiende strijkingen en warme olie, van uw schouders en rug tot uw benen en voeten, zonder haast. Het doel is niet een knoop uit een spier te halen, maar uw hele lichaam tot rust te brengen.",
                                            "U hoeft niets voor te bereiden en niets te weten. U gaat liggen, ademt uit en zij neemt het over."]),
         ("Wat kunt u verwachten?", ["Uw masseuse komt naar u toe, dus de massage vindt plaats in uw eigen hotelkamer of thuis. Een opgemaakt bed of een grote handdoek op het bed is voldoende.",
                                    "De massage bouwt geleidelijk op. Het begint als een ontspannende lichaamsmassage en wordt lichter, trager en plagender naarmate u ontspant. U kunt altijd aangeven wat u prettig vindt."]),
         ("Voor wie is het?", ["Voor reizigers die de hele dag in vergaderingen of in de stad hebben doorgebracht, voor wie slecht slaapt in hotels en voor iedereen die een uur onverdeelde aandacht wil. Een sensuele massage is ook een goede keuze als dit uw eerste erotische massage is."])],
        [("Wat is het verschil tussen een sensuele en een erotische massage?", "Een sensuele massage is de zachtste vorm van erotische massage. De nadruk ligt op langzame, vloeiende aanraking en op het geleidelijk opbouwen van ontspanning en opwinding."),
         ("Hoe lang duurt een sensuele massage?", "U kunt vanaf één uur boeken. Met twee uur is er meer tijd voor een rustige opbouw; elk extra uur is € 160."),
         ("Kan ik een sensuele massage in mijn hotel boeken?", "Ja. Onze masseuses komen naar hotels en privéadressen in Amsterdam en omgeving. Geef uw hotel en gewenste tijd door in de chat.")]),
    "tantra-massage": ("Tantra Massage Amsterdam | Bij u in Hotel of Thuis", "Tantra massage Amsterdam",
        "Een aandachtig ritueel waarin ademhaling, rust en langzame aanraking stap voor stap energie opbouwen.",
        "Tantra massage in Amsterdam bij u in het hotel of thuis. Een aandachtig ritueel met langzame aanraking en ademhaling. Boeken via de chat.",
        [("Wat is een tantra massage?", ["Tantra massage komt uit een traditie waarin aanraking wordt gebruikt om energie op te bouwen in plaats van die zo snel mogelijk los te laten. Vergeleken met andere erotische massages is het trager, stiller en bewuster. Ademhaling speelt een echte rol: uw masseuse nodigt u uit diep te ademen en bij het gevoel te blijven.",
                                          "Omdat niets gehaast wordt, worden sensaties sterker dan u gewend bent. Veel gasten beschrijven het als ontspannen en klaarwakker tegelijk."]),
         ("Wat kunt u verwachten?", ["De massage begint met rustige, aardende strijkingen over de achterkant van uw lichaam. Pas wanneer u volledig ontspannen bent, wordt de aanraking lichter en sensueler. Het hele lichaam doet mee en de opbouw is geleidelijk.",
                                    "Een tantra massage komt het best tot zijn recht met voldoende tijd. Boek als het kan langer dan één uur; elk extra uur kost het extra-uurtarief van onze prijzenpagina."]),
         ("Goed om te weten", ["U heeft geen ervaring met tantra of meditatie nodig. Een rustige kamer, een douche vooraf en een telefoon op stil zijn het enige dat helpt."])],
        [("Wat gebeurt er tijdens een tantra massage?", "Een tantra massage begint met rustige strijkingen en diepe ademhaling. De aanraking wordt langzaam lichter en sensueler en het hele lichaam wordt gemasseerd."),
         ("Heb ik ervaring met tantra nodig?", "Nee. Uw masseuse begeleidt u stap voor stap door de massage."),
         ("Wat kost een tantra massage in Amsterdam?", "In Amsterdam, Schiphol, Haarlem en Hoofddorp is het tarief € 160 voor het eerste uur en € 160 voor elk extra uur. Voor tantra adviseren wij twee uur of langer.")]),
    "body-2-body-massage": ("Body to Body Massage Amsterdam | B2B Massage in uw Hotel", "Body to body massage Amsterdam",
        "Huid op huid met warme olie: uw masseuse gebruikt haar hele lichaam om het uwe te masseren.",
        "Body to body massage in Amsterdam bij u in het hotel of thuis. Huid op huid met warme olie, door een masseuse naar keuze. Boeken via de chat.",
        [("Wat is een body to body massage?", ["Bij een body to body massage, ook wel body 2 body of B2B massage genoemd, gebruikt uw masseuse niet alleen haar handen. Met ruim warme olie glijdt zij met haar armen, benen en bovenlichaam over u heen, zodat u haar hele lichaam tegen het uwe voelt.",
                                                "Het is de meest intieme massage die wij aanbieden. Door het voortdurende, glijdende contact is het bijna onmogelijk om nog aan iets anders te denken."]),
         ("Wat kunt u verwachten?", ["De massage begint meestal met een korte handmassage om uw spieren op te warmen en de olie te verdelen. Daarna volgt het body to body gedeelte, eerst op uw rug en dan op uw voorkant.",
                                    "Omdat er veel olie wordt gebruikt, raden wij aan één of twee grote handdoeken op het bed te leggen. Een douche vooraf en achteraf hoort bij de ervaring."]),
         ("Combineren", ["Een body to body massage laat zich goed combineren met een sensuele massage in een boeking van twee uur, of met een tweede masseuse in een 4 hands massage. Vertel ons in de chat wat u in gedachten heeft."])],
        [("Wat is een body to body massage?", "Bij een body to body massage gebruikt uw masseuse haar hele lichaam en ruim warme olie om het uwe te masseren, huid op huid."),
         ("Is een body to body massage hetzelfde als een nuru massage?", "Ze lijken sterk op elkaar. Beide zijn huid-op-huid massages waarbij de masseuse over uw lichaam glijdt. Een nuru massage gebruikt een speciale gel, een body to body massage warme massageolie."),
         ("Wat moet ik voorbereiden?", "Een douche vooraf en achteraf, en één of twee grote handdoeken op het bed, omdat er veel olie wordt gebruikt.")]),
    "4-hands-massage": ("4 Hands Massage Amsterdam | Twee Masseuses", "4 hands massage Amsterdam",
        "Twee masseuses, vier handen en één ritme. Dubbele aandacht van begin tot eind.",
        "4 hands massage in Amsterdam bij u in het hotel of thuis. Twee masseuses in hetzelfde ritme voor dubbele aandacht. Discreet, boeken via de chat.",
        [("Wat is een 4 hands massage?", ["Bij een 4 hands massage, ook wel vierhandenmassage of duo massage genoemd, masseren twee masseuses u tegelijk. Soms spiegelen ze elkaar, elk aan een kant van uw lichaam. Soms werkt de een aan uw schouders terwijl de ander uw benen verzorgt.",
                                           "Het effect is verrassend. Met twee handen kan uw hoofd nog volgen wat er gebeurt. Met vier geeft het dat al snel op, en precies dan ontspant u volledig."]),
         ("Wat kunt u verwachten?", ["Beide masseuses komen samen naar uw hotel of huis. De massage kan sensueel zijn, body to body of een mix van beide; dat bepaalt u samen aan het begin.",
                                    "Bij een 4 hands massage boekt u twee masseuses voor dezelfde tijd, dus het tarief wijkt af van een massage met één masseuse. Vraag het tarief in de chat; wij bevestigen het voordat u boekt."]),
         ("Boekingstip", ["Niet elke combinatie van masseuses is op elk moment beschikbaar. Wilt u twee specifieke masseuses, noem dan beide namen en boek iets vooruit."])],
        [("Hoe werkt een 4 hands massage?", "Twee masseuses masseren u tegelijk. Ze spiegelen elkaar of werken aan verschillende delen van uw lichaam, zodat u vier handen in één ritme voelt."),
         ("Kan ik beide masseuses kiezen?", "Ja. Noem beide namen in de chat en boek iets vooruit, want niet elke combinatie is altijd vrij."),
         ("Wat kost een 4 hands massage?", "U boekt twee masseuses voor dezelfde tijd, dus het tarief wijkt af van een massage met één masseuse. Vraag het tarief in de chat.")]),
    "thai-massage": ("Thaise Massage Amsterdam | Met een Sensuele Afsluiting", "Thaise massage Amsterdam",
        "Rekken en stevige druk om spanning los te maken, afgesloten met een zachte, sensuele aanraking.",
        "Thaise massage in Amsterdam bij u in het hotel of thuis. Rek- en druktechnieken met een sensuele afsluiting. Boeken via de chat.",
        [("Wat is een Thaise massage?", ["Traditionele Thaise massage werkt met druk langs de spieren en met zachte rekoefeningen. Waar een sensuele massage licht en vloeiend is, is een Thaise massage steviger. Het is de juiste keuze wanneer uw rug, nek of benen stijf zijn van een vlucht, een lange autorit of dagen lopen door de stad.",
                                          "Bij ons wordt het stevige deel gevolgd door een zachter deel met olie. Eerst gaat de spanning weg, daarna begint de sensuele massage."]),
         ("Wat kunt u verwachten?", ["Uw masseuse begint bij uw voeten en benen en werkt omhoog, met haar handpalmen, duimen en onderarmen. U kunt altijd om meer of minder druk vragen.",
                                    "In de tweede helft zakt het tempo en wordt de aanraking traag en plagend."]),
         ("Goed om te weten", ["Vertel uw masseuse vooraf over blessures of gevoelige plekken. Zij past de rekoefeningen aan of laat ze weg."])],
        [("Is dit een traditionele Thaise massage?", "Het eerste deel gebruikt traditionele Thaise technieken: druk langs de spieren en zachte rekoefeningen. Het tweede deel is zachter, met olie en een sensuele afsluiting."),
         ("Doet een Thaise massage pijn?", "Het is steviger dan een sensuele massage, maar het mag nooit pijn doen. U kunt altijd om meer of minder druk vragen."),
         ("Kan dit in mijn hotelkamer?", "Ja. Uw masseuse komt naar uw hotel of huis in Amsterdam en omgeving.")]),
    "full-body-massage": ("Full Body Massage Amsterdam | Bij u in Hotel of Thuis", "Full body massage Amsterdam",
        "Een complete massage van uw schouders tot uw voeten, bij u in het hotel of thuis.",
        "Full body massage in Amsterdam bij u in het hotel of thuis. Een complete lichaamsmassage van schouders tot voeten door een masseuse naar keuze.",
        [("Wat is een full body massage?", ["Een full body massage, of volledige lichaamsmassage, doet wat de naam zegt: geen deel van uw lichaam wordt overgeslagen. Nek, schouders, rug, armen, handen, benen en voeten krijgen allemaal aandacht, met olie en in een rustig tempo.",
                                             "Het is de meest klassieke massage van onze lijst en een goede basis voor al het andere. U kunt het puur ontspannend houden, of het in de tweede helft laten overgaan in een sensuele massage."]),
         ("Wat kunt u verwachten?", ["De massage begint op uw rug, waar de meeste mensen hun spanning dragen, en gaat dan naar uw benen en voeten. Nadat u zich heeft omgedraaid, gaat uw masseuse verder met uw armen, borst en benen.",
                                    "Eén uur is genoeg voor een complete massage. Met twee uur is er tijd om het echt rustig aan te doen."]),
         ("Voor wie is het?", ["Voor iedereen die net geland is, een drukke week achter de rug heeft of een dag in Amsterdam op de meest ontspannen manier wil afsluiten."])],
        [("Wat hoort er bij een full body massage?", "Nek, schouders, rug, armen, handen, benen en voeten. U bepaalt of de massage ontspannend blijft of sensueel wordt."),
         ("Hoe lang duurt een full body massage?", "Eén uur is genoeg voor een complete massage. Met twee uur kunt u er een sensuele massage aan toevoegen."),
         ("Kan ik het combineren met een andere massage?", "Ja. Een geliefde combinatie is een full body massage gevolgd door een body to body massage in een boeking van twee uur.")]),
}

NL_HAPPY = ("Happy Ending Massage Amsterdam | Bij u in Hotel of Thuis", "Happy ending massage Amsterdam",
    "Een complete erotische massage bij u in het hotel of thuis in Amsterdam, met het einde waar u op hoopt.",
    "Happy ending massage in Amsterdam bij u in het hotel of thuis. Een volledige erotische massage door een masseuse naar keuze, ontspannen en discreet.",
    [("Wat is een happy ending massage?", ["Een happy ending massage is een erotische massage die niet stopt waar een gewone massage stopt. Het begint als een ontspannende massage van uw hele lichaam en wordt langzaam sensueler, tot het eindigt met een ontlading die u volledig ontspannen achterlaat.",
                                            "In Amsterdam wordt de term voor van alles gebruikt. Bij ons betekent het simpelweg dit: een rustige erotische massage door een volwassen masseuse die plezier heeft in haar werk, bij u in het hotel of thuis, met een happy ending als natuurlijke afsluiting."]),
     ("Hoe verloopt het?", ["Uw masseuse komt naar u toe op het tijdstip dat u in de chat heeft afgesproken. Na een douche gaat u liggen en begint zij met uw rug, schouders en benen. Er is geen haast, en u kunt altijd zeggen wat u prettig vindt.",
                            "Wanneer u zich omdraait, wordt de massage lichter en plagender. De happy ending hoort bij de massage en is niet iets aparts, dus u hoeft er nooit om te vragen of over te onderhandelen."]),
     ("Welke massage kiest u?", ["Een happy ending hoort bij al onze erotische massages. Een sensuele massage is zacht en traag, een body to body massage is huid op huid, en een tantra massage bouwt de spanning zo lang mogelijk op. Kunt u niet kiezen, vertel ons dan wat u prettig vindt en wij adviseren u."]),
     ("Discreet en respectvol", ["Discretie is het uitgangspunt van elke boeking. Uw gegevens worden alleen gebruikt om uw afspraak te regelen. Onze masseuses behandelen elke gast met respect en verwachten hetzelfde terug."])],
    [("Is een happy ending bij de prijs inbegrepen?", "Ja. Een happy ending hoort bij onze erotische massages en is bij het tarief inbegrepen. In Amsterdam, Schiphol, Haarlem en Hoofddorp is het tarief € 160 per uur."),
     ("Waar vindt de massage plaats?", "Bij u in het hotel of thuis. Onze masseuses komen in Amsterdam en in veel steden en dorpen eromheen."),
     ("Kan ik mijn masseuse kiezen?", "Ja. Bekijk de profielen, kies de masseuse die u aanspreekt en noem haar naam in de chat."),
     ("Hoe boek ik een happy ending massage in Amsterdam?", "Open de chat, kies live chat, WhatsApp of Telegram en vertel ons uw locatie, het gewenste tijdstip en de masseuse van uw keuze. Wij bevestigen alles voordat het definitief is.")])

NL_CITY = {
    "Schiphol": ("Verblijft u in een luchthavenhotel voor een vroege vlucht, of bent u net geland na een lange reis? Onze masseuses bezoeken de hotels rond Schiphol. De luchthaven ligt vlak buiten Amsterdam, dus de reistijd is kort.", "Een erotische massage is een van de beste manieren om een vlucht van u af te schudden. Een uur warme olie en rustige handen doet meer voor stijve schouders en een vol hoofd dan nog een avond in de hotelbar."),
    "Hoofddorp": ("Hoofddorp ligt direct naast Schiphol en telt veel zakenhotels. Bent u hier voor werk, een congres of een tussenstop, dan is een massage een goede afsluiting van de dag.", "Uw masseuse komt naar uw hotelkamer of huisadres in Hoofddorp. U kiest de massage en de masseuse, wij regelen de planning."),
    "Haarlem": ("Haarlem is een historische stad net ten westen van Amsterdam, bekend om het oude centrum en de Grote Markt. Of u hier woont of in een van de hotels verblijft, onze masseuses komen naar u toe.", "Na een dag in de stad, of gewoon thuis op een rustige avond: een erotische massage in Haarlem is eenvoudig geregeld. Eén bericht in de chat is genoeg."),
    "Zandvoort": ("Zandvoort is de badplaats van Amsterdam en de thuisbasis van het circuit. In de zomer en tijdens raceweekenden zitten de hotels en appartementen vol, dus vooruit boeken loont.", "Sluit een dag aan het strand of op het circuit af met een sensuele massage in uw eigen kamer. Uw masseuse reist vanuit Amsterdam naar Zandvoort."),
    "Hilversum": ("Hilversum ligt in het groene Gooi, ten zuidoosten van Amsterdam, en is vooral bekend als mediastad. Onze masseuses bezoeken hotels en privéadressen in Hilversum en de omliggende dorpen.", "Omdat de reis iets langer is dan binnen Amsterdam, raden wij aan ons tijdig te laten weten wanneer u uw massage wilt."),
    "Utrecht": ("Utrecht ligt in het hart van het land, met zijn grachten, de Domtoren en veel hotels rond het station en de Jaarbeurs. Of u er bent voor een beurs, een congres of een stedentrip, onze masseuses komen naar u toe.", "Uw masseuse reist vanuit Amsterdam naar uw hotel of huis in Utrecht. Boek als het kan vooruit, zodat de masseuse van uw keuze vrij is op het tijdstip dat u wenst."),
    "Den Haag": ("Den Haag is de regeringsstad, met veel ambassades en internationale organisaties. Met het strand van Scheveningen om de hoek is het een stad waar zaken en ontspanning samengaan.", "Voor Den Haag werken wij met een minimale boeking van twee uur. Dat geeft u alle tijd voor een rustige massage, zonder dat iemand op de klok kijkt."),
    "Rotterdam": ("Rotterdam is de havenstad van Nederland, met een moderne skyline en een levendig hotelaanbod. Onze masseuses bezoeken hotels en privéadressen in de hele stad.", "Voor Rotterdam werken wij met een minimale boeking van twee uur. Zo is de reis de moeite waard voor uw masseuse en heeft u een lange, ontspannen sessie."),
    "Delft": ("Delft is een kleine historische universiteitsstad tussen Den Haag en Rotterdam, beroemd om zijn grachten en het Delfts blauw. Een geliefde uitvalsbasis voor wie de grote steden wil vermijden.", "Voor Delft werken wij met een minimale boeking van twee uur. Uw masseuse komt naar uw hotel, appartement of huis."),
    "Amstelveen": ("Amstelveen grenst direct aan de zuidkant van Amsterdam, tussen het Amsterdamse Bos en de Zuidas. Er wonen en werken veel internationale bedrijven en expats, en er zijn volop hotels.", "Omdat Amstelveen zo dicht bij Amsterdam ligt, is een massage in uw hotel of thuis hier snel geregeld. Geef uw adres en gewenste tijd door in de chat."),
    "Diemen": ("Diemen ligt aan de oostrand van Amsterdam, bij de A1 en de A10 en vlak bij het ArenA-gebied. Verschillende hotels hier zijn geliefd bij zakenreizigers en concertbezoekers.", "Uw masseuse komt naar uw hotelkamer of huis in Diemen. U kiest de massage en de masseuse, wij regelen de planning."),
    "Zaandam": ("Zaandam ligt net ten noordwesten van Amsterdam en is bekend om zijn groene houten huizen en de molens van de Zaanse Schans. De hotels zijn geliefd bij bezoekers die net buiten de hoofdstad willen verblijven.", "Een erotische massage in Zaandam vindt plaats waar u verblijft. Eén bericht in de chat met uw hotel en gewenste tijd is genoeg om te beginnen."),
    "Purmerend": ("Purmerend is een marktstad ten noorden van Amsterdam, midden in de polders van Waterland. Of u hier woont of in de omgeving verblijft, onze masseuses komen naar u toe.", "De reis vanuit Amsterdam is iets langer dan binnen de stad, dus wij raden aan ons tijdig te laten weten wanneer u uw massage wilt."),
    "Weesp": ("Weesp is een klein vestingstadje aan de Vecht, ten zuidoosten van Amsterdam, en hoort sinds 2022 bij de gemeente Amsterdam. Het oude centrum met grachten en molens voelt ver weg van de drukke stad.", "Uw masseuse bezoekt u thuis of in uw accommodatie in Weesp. Geef uw adres en gewenste tijd door, en wij bevestigen wie beschikbaar is."),
    "Naarden": ("Naarden is beroemd om zijn stervormige vesting, een van de best bewaarde vestingsteden van Europa. Het ligt in het Gooi, tussen Amsterdam en Hilversum.", "Een erotische massage in Naarden krijgt u thuis of in uw hotel. Boek als het kan vooruit, zodat de masseuse van uw keuze vrij is."),
    "Bussum": ("Bussum ligt naast Naarden in het groene Gooi, een lommerrijke plaats met villa's en rustige lanen en een directe verbinding met Amsterdam.", "Onze masseuses bezoeken privéadressen en hotels in Bussum. U kiest de massage en de masseuse, en uw masseuse komt naar u toe."),
    "Huizen": ("Huizen is een voormalig vissersdorp aan het Gooimeer, aan de noordrand van het Gooi. Tegenwoordig is het een rustige woonplaats met een jachthaven en een strand aan het meer.", "Wilt u een erotische massage thuis in Huizen? Geef uw adres en gewenste tijd door in de chat, bij voorkeur iets van tevoren."),
    "Laren": ("Laren is het kunstenaarsdorp van het Gooi, bekend om de Brink, de galeries en de statige villa's. Het is een van de meest exclusieve adressen van Nederland.", "Discretie is belangrijk voor onze gasten in Laren, en daar beginnen wij mee. Uw masseuse bezoekt u thuis of in uw hotel, op het tijdstip dat u met ons afspreekt."),
    "Almere": ("Almere is de jongste stad van Nederland, gebouwd op nieuw land in Flevoland en bekend om zijn moderne architectuur. De stad ligt ten oosten van Amsterdam, aan de overkant van het IJmeer.", "Uw masseuse reist vanuit Amsterdam naar uw huis of hotel in Almere. Boek als het kan vooruit, zodat wij de reis kunnen plannen en de masseuse van uw keuze kunnen bevestigen."),
    "Uithoorn": ("Uithoorn ligt aan de Amstel, ten zuiden van Amsterdam en Amstelveen, met een waterfront vol terrassen. Het is een korte rit vanaf zowel Amsterdam als Schiphol.", "Een erotische massage in Uithoorn krijgt u thuis of in uw accommodatie. Geef uw adres en gewenste tijd door, en wij regelen de rest."),
    "Aalsmeer": ("Aalsmeer is wereldberoemd om de bloemenveiling en de Westeinderplassen. Het ligt direct naast Schiphol, wat het een handige uitvalsbasis maakt voor reizigers.", "Verblijft u in Aalsmeer voor zaken of voor een vlucht? Uw masseuse komt naar uw hotel of huis, en u kiest de massage die u wilt."),
}

PKG_NL = {  # id: (naam, duur, prijs, tekst)
    "amsterdam-tour": ("Amsterdam Tour & Massage", "Vanaf 4 uur", "Vanaf € 640", "Ontdek Amsterdam in charmant gezelschap. Uw masseuse gaat met u mee voor een wandeling door het oude centrum of een rondvaart door de grachten, en daarna gaat u terug naar uw hotel voor een erotische massage met happy ending."),
    "dinner-date": ("Dinner Date & Erotische Massage", "Vanaf 3 uur", "Vanaf € 480", "Begin de avond aan tafel en eindig op uw kamer. U dineert samen in een restaurant naar keuze, gevolgd door een rustige erotische massage in uw hotel."),
    "amsterdam-by-night": ("Amsterdam by Night", "Vanaf 2 uur", "Vanaf € 320", "Samen een drankje in de bar van uw hotel of een cocktailbar in de stad, en daarna naar boven voor uw massage. Korter dan een dinner date, met dezelfde ontspannen start."),
    "schiphol-stopover": ("Schiphol Stopover", "1 uur", "€ 160", "Een paar uur tussen twee vluchten, of één nacht in een luchthavenhotel? Uw masseuse komt naar uw hotel op Schiphol, in Hoofddorp of Aalsmeer."),
    "jetlag-relief": ("Jetlag Relief", "2 uur", "€ 320", "Net geland en stijf van de vlucht? Eerst een stevige full body massage voor rug, nek en benen, daarna een trage, sensuele afsluiting."),
    "after-work": ("After Work", "1 uur", "€ 160", "De vergadering liep uit en de dag was lang. Eén bericht in de chat is genoeg: uw masseuse komt naar uw hotel en de laptop gaat dicht."),
    "duo-deluxe": ("Duo Deluxe", "2 uur · twee masseuses", "Prijs op aanvraag", "Twee masseuses en vier handen, twee volle uren lang. Ze werken in hetzelfde ritme, spiegelen elkaar en wisselen elkaar af."),
    "tantra-ritual": ("Tantra Ritueel", "Vanaf 2 uur", "Vanaf € 320", "Een lange tantrasessie zonder klok. Ademhaling, langzame aanraking en een geleidelijke opbouw van de eerste tot de laatste minuut."),
    "bath-and-massage": ("Bad & Massage", "2 uur", "€ 320", "Begin samen in bad of onder de douche en ga verder met een body to body massage met warme olie. Voor kamers met een bad of een ruime douche."),
    "champagne-evening": ("Champagne-avond", "3 uur", "€ 480", "Champagne op ijs, aardbeien op tafel en drie uur voor u. Een avond met een goed gesprek en een lange sensuele massage."),
    "couples-massage": ("Massage voor stellen", "Vanaf 1 uur", "Prijs op aanvraag", "Een erotische massage voor u samen, in uw hotel of thuis. Kies één masseuse die u beiden verwent, of twee masseuses die u naast elkaar masseren."),
    "massage-lesson": ("Massageles voor stellen", "2 uur", "€ 320", "Leer elkaar een sensuele massage te geven. Uw masseuse laat de strijkingen, het ritme en het gebruik van olie zien, en u oefent op elkaar terwijl zij u begeleidt."),
    "birthday-surprise": ("Verjaardagsverrassing", "Elk pakket", "Prijs op aanvraag", "Verras iemand met een avond die hij niet vergeet. Kies een pakket als cadeau, geef ons de datum, het hotel en de naam, en wij regelen de rest discreet."),
}


def nl_city_price(name):
    price = PRICE_OF.get(name)
    if not price:
        return f"Vraag het tarief voor {name} in de chat. Het hangt af van de afstand vanaf Amsterdam en wij bevestigen het altijd voordat u boekt. Elk extra uur is € 160."
    if "2 hours" in price:
        return f"In {name} is het tarief {price.replace('2 hours ', '')} voor een minimale boeking van twee uur. Elk extra uur is € 160. Uw tarief wordt altijd in de chat bevestigd voordat u boekt."
    return f"In {name} is het tarief {price} per uur. Elk extra uur is € 160. Uw tarief wordt altijd in de chat bevestigd voordat u boekt."


def pkg_card_nl(p, h="h3"):
    pid, photo = p[1], p[5]
    name, dur, price, d = PKG_NL[pid]
    return (f'<li class="pkg" id="{pid}">{pic(photo, name, 600, 400)}<div class="pkg-b"><p class="pkg-m"><span>{E(dur)}</span><strong>{E(price)}</strong></p>'
            f'<{h}>{E(name)}</{h}><p>{E(d)}</p><p><a class="btn btn-sm" href="/nl/contact/" data-chat>Boek dit pakket</a> '
            f'<a class="link" href="/packages/{pid}/" hreflang="en">Meer informatie (Engels)</a></p></div></li>')


def build_nl():
    global L
    L = "nl"
    urls = []
    tile = lambda s, n, d, h: (f'<li><a class="tile tile-img" href="{NLMAP[f"/{s}/"]}">{pic(s + "-amsterdam", n + " in Amsterdam", 600, 400)}'
                               f'<span class="tile-b"><{h}>{E(n)}</{h}><p>{E(d)}</p><span class="more">Lees meer</span></span></a></li>')
    mchips = "".join(f'<li><a href="{NLMAP[f"/{s}/"]}">{E(n)}</a></li>' for s, n, _ in MASSAGES_NL) + '<li><a href="/nl/happy-ending-massage/">Happy ending massage</a></li><li><a href="/nl/nuru-massage/">Nuru massage</a></li>'
    cchips = lambda skip=None: '<li><a href="/nl/">Erotische massage Amsterdam</a></li>' + "".join(
        f'<li><a href="{NLMAP[f"/{s}/"]}">Erotische massage {E(n)}</a></li>' for s, n in CITIES if n != skip) + '<li><a href="/nl/locaties/">Alle locaties</a></li>'
    ncity = len(set(p[0] for p in PRICES) | set(n for _, n in CITIES))

    # ---- home
    title = "Erotische Massage Amsterdam | Bij u in Hotel of Thuis"
    desc = "Erotische massage in Amsterdam bij u in het hotel of thuis. Sensuele, tantra en body to body massage met happy ending door een masseuse naar keuze. Vanaf € 160."
    fq_html, fq_schema = faq_block(NL_FAQ_HOME, "Veelgestelde vragen")
    pk = "".join(pkg_card_nl(p) for p in PACKAGES if p[1] in ("dinner-date", "amsterdam-tour", "duo-deluxe"))
    body = f"""<section class="hero">
<div class="wrap hero-grid">
<div>
<p class="eyebrow">Massage aan huis · Hotel- &amp; thuisbezoek</p>
<h1>Erotische Massage <span class="g">Amsterdam</span></h1>
<p class="lead">Een sensuele massage op de plek waar u verblijft, door een masseuse die u zelf kiest. Vertel ons in de chat uw hotel, uw tijd en uw wensen, en wij regelen de rest discreet.</p>
<p class="cta"><a class="btn" href="/nl/contact/" data-chat>Direct contact</a> <a class="btn btn-ghost" href="/nl/masseuses/">Bekijk onze masseuses</a></p>
<ul class="usp"><li>Hotel- en thuisbezoek</li><li>U kiest uw masseuse</li><li>Discreet vanaf het eerste bericht</li></ul>
</div>
<div class="hero-img">{pic("erotic-massage-amsterdam-hero", "Erotische massage in Amsterdam bij u in het hotel", 720, 900, eager=True)}<p class="badge"><strong>€ 160</strong><span>per uur in Amsterdam</span></p></div>
</div>
</section>

<section class="stats" aria-label="Erotic Massage Amsterdam in cijfers">
<ul class="wrap">
<li><strong>{len(MASSEUSES)}</strong><span>masseuses om uit te kiezen</span></li>
<li><strong>{len(MASSAGES) + 2}</strong><span>erotische massages</span></li>
<li><strong>{ncity}</strong><span>steden en dorpen</span></li>
<li><strong>€ 160</strong><span>per uur in Amsterdam</span></li>
</ul>
</section>

<section class="sec sec-alt">
<div class="wrap split">
<div class="split-img">{pic("erotic-massage-at-your-hotel", "Ontspannende erotische massage met warme olie", 500, 333)}</div>
<div class="prose">
<h2>Welkom</h2>
<p>Amsterdam is een stad van passie, liefde en opwinding. Wilt u dat uw tijd in Amsterdam zo aangenaam mogelijk is, dan is een erotische massage het overwegen waard.</p>
<p>Een erotische massage is de perfecte manier om de stress die u op uw schouders meedraagt kwijt te raken, en om nog lang daarna met een glimlach rond te lopen.</p>
<p>Of u nu wilt ontspannen na een drukke dag of gewoon toe bent aan een moment voor uzelf: een van onze masseuses komt naar u toe en neemt alle spanning weg.</p>
</div>
</div>
</section>

<section class="sec sec-c">
<div class="wrap">
<h2>Onze erotische massages</h2>
<p class="intro">Elke massage is één op één en in uw tempo. Weet u niet welke bij u past? Beschrijf in de chat wat u prettig vindt en wij adviseren u.</p>
<ul class="tiles">{"".join(tile(s, n, d, "h3") for s, n, d in MASSAGES_NL)}</ul>
<p class="center"><a class="link" href="/nl/massages/">Alle massages</a> <a class="link" href="/nl/happy-ending-massage/">Happy ending massage</a></p>
</div>
</section>

<section class="sec sec-wine sec-c">
<div class="wrap">
<h2>Onze masseuses in Amsterdam</h2>
<p class="intro">Een selectie van onze masseuses. Open een profiel voor foto's en meer informatie.</p>
<ul class="cards">{"".join(card(m) for m in MASSEUSES[:10])}</ul>
<p class="center"><a class="link" href="/nl/masseuses/">Bekijk alle masseuses</a></p>
</div>
</section>

<section class="sec sec-alt sec-c">
<div class="wrap">
<h2>Populaire pakketten</h2>
<p class="intro">Combineer uw erotische massage met een diner, een stadstour of een tweede masseuse.</p>
<ul class="pkgs">{pk}</ul>
<p class="center"><a class="btn btn-ghost" href="/nl/pakketten/">Bekijk alle {len(PACKAGES)} pakketten</a></p>
</div>
</section>

<section class="sec">
<div class="wrap narrow prose">
<h2>Erotische massage in Amsterdam</h2>
<div class="float-img">{pic("sensual-erotic-massage", "Sensuele erotische massage in Amsterdam", 560, 840)}</div>
<p>Amsterdam is een drukke stad. Wie er niet aan gewend is, kan het vol en gejaagd vinden. Een erotische massage is dan de ideale manier om even helemaal tot rust te komen. Bij een erotische massage in Amsterdam ontmoet u een van onze dames op de plek die u met ons afspreekt: uw hotelkamer of uw eigen huis.</p>
<p>Het beste wat u tijdens een erotische massage kunt doen, is ontspannen. U laat iemand anders het tempo bepalen en geeft toe aan aanrakingen op plekken die bij een gewone massage worden overgeslagen. Hoe meer u zich overgeeft, hoe intenser en aangenamer de massage wordt.</p>
<p>U krijgt er bovendien iets voor terug: de spanning in uw lichaam en uw hoofd verdwijnt, en u voelt zich daarna lichter, fitter en zelfverzekerder.</p>
<h3>Haal het meeste uit uw lichaam met een erotische massage</h3>
<p>Wij werken met dames die ervaring hebben en plezier beleven aan het geven van een erotische massage. Daardoor kunt u zich volledig laten gaan en gewoon genieten van het hele moment.</p>
<p>Niets maakt het leven lichter dan een massage die u rust en vrijheid geeft, met een perfecte afsluiting waar u de rest van de week op teert. Veel mensen maken zo'n ervaring maar een paar keer in hun leven mee. Onze masseuses hebben de vaardigheid en het talent om daar verandering in te brengen.</p>
</div>
</section>

<section class="sec sec-alt sec-c">
<div class="wrap">
<h2>Zo werkt boeken</h2>
<ol class="steps">
<li><h3>Open de chat</h3><p>Kies live chat, WhatsApp of Telegram en vertel ons uw locatie, gewenste tijd en massage.</p></li>
<li><h3>Wij bevestigen</h3><p>U hoort welke masseuse beschikbaar is en wat het tarief is, voordat u beslist.</p></li>
<li><h3>Zij komt naar u toe</h3><p>Uw masseuse komt op de afgesproken tijd naar uw hotel of huis. U heeft alleen een douche en schone handdoeken nodig.</p></li>
</ol>
<p class="center"><a class="btn" href="/nl/contact/" data-chat>Direct contact</a> <a class="link" href="/nl/prijzen/">Bekijk prijzen</a></p>
</div>
</section>

<section class="sec sec-c">
<div class="wrap">
<h2>Erotische massage in Amsterdam en omgeving</h2>
<p class="intro">Amsterdam is onze thuisbasis. Wij komen ook rond Schiphol, in de plaatsen rond Amsterdam, in het Gooi en in andere steden in de Randstad.</p>
<ul class="chips">{"".join(f'<li><a href="{NLMAP[f"/{s}/"]}">Erotische massage {E(n)}</a></li>' for s, n in CITIES)}<li><a href="/nl/locaties/">Alle locaties</a></li></ul>
</div>
</section>
{fq_html}"""
    wp = {"@context": "https://schema.org", "@type": "WebPage", "@id": SITE + "/nl/#webpage", "url": SITE + "/nl/", "name": title, "description": desc,
          "inLanguage": "nl", "isPartOf": {"@id": SITE + "/#website"}, "about": {"@id": SITE + "/#org"}, "dateModified": TODAY}
    urls.append(page("/nl/", title, desc, body, [ORG, WEBSITE, wp, fq_schema]))

    # ---- massages
    def massage_page(slug, name, data, photo):
        t, h1, lead, d, blocks, faq = data
        fh, fs = faq_block(faq, f"Vragen over {name.lower()}")
        others = "".join(f'<li><a href="{NLMAP[f"/{s}/"]}">{E(n)}</a></li>' for s, n, _ in MASSAGES_NL if s != slug)
        inner = (f'<section class="sec"><div class="wrap narrow prose"><figure class="fig">{pic(photo, name + " in Amsterdam", 600, 400, eager=True)}</figure>{prose(blocks)}'
                 f'<h2>Prijs</h2><p>Een {E(name.lower())} in Amsterdam, Schiphol, Haarlem of Hoofddorp kost € 160 per uur en elk extra uur is € 160. '
                 f'Voor andere steden zie onze <a href="/nl/prijzen/">prijzen</a>.</p></div></section>'
                 f'{cta(f"Boek uw {name.lower()} in de chat. Wij bevestigen masseuse, tijd en tarief voordat iets definitief is.")}{fh}'
                 f'<section class="sec"><div class="wrap"><h2>Andere massages</h2><ul class="chips">{others}<li><a href="/nl/happy-ending-massage/">Happy ending massage</a></li><li><a href="/nl/nuru-massage/">Nuru massage</a></li><li><a href="/nl/massages/">Alle massages</a></li></ul>'
                 f'<h2 class="mt">Waar wij komen</h2><ul class="chips">{cchips()}</ul>'
                 f'<h2 class="mt">Kies uw masseuse</h2><ul class="cards">{"".join(card(m) for m in MASSEUSES[:10])}</ul>'
                 f'<p class="center"><a class="link" href="/nl/masseuses/">Bekijk alle masseuses</a></p></div></section>')
        path = NLMAP[f"/{slug}/"]
        svc = {"@context": "https://schema.org", "@type": "Service", "name": h1, "serviceType": name, "description": d, "provider": {"@id": SITE + "/#org"},
               "areaServed": {"@type": "City", "name": "Amsterdam"}, "url": SITE + path}
        return sub(path, t, d, h1, lead, inner, [("Massages", "/nl/massages/")], [svc, fs])

    for slug, name, _ in MASSAGES_NL:
        urls.append(massage_page(slug, name, NL_MASSAGE[slug], slug + "-amsterdam"))
    urls.append(massage_page("happy-ending-massage", "Happy ending massage", NL_HAPPY, "happy-ending-massage-amsterdam"))
    inner = (f'<section class="sec"><div class="wrap"><ul class="tiles">{"".join(tile(s, n, d, "h2") for s, n, d in MASSAGES_NL)}</ul></div></section>'
             '<section class="sec sec-alt"><div class="wrap split"><div class="split-img">' + pic("hot-stone-massage", "Massage met warme stenen", 900, 600) + '</div><div class="prose"><h2>Eén service, op uw manier</h2>'
             '<p>Elke massage op deze pagina is een massage aan huis: uw masseuse komt naar uw hotel of naar u thuis. U kiest de massage en de masseuse, en u kunt massages combineren in een langere boeking.</p>'
             '<p>Zoekt u een <a href="/nl/happy-ending-massage/">happy ending massage</a>? Die hoort bij al onze erotische massages.</p>'
             '<p>Weet u niet wat bij u past? Vertel ons in de chat wat u prettig vindt, of u zacht of stevig wilt en hoeveel tijd u heeft. Wij stellen een massage en een masseuse voor, en u beslist.</p></div></div></section>' + cta())
    urls.append(sub("/nl/massages/", "Erotische Massages | Alle Massages van Erotic Massage Amsterdam",
                    "Alle erotische massages in Amsterdam: sensuele, tantra, body to body, 4 hands, Thaise en full body massage bij u in het hotel of thuis.",
                    "Onze massages", "Zes massages, allemaal bij u in het hotel of thuis in Amsterdam en omgeving.", inner, []))

    # ---- cities
    for slug, name in CITIES:
        a, b = NL_CITY[name]
        path = NLMAP[f"/{slug}/"]
        pl = nl_city_price(name)
        faq = [(f"Wat kost een erotische massage in {name}?", pl),
               (f"Komen jullie naar hotels en privéadressen in {name}?", f"Ja. Uw masseuse komt naar uw hotel, appartement of huis in {name}. Geef het adres en de gewenste tijd door in de chat."),
               (f"Hoe ver van tevoren moet ik boeken in {name}?", f"Hoe eerder hoe beter, want uw masseuse reist naar {name} en uw favoriet kan al geboekt zijn. Boeken op dezelfde dag is vaak mogelijk; vraag het in de chat."),
               (f"Welke massages kan ik boeken in {name}?", "Al onze erotische massages: sensuele, tantra, body to body, 4 hands, Thaise en full body massage, elk met een happy ending.")]
        fh, fs = faq_block(faq, f"Vragen over erotische massage in {name}")
        inner = (f'<section class="sec"><div class="wrap narrow prose"><h2>Erotische massage aan huis of in uw hotel in {E(name)}</h2><p>{E(a)}</p><p>{E(b)}</p>'
                 f'<h2>Prijs in {E(name)}</h2><p>{E(pl)} Bekijk alle <a href="/nl/prijzen/">prijzen</a>.</p>'
                 f'<h2>Welke massages kunt u boeken in {E(name)}?</h2><p>Al onze massages zijn beschikbaar in {E(name)}:</p><ul class="chips">{mchips}</ul>'
                 f'<h2>Zo boekt u</h2><p>Open de chat, vertel ons uw adres of hotel in {E(name)}, het gewenste tijdstip en de masseuse die u aanspreekt. Wij bevestigen beschikbaarheid en tarief, en uw masseuse komt naar u toe. Lees meer op de pagina <a href="/nl/boeken/">boeken</a>.</p></div></section>'
                 f'<section class="sec sec-wine sec-c"><div class="wrap"><h2>Onze masseuses</h2><ul class="cards">{"".join(card(m) for m in MASSEUSES[:10])}</ul><p class="center"><a class="link" href="/nl/masseuses/">Bekijk alle masseuses</a></p></div></section>'
                 f'{cta(f"Boek uw erotische massage in {name} via de chat.")}{fh}'
                 f'<section class="sec"><div class="wrap"><h2>Andere locaties</h2><ul class="chips">{cchips(name)}</ul></div></section>')
        d = f"Erotische massage in {name} bij u in het hotel of thuis. Sensuele, tantra en body to body massage door masseuses uit Amsterdam. Discreet, boeken via de chat."
        svc = {"@context": "https://schema.org", "@type": "Service", "name": f"Erotische massage {name}", "serviceType": "Erotische massage", "provider": {"@id": SITE + "/#org"},
               "areaServed": {"@type": "City", "name": name}, "url": SITE + path}
        urls.append(sub(path, f"Erotische Massage {name} | Aan Huis & in uw Hotel", d, f"Erotische massage {name}",
                        f"Erotische massage in {name}: uw masseuse komt naar uw hotel of naar u thuis.", inner, [("Locaties", "/nl/locaties/")], [svc, fs]))
    rest = ", ".join(n for _, n in CITIES if n not in PRICE_OF)
    inner = (f'<section class="sec"><div class="wrap narrow prose"><h2>Waar wij komen</h2><p>Amsterdam is onze thuisbasis, maar onze masseuses reizen. Hieronder vindt u de locaties met hun tarief. Voor steden met een eigen pagina leest u meer via de link.</p>{price_table_nl(PRICES)}'
             f'<p>{("Wij komen ook in " + E(rest) + ". Vraag het tarief in de chat.") if rest else ""}</p><p>Staat uw plaats er niet bij? Vraag het ons in de chat. Voor langere afstanden werken wij met een minimum aantal uren.</p></div></section>'
             f'<section class="sec sec-alt"><div class="wrap"><h2>Locaties met een eigen pagina</h2><ul class="chips">{cchips()}</ul></div></section>{cta()}')
    urls.append(sub("/nl/locaties/", "Erotische Massage Locaties | Steden rond Amsterdam",
                    "Erotische massage buiten Amsterdam: Schiphol, Amstelveen, Haarlem, Almere, Utrecht, Rotterdam, Den Haag en meer. Hotel- en thuisbezoek met tarieven per stad.",
                    "Locaties", "Erotische massage bij u in het hotel of thuis, ook buiten Amsterdam.", inner, []))

    # ---- prices
    pf, ps = faq_block([("Wat kost een erotische massage in Amsterdam?", "In Amsterdam, Schiphol, Haarlem en Hoofddorp is het tarief € 160 voor één uur. Elk extra uur is € 160."),
                        ("Is een happy ending bij de prijs inbegrepen?", "Ja. Een happy ending hoort bij onze erotische massages en is bij het tarief inbegrepen."),
                        ("Zijn er extra kosten?", "Nee. Het tarief in de tabel is het tarief voor het bezoek van uw masseuse op die locatie. Bij pakketten betaalt u zelf zaken als diner, drankjes en tickets."),
                        ("Waarom is de prijs buiten Amsterdam hoger?", "Uw masseuse reist vanuit Amsterdam naar u toe. Voor steden die verder weg liggen is het tarief hoger of geldt een minimum aantal uren.")], "Vragen over onze prijzen")
    inner = (f'<section class="sec"><div class="wrap narrow prose"><p>Onze tarieven hangen af van de locatie van uw bezoek. De prijs is voor één uur, tenzij er een minimum aantal uren bij staat. Elk extra uur is € 160. Uw tarief wordt altijd in de chat bevestigd voordat u boekt.</p>{price_table_nl(PRICES)}'
             '<h2>Goed om te weten</h2><ul class="ticks"><li>Het tarief is per masseuse. Vraag voor een 4 hands massage met twee masseuses het tarief in de chat.</li>'
             '<li>Voor steden die verder weg liggen werken wij met een minimum aantal uren; dat staat in de tabel.</li>'
             '<li>Staat uw plaats er niet bij? Vraag het ons in de chat.</li></ul></div></section>' + pf + cta("Vraag uw tarief in de chat. Wij bevestigen het voordat u boekt."))
    urls.append(sub("/nl/prijzen/", "Prijzen & Tarieven | Erotic Massage Amsterdam",
                    "Prijzen voor erotische massage aan huis of in uw hotel: € 160 in Amsterdam, Schiphol, Haarlem en Hoofddorp, € 160 per extra uur. Tarieven per stad.",
                    "Prijzen", "Heldere tarieven per locatie, bevestigd voordat u boekt.", inner, [], [ps]))

    # ---- packages overview
    groups_nl = {"Discover Amsterdam": "Ontdek Amsterdam", "For the business traveller": "Voor de zakenreiziger", "Something special": "Iets bijzonders", "For couples and gifts": "Voor stellen en cadeaus"}
    secs = ""
    for i, g in enumerate(groups_nl):
        secs += f'<section class="sec{" sec-alt" if i % 2 else ""} sec-c"><div class="wrap"><h2>{groups_nl[g]}</h2><ul class="pkgs">{"".join(pkg_card_nl(p) for p in PACKAGES if p[0] == g)}</ul></div></section>'
    kf, ks = faq_block([("Is een happy ending bij de pakketten inbegrepen?", "Elk pakket eindigt met een erotische massage naar keuze, en een happy ending hoort bij onze erotische massages."),
                        ("Wat is bij de prijs inbegrepen?", "De prijs is voor de tijd van uw masseuse in Amsterdam, Schiphol, Haarlem of Hoofddorp. De restaurantrekening, drankjes, champagne en tickets voor een rondvaart of museum betaalt u zelf."),
                        ("Kan ik een pakket aanpassen?", "Ja. Elk pakket is een vertrekpunt. Voeg een uur toe, kies een andere massage of combineer twee pakketten; wij bevestigen het tarief in de chat."),
                        ("Hoe boek ik een pakket?", "Open de chat, vertel ons welk pakket u wilt, uw hotel of adres, de datum en tijd en de masseuse van uw keuze. Wij bevestigen alles voordat het definitief is.")], "Vragen over onze pakketten")
    urls.append(sub("/nl/pakketten/", "Massage Pakketten Amsterdam | 13 Combinaties",
                    "Dertien massagepakketten in Amsterdam: dinner date, stadstour, stopover op Schiphol, duo, bad, champagne-avond en massage voor stellen. Boeken via de chat.",
                    "Pakketten", "Dertien manieren om een erotische massage te combineren met een mooie dag of avond in Amsterdam.", secs + kf + cta("Vertel ons welk pakket u wilt. Wij bevestigen masseuse, tijd en tarief voordat u boekt."), [], [ks]))

    # ---- masseuses overview
    inner = (f'<section class="sec"><div class="wrap"><ul class="cards cards-lg">{"".join(card(m, eager=i < 1) for i, m in enumerate(MASSEUSES))}</ul></div></section>'
             '<section class="sec sec-alt"><div class="wrap narrow prose"><h2>Kies de masseuse die u aanspreekt</h2>'
             '<p>Neem rustig de tijd om de profielen te bekijken. Elke masseuse heeft een eigen pagina met foto\'s en gegevens.</p>'
             '<p>Noem haar naam in de chat wanneer u boekt. Is uw eerste keuze niet beschikbaar op het gewenste tijdstip, dan laten wij dat direct weten en stellen wij iemand anders voor.</p></div></section>' + cta())
    urls.append(sub("/nl/masseuses/", "Onze Masseuses | Erotic Massage Amsterdam",
                    f"Maak kennis met de {len(MASSEUSES)} masseuses van Erotic Massage Amsterdam. Bekijk de profielen en foto's en kies wie u bezoekt in uw hotel of thuis.",
                    "Onze masseuses", "Bekijk alle profielen. U kiest wie er naar u toe komt.", inner, []))

    # ---- bookings + contact
    bf, bs = faq_block([("Hoe snel kan een masseuse bij mij zijn?", "Dat hangt af van het tijdstip en van wie beschikbaar is. Geef uw locatie en gewenste tijd door in de chat en u krijgt direct antwoord."),
                        ("Kan ik voor vandaag boeken?", "Vaak wel. Voor een specifieke masseuse of een langer pakket raden wij aan vooruit te boeken."),
                        ("Welke gegevens hebben jullie nodig?", "Uw hotel en kamernummer of uw adres, de dag en tijd, het aantal uren en de massage en masseuse van uw keuze."),
                        ("Is mijn boeking discreet?", "Ja. Uw gegevens worden alleen gebruikt om uw afspraak te regelen en worden niet gedeeld.")], "Vragen over boeken")
    inner = ('<section class="sec"><div class="wrap narrow prose"><h2>Boeken in drie stappen</h2><ol class="steps steps-col">'
             '<li><h3>Open de chat</h3><p>Gebruik de knop Direct contact en kies live chat, WhatsApp of Telegram.</p></li>'
             '<li><h3>Vertel ons wat u wilt</h3><p>Uw hotel of adres, de dag en tijd, het aantal uren en de massage en masseuse van uw keuze.</p></li>'
             '<li><h3>Ontvang uw bevestiging</h3><p>Wij bevestigen de masseuse, het tijdstip en het tarief. Uw masseuse komt daarna op de afgesproken tijd naar u toe.</p></li></ol>'
             '<h2>Voorbereiden op uw massage</h2><ul class="ticks"><li>Neem een douche voordat uw masseuse arriveert.</li><li>Leg één of twee schone, grote handdoeken klaar.</li>'
             '<li>Verblijft u in een hotel, geef dan uw kamernummer door en zorg dat uw masseuse naar boven kan.</li><li>Zet uw telefoon op stil en geniet.</li></ul>'
             '<h2>Wijzigen of annuleren</h2><p>Plannen veranderen. Wilt u uw boeking verplaatsen of annuleren, laat het ons dan zo vroeg mogelijk weten in de chat, zodat wij uw masseuse kunnen informeren.</p>'
             '<h2>Respect en discretie</h2><p>Onze masseuses behandelen elke gast met respect en verwachten hetzelfde terug. Uw gegevens worden alleen gebruikt om uw afspraak te regelen.</p></div></section>' + bf + cta())
    urls.append(sub("/nl/boeken/", "Erotische Massage Boeken in Amsterdam | Zo werkt het",
                    "Boek een erotische massage in Amsterdam via de chat: live chat, WhatsApp of Telegram. Geef uw hotel, tijd en masseuse door en wij bevestigen alles.",
                    "Boeken", "Boeken kost één bericht. Zo werkt het.", inner, [], [bs]))
    inner = ('<section class="sec"><div class="wrap narrow prose"><p>De snelste manier om ons te bereiken is de chat. Kies live chat, WhatsApp of Telegram en u spreekt direct met ons.</p>'
             '<p><a class="btn" href="/nl/contact/" data-chat>Direct contact</a></p>'
             '<h2>Waarmee kunnen wij u helpen?</h2><ul class="ticks"><li>Een massage boeken in uw hotel of thuis</li><li>Advies over welke massage of masseuse bij u past</li>'
             '<li>Tarieven voor uw stad</li><li>Een boeking wijzigen of annuleren</li></ul>'
             '<h2>Wat zet u in uw eerste bericht?</h2><p>Hoe meer wij weten, hoe sneller wij kunnen bevestigen. Vertel ons de stad en het hotel of adres, de dag en het tijdstip, hoe lang u wilt boeken en welke massage of masseuse uw voorkeur heeft. Voor een vraag hoeft u uw volledige naam niet te geven.</p>'
             '<h2>Discretie</h2><p>Uw gegevens worden gebruikt om uw afspraak te regelen en nergens anders voor.</p>'
             '<p>Zie ook de pagina\'s <a href="/nl/boeken/">boeken</a> en <a href="/nl/prijzen/">prijzen</a>.</p>'
             '<noscript><p>De chat heeft JavaScript nodig. Schakel JavaScript in uw browser in om contact op te nemen.</p></noscript></div></section>')
    urls.append(sub("/nl/contact/", "Contact Opnemen | Erotic Massage Amsterdam",
                    "Neem contact op met Erotic Massage Amsterdam via de chat: live chat, WhatsApp of Telegram. Stel uw vraag of boek een massage in uw hotel of thuis.",
                    "Contact", "Wij zijn bereikbaar via de chat: live chat, WhatsApp of Telegram.", inner, []))
    L = "en"
    return urls
