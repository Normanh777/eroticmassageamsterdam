# --- sub pages (spliced into build.py before build()) ---

PRICES = [  # location, price label, extra hour
    ("Amsterdam", "€ 160", "€ 160"), ("Schiphol", "€ 160", "€ 160"), ("Haarlem", "€ 160", "€ 160"),
    ("Hoofddorp", "€ 160", "€ 160"), ("Leiden", "€ 200", "€ 160"), ("Utrecht", "€ 200", "€ 160"),
    ("Vianen", "€ 200", "€ 160"), ("Rotterdam", "2 hours € 350", "€ 160"), ("Den Haag", "2 hours € 350", "€ 160"),
    ("Eindhoven", "3 hours € 600", "€ 160"), ("Delft", "2 hours € 350", "€ 160"), ("Zandvoort", "€ 180", "€ 160"),
    ("Hilversum", "€ 180", "€ 160"), ("Heemskerk", "€ 180", "€ 160"), ("Maastricht", "6 hours € 1200", "€ 160"),
]
PRICE_OF = {p[0]: p[1] for p in PRICES}
CITY_SLUG = {n: s for s, n in CITIES}

TAGS = {"vicky": ["mysterious", "passionate"], "bianca": ["romantic", "playful"], "olga": ["natural", "passionate"],
        "lavinia": ["natural"], "miki": ["passionate"], "brianna": ["passionate"]}
EXTRA = {"alexandra": {"Height": "168 cm", "Hair": "Brunette", "Eyes": "Brown"}}

