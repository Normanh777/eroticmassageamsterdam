#!/usr/bin/env python3
"""Static site generator for eroticmassageamsterdam.com.
Every old URL keeps its exact path (trailing slash). Output: ./dist
"""
import html, json, os, shutil
from datetime import date

ROOT = os.path.dirname(os.path.abspath(__file__))
DIST = os.path.join(ROOT, "dist")
SITE = "https://www.eroticmassageamsterdam.com"
BRAND = "Erotic Massage Amsterdam"
GLEAP_KEY = "UiBVsUqQcbHiHGp6Di9dlgUtnbhhW54f"  # same Gleap project as passionescorts.nl
TODAY = date.today().isoformat()

# Photos: local files once delivered (images/masseuses/<slug>.jpg); remote Passion thumbs until then.
LOCAL_PHOTOS = True  # photos live on the server in /images/masseuses/ (not in git)
P = "https://passionescorts.nl/hcgi/platform/api/files/escorts/"

MASSEUSES = [
    # slug, name, age, languages, based in ('' = not stated)
    ("bianca", "Bianca", 24, "English", ""),
    ("olga", "Olga", 24, "English", ""),
    ("vicky", "Vicky", 26, "English", ""),
    ("adda", "Adda", 26, "English", ""),
    ("alexandra", "Alexandra", 41, "English", ""),
    ("amanda", "Amanda", 23, "English", ""),
    ("anda", "Anda", 27, "English", ""),
    ("cleopatra", "Cleopatra", 42, "English", ""),
    ("denisa", "Denisa", 23, "English", ""),
    ("katy", "Katy", 25, "Dutch, English", ""),
    ("lavinia", "Lavinia", 24, "English", ""),
    ("livana", "Livana", 27, "English", ""),
    ("lora", "Lora", 27, "English", ""),
    ("noor", "Noor", 28, "English", ""),
    ("roxy", "Roxy", 29, "English", ""),
    ("stephanie", "Stephanie", 23, "English", ""),
    ("brianna", "Brianna", 26, "English", ""),
    ("clarissa", "Clarissa", 26, "English", ""),
    ("miki", "Miki", 23, "English", ""),
    ("roanna", "Roanna", 21, "English", ""),
    ("sophie", "Sophie", 31, "English, Italian, Spanish", ""),
    ("alee", "Alee", 29, "English", ""),
    ("alessia", "Alessia", 24, "English", ""),
    ("anely", "Anely", 23, "English", ""),
    ("angel", "Angel", 25, "English", ""),
    ("annabel", "Annabel", 28, "English", ""),
    ("ariel", "Ariel", 22, "English", ""),
    ("celine", "Celine", 25, "English", ""),
    ("cleo", "Cleo", 27, "English", ""),
    ("dalya", "Dalya", 27, "English", ""),
    ("denise", "Denise", 25, "English", ""),
    ("ines", "Ines", 24, "English", ""),
    ("ingrid", "Ingrid", 26, "English", ""),
    ("jeniffer", "Jeniffer", 27, "English", ""),
    ("jenn", "Jenn", 28, "English", ""),
    ("joy", "Joy", 23, "English", ""),
    ("kim", "Kim", 24, "English", ""),
    ("kimberly", "Kimberly", 35, "English", ""),
    ("lexi", "Lexi", 25, "English", ""),
    ("lisa", "Lisa", 31, "English", ""),
    ("mary", "Mary", 22, "English", ""),
    ("megan", "Megan", 32, "English", ""),
    ("michelle", "Michelle", 28, "English, Dutch", ""),
    ("nicole", "Nicole", 24, "English", ""),
    ("pandora", "Pandora", 25, "English", ""),
    ("raisa", "Raisa", 22, "English", ""),
    ("vanessa", "Vanessa", 24, "English", ""),
    ("angella", "Angella", 31, "English, French, Spanish", ""),
    ("bella", "Bella", 24, "English", ""),
    ("catalina", "Catalina", 29, "English, Portuguese, Spanish", ""),
    ("izabelle", "Izabelle", 35, "Dutch, French, Italian, Portuguese, English", ""),
    ("lucy", "Lucy", 28, "English, Spanish", ""),
    ("lunnie", "Lunnie", 25, "English", ""),
    ("nina", "Nina", 42, "Dutch, English", ""),
    ("rosalie", "Rosalie", 30, "English", ""),
    ("adrianna", "Adrianna", 35, "", "Amsterdam"),
    ("alicia", "Alicia", 21, "", "Amsterdam"),
    ("anna", "Anna", 25, "", "Amsterdam"),
    ("annays", "Annays", 21, "", "Amsterdam"),
    ("arianna", "Arianna", 26, "", "Amsterdam"),
    ("eleni", "Eleni", 24, "", ""),
    ("ella", "Ella", 21, "", "Amsterdam"),
    ("ella-new", "Ella New", 38, "", "Amsterdam"),
    ("isabella", "Isabella", 21, "", "Amsterdam"),
    ("julia", "Julia", 26, "", "Amsterdam"),
    ("lisanne", "Lisanne", 26, "", "Amsterdam"),
    ("lolita", "Lolita", 26, "", "Amsterdam"),
    ("mihaela", "Mihaela", 25, "", "Amsterdam"),
    ("mina", "Mina", 23, "", "Amsterdam"),
    ("nikki", "Nikki", 24, "", "Amsterdam"),
    ("sara", "Sara", 29, "", "Amsterdam"),
    ("tania", "Tania", 29, "", "Amsterdam"),
    ("viky", "Viky", 23, "", ""),
]
MANIFEST = "bianca:4 viky:4 tania:4 sara:4 nikki:4 mina:4 mihaela:4 lolita:4 lisanne:4 kim-den-haag:4 julia:4 jessy:4 jasmine:4 isabella:4 ella-new:4 ella:4 eleni:2 ashley:3 arianna:3 annays:4 anna:4 alicia:4 adrianna:4 sophie:6 rosalie:4 roanna:6 nina:5 miki:3 lunnie:3 lucy:4 izabelle:3 clarissa:9 catalina:6 brianna:6 bella:2 angella:2 vanessa:4 stephanie:3 roxy:4 raisa:3 pandora:3 noor:3 nicole:3 michelle:4 megan:3 mary:3 lora:3 livana:3 lisa:3 lexi:4 lavinia:4 kimberly:3 kim:4 katy:4 joy:4 jenn:4 jeniffer:3 ingrid:4 ines:3 denise:4 denisa:4 dalya:4 cleopatra:3 cleo:4 celine:4 ariel:4 annabel:4 angel:3 anely:3 anda:4 amanda:3 alexandra:4 alessia:4 alee:4 adda:4 vicky:4 olga:5"  # slug:photo-count pairs written by tools/copy-profiles.php
COUNTS = {k: int(v) for k, v in (p.split(':') for p in MANIFEST.split())}

