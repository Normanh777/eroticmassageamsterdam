# Extra landing pages (EN + NL): massage for women, outcall / aan huis. Executed inside build.py's namespace.
NLMAP["/erotic-massage-for-women/"] = "/nl/erotische-massage-voor-vrouwen/"
NLMAP["/outcall-massage-amsterdam/"] = "/nl/erotische-massage-aan-huis/"
ENMAP = {v: k for k, v in NLMAP.items()}

# key: (en, nl); each = (title, h1, lead, description, blocks, faq, faq title, cta text, service type, photo)
EXTRA_PAGES = {
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
                f'<li><a href="{P("/happy-ending-massage/")}">Happy ending massage</a></li><li><a href="{P("/nuru-massage/")}">Nuru massage</a></li>')
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