MASSAGE_TEXT = {
    "sensual-massage": {
        "lead": "A slow, attentive massage with warm oil, given at your hotel or home in Amsterdam.",
        "desc": "Sensual massage in Amsterdam at your hotel or home. Slow, flowing strokes with warm oil by a masseuse you choose. Discreet outcall service, booked by chat.",
        "body": [
            ("What is a sensual massage?", ["A sensual massage is all about pace and attention. Your masseuse works with long, flowing strokes and warm oil, from your shoulders and back down to your legs and feet, without ever rushing. The aim is not to work out a knot in a muscle, but to let your whole body switch off.",
                                             "There is no routine to follow and nothing you need to know in advance. You lie down, you breathe out, and she takes it from there."]),
            ("What to expect", ["Your masseuse comes to you, so the massage takes place in your own hotel room or at home. A freshly made bed or a large towel on the bed is all the preparation that is needed.",
                                "The massage builds up gradually. It starts as a relaxing full body massage and becomes lighter, slower and more teasing as you relax. You are always free to say what you like and what you would rather skip."]),
            ("Who is it for?", ["For travellers who have spent the day in meetings or on their feet in the city, for anyone who sleeps badly in hotels, and for anyone who simply wants an hour of undivided attention. A sensual massage is also a good choice if this is your first erotic massage."]),
        ]},
    "tantra-massage": {
        "lead": "A mindful full-body ritual in which breathing, presence and slow touch build up energy step by step.",
        "desc": "Tantra massage in Amsterdam at your hotel or home. A mindful full-body ritual with slow touch and breathing. Selected masseuses, discreet outcall, booked by chat.",
        "body": [
            ("What is a tantra massage?", ["Tantra massage comes from a tradition in which touch is used to build up energy instead of releasing it as quickly as possible. Compared with other erotic massages it is slower, quieter and more deliberate. Breathing plays a real part: your masseuse will invite you to breathe deeply and to stay with what you feel.",
                                            "Because nothing is hurried, sensations become stronger than you may be used to. Many guests describe it as being relaxed and wide awake at the same time."]),
            ("What to expect", ["The massage starts with calm, grounding strokes over the back of your body. Only when you are fully relaxed does the touch become lighter and more sensual. The whole body is included, and the build-up is gradual from beginning to end.",
                                "A tantra massage works best when there is enough time. If you can, book longer than one hour; every extra hour is charged at the extra hour rate on our prices page."]),
            ("Good to know", ["You do not need any experience with tantra or meditation. A quiet room, a shower beforehand and a phone on silent are the only things that help."]),
        ]},
    "body-2-body-massage": {
        "lead": "Skin to skin with warm oil: your masseuse uses her whole body to massage yours.",
        "desc": "Body 2 body massage in Amsterdam at your hotel or home. Skin to skin with warm oil, by a masseuse you choose. Discreet outcall service, booked by chat.",
        "body": [
            ("What is a body 2 body massage?", ["In a body 2 body massage, also written as body to body or B2B massage, your masseuse does not only use her hands. With plenty of warm oil she glides over you with her arms, legs and upper body, so that you feel her whole body against yours.",
                                                 "It is the most intimate massage we offer. The constant, sliding contact makes it very hard to keep thinking about anything else."]),
            ("What to expect", ["The massage usually begins with a short hand massage to warm up your muscles and spread the oil. After that the body to body part starts, first on your back and then on your front.",
                                "Because a lot of oil is used, we advise putting one or two large towels on the bed. A shower before and after is part of the experience, so a room with a good shower is ideal."]),
            ("Combine it", ["A body 2 body massage combines well with a sensual massage in a two hour booking, or with a second masseuse in a 4 hands massage. Tell us in the chat what you have in mind."]),
        ]},
    "4-hands-massage": {
        "lead": "Two masseuses, four hands and one rhythm. Double the attention from start to finish.",
        "desc": "4 hands massage in Amsterdam at your hotel or home. Two masseuses working in rhythm for double the attention. Discreet outcall service, booked by chat.",
        "body": [
            ("What is a 4 hands massage?", ["In a 4 hands massage two masseuses massage you at the same time. Sometimes they mirror each other, one on each side of your body. Sometimes one works on your shoulders while the other takes care of your legs.",
                                             "The effect is surprising. With two hands your mind can still follow what is happening. With four it soon gives up, and that is exactly when you start to relax completely."]),
            ("What to expect", ["Both masseuses arrive together at your hotel or home. The massage can be sensual, body 2 body or a mix of both; you decide together at the start.",
                                "A 4 hands massage means booking two masseuses for the same time, so the rate differs from a massage with one masseuse. Ask for the rate in the chat and we confirm it before you book."]),
            ("Booking tip", ["Not every combination of masseuses is available at every moment. If you would like two specific masseuses, mention both names and book a little ahead."]),
        ]},
    "thai-massage": {
        "lead": "Stretching and firm pressure to release tension, finished with a soft, sensual touch.",
        "desc": "Thai massage in Amsterdam at your hotel or home. Stretching and pressure techniques with a sensual finish. Selected masseuses, discreet outcall, booked by chat.",
        "body": [
            ("What is a Thai massage?", ["Traditional Thai massage works with pressure along the muscles and with gentle stretches. Where a sensual massage is light and flowing, a Thai massage is firmer. It is the right choice when your back, neck or legs are stiff from a flight, a long drive or days of walking through the city.",
                                          "With us, the firm part is followed by a softer part with oil. First the tension goes, then the sensual massage begins."]),
            ("What to expect", ["Your masseuse starts at your feet and legs and works her way up, using her palms, thumbs and forearms. You can always ask for more or less pressure.",
                                "In the second half the tempo drops and the touch becomes slow and teasing."]),
            ("Good to know", ["Tell your masseuse beforehand about any injuries or sensitive spots. She will adapt the stretches or leave them out."]),
        ]},
    "full-body-massage": {
        "lead": "A complete massage from your shoulders to your feet, at your hotel or home.",
        "desc": "Full body massage in Amsterdam at your hotel or home. A complete massage from shoulders to feet by a masseuse you choose. Discreet outcall, booked by chat.",
        "body": [
            ("What is a full body massage?", ["A full body massage does what the name says: no part of your body is skipped. Neck, shoulders, back, arms, hands, legs and feet all get attention, with oil and at a calm pace.",
                                               "It is the most classic massage on our list and a good base for everything else. You can keep it purely relaxing, or let it turn into a sensual massage in the second half."]),
            ("What to expect", ["The massage starts on your back, where most people carry their tension, and then moves to your legs and feet. After you turn over, your masseuse continues with your arms, chest and legs.",
                                "One hour is enough for a complete massage. With two hours there is time to really take it slowly."]),
            ("Who is it for?", ["For anyone who has just landed, who has a busy week behind them, or who wants to end a day in Amsterdam in the most relaxed way possible."]),
        ]},
}