# Old profile URLs with no current masseuse -> 301 to the overview (see .htaccess)
RETIRED = ["cristina", "yuki"]

MASSAGES = [
    ("sensual-massage", "Sensual Massage", "Slow, flowing strokes with warm oil. Unhurried, attentive and deeply relaxing from the first touch."),
    ("tantra-massage", "Tantra Massage", "A mindful, full-body ritual built around breathing, presence and gradually building energy."),
    ("body-2-body-massage", "Body 2 Body Massage", "Your masseuse uses her whole body to massage yours, skin to skin with warm oil."),
    ("4-hands-massage", "4 Hands Massage", "Two masseuses working in rhythm. Twice the attention, and a sensation that is hard to describe."),
    ("thai-massage", "Thai Massage", "Traditional stretching and pressure techniques to release tension, finished with a sensual touch."),
    ("full-body-massage", "Full Body Massage", "A complete massage from shoulders to feet that takes the stress out of travel and long days."),
]

CITIES = [
    ("erotic-massage-schiphol", "Schiphol"), ("erotic-massage-hoofddorp", "Hoofddorp"),
    ("erotic-massage-haarlem", "Haarlem"), ("erotic-massage-zandvoort", "Zandvoort"),
    ("erotic-massage-hilversum", "Hilversum"), ("erotic-massage-utrecht", "Utrecht"),
    ("erotic-massage-den-haag", "Den Haag"), ("erotic-massage-rotterdam", "Rotterdam"),
    ("erotic-massage-delft", "Delft"),
]

FAQ = [
    ("How do I book an erotic massage in Amsterdam?",
     "Open the chat on this website and choose live chat, WhatsApp or Telegram. Tell us where you are staying, the time you prefer and which massage or masseuse you have in mind. We confirm the details with you before anything is final."),
    ("Do you come to my hotel?",
     "Yes. Our masseuses visit hotels and private addresses in Amsterdam and the surrounding area, including Schiphol, Hoofddorp and Haarlem. For other cities see the prices page."),
    ("Can I choose my masseuse?",
     "Yes. Browse the profiles, pick the masseuse you like and mention her name in the chat. If she is not available at your time, we suggest an alternative and you decide."),
    ("Is the service discreet?",
     "Discretion is the starting point of every booking. Your details are used only to arrange your appointment and are not shared."),
    ("What does a massage cost?",
     "The rate depends on your location. In Amsterdam, Schiphol, Haarlem and Hoofddorp the rate is € 160 and every extra hour is € 160. You find all locations on the prices page."),
]

