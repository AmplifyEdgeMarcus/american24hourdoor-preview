#!/usr/bin/env python3
"""Generates the static site. Edit the NAP block below once and rebuild from the repo root: python3 _build/build.py"""
import json, os, html
# HTML is published at the repo root (parent of this _build/ folder) for GitHub Pages.
OUT = os.path.join(os.path.dirname(__file__), '..')

# ---- NAP: single source of truth (must match Google Business Profile exactly) ----
NAME = "American 24 Hour Door Service"
STREET = "4116 Bent Rd"
CITY = "Kodak"
STATE = "TN"
ZIP = "37764"
PHONE = "(800) 780-6665"
TEL = "+18007806665"
EMAIL = "ar@just4doors.com"
SITE_URL = "https://www.american24hourdoor.com"   # [CONFIRM final domain]
# PREVIEW / NOINDEX: temporary client preview. True emits noindex on every page.
# Set False and rebuild before the real launch on the final domain.
PREVIEW_NOINDEX = True
GOOGLE_REVIEWS_URL = "#GOOGLE-REVIEWS-LINK"          # [PLACEHOLDER]
YEAR_FOUNDED = "[Year founded]"                      # [PLACEHOLDER] sources conflict: 1992 vs 1998
ADDR_LINE = f"{STREET}, {CITY}, {STATE} {ZIP}"
MAP_Q = "4116%20Bent%20Rd%2C%20Kodak%2C%20TN%2037764"

STAR = '<svg class="st" viewBox="0 0 24 24" aria-hidden="true"><polygon fill="currentColor" points="12,1.5 14.7,8.6 22.3,8.9 16.3,13.6 18.4,20.9 12,16.7 5.6,20.9 7.7,13.6 1.7,8.9 9.3,8.6"/></svg>'
STRIPES = '<div class="stripes" aria-hidden="true"></div>'
I = {  # inline icons (stroke)
 'star': STAR,
 'phone':'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M22 16.9v3a2 2 0 0 1-2.2 2 19.8 19.8 0 0 1-8.6-3.1 19.5 19.5 0 0 1-6-6A19.8 19.8 0 0 1 2.1 4.2 2 2 0 0 1 4.1 2h3a2 2 0 0 1 2 1.7c.1 1 .4 1.9.7 2.8a2 2 0 0 1-.5 2.1L8 9.9a16 16 0 0 0 6 6l1.3-1.3a2 2 0 0 1 2.1-.4c.9.3 1.8.6 2.8.7a2 2 0 0 1 1.7 2z"/></svg>',
 'clock':'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><circle cx="12" cy="12" r="9.5"/><path d="M12 6.5V12l3.5 2.2"/></svg>',
 'truck':'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M1.5 5.5h12.5v10H1.5z"/><path d="M14 9h4.5l3 3.5v3H14z"/><circle cx="6" cy="17.5" r="2"/><circle cx="17.5" cy="17.5" r="2"/></svg>',
 'tools':'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M14.7 6.3a1 1 0 0 0 0 1.4l1.6 1.6a1 1 0 0 0 1.4 0l3.8-3.8a6 6 0 0 1-7.9 7.9l-6.9 6.9a2.1 2.1 0 0 1-3-3l6.9-6.9a6 6 0 0 1 7.9-7.9z"/></svg>',
 'home':'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M3 10.5 12 3l9 7.5"/><path d="M5 9v11h14V9"/><path d="M9 20v-6h6v6"/></svg>',
 'store':'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M3 9h18l-1.5-5h-15z"/><path d="M4 9v11h16V9"/><path d="M10 20v-7h4v7"/></svg>',
 'dollar':'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M12 2v20"/><path d="M17 5.5H9.5a3.5 3.5 0 0 0 0 7h5a3.5 3.5 0 0 1 0 7H6"/></svg>',
 'shield':'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"/><path d="m9 12 2 2 4-4"/></svg>',
 'board':'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><rect x="3" y="3" width="18" height="18" rx="1.5"/><path d="M3 9h18M3 15h18"/></svg>',
 'check':'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="3" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M5 12.5l4.5 4.5L19 7.5"/></svg>',
 'pin':'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M12 22s7-6.2 7-12a7 7 0 0 0-14 0c0 5.8 7 12 7 12z"/><circle cx="12" cy="10" r="2.6"/></svg>',
 'menu':'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" aria-hidden="true"><path d="M4 7h16M4 12h16M4 17h16"/></svg>',
 'mail':'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><rect x="2.5" y="4.5" width="19" height="15" rx="2"/><path d="m3 6 9 7 9-7"/></svg>',
}