CITY_TEXT = {
    "Schiphol": ("Staying at an airport hotel before an early flight, or just landed after a long one? Our masseuses visit the hotels around Schiphol Airport. The airport lies just outside Amsterdam, so the journey is short.",
                 "An erotic massage is one of the best ways to shake off a flight. An hour of warm oil and slow hands does more for stiff shoulders and a busy head than another evening in the hotel bar."),
    "Hoofddorp": ("Hoofddorp sits right next to Schiphol and is full of business hotels. If you are staying here for work, a conference or a stopover, a massage is a good way to end the day.",
                  "Your masseuse comes to your hotel room or home address in Hoofddorp. You choose the massage and the masseuse, we take care of the planning."),
    "Haarlem": ("Haarlem is a historic city just west of Amsterdam, known for its old centre and the Grote Markt. Whether you live here or are staying in one of the city's hotels, our masseuses come to you.",
                "After a day in the city, or simply at home on a quiet evening, an erotic massage in Haarlem is easy to arrange. One message in the chat is enough."),
    "Zandvoort": ("Zandvoort is Amsterdam's beach town and home of the race circuit. In summer and on race weekends the hotels and apartments are full, so it pays to book ahead.",
                  "Imagine ending a day at the beach or the track with a sensual massage in your own room. Your masseuse travels from Amsterdam to Zandvoort and brings everything she needs."),
    "Hilversum": ("Hilversum lies in the green Gooi region, south-east of Amsterdam, and is best known as the media city of the Netherlands. Our masseuses visit hotels and private addresses in Hilversum and the surrounding villages.",
                  "Because the journey is a little longer than within Amsterdam, we recommend letting us know in good time when you would like your massage."),
    "Utrecht": ("Utrecht is in the very centre of the country, with its canals, the Dom tower and a large number of hotels around the station and the Jaarbeurs. Whether you are here for a trade fair, a conference or a city trip, our masseuses come to you.",
                "Your masseuse travels from Amsterdam to your hotel or home in Utrecht. Book ahead if you can, so that the masseuse of your choice is free at the time you prefer."),
    "Den Haag": ("Den Haag, The Hague, is the seat of the Dutch government and of many embassies and international organisations. With the beach of Scheveningen around the corner, it is a city where business and relaxation go together.",
                 "For Den Haag we work with a minimum booking of two hours, which gives you all the time you need for an unhurried massage without anyone watching the clock."),
    "Rotterdam": ("Rotterdam is the port city of the Netherlands, with a modern skyline and a lively hotel scene. Our masseuses visit hotels and private addresses throughout the city.",
                  "For Rotterdam we work with a minimum booking of two hours. That makes the trip worthwhile for your masseuse and gives you a long, relaxed session."),
    "Delft": ("Delft is a small historic university town between Den Haag and Rotterdam, famous for its canals and Delft Blue. It is a popular base for visitors who want to avoid the big cities.",
              "For Delft we work with a minimum booking of two hours. Your masseuse comes to your hotel, apartment or home."),
}


def img(m, cls="", eager=False, sizes="(max-width:40rem) 45vw, 400px"):
    slug, name = m[0], m[1]
    base = f"/images/masseuses/{slug}-erotic-massage-amsterdam"
    load = 'fetchpriority="high"' if eager else 'loading="lazy" decoding="async"'
    return (f'<img src="{base}.jpg" srcset="{base}-400.jpg 400w, {base}.jpg 800w" sizes="{sizes}" '
            f'alt="{E(name)}, erotic masseuse in Amsterdam" width="800" height="1000" {load}{" class=" + chr(34) + cls + chr(34) if cls else ""}>')


