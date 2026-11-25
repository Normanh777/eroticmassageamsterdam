# Profile facts taken from the owner's own site passionescorts.nl (height, eye colour, build, style, languages).
_RAW = """bianca|167|blauwe|slanke|Engels|romantisch/speels
sophie|160|bruine||Engels/Italiaans/Spaans|
rosalie|165|blauwe|slank|Engels|
roanna|170|bruine||Engels|elegant
nina|168|groene|vrouwelijke|Nederlands/Engels|
miki|168|bruine|slanke|Engels|passievol
lunnie|153|bruine||Engels|natuurlijk/spontaan
lucy|166|bruine||Engels/Spaans|natuurlijk/spontaan
izabelle|176|bruine|slanke|Engels/Frans/Spaans/Italiaans/Nederlands|
clarissa|165|bruine|slanke|Engels|natuurlijk
catalina|173||slank|Engels/Spaans|
brianna|173|bruine|slanke|Engels|passievol
angella|160|bruine|slanke|Engels/Frans/Spaans|
stephanie|165|||Engels|
roxy|168|blauwe|volle vrouwelijke|Engels|
pandora|158||slanke|Engels|
nicole|167|bruine||Engels|mysterieus/passievol
michelle|168|bruine||Engels/Nederlands|elegant/passievol
megan|170|bruine|slanke|Engels|
mary|168||slank|Engels|
lora|165|bruine||Engels|natuurlijk
livana|167|bruine||Engels|natuurlijk/zorgzaam
lisa|175|blauwe|slanke|Engels|
lexi|164|bruine|slanke|Engels|
lavinia|170|bruine||Engels|natuurlijk
kimberly|182|||Engels|
kim|168|blauwe|slanke|Engels|
katy|165|bruine||Nederlands/Engels|elegant/spontaan
joy|169|bruine|slanke|Engels|
jenn|171|bruine|slanke|Engels|spontaan
jeniffer|172|bruine||Engels|
ines|170|bruine||Engels|
denise|164|blauwe|slanke|Engels|
denisa|170|groene|slanke|Engels|
dalya|166|blauwe|slanke|Engels|
cleopatra|163|bruine||Engels|
cleo|160|bruine||Engels|
celine|175|bruine|slanke|Engels|
ariel|160|bruine||Engels|
angel|164|bruine||Engels|
anely|165|blauwe|slanke|Engels|
anda|168|blauwe|slanke|Engels|
amanda|170|groene||Engels|speels/passievol
alexandra|168|bruine||Engels|
alessia|160|bruine|slanke|Engels|
alee|176|blauwe||Engels|spontaan
adda|170|bruine||Engels|elegant/passievol
vicky|180|bruine|slanke|Engels|mysterieus/passievol
olga|169|blauwe|slank|Engels|natuurlijk/passievol"""
_EYE = {"blauwe": "Blue", "bruine": "Brown", "groene": "Green"}
_BUILD = {"slanke": "Slim", "slank": "Slim", "volle vrouwelijke": "Curvy", "vrouwelijke": "Feminine"}
_TAG = {"romantisch": "romantic", "speels": "playful", "elegant": "elegant", "passievol": "passionate", "natuurlijk": "natural",
        "spontaan": "spontaneous", "mysterieus": "mysterious", "zorgzaam": "caring"}
_LANG = {"Engels": "English", "Nederlands": "Dutch", "Spaans": "Spanish", "Italiaans": "Italian", "Frans": "French"}
TAGS_NL.update({"spontaneous": "spontaan", "caring": "zorgzaam", "elegant": "elegant"})
EYES_NL = {"Blue": "Blauw", "Brown": "Bruin", "Green": "Groen"}
BUILD_NL = {"Slim": "Slank", "Curvy": "Vol", "Feminine": "Vrouwelijk"}
PLANGS = {}
for _row in _RAW.splitlines():
    _s, _h, _e, _b, _l, _t = _row.split("|")
    _x = {"Height": f"{_h} cm"}
    if _e:
        _x["Eyes"] = _EYE[_e]
    if _b:
        _x["Build"] = _BUILD[_b]
    EXTRA[_s] = _x
    if _t:
        TAGS[_s] = [_TAG[t] for t in _t.split("/")]
    PLANGS[_s] = [_LANG[x] for x in _l.split("/")]
# add languages the other site lists and this one did not yet have
for _i, _m in enumerate(MASSEUSES):
    _have = [x for x in _m[3].split(", ") if x] if _m[3] else []
    _add = [x for x in PLANGS.get(_m[0], []) if x not in _have]
    if _add:
        MASSEUSES[_i] = (_m[0], _m[1], _m[2], ", ".join(_have + _add), _m[4])


def fact_line(slug, name, i, nl=False):
    x = EXTRA.get(slug)
    if not x or "Height" not in x:
        return ""
    cm = x["Height"].split()[0]
    m = f"{cm[0]},{cm[1:]}" if nl else f"{cm[0]}.{cm[1:]}"
    eyes, build = x.get("Eyes"), x.get("Build")
    if nl:
        e = {"Blue": "blauwe", "Brown": "bruine", "Green": "groene"}.get(eyes)
        b = {"Slim": "een slank postuur", "Curvy": "volle, vrouwelijke vormen", "Feminine": "een vrouwelijk postuur"}.get(build)
        parts = [p for p in (f"{e} ogen" if e else None, b) if p]
        tail = (" en heeft " + " en ".join(parts)) if parts else ""
        return [f"{name} is {m} meter lang{tail}.",
                f"Met {m} meter is {name} {'een van onze langere masseuses' if int(cm) >= 175 else 'een van onze kleinere masseuses' if int(cm) <= 160 else 'niet groot en niet klein'}{'; ze heeft ' + ' en '.join(parts) if parts else ''}.",
                f"Goed om te weten: {name} is {m} meter lang{tail}.",
                f"In het kort: {m} meter lang" + ("".join(", " + p for p in parts)) + "."][i % 4]
    e = eyes.lower() if eyes else None
    b = {"Slim": "a slim figure", "Curvy": "full, feminine curves", "Feminine": "a feminine figure"}.get(build)
    parts = [p for p in (f"{e} eyes" if e else None, b) if p]
    tail = (" and has " + " and ".join(parts)) if parts else ""
    return [f"{name} is {m} m tall{tail}.",
            f"At {m} m, {name} is {'one of our taller masseuses' if int(cm) >= 175 else 'one of our more petite masseuses' if int(cm) <= 160 else 'neither tall nor small'}{'; she has ' + ' and '.join(parts) if parts else ''}.",
            f"Good to know: {name} is {m} m tall{tail}.",
            f"In short: {m} m tall" + ("".join(", " + p for p in parts)) + "."][i % 4]