# ---- Service areas (from american24hourdoor.com/door-service-locations + home page) ----
# Tennessee statewide (Marc confirmed 2026-11-11). East TN towns are from the old site; Middle/West TN metros added for statewide coverage.
TN_REGIONS = [
 ("East Tennessee", "Headquarters region", [
   ("Sevier County (HQ)", ["Sevierville","Pigeon Forge","Gatlinburg","Kodak"], True),
   ("Knoxville area", ["Knoxville","Farragut","Oak Ridge","Clinton","Maryville","Alcoa","Rockwood"], False),
   ("Lakeway &amp; Tri-Cities", ["Morristown","Jefferson City","Newport","Greeneville","Kingsport","Johnson City","Bristol"], False),
   ("Southeast TN", ["Lenoir City","Loudon","Sweetwater","Athens","Cleveland","Chattanooga"], False),
 ]),
 ("Middle Tennessee", "", [("", ["Nashville","Murfreesboro","Clarksville","Franklin","Cookeville","Columbia","Tullahoma"], False)]),
 ("West Tennessee", "", [("", ["Memphis","Jackson","Bartlett","Dyersburg"], False)]),
]
# Beyond TN: states named on the old site (towns where listed). Ohio omitted: named once, no towns, does not border TN. [CONFIRM with client]
BEYOND = [("Georgia","Dalton"),("North Carolina","Asheville, Fletcher, Hendersonville, Waynesville, Weaverville, Mars Hill"),("Virginia","Bristol"),("Kentucky",""),("Alabama",""),("Mississippi","")]
BEYOND_LINE = "Serving Tennessee and neighboring states including Georgia, North Carolina, Virginia, Kentucky, Alabama and Mississippi."
BRANDS = [("LiftMaster","Garage door openers"),("Tubelite","Storefront systems"),("Kawneer","Storefront systems"),("YKK AP","Storefront systems"),("Vista Wall","Storefront systems"),("Detex","Exit alarms &amp; hardware")]

FAQ = [
 ("Are you really available 24 hours a day?", f"Yes. We operate 24 hours a day, 7 days a week, including holidays. Call {PHONE} any time and a technician will be dispatched. Regular office hours are Monday–Friday, 8:00 am–5:00 pm; emergency rates apply after hours."),
 ("How fast can a technician get to me?", "Our technicians are dispatched by phone from fully equipped service vehicles and can often be on site within three hours of your call, depending on your location and call volume."),
 ("Do you work on both homes and businesses?", "Yes. We handle residential garage doors, openers and entry doors, plus commercial storefronts, automatic and ADA doors, hollow metal doors, rolling steel doors and security gates."),
 ("Can you secure my property after a break-in or storm?", "Yes. We provide emergency board-up to secure broken glass, doors and storefronts until permanent repairs are made, and we can provide documentation to support your insurance claim."),
 ("What types of garage doors do you repair?", "We repair all major types of garage doors, including sectional, roll-up, tilt-up and custom doors, and we work on a wide range of brands and opener systems."),
 ("What areas do you serve?", "We serve the entire state of Tennessee, East, Middle and West, from our headquarters in Kodak (Sevier County), near Sevierville. We also work in neighboring states including Georgia, North Carolina, Virginia, Kentucky, Alabama and Mississippi. Call (800) 780-6665 to confirm service at your location."),
 ("Do you offer preventative maintenance?", "Yes. Preventative maintenance programs help extend the life of your doors by inspecting components, lubricating moving parts, tightening hardware and catching problems before they become costly repairs."),
]

NAV = [("index.html","Home"),("services.html","Services"),("service-areas.html","Service Areas"),("about.html","About"),("contact.html","Contact")]

def schema(page_url, extra=None):
    data = {
      "@context":"https://schema.org",
      "@type":["HomeAndConstructionBusiness","LocalBusiness"],
      "@id": SITE_URL + "/#business",
      "name": NAME, "url": SITE_URL + "/",
      "telephone": "+1-800-780-6665", "email": EMAIL,
      "image": SITE_URL + "/assets/brand/og-image.jpg", "logo": SITE_URL + "/assets/brand/icon-512.png",
      "address":{"@type":"PostalAddress","streetAddress":STREET,"addressLocality":CITY,"addressRegion":STATE,"postalCode":ZIP,"addressCountry":"US"},
      "geo":{"@type":"GeoCoordinates","latitude":35.960794,"longitude":-83.632696},
      "openingHoursSpecification":[{"@type":"OpeningHoursSpecification","dayOfWeek":["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"],"opens":"00:00","closes":"23:59"}],
      "areaServed":[{"@type":"State","name":st} for st in ["Tennessee","Georgia","North Carolina","Virginia","Kentucky","Alabama","Mississippi"]],
      "knowsAbout":["Garage door repair","Commercial door repair","Storefront glass replacement","Automatic doors","Emergency board-up","Hollow metal doors","Door hardware"],
      "priceRange":"$$",
    }
    out = [data]
    if extra: out.append(extra)
    return "\n".join(f'<script type="application/ld+json">{json.dumps(d, ensure_ascii=False)}</script>' for d in out)