def card(m, eager=False):  # overrides the first version: local photos
    slug, name, age, langs, _ = m
    return (f'<li class="card"><a href="/dames/{slug}/">{img(m, eager=eager)}'
            f'<span class="card-b"><strong>{E(name)}</strong><span>{age} · {E(langs)}</span></span></a></li>')


def cta(text="Ready to book? Tell us your location, time and wishes in the chat.", label="Direct contact"):
    return f'<section class="sec sec-alt"><div class="wrap narrow center-box"><p class="cta-t">{E(text)}</p><p><a class="btn" href="/contact/" data-chat>{E(label)}</a> <a class="link" href="/prices/">See prices</a></p></div></section>'


def sub(path, title, desc, h1, lead, inner, trail, schema=None, og_image=None):
    """trail: [(name, path)] between Home and this page."""
    items = [("Home", "/")] + trail + [(h1, path)]
    nav = '<nav class="crumbs" aria-label="Breadcrumb"><ol>' + "".join(
        f'<li><a href="{p}">{E(n)}</a></li>' if i < len(items) - 1 else f'<li aria-current="page">{E(n)}</li>'
        for i, (n, p) in enumerate(items)) + "</ol></nav>"
    bc = {"@context": "https://schema.org", "@type": "BreadcrumbList", "itemListElement": [
        {"@type": "ListItem", "position": i + 1, "name": n, "item": SITE + p} for i, (n, p) in enumerate(items)]}
    wp = {"@context": "https://schema.org", "@type": "WebPage", "@id": SITE + path + "#webpage", "url": SITE + path,
          "name": title, "description": desc, "inLanguage": "en", "isPartOf": {"@id": SITE + "/#website"}, "dateModified": TODAY}
    body = f'<section class="phero"><div class="wrap">{nav}<h1>{E(h1)}</h1><p class="lead">{E(lead)}</p></div></section>\n{inner}'
    return page(path, title, desc, body, [ORG, WEBSITE, wp, bc] + (schema or []), og_image)


def prose(blocks):
    out = ""
    for h, paras in blocks:
        out += f"<h2>{E(h)}</h2>" + "".join(f"<p>{E(p)}</p>" for p in paras)
    return out


def price_table(rows):
    def loc(n):
        return f'<a href="/{CITY_SLUG[n]}/">{E(n)}</a>' if n in CITY_SLUG else E(n)
    return ('<div class="tbl"><table><caption class="vh">Rates per location</caption><thead><tr><th scope="col">Location</th>'
            '<th scope="col">Price</th><th scope="col">Extra hour</th></tr></thead><tbody>' + "".join(
                f'<tr><th scope="row">{loc(n)}</th><td>{E(p)}</td><td>{E(x)}</td></tr>' for n, p, x in rows) + "</tbody></table></div>")


