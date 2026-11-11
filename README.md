# American 24 Hour Door Service — static site

Open `index.html` in a browser, or upload the folder to any static host. No build step is required to preview the pages already in this repo.

Pages: index.html, services.html, service-areas.html, about.html, contact.html
Styles: css/styles.css · Script: js/main.js · Brand: assets/brand/ · Photos: assets/img/

GitHub Pages preview (project site): https://amplifyedgemarcus.github.io/american24hourdoor-preview/

**Preview only, noindex is on, remove before launch.**

Every HTML page includes `<meta name="robots" content="noindex, nofollow, noarchive">` and `<meta name="googlebot" content="noindex, nofollow">`. The switch is `PREVIEW_NOINDEX` at the top of `_build/build.py` (default `True` in this repo). Set it to `False` and run `python3 _build/build.py` before the real launch. This repo has no `robots.txt`. Crawlers need to fetch each page to read the noindex tag. A robots.txt on a project subpath is not the host robots file, and a Disallow rule would hide that tag.

Internal links, stylesheets, scripts, and images use relative paths, and an empty `.nojekyll` file is included so Pages serves this folder as-is (including `_build/`). Canonical, Open Graph, and schema URLs stay on https://www.american24hourdoor.com, the final domain, while noindex is on. They name the production site for launch. They do not make this GitHub Pages URL the indexed address.

## Editing NAP / content
All pages are generated from `_build/build.py`. Change the NAP block once and run `python3 _build/build.py` from the repo root so the name, address, and phone stay identical on every page and in the schema.
You can also edit the HTML directly; keep NAP identical everywhere.

## Before launch
- Contact form is FRONT-END ONLY. Set `action="#FORM-BACKEND-URL"` in contact.html to a real form endpoint.
- Replace `#GOOGLE-REVIEWS-LINK` (home page) with the Google Business Profile reviews URL.
- Fill `[Year founded]` and `[Owner / team story and photo]` on about.html.
- Confirm the final domain (canonical/OG/schema use https://www.american24hourdoor.com).
- Hero flag (assets/img/flag-wave.svg), star field (stars.svg) and star bullet (star.svg) are original generated SVGs, no third-party license. The old Getty hero image was removed.
- Footer motto "Hometown service, American values" is neutral patriotic phrasing; do not change to "American owned" or "veteran owned" unless the client confirms.

## Using this as a template

Business details live in `_build/build.py`:

| Detail | Where |
| --- | --- |
| Name, street, city, state, ZIP, phone, tel link, email | `NAME`, `STREET`, `CITY`, `STATE`, `ZIP`, `PHONE`, `TEL`, `EMAIL` at the top of the file (the NAP block) |
| Public site URL used by canonical, Open Graph, and schema | `SITE_URL` (currently `https://www.american24hourdoor.com`) |
| Preview noindex (on for this repo) | `PREVIEW_NOINDEX` (`True` adds the robots and googlebot noindex tags; set `False` before launch) |
| Tennessee service areas | `TN_REGIONS` |
| Neighboring states | `BEYOND` and `BEYOND_LINE` |
| Brands | `BRANDS` |

Rebuild the five HTML pages from the repo root:

```bash
python3 _build/build.py
```

The script writes `index.html`, `services.html`, `service-areas.html`, `about.html`, and `contact.html` next to `_build/`. CSS, JavaScript, and images stay as files under `css/`, `js/`, and `assets/`.

A one-file homepage (CSS, JS, and images inlined) is optional:

```bash
python3 _build/singlefile.py
```

That writes `American-24-Hour-Door-Service-home.html` at the repo root.

Open placeholders, still in the generator until they are filled in:

- **Year founded.** `YEAR_FOUNDED` is `[Year founded]` (sources conflict: 1992 vs 1998). It renders on about.html.
- **Owner story.** The about-page template in `_build/build.py` still contains `[Owner / team story and photo, provided by the client]`.
- **Google reviews link.** `GOOGLE_REVIEWS_URL` is `#GOOGLE-REVIEWS-LINK` (the “Read our Google reviews” button on the home page).
- **Form backend URL.** The contact form action is `#FORM-BACKEND-URL` in the contact-page template in `_build/build.py`. The form stays front-end only until that action is a real endpoint. `js/main.js` shows a demo message while the action starts with `#`.