E = html.escape


def pic(name, alt, w, h, cls="", eager=False):
    load = 'fetchpriority="high"' if eager else 'loading="lazy" decoding="async"'
    c = f' class="{cls}"' if cls else ""
    return f'<img src="/images/site/{name}.jpg" alt="{E(alt)}" width="{w}" height="{h}" {load}{c}>'
LOGO_MARK = '<svg class="gem" viewBox="0 0 88 72" width="30" height="25" aria-hidden="true"><path d="M16 2h56l15 22-43 46L1 24z" fill="#d4d2da"/><path d="M1 24h86M16 2l12 22 16-22 16 22 12-22M28 24l16 46 16-46" fill="none" stroke="#17121a" stroke-width="3" stroke-linejoin="round"/></svg>'


def photo(m):
    slug, name, _, _, remote = m
    return f"/images/masseuses/{slug}.jpg" if LOCAL_PHOTOS else remote + "?thumb=400x500"


CSS = open(os.path.join(ROOT, "src", "site.css"), encoding="utf-8").read()
JS = open(os.path.join(ROOT, "src", "site.js"), encoding="utf-8").read().replace("__GLEAP_KEY__", GLEAP_KEY)


def minify_css(s):
    import re
    s = re.sub(r"/\*.*?\*/", "", s, flags=re.S)
    s = re.sub(r"\s+", " ", s)
    return re.sub(r"\s*([{}:;,>])\s*", r"\1", s).strip()


CSS_MIN = minify_css(CSS)


def jsonld(obj):
    return '<script type="application/ld+json">' + json.dumps(obj, ensure_ascii=False, separators=(",", ":")) + "</script>"


def header():
    massages = "".join(f'<li><a href="/{s}/">{E(n)}</a></li>' for s, n, _ in MASSAGES)
    return f"""<a class="skip" href="#main">Skip to content</a>
<header class="hdr">
<div class="wrap hdr-in">
<a class="logo" href="/" aria-label="{BRAND} – home">{LOGO_MARK}<span class="logo-t"><span>Erotic Massage</span><small>Amsterdam</small></span></a>
<input type="checkbox" id="nav-t" class="nav-t" aria-hidden="true" tabindex="-1">
<label for="nav-t" class="burger" aria-label="Menu"><span></span></label>
<nav class="nav" aria-label="Main">
<ul>
<li><a href="/our-masseuses/">Masseuses</a></li>
<li class="has-sub"><a href="/services/">Massages</a><ul class="sub">{massages}</ul></li>
<li><a href="/prices/">Prices</a></li>
<li><a href="/packages/">Packages</a></li>
<li><a href="/other-cities/">Locations</a></li>
<li><a href="/bookings/">Bookings</a></li>
</ul>
</nav>
<a class="btn btn-sm hdr-cta" href="/contact/" data-chat>Direct contact</a>
</div>
</header>"""


def footer():
    col = lambda title, items: f'<nav aria-label="{E(title)}"><h2>{E(title)}</h2><ul>' + "".join(
        f'<li><a href="{u}">{E(t)}</a></li>' for u, t in items) + "</ul></nav>"
    return f"""<footer class="ftr">
<div class="wrap ftr-grid">
<div><p class="logo">{LOGO_MARK}<span class="logo-t"><span>Erotic Massage</span><small>Amsterdam</small></span></p>
<p>Sensual outcall massage at your hotel or home in Amsterdam and beyond. Discreet, personal and arranged by chat.</p>
<p><a class="btn btn-sm" href="/contact/" data-chat>Direct contact</a></p></div>
{col("Massages", [(f"/{s}/", n) for s, n, _ in MASSAGES] + [("/services/", "All services")])}
{col("Locations", [(f"/{s}/", f"Erotic massage {n}") for s, n in CITIES] + [("/other-cities/", "Other cities")])}
{col("Information", [("/our-masseuses/", "Our masseuses"), ("/prices/", "Prices"), ("/packages/", "Packages"), ("/bookings/", "Bookings"), ("/our-partners/", "Our partners"), ("/contact/", "Contact")])}
</div>
<div class="wrap ftr-base"><p>© {date.today().year} {BRAND}</p><p>18+ · Adults only</p></div>
</footer>"""


def page(path, title, desc, body, schema, og_image=None):
    url = SITE + path
    head_schema = "".join(jsonld(s) for s in schema)
    og = f'<meta property="og:image" content="{og_image}">' if og_image else ""
    doc = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>{E(title)}</title>