def head(title, desc, path, extra_schema=None):
    url = SITE_URL + "/" + ("" if path=="index.html" else path)
    robots = (
        '<meta name="robots" content="noindex, nofollow, noarchive">\n'
        '<meta name="googlebot" content="noindex, nofollow">\n'
        if PREVIEW_NOINDEX else ""
    )
    return f'''<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
{robots}<title>{title}</title>
<meta name="description" content="{desc}">
<link rel="canonical" href="{url}">
<meta property="og:type" content="website"><meta property="og:title" content="{title}"><meta property="og:description" content="{desc}">
<meta property="og:url" content="{url}"><meta property="og:image" content="{SITE_URL}/assets/brand/og-image.jpg"><meta property="og:site_name" content="{NAME}">
<meta name="theme-color" content="#0A3161">
<link rel="icon" type="image/png" sizes="32x32" href="assets/brand/favicon-32.png"><link rel="icon" type="image/svg+xml" href="assets/brand/icon.svg"><link rel="apple-touch-icon" href="assets/brand/apple-touch-icon.png">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Barlow+Condensed:wght@600;700;800&family=Barlow:wght@400;500;600;700&display=swap" rel="stylesheet">
<link rel="stylesheet" href="css/styles.css">
{schema(url, extra_schema)}
</head>
<body>
<a class="skip" href="#main">Skip to content</a>
'''

def header(active):
    links = "".join(f'<li><a href="{h}"{" aria-current=\"page\"" if h==active else ""}>{t}</a></li>' for h,t in NAV)
    return f'''<div class="topbar"><div class="wrap"><span class="pulse" aria-hidden="true"></span><span>24/7 Emergency Door Service<span class="tb-x"> — Nights, Weekends &amp; Holidays</span></span> <a href="tel:{TEL}">{PHONE}</a></div></div>
<header class="header">
  <div class="wrap">
    <a class="brand" href="index.html" aria-label="{NAME} home"><img src="assets/brand/logo.svg" alt="{NAME} logo — Commercial &amp; Residential" width="300" height="82"></a>
    <nav class="nav" aria-label="Main"><ul>{links}</ul></nav>
    <a class="head-call" href="tel:{TEL}"><small>24/7 Emergency Service</small><strong>{PHONE}</strong></a>
    <div class="head-actions">
      <a class="mobile-call" href="tel:{TEL}">{I['phone']}<span>Call 24/7</span></a>
      <button class="menu-btn" aria-expanded="false" aria-controls="mnav" aria-label="Open menu">{I['menu']}</button>
    </div>
  </div>
  <nav class="mnav" id="mnav" aria-label="Mobile"><ul>{links}<li><a href="tel:{TEL}" style="color:var(--red)">Call {PHONE}</a></li></ul></nav>
</header>
<main id="main">
'''

def cta_band():
    return STRIPES + f'''<section class="cta" aria-labelledby="cta-h"><div class="wrap">
  <div><span class="cta-kicker">{STAR}{STAR}{STAR}</span><h2 id="cta-h">Door won’t open, close or lock?</h2><p>Call now. A technician is on call 24 hours a day, 7 days a week, including holidays.</p></div>
  <div class="cta-btns"><a class="btn btn-white btn-lg" href="tel:{TEL}">{I['phone']} {PHONE}</a><a class="btn btn-outline btn-lg" href="contact.html">Request Service</a></div>
</div></section>
'''

def footer():
    svc = ["Garage Door Repair","Storefront Doors &amp; Glass","Automatic &amp; ADA Doors","Emergency Board-Up","Rolling Steel &amp; Security Gates","Locks &amp; Door Hardware"]
    return f'''</main>
<footer class="footer">
  <div class="foot-stripes" aria-hidden="true"></div>
  <div class="wrap">
    <div class="fgrid">
      <div>
        <img class="logo" src="assets/brand/logo-reverse.svg" alt="{NAME} logo" width="230" height="63" loading="lazy">
        <p>Commercial and residential door repair, installation and 24/7 emergency service across all of Tennessee and neighboring states, from our headquarters in East Tennessee.</p>
        <p class="motto">{STAR} Hometown service, American values {STAR}</p>
      </div>
      <div>
        <h4>Contact</h4>
        <address><strong style="color:#fff">{NAME}</strong><br>{STREET}<br>{CITY}, {STATE} {ZIP}<br>
        <a class="fphone" href="tel:{TEL}">{PHONE}</a><br><a href="mailto:{EMAIL}">{EMAIL}</a></address>
      </div>
      <div>
        <h4>Hours</h4>
        <ul><li><strong style="color:#fff">Open 24 hours, 7 days</strong></li><li>Including holidays</li><li>Office: Mon–Fri, 8:00 am–5:00 pm</li></ul>
      </div>
      <div>
        <h4>Services</h4>
        <ul>{"".join(f'<li><a href="services.html">{s}</a></li>' for s in svc)}</ul>
      </div>
    </div>
    <div class="foot-stars" aria-hidden="true">{STAR}{STAR}{STAR}{STAR}{STAR}</div>
    <div class="legal"><span>© <span id="yr">2026</span> {NAME}. All rights reserved.</span><span>HQ in Kodak (Sevier County), TN · Serving all of Tennessee &amp; neighboring states</span></div>
  </div>
</footer>
<div class="callbar"><a class="c1" href="tel:{TEL}">{I['phone']} Call 24/7</a><a class="c2" href="contact.html">Request Service</a></div>
<script src="js/main.js" defer></script>
</body>
</html>
'''

