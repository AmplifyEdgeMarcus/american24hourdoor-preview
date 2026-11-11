#!/usr/bin/env python3
"""Builds a self-contained single-file homepage (CSS, JS, images, fonts inlined as data URIs)."""
import re, base64, os, urllib.request, mimetypes
ROOT=os.path.join(os.path.dirname(__file__),'..'); SITE=ROOT
OUT=os.path.join(ROOT,'American-24-Hour-Door-Service-home.html')
def datauri(path):
    mt=mimetypes.guess_type(path)[0] or 'application/octet-stream'
    if path.endswith('.svg'): mt='image/svg+xml'
    return f"data:{mt};base64,"+base64.b64encode(open(path,'rb').read()).decode()
html=open(os.path.join(SITE,'index.html')).read()
css=open(os.path.join(SITE,'css/styles.css')).read()
css=re.sub(r'url\("\.\./([^"]+)"\)',lambda m:f'url("{datauri(os.path.join(SITE,m.group(1)))}")',css)
# Google Fonts -> inline woff2 (latin subset only)
fu=re.search(r'href="(https://fonts.googleapis.com/css2[^"]+)"',html).group(1).replace('&amp;','&')
req=urllib.request.Request(fu,headers={'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 Chrome/120 Safari/537.36'})
fcss=urllib.request.urlopen(req,timeout=30).read().decode()
blocks=re.findall(r'/\* ([\w-]+) \*/\s*(@font-face\s*{[^}]+})',fcss)
fonts=[]
for subset,b in blocks:
    if subset!='latin': continue
    u=re.search(r'url\((https://[^)]+)\)',b).group(1)
    d="data:font/woff2;base64,"+base64.b64encode(urllib.request.urlopen(u,timeout=30).read()).decode()
    fonts.append(b.replace(u,d))
html=re.sub(r'<link rel="preconnect"[^>]+>','',html)
html=re.sub(r'<link href="https://fonts.googleapis.com[^>]+>','',html)
html=html.replace('<link rel="stylesheet" href="css/styles.css">','<style>\n'+"\n".join(fonts)+'\n'+css+'\n</style>')
js=open(os.path.join(SITE,'js/main.js')).read()
html=html.replace('<script src="js/main.js" defer></script>','<script>\n'+js+'\n</script>')
html=re.sub(r'(src|href)="(assets/[^"]+)"',lambda m:f'{m.group(1)}="{datauri(os.path.join(SITE,m.group(2)))}"',html)
html=re.sub(r"url\('(assets/[^']+)'\)",lambda m:f"url('{datauri(os.path.join(SITE,m.group(1)))}')",html)
# links to other pages -> live site URLs (single file has no sibling pages)
BASE='https://www.american24hourdoor.com/'
html=re.sub(r'href="index\.html"','href="#main"',html)
html=re.sub(r'href="((?:services|service-areas|about|contact)\.html(?:#[\w-]+)?)"',lambda m:f'href="{BASE}{m.group(1)}"',html)
open(OUT,'w').write(html)
left=re.findall(r'(?:src|href)="((?!data:|https?:|tel:|mailto:|#)[^"]+)"',html)
print(len(fonts),'font faces;',os.path.getsize(OUT),'bytes; unresolved local refs:',left)
