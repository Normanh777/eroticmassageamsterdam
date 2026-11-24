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
    ("erotic-massage-amstelveen", "Amstelveen"), ("erotic-massage-diemen", "Diemen"), ("erotic-massage-zaandam", "Zaandam"),
    ("erotic-massage-purmerend", "Purmerend"), ("erotic-massage-weesp", "Weesp"), ("erotic-massage-naarden", "Naarden"),
    ("erotic-massage-bussum", "Bussum"), ("erotic-massage-huizen", "Huizen"), ("erotic-massage-laren", "Laren"),
    ("erotic-massage-almere", "Almere"), ("erotic-massage-uithoorn", "Uithoorn"), ("erotic-massage-aalsmeer", "Aalsmeer"),
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
    ("Do you offer a happy ending massage in Amsterdam?",
     "Yes. A happy ending is part of all our erotic massages, whether you choose a sensual, tantra or body to body massage."),
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
{col("Massages", [(f"/{s}/", n) for s, n, _ in MASSAGES] + [("/happy-ending-massage/", "Happy Ending Massage"), ("/services/", "All services")])}
{col("Locations", [(f"/{s}/", f"Erotic massage {n}") for s, n in CITIES[:9]] + [("/other-cities/", "All locations")])}
{col("Packages", [("/packages/dinner-date/", "Dinner Date & Massage"), ("/packages/amsterdam-tour/", "Amsterdam Tour & Massage"), ("/packages/duo-deluxe/", "Duo Deluxe"), ("/packages/schiphol-stopover/", "Schiphol Stopover"), ("/packages/couples-massage/", "Couples Massage"), ("/packages/", "All packages")])}
{col("Information", [("/our-masseuses/", "Our masseuses"), ("/prices/", "Prices"), ("/bookings/", "Bookings"), ("/our-partners/", "Our partners"), ("/contact/", "Contact")])}
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
    desc = ("Erotic massage in Amsterdam at your hotel or home. Sensual, tantra and body to body massage with happy ending "
            "by a masseuse you choose. From € 160 per hour.")
    massages = "".join(
        f'<li><a class="tile tile-img" href="/{s}/">{pic(s + "-amsterdam", n + " in Amsterdam", 600, 400)}<span class="tile-b"><h3>{E(n)}</h3><p>{E(d)}</p><span class="more">Read more</span></span></a></li>'
        for s, n, d in MASSAGES)
    cards = "".join(card(m) for m in MASSEUSES[:10])
    cities = "".join(f'<li><a href="/{s}/">Erotic massage {E(n)}</a></li>' for s, n in CITIES)
    faq = "".join(f"<details><summary>{E(q)}</summary><p>{E(a)}</p></details>" for q, a in FAQ)
    pk = "".join(pkg_card(p) for p in PACKAGES if p[1] in ("dinner-date", "amsterdam-tour", "duo-deluxe"))
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
<li><strong>{len(set(p[0] for p in PRICES) | set(n for _, n in CITIES))}</strong><span>cities and towns we visit</span></li>
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
<p class="center"><a class="link" href="/services/">View all services</a> <a class="link" href="/happy-ending-massage/">Happy ending massage</a></p>
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