def faq_html(items):
    return "".join(f'<details><summary>{q}</summary><p>{a}</p></details>' for q,a in items)

def faq_schema(items):
    return {"@context":"https://schema.org","@type":"FAQPage","mainEntity":[{"@type":"Question","name":q,"acceptedAnswer":{"@type":"Answer","text":a}} for q,a in items]}

def chips(cities, key=False):
    return '<ul class="chips">'+"".join(f'<li{" class=\"key\"" if (key and c=="Sevierville") else ""}>{c}</li>' for c in cities)+'</ul>'

def areas_html(compact=False):
    out=['<div class="tn-head"><span class="tn-badge">All of Tennessee</span><p>Statewide service from our East Tennessee headquarters, east to west.</p></div>','<div class="tn-regions">']
    for name,sub,groups in TN_REGIONS:
        body=[]
        for gt,cities,key in groups:
            if compact: cities=cities[:5] if not key else cities
            body.append((f'<h5>{gt}</h5>' if gt else '')+chips(cities,key))
            if compact and name=="East Tennessee" and len(body)==2: break
        tag=f'<span class="hq-tag">{STAR} HQ</span>' if sub else ''
        out.append(f'<div class="tn-region{" is-hq" if sub else ""}"><h4>{name} {tag}</h4>{"".join(body)}</div>')
    out.append('</div>')
    bl="".join(f'<li><strong>{st}</strong>{(" · "+t) if (t and not compact) else ""}</li>' for st,t in BEYOND)
    out.append(f'<div class="region beyond"><h4>Beyond Tennessee</h4><p class="beyond-line">{BEYOND_LINE}</p><ul class="chips states">{bl}</ul></div>')
    return "".join(out)

def brands_html():
    return '<ul class="brands">'+"".join(f'<li><strong>{b}</strong><span>{d}</span></li>' for b,d in BRANDS)+'</ul>'

WHY = [
 ('clock','Open 24/7/365','We operate 24 hours a day, 7 days a week, including holidays, so help is a phone call away when a door fails.'),
 ('truck','A “warehouse on wheels”','Fully equipped service vehicles carry the tools and parts to fix most doors on the spot, often the same day.'),
 ('tools','Cross-trained technicians','One call covers locks, glass, storefront, overhead, garage and automatic doors, so you don’t juggle contractors.'),
 ('store','Commercial &amp; residential','From a homeowner’s garage spring to a storefront on the Parkway, we handle both.'),
 ('dollar','Upfront pricing','You know the cost before we begin any work. No hidden fees, no surprises.'),
 ('board','Emergency board-up','After a break-in, storm or vehicle impact, we secure the opening fast and provide documentation for your insurance claim.'),
]

def why_html():
    return '<div class="grid g3">'+"".join(f'<article class="card"><div class="ico">{I[i]}</div><h3>{t}</h3><p>{d}</p></article>' for i,t,d in WHY)+'</div>'

RES = ["Broken spring replacement (torsion &amp; extension)","Garage door opener repair &amp; installation","Cable, roller, hinge &amp; track repair","Panel repair &amp; replacement","New garage door sales &amp; installation","Battery backup systems","Keyless entry for homes &amp; garages","Entry doors, frames &amp; glass"]
COM = ["Storefront doors &amp; glass replacement","Automatic &amp; ADA-accessible doors","Hollow metal doors &amp; frames","Overhead &amp; rolling steel doors","Counter, mall &amp; security gates","Panic exit devices &amp; Detex alarms","Closers, pivots, hinges &amp; mag locks","Emergency board-up &amp; maintenance plans"]

def checks(items, two=True):
    return f'<ul class="checks{" two" if two else ""}">'+"".join(f'<li>{x}</li>' for x in items)+'</ul>'

def write(name, s):
    with open(os.path.join(OUT,name),'w') as f: f.write(s)

