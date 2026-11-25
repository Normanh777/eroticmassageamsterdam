# Extra landing pages (EN + NL): massage for women, outcall / aan huis. Executed inside build.py's namespace.
NLMAP["/erotic-massage-for-women/"] = "/nl/erotische-massage-voor-vrouwen/"
NLMAP["/outcall-massage-amsterdam/"] = "/nl/erotische-massage-aan-huis/"
NLMAP["/lingam-massage/"] = "/nl/lingam-massage/"
ENMAP = {v: k for k, v in NLMAP.items()}

# key: (en, nl); each = (title, h1, lead, description, blocks, faq, faq title, cta text, service type, photo)
EXTRA_PAGES = {
    "/lingam-massage/": (
        ("Lingam Massage Amsterdam | Tantric Massage at Your Hotel", "Lingam Massage Amsterdam",
         "A slow tantric massage for men, given at your hotel or home in Amsterdam.",
         "Lingam massage in Amsterdam at your hotel or home. A slow tantric massage for men by a masseuse you choose, with full attention and without hurry. Booked by chat.",
         [("What is a lingam massage?", ["Lingam is the Sanskrit word for the male sex organ, and in the tantra tradition it is treated with attention and respect. A lingam massage is a slow, deliberate massage of the lingam and the area around it, as part of a massage of the whole body.",
                                        "The goal is not to reach a climax as quickly as possible. It is the opposite: your masseuse builds the tension slowly, lets it ebb and builds it again, so that the feeling spreads through your whole body."]),
          ("How does it go?", ["Your masseuse comes to your hotel or home. After a warm shower the massage starts with your back, legs and shoulders, with warm oil and long strokes, so your body can let go of the day.",
                               "Only when you are fully relaxed does she turn to the lingam massage itself: slow, varied and attentive, with pauses in which you simply breathe. The massage ends with a happy ending, at a moment that you both feel is right."]),
          ("Lingam, tantra or happy ending?", ["A tantra massage is a ritual for the whole body, in which breathing and energy are central. A lingam massage comes from the same tradition, but gives the lingam the leading role. A happy ending is the release at the end of any of our erotic massages. If you want the longest and slowest build-up, a lingam massage is the one to choose."]),
          ("For whom?", ["For men who want more than a quick release, and who are curious what happens when there is no hurry. It is also a good choice if you find it hard to switch off: the slow pace does that for you. Book at least an hour, and preferably longer."])],
         [("What does lingam mean?", "Lingam is the Sanskrit word for the male sex organ. In tantra it is approached with attention and respect."),
          ("What is the difference between a lingam massage and a happy ending?", "A happy ending is the release at the end of a massage. In a lingam massage the slow build-up is the massage itself, and the release comes at the very end."),
          ("How long does a lingam massage take?", "Book at least one hour. With ninety minutes or two hours there is more time for the full body massage beforehand and for a slower build-up."),
          ("How much is a lingam massage in Amsterdam?", "In Amsterdam the rate is € 160 per hour and every extra hour is € 160. For other locations see the prices page.")],
         "Questions about lingam massage", "Book your lingam massage in the chat. We confirm masseuse, time and rate before anything is final.", "Lingam massage", "tantra-massage-amsterdam"),
        ("Lingam Massage Amsterdam | Tantrische Massage in uw Hotel", "Lingam massage Amsterdam",
         "Een trage tantrische massage voor mannen, bij u in het hotel of thuis in Amsterdam.",
         "Lingam massage in Amsterdam, in uw hotel of thuis. Een trage tantrische massage voor mannen door een masseuse naar keuze, met volle aandacht en zonder haast.",
         [("Wat is een lingam massage?", ["Lingam is het Sanskriet voor het mannelijk geslachtsdeel, en in de tantratraditie wordt het met aandacht en respect benaderd. Een lingam massage is een trage, bewuste massage van de lingam en het gebied eromheen, als onderdeel van een massage van het hele lichaam.",
                                         "Het doel is niet om zo snel mogelijk een hoogtepunt te bereiken. Het is juist andersom: uw masseuse bouwt de spanning langzaam op, laat haar zakken en bouwt haar opnieuw op, zodat het gevoel zich door uw hele lichaam verspreidt."]),
          ("Hoe verloopt het?", ["Uw masseuse komt naar uw hotel of naar u thuis. Na een warme douche begint de massage bij uw rug, benen en schouders, met warme olie en lange strijkingen, zodat uw lichaam de dag kan loslaten.",
                                 "Pas als u volledig ontspannen bent, gaat zij over op de lingam massage zelf: traag, afwisselend en aandachtig, met pauzes waarin u alleen maar ademt. De massage eindigt met een happy ending, op een moment dat voor u beiden goed voelt."]),
          ("Lingam, tantra of happy ending?", ["Een tantra massage is een ritueel voor het hele lichaam, waarin ademhaling en energie centraal staan. Een lingam massage komt uit dezelfde traditie, maar geeft de lingam de hoofdrol. Een happy ending is de ontlading aan het einde van elk van onze erotische massages. Wilt u de langste en traagste opbouw, kies dan voor een lingam massage."]),
          ("Voor wie?", ["Voor mannen die meer willen dan een snelle ontlading en die benieuwd zijn wat er gebeurt als er geen haast is. Het is ook een goede keuze als u moeilijk kunt afschakelen: het trage tempo doet dat voor u. Boek minimaal een uur, en liever langer."])],
         [("Wat betekent lingam?", "Lingam is het Sanskriet voor het mannelijk geslachtsdeel. In tantra wordt het met aandacht en respect benaderd."),
          ("Wat is het verschil tussen een lingam massage en een happy ending?", "Een happy ending is de ontlading aan het einde van een massage. Bij een lingam massage is de trage opbouw de massage zelf, en komt de ontlading helemaal aan het eind."),
          ("Hoe lang duurt een lingam massage?", "Boek minimaal een uur. Met anderhalf of twee uur is er meer tijd voor de massage van het hele lichaam vooraf en voor een tragere opbouw."),
          ("Wat kost een lingam massage in Amsterdam?", "In Amsterdam is het tarief € 160 per uur en elk extra uur is € 160. Voor andere locaties zie de prijzenpagina.")],
         "Vragen over lingam massage", "Boek uw lingam massage in de chat. Wij bevestigen masseuse, tijd en tarief voordat iets definitief is.", "Lingam massage", "tantra-massage-amsterdam"),
    ),
    "/erotic-massage-for-women/": (
        ("Erotic Massage for Women Amsterdam | At Your Hotel or Home", "Erotic Massage for Women in Amsterdam",
         "A sensual massage for women, by a masseuse who comes to your hotel or home.",
         "Erotic massage for women in Amsterdam at your hotel or home. A slow, sensual massage by a masseuse you choose, at your own pace. Discreet, booked by chat.",
         [("An erotic massage for women", ["Erotic massage is not only for men. Women book with us too, on their own or together with a partner. Your masseuse comes to your hotel or home in Amsterdam and the surrounding area, so you are in a place where you feel at ease.",
                                          "Tell us in the chat that the booking is for a woman. We let you know which masseuses are available for you, and you choose."]),
          ("At your own pace", ["The massage starts with your back, shoulders and legs, with warm oil and slow strokes. From there it follows what you like. You decide how sensual the massage becomes and where the boundaries are, and you can say so at any moment.",
                               "If this is your first erotic massage, a sensual massage is a good place to start. Have you done this before and do you want more closeness, then choose a body to body or tantra massage."]),
          ("What do you need?", ["A made bed with a large towel on it and a shower. Your masseuse brings the oil. Everything else is arranged in the chat beforehand, so there are no surprises."]),
          ("Booking and price", ["Open the chat and tell us your hotel or address, the time you prefer and what you have in mind. " + HOURS_EN + " The rates per location are on the prices page, and we confirm your rate before you book."])],
         [("Can women book an erotic massage with you?", "Yes. Women can book an erotic massage at their hotel or home. Tell us in the chat that the booking is for a woman, and we let you know which masseuses are available."),
          ("Is the massage given by a woman?", "Yes. All our masseuses are women."),
          ("Who decides how far the massage goes?", "You do. You tell your masseuse what you like and what you do not want, before and during the massage."),
          ("Can I book together with my partner?", "Yes. For a massage for two, see our couples massage.")],
         "Questions about erotic massage for women", "Book your massage in the chat. Tell us it is for a woman and we do the rest.", "Erotic massage for women", "sensual-erotic-massage"),
        ("Erotische Massage voor Vrouwen | Bij u Thuis of in uw Hotel", "Erotische massage voor vrouwen",
         "Een sensuele massage voor vrouwen, door een masseuse die naar uw hotel of naar u thuis komt.",
         "Erotische massage voor vrouwen in Amsterdam en omgeving, bij u thuis of in uw hotel. Een trage, sensuele massage door een masseuse naar keuze, in uw eigen tempo.",
         [("Een erotische massage voor vrouwen", ["Een erotische massage is er niet alleen voor mannen. Ook vrouwen boeken bij ons, alleen of samen met een partner. Uw masseuse komt naar uw hotel of naar u thuis in Amsterdam en omgeving, zodat u op een plek bent waar u zich op uw gemak voelt.",
                                                 "Geef in de chat aan dat de boeking voor een vrouw is. Wij laten u weten welke masseuses voor u beschikbaar zijn, en u kiest."]),
          ("In uw eigen tempo", ["De massage begint bij uw rug, schouders en benen, met warme olie en trage strijkingen. Daarna volgt de massage wat u prettig vindt. U bepaalt hoe sensueel de massage wordt en waar de grenzen liggen, en dat kunt u op elk moment aangeven.",
                                "Is dit uw eerste erotische massage, dan is een sensuele massage een goed begin. Heeft u dit vaker gedaan en wilt u meer nabijheid, kies dan voor een body to body of tantra massage."]),
          ("Wat heeft u nodig?", ["Een opgemaakt bed met een grote handdoek erop en een douche. Uw masseuse neemt de olie mee. Al het andere wordt vooraf in de chat afgesproken, zodat er geen verrassingen zijn."]),
          ("Boeken en prijs", ["Open de chat en vertel ons uw hotel of adres, het gewenste tijdstip en wat u in gedachten heeft. " + HOURS_NL + " De tarieven per locatie staan op de prijzenpagina, en wij bevestigen uw tarief voordat u boekt."])],
         [("Kunnen vrouwen bij jullie een erotische massage boeken?", "Ja. Vrouwen kunnen een erotische massage boeken in hun hotel of thuis. Geef in de chat aan dat de boeking voor een vrouw is, dan laten wij weten welke masseuses beschikbaar zijn."),
          ("Wordt de massage door een vrouw gegeven?", "Ja. Al onze masseuses zijn vrouwen."),
          ("Wie bepaalt hoe ver de massage gaat?", "U. U vertelt uw masseuse wat u prettig vindt en wat u niet wilt, voor en tijdens de massage."),
          ("Kan ik samen met mijn partner boeken?", "Ja. Voor een massage voor twee leest u meer bij onze massage voor koppels.")],
         "Vragen over erotische massage voor vrouwen", "Boek uw massage in de chat. Geef aan dat het voor een vrouw is en wij regelen de rest.", "Erotische massage voor vrouwen", "sensual-erotic-massage"),
    ),
    "/outcall-massage-amsterdam/": (
        ("Outcall Massage Amsterdam | Your Masseuse Comes to You", "Outcall Massage Amsterdam",
         "We have no salon. Your masseuse comes to your hotel room, apartment or home.",
         "Outcall massage in Amsterdam: your masseuse comes to your hotel, apartment or home. Open daily from 16:00 to 05:00, Friday and Saturday until 06:00. Booked by chat.",
         [("What is an outcall massage?", ["With an outcall massage you do not travel to a salon: the masseuse travels to you. That is the only way we work. You stay in your hotel room or at home, and she arrives at the time you agreed in the chat.",
                                          "It saves you a trip through the city, and afterwards you do not have to go anywhere. You can stay where you are, relaxed."]),
          ("Where do we come?", ["Amsterdam is our home base. We also visit Schiphol, Amstelveen, Haarlem, Hoofddorp and many other places around the city, and for longer bookings also cities further away. Every location with its rate is on the locations page."]),
          ("When can you book?", [HOURS_EN + " In Amsterdam your masseuse can be with you within 45 minutes, outside Amsterdam within an hour. For Eindhoven and Maastricht we agree the time with you. If you have a favourite masseuse or a fixed time in mind, book earlier."]),
          ("What do you need?", ["A made bed with a large towel on it and a shower for before and after. Your masseuse brings the oil. If you are staying in a hotel, give us your room number once the booking is confirmed."])],
         [("Do you have a salon in Amsterdam?", "No. We only do outcall: your masseuse comes to your hotel, apartment or home."),
          ("What are your opening hours?", HOURS_EN),
          ("How much is an outcall massage in Amsterdam?", "In Amsterdam the rate is € 160 per hour and every extra hour is € 160. For other locations see the prices page."),
          ("Which areas do you visit?", "Amsterdam and the surrounding area, including Schiphol, Amstelveen, Haarlem and Hoofddorp, and for longer bookings cities further away. See the locations page.")],
         "Questions about outcall massage", "Tell us your hotel or address and the time you prefer in the chat.", "Outcall erotic massage", "erotic-massage-at-your-hotel"),
        ("Erotische Massage aan Huis | Uw Masseuse Komt naar u Toe", "Erotische massage aan huis",
         "Wij hebben geen salon. Uw masseuse komt naar u thuis, naar uw appartement of naar uw hotelkamer.",
         "Erotische massage aan huis in Amsterdam en omgeving: uw masseuse komt naar u thuis of naar uw hotel. Dagelijks 16:00 tot 05:00 uur, vrijdag en zaterdag tot 06:00.",
         [("Wat is een erotische massage aan huis?", ["Bij een massage aan huis gaat u niet naar een salon: de masseuse komt naar u toe. Dat is de enige manier waarop wij werken. U blijft thuis of in uw hotelkamer, en zij komt op het tijdstip dat u in de chat heeft afgesproken.",
                                                      "U hoeft de stad niet door, en na afloop hoeft u nergens meer heen. U kunt ontspannen blijven waar u bent."]),
          ("Waar komen wij?", ["Amsterdam is onze thuisbasis. Wij komen ook in Schiphol, Amstelveen, Haarlem, Hoofddorp en veel andere plaatsen rond de stad, en voor langere boekingen ook in steden die verder weg liggen. Alle locaties met hun tarief staan op de locatiepagina."]),
          ("Wanneer kunt u boeken?", [HOURS_NL + " In Amsterdam kan uw masseuse binnen 45 minuten bij u zijn, buiten Amsterdam binnen een uur. Voor Eindhoven en Maastricht spreken wij de tijd in overleg af. Heeft u een favoriete masseuse of een vast tijdstip in gedachten, boek dan eerder."]),
          ("Wat heeft u nodig?", ["Een opgemaakt bed met een grote handdoek erop en een douche voor vooraf en achteraf. Uw masseuse neemt de olie mee. Verblijft u in een hotel, geef dan uw kamernummer door zodra de boeking is bevestigd."])],
         [("Hebben jullie een salon in Amsterdam?", "Nee. Wij werken alleen op locatie: uw masseuse komt naar u thuis, naar uw appartement of naar uw hotel."),
          ("Wat zijn jullie openingstijden?", HOURS_NL),
          ("Wat kost een erotische massage aan huis in Amsterdam?", "In Amsterdam is het tarief € 160 per uur en elk extra uur is € 160. Voor andere locaties zie de prijzenpagina."),
          ("In welke plaatsen komen jullie?", "In Amsterdam en omgeving, waaronder Schiphol, Amstelveen, Haarlem en Hoofddorp, en voor langere boekingen ook in steden verder weg. Zie de locatiepagina.")],
         "Vragen over massage aan huis", "Geef in de chat uw adres of hotel en het gewenste tijdstip door.", "Erotische massage aan huis", "erotic-massage-at-your-hotel"),
    ),
}