def massage_pages():
    urls = []
    for slug, name, short in MASSAGES:
        t = MASSAGE_TEXT[slug]
        others = "".join(f'<li><a href="/{s}/">{E(n)}</a></li>' for s, n, _ in MASSAGES if s != slug)
        inner = (f'<section class="sec"><div class="wrap narrow prose">{prose(t["body"])}'
                 f'<h2>Price</h2><p>A {E(name.lower())} in Amsterdam, Schiphol, Haarlem or Hoofddorp is {PRICE_OF["Amsterdam"]}, and every extra hour is € 160. '
                 f'For other cities see our <a href="/prices/">prices</a>.</p></div></section>'
                 f'{cta(f"Book your {name.lower()} in the chat. We confirm masseuse, time and rate before anything is final.")}'
                 f'<section class="sec"><div class="wrap"><h2>Other massages</h2><ul class="chips">{others}<li><a href="/services/">All services</a></li></ul>'
                 f'<h2 class="mt">Choose your masseuse</h2><ul class="cards">{"".join(card(m) for m in MASSEUSES[:6])}</ul>'
                 f'<p class="center"><a class="link" href="/our-masseuses/">View all masseuses</a></p></div></section>')
        svc = {"@context": "https://schema.org", "@type": "Service", "name": f"{name} Amsterdam", "serviceType": name,
               "description": t["desc"], "provider": {"@id": SITE + "/#org"}, "areaServed": {"@type": "City", "name": "Amsterdam"},
               "url": f"{SITE}/{slug}/"}
        urls.append(sub(f"/{slug}/", f"{name} Amsterdam | Erotic Massage Amsterdam", t["desc"], f"{name} Amsterdam", t["lead"], inner,
                        [("Services", "/services/")], [svc]))
    tiles = "".join(f'<li><a class="tile" href="/{s}/"><h2>{E(n)}</h2><p>{E(d)}</p><span class="more">Read more</span></a></li>' for s, n, d in MASSAGES)
    inner = (f'<section class="sec"><div class="wrap"><ul class="tiles">{tiles}</ul></div></section>'
             '<section class="sec sec-alt"><div class="wrap narrow prose"><h2>One service, your way</h2>'
             '<p>Every massage on this page is an outcall massage: your masseuse comes to your hotel or home. You choose the massage and the masseuse, and you can combine massages in a longer booking.</p>'
             '<p>Not sure what suits you? Tell us in the chat what you enjoy, whether you prefer soft or firm, and how much time you have. We suggest a massage and a masseuse, and you decide.</p></div></section>'
             f'{cta()}')
    urls.append(sub("/services/", "Erotic Massage Services | Erotic Massage Amsterdam",
                    "All erotic massage services in Amsterdam: sensual, tantra, body 2 body, 4 hands, Thai and full body massage at your hotel or home. Booked by chat.",
                    "Our services", "Six massages, all given at your hotel or home in Amsterdam and beyond.", inner, []))
    return urls


def city_pages():
    urls = []
    for slug, name in CITIES:
        a, b = CITY_TEXT[name]
        price = PRICE_OF[name]
        minimum = "2 hours" in price
        price_line = (f"In {name} the rate is {price.replace('2 hours ', '')} for a minimum booking of two hours. " if minimum
                      else f"In {name} the rate is {price}. ") + "Every extra hour is € 160. Your rate is always confirmed in the chat before you book."
        others = "".join(f'<li><a href="/{s}/">Erotic massage {E(n)}</a></li>' for s, n in CITIES if s != slug)
        ml = "".join(f'<li><a href="/{s}/">{E(n)}</a></li>' for s, n, _ in MASSAGES)
        inner = (f'<section class="sec"><div class="wrap narrow prose"><h2>Erotic massage at your hotel or home in {E(name)}</h2><p>{E(a)}</p><p>{E(b)}</p>'
                 f'<h2>Price in {E(name)}</h2><p>{E(price_line)} See all <a href="/prices/">prices</a>.</p>'
                 f'<h2>Which massages can I book in {E(name)}?</h2><p>All our massages are available in {E(name)}:</p><ul class="chips">{ml}</ul>'
                 f'<h2>How to book</h2><p>Open the chat, tell us your address or hotel in {E(name)}, the time you prefer and the masseuse you like. We confirm availability and rate, and your masseuse comes to you. Read more on the <a href="/bookings/">bookings</a> page.</p></div></section>'
                 f'<section class="sec sec-alt"><div class="wrap"><h2>Our masseuses</h2><ul class="cards">{"".join(card(m) for m in MASSEUSES)}</ul></div></section>'
                 f'{cta(f"Book your erotic massage in {name} in the chat.")}'
                 f'<section class="sec"><div class="wrap"><h2>Other locations</h2><ul class="chips"><li><a href="/">Erotic massage Amsterdam</a></li>{others}<li><a href="/other-cities/">Other cities</a></li></ul></div></section>')
        desc = f"Erotic massage in {name} at your hotel or home. Sensual, tantra and body 2 body massage by selected masseuses from Amsterdam. Discreet, booked by chat."
        svc = {"@context": "https://schema.org", "@type": "Service", "name": f"Erotic massage {name}", "serviceType": "Erotic massage",
               "provider": {"@id": SITE + "/#org"}, "areaServed": {"@type": "City", "name": name}, "url": f"{SITE}/{slug}/"}
        urls.append(sub(f"/{slug}/", f"Erotic Massage {name} | Hotel & Home Visits", desc, f"Erotic Massage {name}",
                        f"Outcall erotic massage in {name}: your masseuse comes to your hotel or home.", inner, [("Locations", "/other-cities/")], [svc]))
    chips = "".join(f'<li><a href="/{s}/">Erotic massage {E(n)}</a></li>' for s, n in CITIES)
    inner = (f'<section class="sec"><div class="wrap narrow prose"><h2>Where we come</h2><p>Amsterdam is our home base, but our masseuses travel. Below you find every location we visit, with the rate for each one. For the cities with their own page you can read more by following the link.</p>{price_table(PRICES)}'
             '<p>Is your city not listed? Ask us in the chat. For longer distances we work with a minimum number of hours.</p></div></section>'
             f'<section class="sec sec-alt"><div class="wrap"><h2>Locations with their own page</h2><ul class="chips"><li><a href="/">Erotic massage Amsterdam</a></li>{chips}</ul></div></section>{cta()}')
    urls.append(sub("/other-cities/", "Erotic Massage in Other Cities | Erotic Massage Amsterdam",
                    "Erotic massage outside Amsterdam: Schiphol, Haarlem, Utrecht, Rotterdam, Den Haag, Leiden, Eindhoven and more. Hotel and home visits with rates per city.",
                    "Other cities", "Erotic massage at your hotel or home, also outside Amsterdam.", inner, []))
    return urls