<meta name="description" content="{E(desc)}">
<link rel="canonical" href="{url}">
<meta name="robots" content="index,follow,max-image-preview:large">
<meta name="rating" content="adult">
<meta name="theme-color" content="#17121a">
<meta property="og:type" content="website">
<meta property="og:site_name" content="{BRAND}">
<meta property="og:title" content="{E(title)}">
<meta property="og:description" content="{E(desc)}">
<meta property="og:url" content="{url}">
<meta property="og:locale" content="en_GB">
{og}
<meta name="twitter:card" content="summary_large_image">
<link rel="icon" href="/favicon.svg" type="image/svg+xml">
<link rel="preconnect" href="https://passionescorts.nl" crossorigin>
<style>{CSS_MIN}</style>
{head_schema}
</head>
<body>
{header()}
<main id="main">
{body}
</main>
{footer()}
<script>{JS}</script>
</body>
</html>
"""
    if LOCAL_PHOTOS:
        doc = doc.replace('<link rel="preconnect" href="https://passionescorts.nl" crossorigin>\n', "")
    out = os.path.join(DIST, path.strip("/"), "index.html")
    os.makedirs(os.path.dirname(out), exist_ok=True)
    open(out, "w", encoding="utf-8").write(doc)
    return url


def card(m, eager=False):
    slug, name, age, langs, _ = m
    load = 'fetchpriority="high"' if eager else 'loading="lazy" decoding="async"'
    return f"""<li class="card"><a href="/dames/{slug}/">
<img src="{photo(m)}" alt="{E(name)}, erotic masseuse in Amsterdam" width="400" height="500" {load}>
<span class="card-b"><strong>{E(name)}</strong><span>{age} · {E(langs)}</span></span></a></li>"""


ORG = {"@context": "https://schema.org", "@type": "Organization", "@id": SITE + "/#org", "name": BRAND,
       "url": SITE + "/", "logo": SITE + "/logo.svg", "areaServed": [{"@type": "City", "name": "Amsterdam"}] + [{"@type": "City", "name": n} for _, n in CITIES]}
WEBSITE = {"@context": "https://schema.org", "@type": "WebSite", "@id": SITE + "/#website", "name": BRAND,
           "url": SITE + "/", "inLanguage": "en", "publisher": {"@id": SITE + "/#org"}}


def home():
    title = "Erotic Massage Amsterdam | Sensual Outcall Massage"
    desc = ("Erotic massage in Amsterdam at your hotel or home. Sensual, tantra, body 2 body and 4 hands massage "
            "by selected masseuses. Discreet service, booked by chat.")
    massages = "".join(
        f'<li><a class="tile tile-img" href="/{s}/">{pic(s + "-amsterdam", n + " in Amsterdam", 600, 400)}<span class="tile-b"><h3>{E(n)}</h3><p>{E(d)}</p><span class="more">Read more</span></span></a></li>'
        for s, n, d in MASSAGES)
    cards = "".join(card(m) for m in MASSEUSES[:10])
    cities = "".join(f'<li><a href="/{s}/">Erotic massage {E(n)}</a></li>' for s, n in CITIES)
    faq = "".join(f"<details><summary>{E(q)}</summary><p>{E(a)}</p></details>" for q, a in FAQ)
    body = f"""<section class="hero">
<div class="wrap hero-grid">
<div>
<p class="eyebrow">Outcall massage · Hotel &amp; home visits</p>
<h1>Erotic Massage <span class="g">Amsterdam</span></h1>
<p class="lead">A sensual massage where you are staying, given by a masseuse you choose yourself. Tell us your hotel, your time and your wishes in the chat, and we arrange the rest discreetly.</p>
<p class="cta"><a class="btn" href="/contact/" data-chat>Direct contact</a> <a class="btn btn-ghost" href="/our-masseuses/">Meet our masseuses</a></p>
<ul class="usp"><li>Hotel and home visits</li><li>You choose your masseuse</li><li>Discreet from first message</li></ul>
</div>
<div class="hero-img">{pic("erotic-massage-amsterdam-hero", "Erotic massage in Amsterdam at your hotel", 720, 900, eager=True)}<p class="badge"><strong>€ 160</strong><span>per hour in Amsterdam</span></p></div>
</div>
</section>

<section class="stats" aria-label="Erotic Massage Amsterdam in numbers">
<ul class="wrap">
<li><strong>{len(MASSEUSES)}</strong><span>masseuses to choose from</span></li>
<li><strong>{len(MASSAGES)}</strong><span>erotic massages</span></li>
<li><strong>{len(PRICES)}</strong><span>cities we visit</span></li>
<li><strong>€ 160</strong><span>per hour in Amsterdam</span></li>
</ul>
</section>