# ================= HOME =================
home = head(f"{NAME} | 24/7 Door Repair Across Tennessee | HQ Sevierville, TN",
  f"{NAME}: 24/7 commercial &amp; residential door repair across all of Tennessee, headquartered near Sevierville, TN. Garage doors, storefronts, board-up. Call {PHONE}.",
  "index.html", faq_schema(FAQ)) + header("index.html") + f'''
<section class="hero" aria-labelledby="hero-h">
  <div class="hero-flag" aria-hidden="true"></div>
  <div class="wrap">
    <span class="hero-kicker">{STAR}{STAR}{STAR} Proudly serving all of Tennessee</span>
    <h1 id="hero-h">Door repair, day or night. <em>24/7.</em></h1>
    <p class="lead">Garage doors, storefronts, automatic doors, locks and emergency board-up for homes and businesses. One call to {NAME} gets a fully equipped technician on the way.</p>
    <div class="hero-ctas">
      <a class="btn btn-red btn-lg" href="tel:{TEL}">{I['phone']} Call {PHONE}</a>
      <a class="btn btn-outline btn-lg" href="contact.html">Request Service</a>
    </div>
    <ul class="badges">
      <li>{I['check']} Open 24 hours, 7 days</li>
      <li>{I['check']} Commercial &amp; residential</li>
      <li>{I['check']} Most repairs same day</li>
    </ul>
  </div>
</section>
{STRIPES}

<section class="strip starband" aria-label="Highlights"><div class="wrap"><ul>
  <li>{I['clock']} 24/7 including holidays</li>
  <li>{I['truck']} Fully stocked service vehicles</li>
  <li>{I['shield']} Licensed &amp; insured</li>
  <li>{I['pin']} Statewide across Tennessee</li>
</ul></div></section>

<section class="section" aria-labelledby="why-h"><div class="wrap">
  <div class="sec-head center starrule"><span class="eyebrow">{STAR} Why customers choose us {STAR}</span><h2 id="why-h">Fast, prepared and on call around the clock</h2>
  <p class="lead">When a door fails, your home or business is exposed. Here’s why property owners across Tennessee call us first.</p></div>
  {why_html()}
</div></section>

<section class="section bg-light" aria-labelledby="svc-h"><div class="wrap">
  <div class="sec-head center starrule"><span class="eyebrow">{STAR} What we do {STAR}</span><h2 id="svc-h">Door services for homes &amp; businesses</h2></div>
  <div class="split">
    <article class="svc">
      <img class="svc-img" src="assets/img/full-view-garage-doors.jpg" alt="Full-view aluminum and glass garage doors on a red metal building" width="693" height="390" loading="lazy">
      <div class="svc-body"><span class="svc-tag">Residential</span><h3>Garage &amp; entry doors</h3>
      {checks(RES)}
      <a class="btn btn-navy" href="services.html#residential">Residential services</a></div>
    </article>
    <article class="svc">
      <img class="svc-img" src="assets/img/aluminum-storefront-doors.jpg" alt="Aluminum storefront double doors with glass at a retail store entrance" width="475" height="267" loading="lazy" style="object-position:center 35%">
      <div class="svc-body"><span class="svc-tag red">Commercial</span><h3>Storefront, automatic &amp; steel doors</h3>
      {checks(COM)}
      <a class="btn btn-red" href="services.html#commercial">Commercial services</a></div>
    </article>
  </div>
</div></section>

<section class="section bg-navy" aria-labelledby="how-h"><div class="wrap">
  <div class="sec-head center starrule"><span class="eyebrow" style="color:#fff">{STAR} How it works {STAR}</span><h2 id="how-h">From your call to a working door</h2></div>
  <ol class="steps">
    <li><h3>Call any time</h3><p>Reach us 24/7 at {PHONE} and tell us what’s wrong and where you are.</p></li>
    <li><h3>We dispatch</h3><p>A technician in a fully stocked vehicle is sent your way, often within three hours.</p></li>
    <li><h3>Upfront price</h3><p>We diagnose the problem and explain the fix and cost before work begins.</p></li>
    <li><h3>Fixed &amp; tested</h3><p>Most repairs are done on the spot, and we test everything before we leave.</p></li>
  </ol>
</div></section>

<section class="section" aria-labelledby="area-h"><div class="wrap">
  <div class="areas">
    <div>
      <span class="eyebrow">{STAR} Service areas {STAR}</span><h2 id="area-h">Statewide across Tennessee &amp; beyond</h2>
      <div class="hq"><h3>Headquarters: East Tennessee</h3><p>{NAME} · {ADDR_LINE} (Sevier County)</p></div>
      {areas_html(compact=True)}
      <a class="btn btn-navy" href="service-areas.html">See all service areas</a>
    </div>
    <div class="mapwrap" style="--mh:520px"><a class="map-fallback" href="https://www.google.com/maps/search/?api=1&amp;query={MAP_Q}" target="_blank" rel="noopener">{I['pin']}<strong>{NAME}</strong><span>{ADDR_LINE}</span><em>Open in Google Maps</em></a><iframe class="map" title="Map of {NAME} headquarters in Sevier County, TN" src="https://maps.google.com/maps?q={MAP_Q}&amp;z=6&amp;ie=UTF8&amp;iwloc=&amp;output=embed" loading="lazy" referrerpolicy="no-referrer-when-downgrade"></iframe></div>
  </div>
</div></section>

<section class="section bg-light" aria-labelledby="brand-h"><div class="wrap">
  <div class="sec-head center starrule"><span class="eyebrow">{STAR} Brands we work with {STAR}</span><h2 id="brand-h">Quality products we install &amp; service</h2>
  <p class="lead">A few of the brands we work with regularly. Our technicians service most major makes and models.</p></div>
  {brands_html()}
</div></section>

<section class="section" aria-labelledby="rev-h"><div class="wrap">
  <div class="reviews-band">
    <div><h3 id="rev-h">See what our customers say</h3><p>Read reviews of {NAME} on Google, or leave one after your service.</p></div>
    <a class="btn btn-navy" href="{GOOGLE_REVIEWS_URL}">Read our Google reviews</a>
  </div>
</div></section>

<section class="section bg-light" aria-labelledby="faq-h"><div class="wrap">
  <div class="sec-head center starrule"><span class="eyebrow">{STAR} FAQ {STAR}</span><h2 id="faq-h">Common questions</h2></div>
  <div class="faq">{faq_html(FAQ)}</div>
</div></section>
''' + cta_band() + footer()
write("index.html", home)