def extra_pages():
    global L
    urls = []
    for en_path, pair in EXTRA_PAGES.items():
        for lang, data in zip(("en", "nl"), pair):
            L = lang
            nl = lang == "nl"
            t, h1, lead, d, blocks, faq, ftitle, ctat, stype, photo_name = data
            fh, fs = faq_block(faq, ftitle)
            ms = MASSAGES_NL if nl else MASSAGES
            ml = "".join(f'<li><a href="{P(f"/{s}/")}">{E(n)}</a></li>' for s, n, _ in ms) + (
                f'<li><a href="{P("/happy-ending-massage/")}">Happy ending massage</a></li><li><a href="{P("/nuru-massage/")}">Nuru massage</a></li><li><a href="{P("/lingam-massage/")}">Lingam massage</a></li>')
            more = [(P("/prices/"), "Prijzen" if nl else "Prices"), (P("/other-cities/"), "Locaties" if nl else "Locations"),
                    (P("/bookings/"), "Boeken" if nl else "Bookings"),
                    ("/nl/pakketten/couples-massage/" if nl else "/packages/couples-massage/", "Massage voor koppels" if nl else "Couples massage")]
            other = [p for p in EXTRA_PAGES if p != en_path]
            more += [(P(p), EXTRA_PAGES[p][1 if nl else 0][1]) for p in other]
            inner = (f'<section class="sec"><div class="wrap narrow prose"><figure class="fig">{pic(photo_name, h1, 600, 400, eager=True)}</figure>{prose(blocks)}</div></section>'
                     f'{cta(ctat)}{fh}'
                     f'<section class="sec"><div class="wrap">{link_row("Meer informatie" if nl else "More information", more).replace(chr(32) + "class=" + chr(34) + "mt" + chr(34), "")}'
                     f'<h2 class="mt">{"Onze massages" if nl else "Our massages"}</h2><ul class="chips">{ml}</ul>'
                     f'<h2 class="mt">{"Kies uw masseuse" if nl else "Choose your masseuse"}</h2><ul class="cards">{"".join(card(m) for m in MASSEUSES[:10])}</ul>'
                     f'<p class="center"><a class="link" href="{P("/our-masseuses/")}">{"Bekijk alle masseuses" if nl else "View all masseuses"}</a></p></div></section>')
            path = P(en_path)
            svc = {"@context": "https://schema.org", "@type": "Service", "name": h1, "serviceType": stype, "description": d, "provider": {"@id": SITE + "/#org"},
                   "areaServed": {"@type": "City", "name": "Amsterdam"}, "url": SITE + path}
            urls.append(sub(path, t, d, h1, lead, inner, [("Massages" if nl else "Services", P("/services/"))], [svc, fs]))
    L = "en"
    return urls