<section class="sec sec-alt" aria-labelledby="h-welcome">
<div class="wrap split">
<div class="split-img">{pic("erotic-massage-at-your-hotel", "Relaxing erotic massage with warm oil", 500, 333)}</div>
<div class="prose">
<h2 id="h-welcome">Welcome</h2>
<p>Amsterdam is a city of genuine passion, love and excitement. If you want to make sure that your time here in Amsterdam is going to be as enjoyable as it possibly can, then you should consider hiring an erotic massage therapist.</p>
<p>An erotic massage can be the perfect way to get rid of all that stress that you are carrying on your shoulders, and make sure that you can walk around with a smile on your face for quite some time!</p>
<p>A massage can be the perfect answer for anyone who wants to just chill out and remove some stress and strain from your life – if you are finding life to be more of a challenge at the moment than it should be, you should consider hiring one of our excellent masseuses to help you relieve all of that stress and tension!</p>
</div>
</div>
</section>

<section class="sec sec-c" aria-labelledby="h-massages">
<div class="wrap">
<h2 id="h-massages">Our erotic massages</h2>
<p class="intro">Every massage is given one to one, at your pace. Not sure which one suits you? Describe what you like in the chat and we advise you.</p>
<ul class="tiles">{massages}</ul>
<p class="center"><a class="link" href="/services/">View all services</a></p>
</div>
</section>

<section class="sec sec-wine sec-c" aria-labelledby="h-masseuses">
<div class="wrap">
<h2 id="h-masseuses">Our masseuses in Amsterdam</h2>
<p class="intro">A selection of our masseuses. Open a profile to see photos and read more.</p>
<ul class="cards">{cards}</ul>
<p class="center"><a class="link" href="/our-masseuses/">View all masseuses</a></p>
</div>
</section>

<section class="sec" aria-labelledby="h-about">
<div class="wrap narrow prose">
<h2 id="h-about">Erotic massage</h2>
<div class="float-img">{pic("sensual-erotic-massage", "Sensual erotic massage in Amsterdam", 560, 840)}</div>
<p>The city of Amsterdam sure is a busy place. It can actually feel a touch crowded and stressful if you are not used to spending time in this part of the world. One thing you will find with an erotic massage, though, is that going for one can be the ideal way to spend some time. With an erotic massage session in Amsterdam, you are meeting up with one of our girls. They will meet you at an agreed place, and you will both come together and do some very interesting things to one another.</p>
<p>During an erotic massage, though, the single best thing that you can do is relax. With this kind of massage therapy, you are letting someone take you to places you have never been to before. It means allowing the massage to allow places that you would normally consider off-limits to be touched. You need to simply let your masseuse do the job that she has in mind. It will be helpful if you can relax, then, as it will allow the massage to feel as realistic and as enjoyable as is possible. Not only that, but you will find that the massage will generally give you some added self-confidence back. Why?</p>
<p>Because you will be getting so much relief mentally and sexually. When you get to finally unearth all of that tension, you will soon start feeling pretty tremendous. On top of that, you will enjoy an erotic massage unlike any other. It will give you all of the help that you need to enjoy the session, and to sit back and feel it working its benefits. You will leave the massage room feeling happier, healthier, and like a brand new kind of man!</p>
<h3>Make the most of your body with an erotic massage in Amsterdam</h3>
<p>When you want to enjoy a city like Amsterdam, you have to appreciate that a major part of it comes from its people. The people are what make Amsterdam, and our escorts are proud to be from here. We look to only use girls with long lasting experience and passion for an erotic massage. This allows you to enjoy the full experience like never before. It will mean that you can rest, relax, and just enjoy the whole thing.</p>
<p>What more could you want if you are looking for a simple way to just have some fun and rest, relax, and enjoy the show?</p>
<p>It’s a big reason why we recommend that you take the time to look at getting an erotic massage session in Amsterdam. It’s something that we think you should definitely look to do if you are looking to have some fun and to just relax. Don’t let anything get in the way of making sure you can have the fun that you want, when you want. So, why not make sure you can make the most of your body and enjoy an erotic massage today? You are worth it – so don’t let yourself believe otherwise!</p>
<h3>Erotic and sensual massage in Amsterdam</h3>
<p>Nothing makes life easier than a simple massage made to give you comfort and freedom, with a perfect ending to set you up for the rest of the week.</p>
<p>Maybe you once spent time with a lady who was so wonderful that she left you feeling lively and extraordinary. Perhaps her touch was so sensual that you were simply fascinated by her, or she used her whole body on yours in a way so passionate and delightful that you were turned on in a manner you never thought possible.</p>
<p>Most people never experience sensual perfection at this level. Many claim that they can give a great erotic massage, but we all know that very few really deliver.</p>
<p>Erotic and Sensual Massage Amsterdam offers this level of experience, with the skill and specialist knowledge to create a sensuous encounter so delightful and intense that you will cherish the time spent with one of our stunning masseuses.</p>
<p>Most people have a remarkable encounter only a couple of times in their lifetime. The masseuses of Erotic Massage Amsterdam have the expertise, training and talent to change that, and let you indulge in a sensual experience you can enjoy again and again.</p>
</div>
</section>