def profile_text(m):
    slug, name, age, langs, _ = m
    tags = TAGS.get(slug, [])
    lang_list = langs.replace(", ", ", ").rsplit(", ", 1)
    lang_s = " and ".join(lang_list) if len(lang_list) > 1 else langs
    p1 = f"{name} is {age} years old and is one of the erotic masseuses of Erotic Massage Amsterdam. She speaks {lang_s}"
    p1 += f". Her style is {' and '.join(tags)}." if tags else "."
    p2 = (f"{name} visits you at your hotel or home in Amsterdam and the surrounding area. You can book her for every massage on our "
          f"services page, from a sensual massage to a body 2 body massage.")
    p3 = f"Would you like to book {name}? Mention her name in the chat, together with your location and the time you prefer. If she is not available, we suggest an alternative and you decide."
    return [p1, p2, p3]


def masseuse_pages():
    urls = []
    for m in MASSEUSES:
        slug, name, age, langs, _ = m
        facts = {"Age": str(age), "Languages": langs, "Based in": "Amsterdam"}
        facts.update(EXTRA.get(slug, {}))
        dl = "".join(f"<div><dt>{E(k)}</dt><dd>{E(v)}</dd></div>" for k, v in facts.items())
        ml = "".join(f'<li><a href="/{s}/">{E(n)}</a></li>' for s, n, _ in MASSAGES)
        rest = "".join(card(x) for x in MASSEUSES if x[0] != slug)
        inner = (f'<section class="sec"><div class="wrap prof"><div class="prof-img">{img(m, eager=True, sizes="(max-width:48rem) 90vw, 420px")}</div>'
                 f'<div class="prose"><h2>About {E(name)}</h2>{"".join(f"<p>{E(p)}</p>" for p in profile_text(m))}<dl class="facts">{dl}</dl>'
                 f'<p><a class="btn" href="/contact/" data-chat>Book {E(name)}</a> <a class="link" href="/prices/">See prices</a></p>'
                 f'<h2>Massages with {E(name)}</h2><ul class="chips">{ml}</ul></div></div></section>'
                 f'<section class="sec sec-alt"><div class="wrap"><h2>More masseuses</h2><ul class="cards">{rest}</ul></div></section>')
        ogi = f"{SITE}/images/masseuses/{slug}-erotic-massage-amsterdam.jpg"
        desc = f"{name} ({age}) is an erotic masseuse in Amsterdam. She speaks {langs} and visits you at your hotel or home. Book {name} by chat."
        urls.append(sub(f"/dames/{slug}/", f"{name} – Erotic Masseuse in Amsterdam", desc, f"{name} – erotic masseuse in Amsterdam",
                        f"{age} years · {langs} · Hotel and home visits", inner, [("Our masseuses", "/our-masseuses/")], og_image=ogi))
    lst = {"@context": "https://schema.org", "@type": "ItemList", "name": "Masseuses of Erotic Massage Amsterdam", "itemListElement": [
        {"@type": "ListItem", "position": i + 1, "name": m[1], "url": f"{SITE}/dames/{m[0]}/"} for i, m in enumerate(MASSEUSES)]}
    inner = (f'<section class="sec"><div class="wrap"><ul class="cards cards-lg">{"".join(card(m, eager=i < 2) for i, m in enumerate(MASSEUSES))}</ul></div></section>'
             '<section class="sec sec-alt"><div class="wrap narrow prose"><h2>Choose the masseuse you like</h2>'
             '<p>Our team is small on purpose, so that we know every masseuse we send to you.</p>'
             '<p>Open a profile to read more, and mention her name in the chat when you book. If your first choice is not available at the time you want, we tell you straight away and suggest someone else.</p></div></section>'
             f'{cta()}')
    urls.append(sub("/our-masseuses/", "Our Masseuses | Erotic Massage Amsterdam",
                    "Meet the masseuses of Erotic Massage Amsterdam. Real profiles, a small selected team, and you choose who visits you at your hotel or home.",
                    "Our masseuses", "A small, selected team. You choose who comes to you.", inner, [], [lst]))
    return urls


