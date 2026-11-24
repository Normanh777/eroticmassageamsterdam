# About, privacy and terms pages in both languages. Executed inside build.py's namespace after nl2.py.
LICENCE = "D18.000305"
NLMAP.update({"/about/": "/nl/over-ons/", "/privacy/": "/nl/privacy/", "/terms/": "/nl/voorwaarden/"})
ENMAP = {v: k for k, v in NLMAP.items()}


def legal_pages():
    global L
    urls = []
    ncity = len(set(p[0] for p in PRICES) | set(n for _, n in CITIES))
    doc = lambda blocks: '<section class="sec"><div class="wrap narrow prose">' + "".join(
        f"<h2>{E(h)}</h2>" + "".join(x if x.startswith("<") else f"<p>{x}</p>" for x in ps) for h, ps in blocks) + "</div></section>"
    for lang in ("en", "nl"):
        L = lang
        nl = lang == "nl"
        if not nl:
            about = [("Who we are", ["Erotic Massage Amsterdam is a licensed outcall massage service based in Amsterdam. Our masseuses do not receive guests at a salon: they come to you, at your hotel or at your home.",
                                     f"We work under licence number {LICENCE}."]),
                     ("What we do", [f"You can choose from {len(MASSEUSES)} masseuses and from eight erotic massages, from a <a href=\"/sensual-massage/\">sensual massage</a> and a <a href=\"/tantra-massage/\">tantra massage</a> to a <a href=\"/body-2-body-massage/\">body to body massage</a> and a <a href=\"/nuru-massage/\">nuru massage</a>. We also offer <a href=\"/packages/\">packages</a> that combine a massage with a dinner, a tour of the city or a second masseuse.",
                                     f"Amsterdam is our home base. We also visit Schiphol and {ncity - 1} other cities and towns; you find them all on the <a href=\"/prices/\">prices</a> page."]),
                     ("How we work", ["Everything is arranged by chat: live chat, WhatsApp or Telegram. You tell us where you are staying, when you would like your massage and which masseuse you prefer. We confirm the masseuse, the time and the rate before anything is final, so there are no surprises.",
                                      "Discretion is where every booking starts. Your details are used only to arrange your appointment. You can read exactly how we handle them in our <a href=\"/privacy/\">privacy statement</a>."]),
                     ("For adults only", ["Our service is intended for adults aged 18 and over. All our masseuses are adults, and they treat every guest with respect. We expect the same in return."])]
            privacy = [("Who is responsible", [f"This website is run by Erotic Massage Amsterdam, licence number {LICENCE}. For any question about your personal data you can reach us through the chat on this website."]),
                       ("Which data we process", ["We only process the data you give us yourself when you contact us or make a booking:",
                                                  '<ul class="ticks"><li>the name you use in the chat;</li><li>your phone number or username, if you contact us by WhatsApp or Telegram;</li><li>the hotel and room number or the address where the massage takes place;</li><li>the date, time and details of your booking;</li><li>the content of your messages.</li></ul>',
                                                  "This website has no contact forms and no customer accounts."]),
                       ("Why we process it", ["We use your data for one purpose: to answer your question and to arrange and carry out your appointment. We do not use it for advertising and we do not sell or rent it to anyone."]),
                       ("Chat and other services", ["The chat on this website is provided by Gleap. When you open the chat, Gleap processes your messages and technical data such as your browser type on our behalf, and it may store a small file in your browser to recognise your conversation.",
                                                    "If you choose WhatsApp or Telegram, your conversation takes place in that app and their own privacy policies apply. The website itself is hosted by Hostinger, which keeps standard server logs to keep the site secure."]),
                       ("Cookies", ["This website does not use advertising or tracking cookies. Only when you open the chat is a functional file stored that the chat needs to work."]),
                       ("How long we keep it", ["We keep your data no longer than is necessary to arrange your appointment and to meet our legal obligations."]),
                       ("Your rights", ["You have the right to see which data we hold about you, to have it corrected or deleted, and to object to its use. Send us a message in the chat and we will deal with your request. If you are not satisfied, you can file a complaint with the Dutch Data Protection Authority (Autoriteit Persoonsgegevens)."]),
                       ("Changes", [f"We may update this privacy statement. This version was last updated on {date.today().strftime('%d %B %Y')}."])]
            terms = [("Who we are", [f"These terms apply to all bookings with Erotic Massage Amsterdam, licence number {LICENCE}."]),
                     ("Adults only", ["Our service is only for adults aged 18 and over. By booking you confirm that you are 18 or older."]),
                     ("Bookings", ["A booking is made through the chat. It is final once we have confirmed the masseuse, the date and time, the location and the rate to you."]),
                     ("Rates and payment", ["The rates are listed on the <a href=\"/prices/\">prices</a> page and depend on the location. Your rate is always confirmed before you book. For packages, costs such as dinner, drinks, champagne and tickets are paid by you."]),
                     ("Changing or cancelling", ["If you need to change or cancel your booking, let us know in the chat as early as possible, so that we can inform your masseuse."]),
                     ("Respect and safety", ["Our masseuses treat every guest with respect and expect the same in return. A masseuse may end an appointment if a guest behaves disrespectfully or if she does not feel safe."]),
                     ("Privacy", ["We handle your details as described in our <a href=\"/privacy/\">privacy statement</a>."])]
            pages = [("/about/", "About Us | Licensed Outcall Massage Service in Amsterdam", "About Erotic Massage Amsterdam: a licensed outcall massage service. Our masseuses visit you at your hotel or home in Amsterdam and beyond.", "About us", "A licensed outcall massage service from Amsterdam.", about, True),
                     ("/privacy/", "Privacy Statement | Erotic Massage Amsterdam", "Privacy statement of Erotic Massage Amsterdam: which personal data we process when you chat or book, why, and what your rights are.", "Privacy statement", "How we handle your personal data.", privacy, False),
                     ("/terms/", "Terms and Conditions | Erotic Massage Amsterdam", "Terms and conditions of Erotic Massage Amsterdam: bookings, rates, changes and cancellations, and the rules for a respectful appointment.", "Terms and conditions", "The agreements that apply to every booking.", terms, False)]
        else:
            about = [("Wie wij zijn", ["Erotic Massage Amsterdam is een massageservice aan huis met vergunning, gevestigd in Amsterdam. Onze masseuses ontvangen geen gasten in een salon: zij komen naar u toe, in uw hotel of bij u thuis.",
                                       f"Wij werken onder licentienummer {LICENCE}."]),
                     ("Wat wij doen", [f"U kunt kiezen uit {len(MASSEUSES)} masseuses en uit acht erotische massages, van een <a href=\"/nl/sensuele-massage/\">sensuele massage</a> en een <a href=\"/nl/tantra-massage/\">tantra massage</a> tot een <a href=\"/nl/body-to-body-massage/\">body to body massage</a> en een <a href=\"/nl/nuru-massage/\">nuru massage</a>. Daarnaast bieden wij <a href=\"/nl/pakketten/\">pakketten</a> waarin u een massage combineert met een diner, een stadstour of een tweede masseuse.",
                                       f"Amsterdam is onze thuisbasis. Wij komen ook op Schiphol en in {ncity - 1} andere steden en dorpen; u vindt ze allemaal op de pagina <a href=\"/nl/prijzen/\">prijzen</a>."]),
                     ("Hoe wij werken", ["Alles wordt geregeld via de chat: live chat, WhatsApp of Telegram. U vertelt ons waar u verblijft, wanneer u uw massage wilt en welke masseuse uw voorkeur heeft. Wij bevestigen de masseuse, het tijdstip en het tarief voordat iets definitief is, zodat u niet voor verrassingen komt te staan.",
                                         "Discretie is het uitgangspunt van elke boeking. Uw gegevens worden alleen gebruikt om uw afspraak te regelen. Hoe wij daarmee omgaan leest u in onze <a href=\"/nl/privacy/\">privacyverklaring</a>."]),
                     ("Alleen voor volwassenen", ["Onze service is bedoeld voor volwassenen van 18 jaar en ouder. Al onze masseuses zijn volwassen, en zij behandelen elke gast met respect. Wij verwachten hetzelfde terug."])]
            privacy = [("Wie is verantwoordelijk", [f"Deze website is van Erotic Massage Amsterdam, licentienummer {LICENCE}. Met vragen over uw persoonsgegevens kunt u ons bereiken via de chat op deze website."]),
                       ("Welke gegevens wij verwerken", ["Wij verwerken alleen de gegevens die u zelf aan ons geeft wanneer u contact opneemt of boekt:",
                                                        '<ul class="ticks"><li>de naam die u in de chat gebruikt;</li><li>uw telefoonnummer of gebruikersnaam, als u via WhatsApp of Telegram contact opneemt;</li><li>het hotel en kamernummer of het adres waar de massage plaatsvindt;</li><li>de datum, het tijdstip en de details van uw boeking;</li><li>de inhoud van uw berichten.</li></ul>',
                                                        "Deze website heeft geen contactformulieren en geen klantaccounts."]),
                       ("Waarom wij ze verwerken", ["Wij gebruiken uw gegevens voor één doel: uw vraag beantwoorden en uw afspraak regelen en uitvoeren. Wij gebruiken ze niet voor reclame en verkopen of verhuren ze aan niemand."]),
                       ("Chat en andere diensten", ["De chat op deze website wordt geleverd door Gleap. Wanneer u de chat opent, verwerkt Gleap in onze opdracht uw berichten en technische gegevens zoals uw browsertype, en kan er een klein bestand in uw browser worden opgeslagen om uw gesprek te herkennen.",
                                                    "Kiest u voor WhatsApp of Telegram, dan verloopt uw gesprek in die app en geldt hun eigen privacybeleid. De website zelf wordt gehost door Hostinger, dat standaard serverlogs bijhoudt om de site veilig te houden."]),
                       ("Cookies", ["Deze website gebruikt geen advertentie- of trackingcookies. Alleen wanneer u de chat opent, wordt een functioneel bestand opgeslagen dat de chat nodig heeft om te werken."]),
                       ("Hoe lang wij ze bewaren", ["Wij bewaren uw gegevens niet langer dan nodig is om uw afspraak te regelen en om aan onze wettelijke verplichtingen te voldoen."]),
                       ("Uw rechten", ["U heeft het recht om in te zien welke gegevens wij van u hebben, deze te laten corrigeren of verwijderen en bezwaar te maken tegen het gebruik ervan. Stuur ons een bericht in de chat en wij handelen uw verzoek af. Bent u niet tevreden, dan kunt u een klacht indienen bij de Autoriteit Persoonsgegevens."]),
                       ("Wijzigingen", [f"Wij kunnen deze privacyverklaring aanpassen. Deze versie is voor het laatst bijgewerkt op {date.today().strftime('%d-%m-%Y')}."])]
            terms = [("Wie wij zijn", [f"Deze voorwaarden gelden voor alle boekingen bij Erotic Massage Amsterdam, licentienummer {LICENCE}."]),
                     ("Alleen voor volwassenen", ["Onze service is uitsluitend voor volwassenen van 18 jaar en ouder. Door te boeken bevestigt u dat u 18 jaar of ouder bent."]),
                     ("Boekingen", ["Een boeking komt tot stand via de chat. De boeking is definitief zodra wij de masseuse, de datum en tijd, de locatie en het tarief aan u hebben bevestigd."]),
                     ("Tarieven en betaling", ["De tarieven staan op de pagina <a href=\"/nl/prijzen/\">prijzen</a> en hangen af van de locatie. Uw tarief wordt altijd bevestigd voordat u boekt. Bij pakketten betaalt u zelf kosten zoals diner, drankjes, champagne en tickets."]),
                     ("Wijzigen of annuleren", ["Wilt u uw boeking wijzigen of annuleren, laat het ons dan zo vroeg mogelijk weten in de chat, zodat wij uw masseuse kunnen informeren."]),
                     ("Respect en veiligheid", ["Onze masseuses behandelen elke gast met respect en verwachten hetzelfde terug. Een masseuse mag een afspraak beëindigen als een gast zich respectloos gedraagt of als zij zich niet veilig voelt."]),
                     ("Privacy", ["Wij gaan met uw gegevens om zoals beschreven in onze <a href=\"/nl/privacy/\">privacyverklaring</a>."])]
            pages = [("/nl/over-ons/", "Over Ons | Massageservice aan Huis met Vergunning", "Over Erotic Massage Amsterdam: een massageservice aan huis met vergunning. Onze masseuses bezoeken u in uw hotel of thuis in Amsterdam en omgeving.", "Over ons", "Een massageservice aan huis met vergunning, vanuit Amsterdam.", about, True),
                     ("/nl/privacy/", "Privacyverklaring | Erotic Massage Amsterdam", "Privacyverklaring van Erotic Massage Amsterdam: welke persoonsgegevens wij verwerken als u chat of boekt, waarom, en wat uw rechten zijn.", "Privacyverklaring", "Hoe wij met uw persoonsgegevens omgaan.", privacy, False),
                     ("/nl/voorwaarden/", "Algemene Voorwaarden | Erotic Massage Amsterdam", "Algemene voorwaarden van Erotic Massage Amsterdam: boekingen, tarieven, wijzigen en annuleren, en de regels voor een respectvolle afspraak.", "Algemene voorwaarden", "De afspraken die voor elke boeking gelden.", terms, False)]
        for path, t, d, h1, lead, blocks, with_cta in pages:
            inner = doc(blocks) + (cta() if with_cta else "")
            urls.append(sub(path, t, d, h1, lead, inner, []))
    L = "en"
    return urls