<section class="sec sec-alt sec-c" aria-labelledby="h-how">
<div class="wrap">
<h2 id="h-how">How booking works</h2>
<ol class="steps">
<li><h3>Open the chat</h3><p>Choose live chat, WhatsApp or Telegram and tell us your location, preferred time and massage.</p></li>
<li><h3>We confirm</h3><p>You hear which masseuse is available and what the rate is, before you decide.</p></li>
<li><h3>She comes to you</h3><p>Your masseuse arrives at your hotel or home at the agreed time. All you need is a shower and fresh towels.</p></li>
</ol>
<p class="center"><a class="btn" href="/contact/" data-chat>Direct contact</a> <a class="link" href="/prices/">See prices</a></p>
</div>
</section>

<section class="sec sec-c" aria-labelledby="h-areas">
<div class="wrap">
<h2 id="h-areas">Erotic massage in Amsterdam and beyond</h2>
<p class="intro">Amsterdam is our home base. We also visit the airport area and other cities in the Randstad.</p>
<ul class="chips">{cities}<li><a href="/other-cities/">Other cities</a></li></ul>
</div>
</section>

<section class="sec sec-alt sec-c" aria-labelledby="h-faq">
<div class="wrap narrow">
<h2 id="h-faq">Frequently asked questions</h2>
<div class="faq">{faq}</div>
</div>
</section>"""
    schema = [ORG, WEBSITE,
              {"@context": "https://schema.org", "@type": "WebPage", "@id": SITE + "/#webpage", "url": SITE + "/",
               "name": title, "description": desc, "inLanguage": "en", "isPartOf": {"@id": SITE + "/#website"},
               "about": {"@id": SITE + "/#org"}, "dateModified": TODAY},
              {"@context": "https://schema.org", "@type": "ItemList", "name": "Erotic massages in Amsterdam",
               "itemListElement": [{"@type": "ListItem", "position": i + 1, "name": n, "url": f"{SITE}/{s}/"}
                                   for i, (s, n, _) in enumerate(MASSAGES)]},
              {"@context": "https://schema.org", "@type": "FAQPage",
               "mainEntity": [{"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in FAQ]}]
    return page("/", title, desc, body, schema)


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
        "desc": "Tantra massage in Amsterdam at your hotel or home. A mindful full-body ritual with slow touch and breathing. Selected masseuses, booked by chat.",
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


def meta_line(m):
    return " · ".join(x for x in (f"{m[2]} years", m[3], m[4]) if x)


def img(m, cls="", eager=False, sizes="(max-width:40rem) 45vw, 400px"):
    slug, name = m[0], m[1]
    base = f"/images/masseuses/{slug}-erotic-massage-amsterdam-card"
    load = 'fetchpriority="high"' if eager else 'loading="lazy" decoding="async"'
    return (f'<img src="{base}.jpg" srcset="{base}-400.jpg 400w, {base}.jpg 800w" sizes="{sizes}" '
            f'alt="{E(name)}, erotic masseuse in Amsterdam" width="800" height="1000" {load}>')


def card(m, eager=False):  # overrides the first version: local photos
    slug, name, age, langs, city = m
    sub_l = " · ".join(x for x in (str(age), langs or city) if x)
    return (f'<li class="card"><a href="/dames/{slug}/">{img(m, eager=eager)}'
            f'<span class="card-b"><strong>{E(name)}</strong><span>{E(sub_l)}</span></span></a></li>')


def cta(text="Ready to book? Tell us your location, time and wishes in the chat.", label="Direct contact"):
    return f'<section class="sec band">{pic("massage-candles-stones", "", 1000, 400, cls="band-bg")}<div class="wrap narrow center-box"><p class="cta-t">{E(text)}</p><p><a class="btn" href="/contact/" data-chat>{E(label)}</a> <a class="link" href="/prices/">See prices</a></p></div></section>'


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
        inner = (f'<section class="sec"><div class="wrap narrow prose"><figure class="fig">{pic(slug + "-amsterdam", name + " in Amsterdam", 600, 400, eager=True)}</figure>{prose(t["body"])}'
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
    tiles = "".join(f'<li><a class="tile tile-img" href="/{s}/">{pic(s + "-amsterdam", n + " in Amsterdam", 600, 400)}<span class="tile-b"><h2>{E(n)}</h2><p>{E(d)}</p><span class="more">Read more</span></span></a></li>' for s, n, d in MASSAGES)
    inner = (f'<section class="sec"><div class="wrap"><ul class="tiles">{tiles}</ul></div></section>'
             '<section class="sec sec-alt"><div class="wrap split"><div class="split-img">' + pic("hot-stone-massage", "Massage with warm stones", 900, 600) + '</div><div class="prose"><h2>One service, your way</h2>'
             '<p>Every massage on this page is an outcall massage: your masseuse comes to your hotel or home. You choose the massage and the masseuse, and you can combine massages in a longer booking.</p>'
             '<p>Not sure what suits you? Tell us in the chat what you enjoy, whether you prefer soft or firm, and how much time you have. We suggest a massage and a masseuse, and you decide.</p></div></div></section>'
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
                 f'<section class="sec sec-alt"><div class="wrap"><h2>Our masseuses</h2><ul class="cards">{"".join(card(m) for m in MASSEUSES[:8])}</ul><p class="center"><a class="link" href="/our-masseuses/">View all masseuses</a></p></div></section>'
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


def profile_text(m, i):
    slug, name, age, langs, city = m
    tags = TAGS.get(slug, [])
    ll = langs.rsplit(", ", 1) if langs else []
    lang_s = " and ".join(ll)
    open_v = [f"{name} is {age} years old and is one of the erotic masseuses of Erotic Massage Amsterdam.",
              f"Meet {name}, {age}, one of the masseuses you can book through Erotic Massage Amsterdam.",
              f"{name} ({age}) is part of the team of Erotic Massage Amsterdam.",
              f"At {age}, {name} is one of the masseuses of Erotic Massage Amsterdam."][i % 4]
    p1 = open_v
    if lang_s:
        p1 += f" She speaks {lang_s}."
    if city:
        p1 += f" She is based in {city}."
    if tags:
        p1 += f" Her style is {' and '.join(tags)}."
    visit_v = [f"{name} visits you at your hotel or home. You can book her for the massages on our services page, from a sensual massage to a body 2 body massage.",
               f"Like all our masseuses, {name} comes to you: to your hotel room or your home address. Choose the massage you like on our services page.",
               f"A massage with {name} takes place where you are staying, at your hotel or at home. On our services page you find the massages you can choose from."][i % 3]
    p3 = f"Would you like to book {name}? Mention her name in the chat, together with your location and the time you prefer. If she is not available, we suggest an alternative and you decide."
    return [p1, visit_v, p3]


def gallery(m):
    slug, name = m[0], m[1]
    n = COUNTS.get(slug, 0)
    if n < 2:
        return ""
    base = f"/images/masseuses/{slug}-erotic-massage-amsterdam"
    items = "".join(f'<li><a href="{base}-{i}.jpg"><img src="{base}-{i}-400.jpg" alt="{E(name)}, photo {i}" loading="lazy" decoding="async"></a></li>'
                    for i in range(1, n + 1))
    return f'<section class="sec"><div class="wrap"><h2>Photos of {E(name)}</h2><ul class="gal">{items}</ul></div></section>'


def masseuse_pages():
    urls = []
    for idx, m in enumerate(MASSEUSES):
        slug, name, age, langs, city = m
        facts = {"Age": str(age)}
        if langs:
            facts["Languages"] = langs
        if city:
            facts["Based in"] = city
        facts.update(EXTRA.get(slug, {}))
        dl = "".join(f"<div><dt>{E(k)}</dt><dd>{E(v)}</dd></div>" for k, v in facts.items())
        ml = "".join(f'<li><a href="/{s}/">{E(n)}</a></li>' for s, n, _ in MASSAGES)
        k = len(MASSEUSES)
        rest = "".join(card(MASSEUSES[(idx + j) % k]) for j in range(1, 9))
        inner = (f'<section class="sec"><div class="wrap prof"><div class="prof-img">{img(m, eager=True, sizes="(max-width:48rem) 90vw, 420px")}</div>'
                 f'<div class="prose"><h2>About {E(name)}</h2>{"".join(f"<p>{E(p)}</p>" for p in profile_text(m, idx))}<dl class="facts">{dl}</dl>'
                 f'<p><a class="btn" href="/contact/" data-chat>Book {E(name)}</a> <a class="link" href="/prices/">See prices</a></p>'
                 f'<h2>Massages with {E(name)}</h2><ul class="chips">{ml}</ul></div></div></section>{gallery(m)}'
                 f'<section class="sec sec-alt"><div class="wrap"><h2>More masseuses</h2><ul class="cards">{rest}</ul>'
                 f'<p class="center"><a class="link" href="/our-masseuses/">View all masseuses</a></p></div></section>')
        ogi = f"{SITE}/images/masseuses/{slug}-erotic-massage-amsterdam-card.jpg"
        bits = [f"{name} ({age}) is an erotic masseuse of Erotic Massage Amsterdam."]
        if langs:
            bits.append(f"She speaks {langs}.")
        bits.append(f"Hotel and home visits. Book {name} by chat." if len(langs) < 30 else f"Book {name} by chat.")
        urls.append(sub(f"/dames/{slug}/", f"{name} – Erotic Masseuse | Erotic Massage Amsterdam", " ".join(bits), f"{name} – erotic masseuse in Amsterdam",
                        meta_line(m) + " · Hotel and home visits", inner, [("Our masseuses", "/our-masseuses/")], og_image=ogi))
    lst = {"@context": "https://schema.org", "@type": "ItemList", "name": "Masseuses of Erotic Massage Amsterdam", "itemListElement": [
        {"@type": "ListItem", "position": i + 1, "name": m[1], "url": f"{SITE}/dames/{m[0]}/"} for i, m in enumerate(MASSEUSES)]}
    inner = (f'<section class="sec"><div class="wrap"><ul class="cards cards-lg">{"".join(card(m, eager=i < 2) for i, m in enumerate(MASSEUSES))}</ul></div></section>'
             '<section class="sec sec-alt"><div class="wrap narrow prose"><h2>Choose the masseuse you like</h2>'
             '<p>Take your time to browse the profiles. Every masseuse has her own page with photos and details.</p>'
             '<p>Open a profile to read more, and mention her name in the chat when you book. If your first choice is not available at the time you want, we tell you straight away and suggest someone else.</p></div></section>'
             f'{cta()}')
    urls.append(sub("/our-masseuses/", "Our Masseuses | Erotic Massage Amsterdam",
                    "Meet the 73 masseuses of Erotic Massage Amsterdam. Browse the profiles and photos and choose who visits you at your hotel or home.",
                    "Our masseuses", "Browse all profiles. You choose who comes to you.", inner, [], [lst]))
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


def build():
    shutil.rmtree(DIST, ignore_errors=True)
    os.makedirs(DIST)
    static = os.path.join(ROOT, "static")
    if os.path.isdir(static):
        shutil.copytree(static, DIST, dirs_exist_ok=True)
    urls = [home()] + masseuse_pages() + massage_pages() + city_pages() + info_pages()
    sm = '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n' + "".join(
        f"<url><loc>{u}</loc><lastmod>{TODAY}</lastmod></url>\n" for u in urls) + "</urlset>\n"
    open(os.path.join(DIST, "sitemap.xml"), "w").write(sm)
    open(os.path.join(DIST, "robots.txt"), "w").write(f"User-agent: *\nAllow: /\n\nSitemap: {SITE}/sitemap.xml\n")
    redirects = "".join(f"RewriteRule ^dames/{s}/?$ /our-masseuses/ [R=301,L]\n" for s in RETIRED)
    ht = f"""# eroticmassageamsterdam.com
Options -Indexes
DirectoryIndex index.html
ErrorDocument 404 /404.html
RewriteEngine On
# GO-LIVE: uncomment the next 3 lines once DNS points to Hostinger (forces https + www)
# RewriteCond %{{HTTPS}} !=on [OR]
# RewriteCond %{{HTTP_HOST}} !^www\\. [NC]
# RewriteRule ^ https://www.eroticmassageamsterdam.com%{{REQUEST_URI}} [R=301,L]
RewriteRule ^index\\.html$ / [R=301,L]
RedirectMatch 404 /\\.git
RedirectMatch 404 ^/_tools
# Old profiles without a current masseuse
{redirects}
<IfModule mod_headers.c>
Header set X-Content-Type-Options "nosniff"
Header set Referrer-Policy "strict-origin-when-cross-origin"
<FilesMatch "\\.(jpg|jpeg|png|webp|avif|svg|ico|woff2)$">
Header set Cache-Control "public, max-age=31536000, immutable"
</FilesMatch>
</IfModule>
"""
    open(os.path.join(DIST, ".htaccess"), "w").write(ht)
    print("built", len(urls), "page(s);", "local photos" if LOCAL_PHOTOS else "remote photos (temporary)")


if __name__ == "__main__":
    build()