def info_pages():
    urls = []
    inner = (f'<section class="sec"><div class="wrap narrow prose"><p>Our rates depend on the location of your visit. The price is for one hour unless a minimum number of hours is shown. Every extra hour is € 160. Your rate is always confirmed in the chat before you book.</p>{price_table(PRICES)}'
             '<h2>Good to know</h2><ul class="ticks"><li>The rate is per masseuse. For a 4 hands massage with two masseuses, ask for the rate in the chat.</li>'
             '<li>For cities further away we work with a minimum number of hours, shown in the table.</li>'
             '<li>Is your city not listed? Ask us in the chat.</li></ul></div></section>' + cta("Ask for your rate in the chat. We confirm it before you book."))
    urls.append(sub("/prices/", "Prices | Erotic Massage Amsterdam",
                    "Prices for erotic massage at your hotel or home: € 160 in Amsterdam, Schiphol, Haarlem and Hoofddorp, € 160 per extra hour. Rates for all other cities.",
                    "Prices", "Clear rates per location, confirmed before you book.", inner, []))

    packs = [("One hour", "€ 160", "One massage of your choice with one masseuse. A good choice for a first visit."),
             ("Two hours", "€ 320", "Time to combine two massages, for example a full body massage followed by a body 2 body massage."),
             ("Three hours", "€ 480", "A long, slow evening without looking at the clock. Ideal for a tantra massage.")]
    tiles = "".join(f'<li><div class="tile"><h2>{E(n)}</h2><p class="price">{E(p)}</p><p>{E(d)}</p></div></li>' for n, p, d in packs)
    inner = (f'<section class="sec"><div class="wrap"><ul class="tiles">{tiles}</ul>'
             '<p class="note">Rates for Amsterdam, Schiphol, Haarlem and Hoofddorp: € 160 for the first hour and € 160 for every extra hour. For other cities see the <a href="/prices/">prices</a> page.</p></div></section>'
             '<section class="sec sec-alt"><div class="wrap narrow prose"><h2>Make your own combination</h2>'
             '<p>You are free to put together your own booking: choose the number of hours, the massage or massages and the masseuse. Would you like two masseuses for a 4 hands massage? Tell us in the chat and we give you the rate for your combination.</p></div></section>' + cta())
    urls.append(sub("/packages/", "Packages | Erotic Massage Amsterdam",
                    "Erotic massage packages in Amsterdam: one, two or three hours at your hotel or home. € 160 per hour, combine massages and choose your masseuse.",
                    "Packages", "Book one hour, or take your time with two or three.", inner, []))

    inner = ('<section class="sec"><div class="wrap narrow prose"><h2>Booking in three steps</h2><ol class="steps steps-col">'
             '<li><h3>Open the chat</h3><p>Use the Direct contact button and choose live chat, WhatsApp or Telegram.</p></li>'
             '<li><h3>Tell us what you would like</h3><p>Your hotel or address, the day and time, the number of hours, and the massage and masseuse you prefer.</p></li>'
             '<li><h3>Receive your confirmation</h3><p>We confirm the masseuse, the time and the rate. Your masseuse then comes to you at the agreed time.</p></li></ol>'
             '<h2>Preparing for your massage</h2><ul class="ticks"><li>Take a shower before your masseuse arrives.</li><li>Have one or two clean, large towels ready.</li>'
             '<li>If you are in a hotel, tell us your room number and make sure your masseuse can come up.</li><li>Put your phone on silent and enjoy.</li></ul>'
             '<h2>Changing or cancelling</h2><p>Plans change. If you need to move or cancel your booking, let us know in the chat as early as you can, so we can inform your masseuse.</p>'
             '<h2>Respect and discretion</h2><p>Our masseuses treat every guest with respect and expect the same in return. Your details are used only to arrange your appointment.</p></div></section>' + cta())
    urls.append(sub("/bookings/", "Bookings | Erotic Massage Amsterdam",
                    "Book an erotic massage in Amsterdam by chat: live chat, WhatsApp or Telegram. Tell us your hotel, time and masseuse and we confirm before anything is final.",
                    "Bookings", "Booking takes one message. Here is how it works.", inner, []))

    inner = ('<section class="sec"><div class="wrap narrow prose"><p>The fastest way to reach us is the chat. Choose live chat, WhatsApp or Telegram, and you are talking to us directly.</p>'
             '<p><a class="btn" href="/contact/" data-chat>Direct contact</a></p>'
             '<h2>What can we help you with?</h2><ul class="ticks"><li>Booking a massage at your hotel or home</li><li>Advice on which massage or masseuse suits you</li>'
             '<li>Rates for your city</li><li>Changing or cancelling a booking</li></ul>'
             '<p>See also our <a href="/bookings/">bookings</a> and <a href="/prices/">prices</a> pages.</p>'
             '<noscript><p>The chat needs JavaScript. Please enable JavaScript in your browser to contact us.</p></noscript></div></section>')
    urls.append(sub("/contact/", "Contact | Erotic Massage Amsterdam",
                    "Contact Erotic Massage Amsterdam by chat: live chat, WhatsApp or Telegram. Ask your question or book a massage at your hotel or home.",
                    "Contact", "We are reachable by chat: live chat, WhatsApp or Telegram.", inner, []))

    inner = ('<section class="sec"><div class="wrap narrow prose"><p>Erotic Massage Amsterdam is open to working with partners in and around Amsterdam.</p>'
             '<h2>Become a partner</h2><p>Do you run a hotel, a concierge service or a website and would you like to work with us? Send us a message in the chat and tell us about your idea.</p>'
             '<p><a class="btn" href="/contact/" data-chat>Direct contact</a></p></div></section>')
    urls.append(sub("/our-partners/", "Our Partners | Erotic Massage Amsterdam",
                    "Partners of Erotic Massage Amsterdam. Do you run a hotel, concierge service or website in Amsterdam? Contact us by chat to work together.",
                    "Our partners", "Working together in and around Amsterdam.", inner, []))
    return urls