<section class="sec sec-alt sec-c" aria-labelledby="h-pk">
<div class="wrap">
<h2 id="h-pk">Popular packages</h2>
<p class="intro">Combine your erotic massage with a dinner, a tour of the city or a second masseuse.</p>
<ul class="pkgs">{pk}</ul>
<p class="center"><a class="btn btn-ghost" href="/packages/">View all {len(PACKAGES)} packages</a></p>
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
<p class="intro">Amsterdam is our home base. We also visit the airport area, the towns around Amsterdam, the Gooi region and other cities in the Randstad.</p>
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
    "Amstelveen": ("Amstelveen borders Amsterdam directly to the south, between the Amsterdamse Bos and the Zuidas business district. It is home to many international companies and residents, and to a good number of hotels.",
                   "Because Amstelveen is so close to Amsterdam, a massage at your hotel or home here is easy to arrange. Tell us your address and the time you prefer in the chat."),
    "Diemen": ("Diemen lies on the eastern edge of Amsterdam, next to the A1 and A10 and close to the Amsterdam Arena area. Several hotels here are popular with business travellers and concert visitors.",
               "Your masseuse comes to your hotel room or home in Diemen. You choose the massage and the masseuse, and we take care of the planning."),
    "Zaandam": ("Zaandam is just north-west of Amsterdam, known for its green wooden houses and the windmills of the nearby Zaanse Schans. Its hotels are a favourite with visitors who want to stay just outside the capital.",
                "An erotic massage in Zaandam takes place where you are staying. One message in the chat with your hotel and preferred time is enough to get started."),
    "Purmerend": ("Purmerend is a market town north of Amsterdam, in the middle of the Waterland polders. Whether you live here or are staying in the area, our masseuses come to you.",
                  "The journey from Amsterdam is a little longer than within the city, so we recommend letting us know in good time when you would like your massage."),
    "Weesp": ("Weesp is a small fortified town on the river Vecht, south-east of Amsterdam, and has been part of the municipality of Amsterdam since 2022. Its old centre with canals and windmills feels a world away from the busy city.",
              "Your masseuse visits you at home or at your accommodation in Weesp. Tell us your address and the time you prefer, and we confirm who is available."),
    "Naarden": ("Naarden is famous for its star-shaped fortress, one of the best preserved fortified towns in Europe. It lies in the Gooi region, between Amsterdam and Hilversum.",
                "An erotic massage in Naarden is given at your home or hotel. Book ahead if you can, so that the masseuse of your choice is free at the time you prefer."),
    "Bussum": ("Bussum lies next to Naarden in the green Gooi region, a leafy town of villas and quiet streets with a direct connection to Amsterdam.",
               "Our masseuses visit private addresses and hotels in Bussum. You choose the massage and the masseuse, and your masseuse comes to you."),
    "Huizen": ("Huizen is a former fishing village on the Gooimeer, on the northern edge of the Gooi region. Today it is a quiet residential town with a marina and a beach on the lake.",
               "Would you like an erotic massage at home in Huizen? Let us know your address and preferred time in the chat, ideally a little in advance."),
    "Laren": ("Laren is the artists' village of the Gooi region, known for its village green, galleries and elegant villas. It is one of the most exclusive addresses in the Netherlands.",
              "Discretion matters to our guests in Laren, and it is where we start. Your masseuse visits you at home or at your hotel, at the time you agree with us."),
    "Almere": ("Almere is the youngest city in the Netherlands, built on reclaimed land in Flevoland and known for its modern architecture. It lies east of Amsterdam, across the IJmeer.",
               "Your masseuse travels from Amsterdam to your home or hotel in Almere. Book ahead if you can, so we can plan the journey and confirm the masseuse you prefer."),
    "Uithoorn": ("Uithoorn lies on the river Amstel, south of Amsterdam and Amstelveen, with a waterfront full of terraces. It is a short drive from both Amsterdam and Schiphol.",
                 "An erotic massage in Uithoorn is given at your home or accommodation. Tell us your address and the time you prefer, and we arrange the rest."),
    "Aalsmeer": ("Aalsmeer is known worldwide for its flower auction and for the Westeinderplassen lakes. It sits right next to Schiphol, which makes it a convenient base for travellers.",
                 "Staying in Aalsmeer for business or before a flight? Your masseuse comes to your hotel or home, and you choose the massage you like."),
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
                 '<!--faq-->'
                 f'<section class="sec"><div class="wrap"><h2>Other massages</h2><ul class="chips">{others}<li><a href="/happy-ending-massage/">Happy Ending Massage</a></li><li><a href="/services/">All services</a></li></ul>'
                 f'{link_row("Popular packages", TOP_PKG)}{link_row("Where we come", [("/", "Amsterdam")] + [(f"/{cs}/", cn) for cs, cn in CITIES[:11]] + [("/other-cities/", "All locations")])}'
                 f'<h2 class="mt">Choose your masseuse</h2><ul class="cards">{"".join(card(m) for m in MASSEUSES[:6])}</ul>'
                 f'<p class="center"><a class="link" href="/our-masseuses/">View all masseuses</a></p></div></section>')
        svc = {"@context": "https://schema.org", "@type": "Service", "name": f"{name} Amsterdam", "serviceType": name,
               "description": t["desc"], "provider": {"@id": SITE + "/#org"}, "areaServed": {"@type": "City", "name": "Amsterdam"},
               "url": f"{SITE}/{slug}/"}
        m_title, m_h1, m_faq = MASSAGE_SEO[slug]
        fq_html, fq_schema = faq_block(m_faq, f"Questions about {name.lower()}")
        inner = inner.replace("<!--faq-->", fq_html)
        urls.append(sub(f"/{slug}/", m_title, t["desc"], m_h1, t["lead"], inner,
                        [("Services", "/services/")], [svc, fq_schema]))
    hq_html, hq_schema = faq_block(HAPPY["faq"], "Questions about a happy ending massage")
    ml = "".join(f'<li><a href="/{s}/">{E(n)}</a></li>' for s, n, _ in MASSAGES)
    inner = (f'<section class="sec"><div class="wrap narrow prose"><figure class="fig">{pic("happy-ending-massage-amsterdam", "Happy ending massage in Amsterdam", 600, 400, eager=True)}</figure>{prose(HAPPY["body"])}'
             f'<h2>Price</h2><p>A happy ending massage in Amsterdam, Schiphol, Haarlem or Hoofddorp is € 160 per hour, and every extra hour is € 160. For other cities see our <a href="/prices/">prices</a>.</p></div></section>'
             f'{cta("Book your happy ending massage in the chat. We confirm masseuse, time and rate before anything is final.")}{hq_html}'
             f'<section class="sec"><div class="wrap"><h2>Choose your massage</h2><ul class="chips">{ml}</ul>{link_row("Popular packages", TOP_PKG)}'
             f'<h2 class="mt">Choose your masseuse</h2><ul class="cards">{"".join(card(m) for m in MASSEUSES[:10])}</ul><p class="center"><a class="link" href="/our-masseuses/">View all masseuses</a></p></div></section>')
    urls.append(sub("/happy-ending-massage/", HAPPY["title"], HAPPY["desc"], "Happy Ending Massage Amsterdam", HAPPY["lead"], inner, [("Services", "/services/")],
                    [{"@context": "https://schema.org", "@type": "Service", "name": "Happy ending massage Amsterdam", "serviceType": "Erotic massage", "provider": {"@id": SITE + "/#org"},
                      "areaServed": {"@type": "City", "name": "Amsterdam"}, "url": SITE + "/happy-ending-massage/"}, hq_schema]))
    tiles = "".join(f'<li><a class="tile tile-img" href="/{s}/">{pic(s + "-amsterdam", n + " in Amsterdam", 600, 400)}<span class="tile-b"><h2>{E(n)}</h2><p>{E(d)}</p><span class="more">Read more</span></span></a></li>' for s, n, d in MASSAGES)
    inner = (f'<section class="sec"><div class="wrap"><ul class="tiles">{tiles}</ul></div></section>'
             '<section class="sec sec-alt"><div class="wrap split"><div class="split-img">' + pic("hot-stone-massage", "Massage with warm stones", 900, 600) + '</div><div class="prose"><h2>One service, your way</h2>'
             '<p>Every massage on this page is an outcall massage: your masseuse comes to your hotel or home. You choose the massage and the masseuse, and you can combine massages in a longer booking.</p>'
             '<p>Looking for a <a href="/happy-ending-massage/">happy ending massage</a>? It is part of all our erotic massages.</p><p>Not sure what suits you? Tell us in the chat what you enjoy, whether you prefer soft or firm, and how much time you have. We suggest a massage and a masseuse, and you decide.</p></div></div></section>'
             f'{cta()}')
    urls.append(sub("/services/", "Erotic Massage Services | Erotic Massage Amsterdam",
                    "All erotic massage services in Amsterdam: sensual, tantra, body 2 body, 4 hands, Thai and full body massage at your hotel or home. Booked by chat.",
                    "Our services", "Six massages, all given at your hotel or home in Amsterdam and beyond.", inner, []))
    return urls