# ================= SERVICES =================
SVC_GROUPS = [
 ("residential","Garage Doors","Residential",["Sales and installation of new garage doors","Broken spring replacement (torsion &amp; extension)","Opener repair &amp; installation (chain, belt &amp; screw drive)","Cable, roller, hinge &amp; track repair","Panel repair &amp; replacement","Battery backup systems","Keyless entry systems","Sectional, roll-up, tilt-up &amp; custom doors"]),
 ("entry","Entry, Wood &amp; Glass Doors","Residential &amp; Commercial",["Entry doors &amp; door frames","Solid core &amp; hollow wood doors","Glass replacement: safety, laminated, tempered &amp; Herculite","Door chimes","Doors off the hinges or out of square"]),
 ("commercial","Commercial Storefront Doors","Commercial",["Full-view aluminum storefront doors","Storefront door installation","Tubelite, Kawneer, YKK &amp; Vista Wall systems","Storefront glass replacement","Energy-efficient &amp; break-in resistant glass options"]),
 ("automatic","Automatic &amp; ADA Doors","Commercial",["Automatic entry &amp; exit doors","Handicap-accessible doors &amp; accessories","Manual and automatic door hardware"]),
 ("steel","Overhead, Rolling Steel &amp; Gates","Commercial",["Sales &amp; service for all types of overhead doors","Rolling steel doors","Rolling steel counter gates","Mall &amp; security gates","Complete hardware support &amp; replacement"]),
 ("metal","Hollow Metal Doors &amp; Security","Commercial",["Hollow metal doors with hardware","Panic exit devices &amp; Detex alarms","Security bars","Magnetic locks &amp; keyless entry","Locks, closers, pivots &amp; hinges of all types"]),
 ("emergency","Emergency Board-Up","24/7 Emergency",["Broken storefront glass &amp; windows","Storm, wildfire &amp; wind damage","Vehicle impact, vandalism &amp; forced entry","Overhead door openings awaiting parts","Documentation for your insurance claim"]),
 ("maintenance","Preventative Maintenance","Commercial &amp; Residential",["Preventative maintenance programs","Inspection of springs, cables, rollers &amp; hardware","Lubrication &amp; adjustment","Catch small problems before they become costly repairs"]),
]
cards = "".join(f'<article class="card" id="{i}"><span class="svc-tag{" red" if "Emergency" in tag or tag=="Commercial" else ""}">{tag}</span><h3>{t}</h3>{checks(items, False)}</article>' for i,t,tag,items in SVC_GROUPS)
svc_schema = {"@context":"https://schema.org","@type":"ItemList","name":f"{NAME} services","itemListElement":[{"@type":"ListItem","position":n+1,"item":{"@type":"Service","name":html.unescape(t),"provider":{"@id":SITE_URL+"/#business"},"areaServed":"Tennessee"}} for n,(i,t,tag,items) in enumerate(SVC_GROUPS)]}
services = head(f"Door Repair &amp; Installation Services | {NAME} | Tennessee",
  f"Garage door repair, storefront doors &amp; glass, automatic &amp; ADA doors, rolling steel, hollow metal and 24/7 emergency board-up from {NAME}, serving all of Tennessee from Sevierville, TN.",
  "services.html", svc_schema) + header("services.html") + f'''
<section class="page-hero"><div class="hero-flag" aria-hidden="true"></div><div class="wrap"><p class="crumbs"><a href="index.html">Home</a> / Services</p>
<h1>Door Services</h1><p>Repair, installation and 24/7 emergency service for residential and commercial doors. Below are our most requested services, and our capabilities go well beyond this list.</p></div></section>
<section class="section"><div class="wrap">
  <div class="two-col" style="margin-bottom:48px">
    <div><span class="eyebrow">{STAR} A warehouse on wheels {STAR}</span><h2>We fix most doors on the spot</h2>
    <p>Our fully equipped service vehicles carry the tools and replacement parts for most residential and commercial doors. That means fewer return trips and most repairs finished the same day.</p>
    <p>Our technicians are cross-trained in locks, glass, storefront, overhead, garage and automatic doors, so a single visit can take care of the door, the frame, the closer and the hardware.</p>
    <a class="btn btn-red" href="tel:{TEL}">{I['phone']} Call {PHONE}</a></div>
    <div class="photo-stack"><img src="assets/img/commercial-overhead-door.jpg" alt="Commercial overhead sectional door inside a warehouse" width="900" height="1200" loading="lazy"><img src="assets/img/hollow-metal-door.jpg" alt="Hollow metal service door at a commercial building" width="480" height="640" loading="lazy"></div>
  </div>
  <div class="svc-list">{cards}</div>
</div></section>
<section class="section bg-light"><div class="wrap"><div class="sec-head center starrule"><span class="eyebrow">{STAR} Brands we work with {STAR}</span><h2>Trusted products</h2></div>{brands_html()}</div></section>
''' + cta_band() + footer()
write("services.html", services)

# ================= SERVICE AREAS =================
areas_page = head(f"Service Areas | {NAME} | All of Tennessee &amp; Neighboring States",
  f"{NAME} serves all of Tennessee (East, Middle &amp; West) from its Sevierville-area HQ, plus GA, NC, VA, KY, AL &amp; MS. 24/7: {PHONE}.",
  "service-areas.html") + header("service-areas.html") + f'''
<section class="page-hero"><div class="hero-flag" aria-hidden="true"></div><div class="wrap"><p class="crumbs"><a href="index.html">Home</a> / Service Areas</p>
<h1>Service Areas</h1><p>Headquartered in East Tennessee, we serve homes and businesses across the entire state of Tennessee and into neighboring states.</p></div></section>
<section class="section"><div class="wrap"><div class="areas">
  <div>
    <div class="hq"><h3>Headquarters: East Tennessee</h3><p>{NAME}<br>{ADDR_LINE} (Sevier County)<br><a href="tel:{TEL}" style="color:#fff;font-weight:700">{PHONE}</a> · Open 24/7</p></div>
    {areas_html()}
    <p class="note">Don’t see your town? Call {PHONE}. Our mobile technicians cover many communities not listed here.</p>
  </div>
  <div class="mapwrap" style="--mh:600px"><a class="map-fallback" href="https://www.google.com/maps/search/?api=1&amp;query={MAP_Q}" target="_blank" rel="noopener">{I['pin']}<strong>{NAME}</strong><span>{ADDR_LINE}</span><em>Open in Google Maps</em></a><iframe class="map" title="Map of {NAME} service area" src="https://maps.google.com/maps?q={MAP_Q}&amp;z=6&amp;ie=UTF8&amp;iwloc=&amp;output=embed" loading="lazy" referrerpolicy="no-referrer-when-downgrade"></iframe></div>
</div></div></section>
<section class="section bg-light"><div class="wrap">
  <div class="sec-head"><span class="eyebrow">{STAR} Local know-how {STAR}</span><h2>Around our HQ: Sevierville, Pigeon Forge &amp; Gatlinburg</h2></div>
  <div class="grid g3">
    <article class="card"><h3>Sevierville</h3><p>Storefront glass, commercial doors and garage door repair for businesses and homes from downtown to the outlet corridor along Winfield Dunn Parkway.</p></article>
    <article class="card"><h3>Pigeon Forge</h3><p>Garage door repair, storefront glass replacement and fast emergency service for shops, attractions and homes along the Parkway.</p></article>
    <article class="card"><h3>Gatlinburg</h3><p>24/7 emergency board-up for storefronts, cabins and vacation rentals after storms, wildfires, vandalism or vehicle impact.</p></article>
  </div>
</div></section>
''' + cta_band() + footer()
write("service-areas.html", areas_page)

# ================= ABOUT =================
about = head(f"About Us | {NAME} | Sevierville, TN",
  f"About {NAME}: a door company headquartered in Sevier County, TN, providing statewide 24/7 commercial and residential door repair, installation and emergency board-up.",
  "about.html") + header("about.html") + f'''
<section class="page-hero"><div class="hero-flag" aria-hidden="true"></div><div class="wrap"><p class="crumbs"><a href="index.html">Home</a> / About</p>
<h1>About {NAME}</h1><p>Our mission is simple: to service all of your door repair and maintenance needs, any hour of the day.</p></div></section>
<section class="section"><div class="wrap"><div class="two-col">
  <div class="prose">
    <span class="eyebrow">{STAR} Who we are {STAR}</span><h2 style="margin-top:0">Your local door experts, on call 24/7</h2>
    <p>{NAME} provides fast, reliable and professional door solutions for residential and commercial properties. We have served customers since <span class="placeholder">{YEAR_FOUNDED}</span>, with personalized, quality workmanship at competitive prices and dependable 24-hour emergency service.</p>
    <p>We set a high standard for customer service, quality work and the quality of parts we use. Our professional technicians are well trained, cross-trained across door types, and available 24/7.</p>
    <p>Our service vehicles are equipped specifically to bring you fast service. They carry the tools and parts needed to repair most doors, so we can fix most doors the same day.</p>
    <p><span class="placeholder">[Owner / team story and photo, provided by the client]</span></p>
  </div>
  <img class="photo" src="assets/img/commercial-overhead-door.jpg" alt="Commercial overhead door serviced by {NAME}" width="900" height="1200" loading="lazy" style="max-height:560px">
</div></div></section>
<section class="section bg-light"><div class="wrap">
  <div class="sec-head center starrule"><span class="eyebrow">{STAR} Why customers choose us {STAR}</span><h2>What you can count on</h2></div>
  {why_html()}
</div></section>
''' + cta_band() + footer()
write("about.html", about)