def city_pages():
    urls = []
    for slug, name in CITIES:
        a, b = CITY_TEXT[name]
        price = PRICE_OF.get(name)
        minimum = bool(price) and "2 hours" in price
        if not price:
            price_line = f"Ask us for the rate for {name} in the chat. It depends on the distance from Amsterdam, and we always confirm it before you book. Every extra hour is € 160."
        else:
            price_line = (f"In {name} the rate is {price.replace('2 hours ', '')} for a minimum booking of two hours. " if minimum
                          else f"In {name} the rate is {price}. ") + "Every extra hour is € 160. Your rate is always confirmed in the chat before you book."
        others = "".join(f'<li><a href="/{s}/">Erotic massage {E(n)}</a></li>' for s, n in CITIES if s != slug)
        ml = "".join(f'<li><a href="/{s}/">{E(n)}</a></li>' for s, n, _ in MASSAGES)
        if not price:
            nl_price = f"Vraag het tarief voor {name} in de chat."
        elif minimum:
            nl_price = f"Het tarief in {name} is {price.replace('2 hours ', '')} voor minimaal 2 uur; elk extra uur is € 160."
        else:
            nl_price = f"Het tarief in {name} is {price} per uur; elk extra uur is € 160."
        nl = (f'<h2 lang="nl">Erotische massage {E(name)}</h2><p lang="nl">Zoekt u een erotische massage in {E(name)}? Onze masseuses komen naar uw hotel of bij u thuis in {E(name)}. '
              f'U kiest zelf de massage en de masseuse en boekt eenvoudig via de chat, met live chat, WhatsApp of Telegram. {E(nl_price)}</p>')
        c_faq = [(f"What does an erotic massage in {name} cost?", price_line),
                 (f"Do you visit hotels and private addresses in {name}?", f"Yes. Your masseuse comes to your hotel, apartment or home in {name}. Tell us the address and the time you prefer in the chat."),
                 (f"How far in advance should I book in {name}?", f"The earlier the better, because your masseuse travels to {name} and your favourite may be booked. Same day bookings are often possible; ask us in the chat."),
                 (f"Which massages can I book in {name}?", f"All our erotic massages: sensual, tantra, body to body, 4 hands, Thai and full body massage, each with a happy ending.")]
        cf_html, cf_schema = faq_block(c_faq, f"Questions about erotic massage in {name}")
        inner = (f'<section class="sec"><div class="wrap narrow prose"><h2>Erotic massage at your hotel or home in {E(name)}</h2><p>{E(a)}</p><p>{E(b)}</p>'
                 f'<h2>Price in {E(name)}</h2><p>{E(price_line)} See all <a href="/prices/">prices</a>.</p>'
                 f'<h2>Which massages can I book in {E(name)}?</h2><p>All our massages are available in {E(name)}:</p><ul class="chips">{ml}</ul>'
                 f'<h2>How to book</h2><p>Open the chat, tell us your address or hotel in {E(name)}, the time you prefer and the masseuse you like. We confirm availability and rate, and your masseuse comes to you. Read more on the <a href="/bookings/">bookings</a> page.</p>{nl}</div></section>'
                 f'<section class="sec sec-alt"><div class="wrap"><h2>Our masseuses</h2><ul class="cards">{"".join(card(m) for m in MASSEUSES[:8])}</ul><p class="center"><a class="link" href="/our-masseuses/">View all masseuses</a></p></div></section>'
                 f'{cta(f"Book your erotic massage in {name} in the chat.")}'
                 f'{cf_html}'
                 f'<section class="sec"><div class="wrap"><h2>Other locations</h2><ul class="chips"><li><a href="/">Erotic massage Amsterdam</a></li>{others}<li><a href="/other-cities/">Other cities</a></li></ul>{link_row("Popular packages", TOP_PKG)}</div></section>')
        desc = f"Erotic massage in {name} at your hotel or home. Sensual, tantra and body 2 body massage by selected masseuses from Amsterdam. Discreet, booked by chat."
        svc = {"@context": "https://schema.org", "@type": "Service", "name": f"Erotic massage {name}", "serviceType": "Erotic massage",
               "provider": {"@id": SITE + "/#org"}, "areaServed": {"@type": "City", "name": name}, "url": f"{SITE}/{slug}/"}
        urls.append(sub(f"/{slug}/", f"Erotic Massage {name} | Erotische Massage {name}", desc, f"Erotic Massage {name}",
                        f"Outcall erotic massage in {name}: your masseuse comes to your hotel or home.", inner, [("Locations", "/other-cities/")], [svc, cf_schema]))
    chips = "".join(f'<li><a href="/{s}/">Erotic massage {E(n)}</a></li>' for s, n in CITIES)
    inner = (f'<section class="sec"><div class="wrap narrow prose"><h2>Where we come</h2><p>Amsterdam is our home base, but our masseuses travel. Below you find every location we visit, with the rate for each one. For the cities with their own page you can read more by following the link.</p>{price_table(PRICES)}'
             '<p>We also visit ' + ', '.join(n for _, n in CITIES if n not in PRICE_OF) + '. Ask us for the rate for these places in the chat.</p><p>Is your city not listed? Ask us in the chat. For longer distances we work with a minimum number of hours.</p></div></section>'
             f'<section class="sec sec-alt"><div class="wrap"><h2>Locations with their own page</h2><ul class="chips"><li><a href="/">Erotic massage Amsterdam</a></li>{chips}</ul></div></section>{cta()}')
    urls.append(sub("/other-cities/", "Erotic Massage in Other Cities | Erotic Massage Amsterdam",
                    "Erotic massage outside Amsterdam: Schiphol, Amstelveen, Haarlem, Almere, Utrecht, Rotterdam, Den Haag and more. Hotel and home visits, rates per city.",
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
                 f'<h2>Massages with {E(name)}</h2><ul class="chips">{ml}<li><a href="/happy-ending-massage/">Happy Ending Massage</a></li></ul>'
                 f'<h2>Packages with {E(name)}</h2><ul class="chips">{"".join(f"<li><a href=" + chr(34) + u + chr(34) + f">{E(t)}</a></li>" for u, t in TOP_PKG)}</ul></div></div></section>{gallery(m)}'
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


PACKAGES = [  # group, id, name, duration, price label, photo, description, includes
    ("Discover Amsterdam", "amsterdam-tour", "Amsterdam Tour & Massage", "From 4 hours", "From € 640", "erotic-massage-at-your-hotel",
     "See Amsterdam with charming company. Your masseuse joins you for a walk through the old centre or a cruise on the canals, and afterwards you go back to your hotel for an erotic massage with a happy ending.",
     ["A walk or canal cruise together", "Erotic massage of your choice at your hotel", "Route and timing agreed with you in the chat"]),
    ("Discover Amsterdam", "dinner-date", "Dinner Date & Erotic Massage", "From 3 hours", "From € 480", "dinner-date-erotic-massage",
     "Start the evening at the table and end it in your room. You have dinner together at a restaurant of your choice, followed by an unhurried erotic massage at your hotel.",
     ["Dinner together at your restaurant", "Erotic massage of your choice afterwards", "The perfect evening for one night in Amsterdam"]),
    ("Discover Amsterdam", "amsterdam-by-night", "Amsterdam by Night", "From 2 hours", "From € 320", "amsterdam-by-night-massage",
     "A drink together at your hotel bar or a cocktail bar in the city, and then upstairs for your massage. Shorter than a dinner date, with the same relaxed start.",
     ["A drink together to break the ice", "Sensual or body 2 body massage", "Easy to book on the day itself"]),
    ("For the business traveller", "schiphol-stopover", "Schiphol Stopover", "1 hour", "€ 160", "full-body-massage-amsterdam",
     "A few hours between two flights, or one night at an airport hotel? Your masseuse comes to your hotel at Schiphol, Hoofddorp or Aalsmeer and makes the wait the best part of your trip.",
     ["At your airport hotel", "Massage of your choice", "Timed around your flight"]),
    ("For the business traveller", "jetlag-relief", "Jetlag Relief", "2 hours", "€ 320", "jetlag-relief-massage",
     "Just landed and stiff from the flight? First a firm full body massage for your back, neck and legs, then a slow, sensual finish that helps you switch off completely.",
     ["Full body massage to start", "Sensual finish", "Ideal on your day of arrival"]),
    ("For the business traveller", "after-work", "After Work", "1 hour", "€ 160", "after-work-massage",
     "The meeting ran late and the day was long. One message in the chat is enough: your masseuse comes to your hotel and you close the laptop for good.",
     ["Late evening visits", "At your hotel or home", "Discreet from first message"]),
    ("Something special", "duo-deluxe", "Duo Deluxe", "2 hours · two masseuses", "Rate on request", "duo-massage-two-masseuses",
     "Two masseuses and four hands for two full hours. They work in rhythm, mirror each other and take turns, and you stop keeping track of whose hands are where.",
     ["Two masseuses of your choice", "4 hands and body 2 body massage", "Mention both names when you book"]),
    ("Something special", "tantra-ritual", "Tantra Ritual", "From 2 hours", "From € 320", "tantra-massage-amsterdam",
     "A long tantra session without a clock. Breathing, slow touch and a gradual build-up of energy from the first minute to the last.",
     ["Extended tantra massage", "No rush, no routine", "Best with two or three hours"]),
    ("Something special", "bath-and-massage", "Bath & Massage", "2 hours", "€ 320", "bath-and-massage",
     "Begin together in the bath or under the shower and move on to a body 2 body massage with warm oil. For rooms with a bathtub or a spacious shower.",
     ["Bath or shower together", "Body 2 body massage", "For hotel rooms with a bath"]),
    ("Something special", "champagne-evening", "Champagne Evening", "3 hours", "€ 480", "champagne-evening-massage",
     "Champagne on ice, strawberries on the table and three hours ahead of you. An evening of conversation, laughter and a long sensual massage.",
     ["Three hours together", "Sensual massage of your choice", "Order the champagne through your hotel"]),
    ("For couples and gifts", "couples-massage", "Couples Massage", "From 1 hour", "Rate on request", "4-hands-massage-amsterdam",
     "An erotic massage for the two of you, at your hotel or at home. Choose one masseuse who looks after you both, or two masseuses who massage you side by side.",
     ["For couples", "One or two masseuses", "Tell us your wishes in the chat"]),
    ("For couples and gifts", "massage-lesson", "Massage Lesson for Couples", "2 hours", "€ 320", "sensual-massage-amsterdam",
     "Learn how to give each other a sensual massage. Your masseuse shows you the strokes, the rhythm and the use of oil, and you practise on each other while she guides you.",
     ["Hands-on lesson for two", "Techniques you can use at home", "A gift that lasts longer than one evening"]),
    ("For couples and gifts", "birthday-surprise", "Birthday Surprise", "Any package", "Rate on request", "body-2-body-massage-amsterdam",
     "Surprise someone with an evening he will not forget. Choose any package as a gift, give us the date, the hotel and the name, and we arrange the rest discreetly.",
     ["Any package as a gift", "Arranged in advance by chat", "For birthdays, bachelor weekends and celebrations"]),
]


def pkg_card(p, h="h3"):
    g, pid, name, dur, price, photo, d, inc = p
    lis = "".join(f"<li>{E(x)}</li>" for x in inc)
    return (f'<li class="pkg" id="{pid}">{pic(photo, name, 600, 400)}<div class="pkg-b"><p class="pkg-m"><span>{E(dur)}</span><strong>{E(price)}</strong></p>'
            f'<{h}>{E(name)}</{h}><p>{E(d)}</p><ul class="ticks">{lis}</ul>'
            f'<p><a class="btn btn-sm" href="/contact/" data-chat>Book this package</a> <a class="link" href="/packages/{pid}/">More about {E(name)}</a></p></div></li>')


def faq_block(qas, title="Frequently asked questions", alt=True):
    fq = "".join(f"<details><summary>{E(q)}</summary><p>{E(a)}</p></details>" for q, a in qas)
    html_ = f'<section class="sec{" sec-alt" if alt else ""} sec-c"><div class="wrap narrow"><h2>{E(title)}</h2><div class="faq">{fq}</div></div></section>'
    schema = {"@context": "https://schema.org", "@type": "FAQPage", "mainEntity": [
        {"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in qas]}
    return html_, schema


def link_row(title, items):
    return f'<h2 class="mt">{E(title)}</h2><ul class="chips">' + "".join(f'<li><a href="{u}">{E(t)}</a></li>' for u, t in items) + "</ul>"


TOP_PKG = [("/packages/dinner-date/", "Dinner Date & Erotic Massage"), ("/packages/amsterdam-tour/", "Amsterdam Tour & Massage"),
           ("/packages/duo-deluxe/", "Duo Deluxe"), ("/packages/schiphol-stopover/", "Schiphol Stopover"), ("/packages/", "All packages")]

MASSAGE_SEO = {  # slug: (title, h1, [faq])
    "sensual-massage": ("Sensual Massage Amsterdam | At Your Hotel or Home", "Sensual Massage Amsterdam", [
        ("What is the difference between a sensual and an erotic massage?", "A sensual massage is the softest form of erotic massage. The focus is on slow, flowing touch over the whole body and on building up relaxation and excitement gradually."),
        ("How long does a sensual massage take?", "You can book from one hour. With two hours there is more time for a slow build-up, and every extra hour is € 160."),
        ("Can I book a sensual massage at my hotel in Amsterdam?", "Yes. Our masseuses visit hotels and private addresses in Amsterdam and the surrounding area. Tell us your hotel and preferred time in the chat."),
    ]),
    "tantra-massage": ("Tantra Massage Amsterdam | At Your Hotel or Home", "Tantra Massage Amsterdam", [
        ("What happens during a tantra massage?", "A tantra massage starts with calm, grounding strokes and deep breathing. The touch slowly becomes lighter and more sensual, and the whole body is included."),
        ("Do I need experience with tantra?", "No. You do not need any experience with tantra or meditation. Your masseuse guides you through the massage step by step."),
        ("How much is a tantra massage in Amsterdam?", "In Amsterdam, Schiphol, Haarlem and Hoofddorp the rate is € 160 for the first hour and € 160 for every extra hour. For tantra we advise two hours or more."),
    ]),
    "body-2-body-massage": ("Body to Body Massage Amsterdam | B2B at Your Hotel", "Body 2 Body Massage Amsterdam", [
        ("What is a body to body massage?", "In a body to body massage, also called B2B or body 2 body massage, your masseuse uses her whole body and plenty of warm oil to massage yours, skin to skin."),
        ("Is a body to body massage the same as a nuru massage?", "They are close relatives. Both are skin to skin massages in which the masseuse glides over your body. A nuru massage uses a special gel, a body to body massage uses warm massage oil."),
        ("What do I need to prepare?", "A shower before and after, and one or two large towels on the bed, because a lot of oil is used."),
    ]),
    "4-hands-massage": ("4 Hands Massage Amsterdam | Two Masseuses", "4 Hands Massage Amsterdam", [
        ("How does a 4 hands massage work?", "Two masseuses massage you at the same time. They mirror each other or work on different parts of your body, so you feel four hands in one rhythm."),
        ("Can I choose both masseuses?", "Yes. Mention both names in the chat and book a little ahead, because not every combination is free at every moment."),
        ("What does a 4 hands massage cost?", "You book two masseuses for the same time, so the rate differs from a massage with one masseuse. Ask for the rate in the chat and we confirm it before you book."),
    ]),
    "thai-massage": ("Thai Massage Amsterdam | With a Sensual Finish", "Thai Massage Amsterdam", [
        ("Is this a traditional Thai massage?", "The first part uses traditional Thai techniques: pressure along the muscles and gentle stretches. The second part is softer, with oil and a sensual finish."),
        ("Is a Thai massage painful?", "It is firmer than a sensual massage, but it should never hurt. You can always ask your masseuse for more or less pressure."),
        ("Can I have a Thai massage in my hotel room?", "Yes. Your masseuse comes to your hotel or home in Amsterdam and the surrounding area."),
    ]),
    "full-body-massage": ("Full Body Massage Amsterdam | At Your Hotel or Home", "Full Body Massage Amsterdam", [
        ("What is included in a full body massage?", "Neck, shoulders, back, arms, hands, legs and feet. No part of your body is skipped, and you decide whether the massage stays relaxing or becomes sensual."),
        ("How long does a full body massage take?", "One hour is enough for a complete massage. With two hours there is time to take it slowly and add a sensual massage."),
        ("Can I combine a full body massage with another massage?", "Yes. A popular combination is a full body massage followed by a body to body massage in a two hour booking."),
    ]),
}

HAPPY = {
    "title": "Happy Ending Massage Amsterdam | At Your Hotel or Home",
    "desc": "Happy ending massage in Amsterdam at your hotel or home. A full erotic massage by a masseuse you choose, with a relaxed and discreet finish. Booked by chat.",
    "lead": "A complete erotic massage at your hotel or home in Amsterdam, with the ending you are hoping for.",
    "body": [
        ("What is a happy ending massage?", ["A happy ending massage is an erotic massage that does not stop where a regular massage stops. It begins as a relaxing massage of your whole body and slowly becomes more sensual, until it ends with a release that leaves you completely relaxed.",
                                             "In Amsterdam the term is used for many different things. With us it simply means this: an unhurried erotic massage by an adult masseuse who enjoys her work, at your hotel or at home, with a happy ending as the natural finish."]),
        ("How does it go?", ["Your masseuse comes to you at the time you agreed in the chat. After a shower you lie down, and she starts with your back, shoulders and legs. There is no rush, and you can always say what you like.",
                             "When you turn over, the massage becomes lighter and more teasing. The happy ending is part of the massage, not something separate, so you never have to ask or negotiate."]),
        ("Which massage should I choose?", ["A happy ending is part of all our erotic massages. A sensual massage is soft and slow, a body to body massage is skin to skin, and a tantra massage builds up the tension for as long as possible. If you cannot choose, tell us what you like and we advise you."]),
        ("Discreet and respectful", ["Discretion is where every booking starts. Your details are used only to arrange your appointment. Our masseuses treat every guest with respect and expect the same in return."]),
    ],
    "faq": [
        ("Is a happy ending included in the price?", "Yes. A happy ending is part of our erotic massages and is included in the rate. In Amsterdam, Schiphol, Haarlem and Hoofddorp the rate is € 160 per hour."),
        ("Where does the massage take place?", "At your hotel or at your home. Our masseuses visit Amsterdam and many cities and towns around it."),
        ("Can I choose my masseuse?", "Yes. Browse the profiles, choose the masseuse you like and mention her name in the chat."),
        ("How do I book a happy ending massage in Amsterdam?", "Open the chat, choose live chat, WhatsApp or Telegram, and tell us your location, the time you prefer and the masseuse you like. We confirm everything before it is final."),
    ],
}

PKG_MORE = {
    "amsterdam-tour": ("Amsterdam Tour with Happy Ending | Tour & Erotic Massage", "Amsterdam is at its best when you see it with someone who knows the city. With this package you spend the first part of your time outside, and the second part in your hotel room.",
        [("Meet at your hotel", "Your masseuse meets you in the lobby or at a place you agree on in the chat."), ("Discover the city together", "Walk through the old centre and along the canals, or take a canal cruise. You decide the route and the pace."), ("Back to your room", "Afterwards you return to your hotel for the erotic massage of your choice, with a happy ending.")],
        ["Tickets for a cruise or museum and any drinks along the way are paid by you.", "Four hours is the minimum, so that neither the tour nor the massage feels rushed.", "Tell us in the chat what you would like to see, and we plan the timing with you."],
        [("Can I choose the route of the tour?", "Yes. Tell us what you would like to see, for example the canals, the Jordaan or the Red Light District, and we plan it with you."), ("Is the massage part of the four hours?", "Yes. The package is four hours in total. You decide how you divide the time between the tour and the massage.")]),
    "dinner-date": ("Dinner Date & Erotic Massage Amsterdam | Evening Package", "Some evenings deserve more than an hour. A dinner date gives you time to talk, laugh and get to know each other before the massage begins, and that makes everything afterwards better.",
        [("Choose your restaurant", "Pick a restaurant in Amsterdam or have dinner at your hotel. Your masseuse meets you there, dressed for the occasion."), ("Enjoy dinner together", "Take your time. Good food and good conversation are the best start of the evening."), ("End the evening in your room", "After dinner you go to your hotel for an unhurried erotic massage of your choice.")],
        ["The restaurant bill is paid by you.", "Three hours is the minimum. With four hours you do not have to watch the clock at the table.", "Let us know the restaurant and time in advance, so your masseuse can dress appropriately."],
        [("Can you recommend a restaurant?", "We are happy to think along. Tell us in the chat where you are staying and what kind of food you like."), ("What will my masseuse wear to dinner?", "She dresses stylishly and appropriately for the restaurant you choose. If you have a preference, mention it in the chat.")]),
    "amsterdam-by-night": ("Amsterdam by Night | Drinks & Erotic Massage", "Not hungry, but not in a hurry either? A drink together is the easiest way to break the ice. By the time you go upstairs, you already feel at ease with each other.",
        [("Meet for a drink", "At your hotel bar or a cocktail bar nearby. You choose the place."), ("Relax and get acquainted", "One or two drinks, no programme, no pressure."), ("Your massage", "Then you go to your room for a sensual or body to body massage.")],
        ["Drinks are paid by you.", "Two hours is the minimum; add an hour if you like to take your time.", "Often possible on the day itself, depending on availability."],
        [("Can I book this for tonight?", "Often you can. Send us a message in the chat with your hotel and the time you have in mind, and we tell you who is available."), ("Do we have to go out for the drink?", "No. Many guests choose the bar of their own hotel, or simply a drink in the room.")]),
    "schiphol-stopover": ("Schiphol Stopover Massage | Erotic Massage Airport Hotel", "A long layover or a night at an airport hotel does not have to be lost time. Your masseuse comes to your hotel at or near Schiphol, so you never have to go into the city.",
        [("Send your flight times", "Tell us in the chat when you land and when you have to leave again."), ("Your masseuse comes to your hotel", "She visits hotels at Schiphol and in Hoofddorp and Aalsmeer."), ("Relax before you fly", "An hour of massage and you board your next flight a different person.")],
        ["Possible at hotels at Schiphol, in Hoofddorp and in Aalsmeer.", "Book as early as you can if your time window is short.", "Extra time is € 160 per hour."],
        [("Is one hour enough?", "Yes. One hour is enough for a complete sensual or full body massage. If you have more time, you can add an hour."), ("Can I book before I land?", "Yes, and we recommend it. Send us your hotel and arrival time, and your masseuse is planned around your flight.")]),
    "jetlag-relief": ("Jetlag Relief Massage Amsterdam | Massage After Your Flight", "A long flight leaves its mark: a stiff neck, heavy legs and a head that will not switch off. This package tackles the body first, and the mind right after.",
        [("Arrive and shower", "Check in, take a warm shower and let us know you are ready."), ("First hour: full body massage", "Firm, calm strokes for your back, neck, shoulders and legs."), ("Second hour: sensual finish", "The pace drops, the touch becomes lighter, and the tension disappears completely.")],
        ["Two hours in total.", "Tell your masseuse where you feel the flight most.", "Most guests book this for their day of arrival."],
        [("Does a massage help against jetlag?", "A massage relaxes muscles that have been still for hours and helps you unwind, which makes it easier to fall asleep at the right time."), ("Can I book this late in the evening?", "Tell us your arrival time in the chat and we check which masseuse is available.")]),
    "after-work": ("After Work Massage Amsterdam | Late Evening at Your Hotel", "In Amsterdam for work? After a day of meetings, presentations or a trade fair, the best plan is no plan. Let your masseuse come to you.",
        [("One message in the chat", "Your hotel, the time and the massage you feel like."), ("We confirm", "You hear who is available and what the rate is."), ("Your masseuse arrives", "At your hotel or home. You only have to open the door.")],
        ["One hour, with the option to extend for € 160 per hour.", "At your hotel or at home.", "Discreet from first message to goodbye."],
        [("How late can I book?", "Tell us the time you have in mind. Availability in the late evening differs per day, and we answer in the chat straight away."), ("Can I pay for an extra hour on the spot?", "If your masseuse has time, you can extend. The extra hour rate is € 160.")]),
    "duo-deluxe": ("Duo Massage Amsterdam | 4 Hands with Two Masseuses", "One masseuse is a treat. Two is an experience you will talk about for a long time, even if only to yourself. Duo Deluxe gives you two masseuses for two full hours.",
        [("Choose two masseuses", "Pick your favourites from the profiles, or let us suggest a duo that works well together."), ("Four hands in rhythm", "They start with a 4 hands massage in which they mirror each other."), ("Body 2 body for two", "In the second part they take turns and work together, skin to skin.")],
        ["Two masseuses for two hours.", "The rate depends on the two masseuses you choose; ask for it in the chat.", "Book ahead, because both masseuses must be free at the same time."],
        [("Can I choose both masseuses myself?", "Yes. Mention both names in the chat. If one of them is not available, we suggest an alternative."), ("Is two hours necessary?", "It is what we recommend. With two masseuses there is a lot to experience, and one hour goes by very quickly.")]),
    "tantra-ritual": ("Tantra Ritual Amsterdam | Extended Tantra Massage", "A tantra massage needs time. In this ritual nothing is hurried: every stage of the massage gets the attention it deserves.",
        [("Arrive in the moment", "The ritual starts with breathing and calm, grounding touch."), ("Slow build-up", "The whole body is massaged, with long strokes that become lighter and more sensual."), ("The finish", "Tension is built up, released and built up again, until the massage reaches its natural ending.")],
        ["From two hours; three hours is ideal.", "No experience with tantra is needed.", "A quiet room and a phone on silent make a real difference."],
        [("What makes this different from a regular tantra massage?", "The length. With two or three hours the build-up is much slower, and the experience is deeper."), ("Is a tantra ritual suitable for beginners?", "Yes. Your masseuse guides you, and you only have to follow your breathing.")]),
    "bath-and-massage": ("Bath & Massage Amsterdam | Bath or Shower with Body 2 Body", "Warm water is the best start of any massage. It relaxes your muscles, clears your head and breaks the ice in the most natural way.",
        [("Start in the water", "Together in the bath, or under a warm shower."), ("Dry off and lie down", "Towels on the bed, warm oil within reach."), ("Body 2 body massage", "Skin to skin, with slow gliding movements from head to toe.")],
        ["Two hours in total.", "You need a hotel room or home with a bathtub or a spacious shower.", "Have a few extra large towels ready."],
        [("My room only has a shower. Is that a problem?", "Not at all. A spacious shower works just as well as a bath."), ("Do I need to bring anything?", "Only towels. Ask your hotel for a few extra if needed.")]),
    "champagne-evening": ("Champagne Evening Amsterdam | Champagne & Sensual Massage", "For a birthday, a closed deal, or no reason at all. Three hours with champagne, good company and a long sensual massage.",
        [("Open the bottle", "Order champagne through your hotel or bring your own, and toast to the evening."), ("Take your time", "Conversation, music, strawberries. There is no schedule."), ("A long sensual massage", "The massage is spread over the evening, with all the time you need.")],
        ["Three hours in total.", "Champagne and snacks are ordered and paid by you.", "A hotel room with a seating area makes the evening complete."],
        [("Is the champagne included?", "No. You order it through your hotel or bring it yourself, so you can choose exactly what you like."), ("Can I extend the evening?", "Yes, if your masseuse has time. Every extra hour is € 160.")]),
    "couples-massage": ("Couples Massage Amsterdam | Erotic Massage for Two", "Sharing an erotic massage is a special experience for a couple. You both relax, you both enjoy, and you take that feeling home with you.",
        [("Tell us your wishes", "One masseuse or two, and what you are both comfortable with."), ("We advise and confirm", "You hear which masseuses are open to couples and what the rate is."), ("Your massage", "At your hotel or at home, side by side or one after the other.")],
        ["For couples.", "With one or two masseuses.", "Everything is discussed beforehand, so there are no surprises."],
        [("Do you offer massages for couples?", "Yes. Tell us in the chat that you are booking as a couple, and we select masseuses who enjoy that."), ("Can we be massaged at the same time?", "With two masseuses, yes. With one masseuse you take turns, or she divides her attention between you.")]),
    "massage-lesson": ("Sensual Massage Lesson for Couples Amsterdam", "A massage is over after an evening. Knowing how to give one lasts a lifetime. In this lesson you learn from an experienced masseuse how to massage each other.",
        [("The basics", "How to use oil, pressure and rhythm, and how to make the other person feel at ease."), ("Practise on each other", "First one of you, then the other, with your masseuse guiding your hands."), ("Make it sensual", "The slow strokes and the build-up that turn a relaxing massage into a sensual one.")],
        ["Two hours for two people.", "At your hotel or at home.", "A nice gift for an anniversary or a weekend in Amsterdam."],
        [("Do we need experience?", "No. The lesson starts with the basics and adapts to your pace."), ("Is this also possible for one person?", "Yes. Tell us in the chat and we adapt the lesson.")]),
    "birthday-surprise": ("Birthday Surprise Amsterdam | Erotic Massage as a Gift", "Looking for a gift he will not see coming? Any of our packages can be booked as a surprise, for a birthday, a bachelor weekend or a celebration.",
        [("Choose a package", "From one hour of massage to a dinner date or a duo."), ("Give us the details", "The date, the hotel or address, and the name of the lucky one."), ("We arrange the rest", "Discreetly, and in consultation with you.")],
        ["Any package can be given as a gift.", "Book in advance so we can plan the surprise.", "The rate depends on the package you choose."],
        [("Can I pay for someone else?", "Yes. Tell us in the chat that it is a gift and we explain how it works."), ("Does the birthday boy have to know?", "It is up to you. For a home address we always check that the visit is welcome.")]),
}


def info_pages():
    urls = []
    inner = (f'<section class="sec"><div class="wrap narrow prose"><p>Our rates depend on the location of your visit. The price is for one hour unless a minimum number of hours is shown. Every extra hour is € 160. Your rate is always confirmed in the chat before you book.</p>{price_table(PRICES)}'
             '<h2>Good to know</h2><ul class="ticks"><li>The rate is per masseuse. For a 4 hands massage with two masseuses, ask for the rate in the chat.</li>'
             '<li>For cities further away we work with a minimum number of hours, shown in the table.</li>'
             '<li>Is your city not listed? Ask us in the chat.</li></ul></div></section>' + cta("Ask for your rate in the chat. We confirm it before you book."))
    pr_html, pr_schema = faq_block([("How much is an erotic massage in Amsterdam?", "In Amsterdam, Schiphol, Haarlem and Hoofddorp the rate is € 160 for one hour. Every extra hour is € 160."),
                                    ("Is a happy ending included in the price?", "Yes. A happy ending is part of our erotic massages and is included in the rate."),
                                    ("Are there extra costs?", "No. The rate in the table is the rate for the visit of your masseuse at that location. For packages, things like dinner, drinks and tickets are paid by you."),
                                    ("Why is the price higher outside Amsterdam?", "Your masseuse travels from Amsterdam to you. For cities further away the rate is higher or a minimum number of hours applies.")], "Questions about our prices")
    inner = inner.replace(cta("Ask for your rate in the chat. We confirm it before you book."), pr_html + cta("Ask for your rate in the chat. We confirm it before you book.") + '<section class="sec"><div class="wrap">' + link_row("Popular packages", TOP_PKG).replace(' class="mt"', "") + "</div></section>")
    urls.append(sub("/prices/", "Erotic Massage Amsterdam Prices | From € 160 per Hour",
                    "Prices for erotic massage at your hotel or home: € 160 in Amsterdam, Schiphol, Haarlem and Hoofddorp, € 160 per extra hour. Rates for all other cities.",
                    "Prices", "Clear rates per location, confirmed before you book.", inner, [], [pr_schema]))

    groups = []
    for p in PACKAGES:
        if p[0] not in groups:
            groups.append(p[0])
    secs = ""
    for i, g in enumerate(groups):
        cards = "".join(pkg_card(p) for p in PACKAGES if p[0] == g)
        secs += f'<section class="sec{" sec-alt" if i % 2 else ""} sec-c"><div class="wrap"><h2>{E(g)}</h2><ul class="pkgs">{cards}</ul></div></section>'
    hours = [("One hour", "€ 160", "One massage of your choice with one masseuse. A good choice for a first visit."),
             ("Two hours", "€ 320", "Time to combine two massages, for example a full body massage followed by a body 2 body massage."),
             ("Three hours", "€ 480", "A long, slow evening without looking at the clock. Ideal for a tantra massage.")]
    tiles = "".join(f'<li><div class="tile"><h3>{E(n)}</h3><p class="price">{E(p)}</p><p>{E(d)}</p></div></li>' for n, p, d in hours)
    pfaq = [("Is a happy ending included in the packages?", "Every package ends with an erotic massage of your choice, and a happy ending is part of our erotic massages."),
            ("What is included in the price?", "The price is for the time of your masseuse in Amsterdam, Schiphol, Haarlem or Hoofddorp. Restaurant bills, drinks, champagne and tickets for a cruise or museum are paid by you. For other cities see the prices page."),
            ("Can I change a package?", "Yes. Every package is a starting point. Add an hour, choose another massage or combine two packages, and we confirm the rate in the chat before you book."),
            ("How do I book a package?", "Open the chat, tell us which package you would like, your hotel or address, the date and time, and the masseuse you prefer. We confirm everything before it is final.")]
    fq = "".join(f"<details><summary>{E(q)}</summary><p>{E(a)}</p></details>" for q, a in pfaq)
    inner = (secs + '<section class="sec sec-c"><div class="wrap"><h2>Just a massage</h2><p class="intro">Prefer to keep it simple? Book by the hour and choose your massage on the day.</p>'
             f'<ul class="tiles">{tiles}</ul><p class="note">Rates for Amsterdam, Schiphol, Haarlem and Hoofddorp: € 160 for the first hour and € 160 for every extra hour. For other cities see the <a href="/prices/">prices</a> page.</p></div></section>'
             f'<section class="sec sec-alt sec-c"><div class="wrap narrow"><h2>Questions about our packages</h2><div class="faq">{fq}</div></div></section>' + cta("Tell us which package you would like. We confirm masseuse, time and rate before you book."))
    for p in PACKAGES:
        g, pid, name, dur, price, photo, d, inc = p
        p_title, p_intro, flow, know, pq = PKG_MORE[pid]
        pq = pq + [("What does this package cost?", (f"{name} is {price.lower()} ({dur.lower()}) in Amsterdam, Schiphol, Haarlem and Hoofddorp. " if "€" in price else f"The rate for {name} depends on your choices. ") + "Every extra hour is € 160, and we confirm your rate in the chat before you book."),
                   ("How do I book?", "Open the chat, tell us which package you would like, your hotel or address, the date and time, and the masseuse you prefer. We confirm everything before it is final.")]
        pf_html, pf_schema = faq_block(pq, f"Questions about {name}")
        steps = "".join(f"<li><h3>{E(t)}</h3><p>{E(x)}</p></li>" for t, x in flow)
        related = [x for x in PACKAGES if x[0] == g and x[1] != pid] + [x for x in PACKAGES if x[0] != g][:2]
        rel = "".join(f'<li><a href="/packages/{x[1]}/">{E(x[2])}</a></li>' for x in related)
        ml = "".join(f'<li><a href="/{s}/">{E(n)}</a></li>' for s, n, _ in MASSAGES)
        inner = (f'<section class="sec"><div class="wrap split"><div class="split-img">{pic(photo, name, 600, 400, eager=True)}</div>'
                 f'<div class="prose"><p class="pkg-m"><span>{E(dur)}</span><strong>{E(price)}</strong></p><h2>{E(name)}</h2><p>{E(d)}</p><p>{E(p_intro)}</p>'
                 f'<p><a class="btn" href="/contact/" data-chat>Book this package</a> <a class="link" href="/packages/">All packages</a></p></div></div></section>'
                 f'<section class="sec sec-alt sec-c"><div class="wrap"><h2>How it works</h2><ol class="steps">{steps}</ol></div></section>'
                 f'<section class="sec"><div class="wrap narrow prose"><h2>What is included</h2><ul class="ticks">{"".join(f"<li>{E(x)}</li>" for x in inc)}</ul>'
                 f'<h2>Good to know</h2><ul class="ticks">{"".join(f"<li>{E(x)}</li>" for x in know)}</ul>'
                 f'<h2>Choose your massage</h2><p>Every package includes an erotic massage of your choice, with a happy ending. Read more about each massage:</p><ul class="chips">{ml}<li><a href="/happy-ending-massage/">Happy Ending Massage</a></li></ul></div></section>'
                 f'{pf_html}{cta(f"Book {name} in the chat. We confirm masseuse, time and rate before you book.")}'
                 f'<section class="sec"><div class="wrap"><h2>Choose your masseuse</h2><ul class="cards">{"".join(card(m) for m in MASSEUSES[:10])}</ul><p class="center"><a class="link" href="/our-masseuses/">View all masseuses</a></p>'
                 f'<h2 class="mt">More packages</h2><ul class="chips">{rel}<li><a href="/packages/">All packages</a></li></ul></div></section>')
        p_desc = (d[:150].rsplit(" ", 1)[0] + "…") if len(d) > 155 else d
        svc = {"@context": "https://schema.org", "@type": "Service", "name": name, "serviceType": "Erotic massage package", "description": d,
               "provider": {"@id": SITE + "/#org"}, "areaServed": {"@type": "City", "name": "Amsterdam"}, "url": f"{SITE}/packages/{pid}/"}
        urls.append(sub(f"/packages/{pid}/", p_title, p_desc, name, f"{dur} · {price}", inner, [("Packages", "/packages/")], [svc, pf_schema]))
    cat = {"@context": "https://schema.org", "@type": "ItemList", "name": "Erotic massage packages in Amsterdam", "itemListElement": [
        {"@type": "ListItem", "position": i + 1, "name": p[2], "url": f"{SITE}/packages/{p[1]}/"} for i, p in enumerate(PACKAGES)]}
    fqs = {"@context": "https://schema.org", "@type": "FAQPage", "mainEntity": [{"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in pfaq]}
    urls.append(sub("/packages/", "Erotic Massage Packages Amsterdam | Dinner Date & Tour",
                    "Erotic massage packages in Amsterdam: dinner date, Amsterdam tour with happy ending, Schiphol stopover, duo, tantra ritual and couples massage. Booked by chat.",
                    "Packages", "Thirteen ways to combine an erotic massage with a great day or night in Amsterdam.", inner, [], [cat, fqs]))

    inner = ('<section class="sec"><div class="wrap narrow prose"><h2>Booking in three steps</h2><ol class="steps steps-col">'
             '<li><h3>Open the chat</h3><p>Use the Direct contact button and choose live chat, WhatsApp or Telegram.</p></li>'
             '<li><h3>Tell us what you would like</h3><p>Your hotel or address, the day and time, the number of hours, and the massage and masseuse you prefer.</p></li>'
             '<li><h3>Receive your confirmation</h3><p>We confirm the masseuse, the time and the rate. Your masseuse then comes to you at the agreed time.</p></li></ol>'
             '<h2>Preparing for your massage</h2><ul class="ticks"><li>Take a shower before your masseuse arrives.</li><li>Have one or two clean, large towels ready.</li>'
             '<li>If you are in a hotel, tell us your room number and make sure your masseuse can come up.</li><li>Put your phone on silent and enjoy.</li></ul>'
             '<h2>Changing or cancelling</h2><p>Plans change. If you need to move or cancel your booking, let us know in the chat as early as you can, so we can inform your masseuse.</p>'
             '<h2>Respect and discretion</h2><p>Our masseuses treat every guest with respect and expect the same in return. Your details are used only to arrange your appointment.</p></div></section>' + cta())
    bk_html, bk_schema = faq_block([("How quickly can a masseuse be with me?", "That depends on the time of day and on who is available. Tell us your location and preferred time in the chat and we answer straight away."),
                                    ("Can I book for today?", "Often you can. For a specific masseuse or a longer package we recommend booking ahead."),
                                    ("Which details do you need from me?", "Your hotel and room number or your address, the day and time, the number of hours, and the massage and masseuse you prefer."),
                                    ("Is my booking discreet?", "Yes. Your details are used only to arrange your appointment and are not shared.")], "Questions about booking")
    inner = inner.replace(cta(), bk_html + cta())
    urls.append(sub("/bookings/", "Book an Erotic Massage in Amsterdam | Bookings",
                    "Book an erotic massage in Amsterdam by chat: live chat, WhatsApp or Telegram. Tell us your hotel, time and masseuse and we confirm before anything is final.",
                    "Bookings", "Booking takes one message. Here is how it works.", inner, [], [bk_schema]))

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