# ================= CONTACT =================
contact = head(f"Contact Us | {NAME} | 24/7 Door Service, Sevierville, TN",
  f"Contact {NAME} 24/7 at {PHONE}. {ADDR_LINE}. Request garage, storefront or commercial door service anywhere in Tennessee, from our HQ near Sevierville.",
  "contact.html") + header("contact.html") + f'''
<section class="page-hero"><div class="hero-flag" aria-hidden="true"></div><div class="wrap"><p class="crumbs"><a href="index.html">Home</a> / Contact</p>
<h1>Contact Us</h1><p>For emergencies, call. For everything else, send a request and we’ll get back to you as soon as possible.</p></div></section>
<section class="section"><div class="wrap"><div class="contact-grid">
  <div>
    <div class="emerg"><strong>Emergency?</strong> Don’t use the form. Call <a href="tel:{TEL}"><strong>{PHONE}</strong></a> now. We answer 24 hours a day, 7 days a week.</div>
    <!-- FORM BACKEND NEEDED: this form is front-end only. Connect it to a form service (e.g. the agency CRM, Formspree, Netlify Forms) by setting the action URL below. -->
    <form class="form" id="service-form" action="#FORM-BACKEND-URL" method="post" novalidate>
      <h2 style="font-size:2rem">Request Service</h2>
      <div class="row">
        <div class="field"><label for="fn">First name</label><input id="fn" name="first_name" autocomplete="given-name" required></div>
        <div class="field"><label for="ln">Last name</label><input id="ln" name="last_name" autocomplete="family-name" required></div>
      </div>
      <div class="row">
        <div class="field"><label for="ph">Phone</label><input id="ph" name="phone" type="tel" autocomplete="tel" required></div>
        <div class="field"><label for="em">Email</label><input id="em" name="email" type="email" autocomplete="email"></div>
      </div>
      <div class="row">
        <div class="field"><label for="ty">Property type</label><select id="ty" name="property_type"><option>Residential</option><option>Commercial</option></select></div>
        <div class="field"><label for="ci">City</label><input id="ci" name="city" autocomplete="address-level2" placeholder="e.g. Sevierville"></div>
      </div>
      <div class="field"><label for="sv">Service needed</label><select id="sv" name="service">
        <option>Garage door repair</option><option>New garage door / opener</option><option>Storefront door or glass</option><option>Automatic / ADA door</option><option>Rolling steel / overhead door</option><option>Locks &amp; hardware</option><option>Emergency board-up</option><option>Preventative maintenance</option><option>Other</option></select></div>
      <div class="field"><label for="msg">Tell us what’s going on</label><textarea id="msg" name="message" rows="5"></textarea></div>
      <button class="btn btn-red btn-lg" type="submit">Send Request</button>
      <p class="hint">We’ll contact you to confirm details and timing. For urgent issues, call {PHONE}.</p>
      <div class="form-status" role="status" aria-live="polite"></div>
    </form>
  </div>
  <aside class="info-card" aria-label="Contact information">
    <h3 style="font-size:1.8rem">{NAME}</h3>
    <dl>
      <dt>24/7 Phone</dt><dd><a class="big" href="tel:{TEL}">{PHONE}</a></dd>
      <dt>Address</dt><dd>{STREET}<br>{CITY}, {STATE} {ZIP}</dd>
      <dt>Email</dt><dd><a href="mailto:{EMAIL}">{EMAIL}</a></dd>
      <dt>Hours</dt><dd>Open 24 hours, 7 days a week, including holidays<br>Office: Mon–Fri, 8:00 am–5:00 pm</dd>
    </dl>
    <div class="mapwrap" style="--mh:260px;margin-top:20px"><a class="map-fallback" href="https://www.google.com/maps/search/?api=1&amp;query={MAP_Q}" target="_blank" rel="noopener">{I['pin']}<strong>{NAME}</strong><span>{ADDR_LINE}</span><em>Open in Google Maps</em></a><iframe class="map" title="Map to {NAME}" src="https://maps.google.com/maps?q={MAP_Q}&amp;z=12&amp;ie=UTF8&amp;iwloc=&amp;output=embed" loading="lazy" referrerpolicy="no-referrer-when-downgrade"></iframe></div>
  </aside>
</div></div></section>
''' + footer()
write("contact.html", contact)
print("built")
