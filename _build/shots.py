import asyncio
from playwright.async_api import async_playwright
PAGES=['index','services','service-areas','about','contact']
async def main():
    async with async_playwright() as p:
        try: b=await p.chromium.launch()
        except Exception: b=await p.chromium.launch(executable_path='/usr/bin/google-chrome')
        for vw,tag in [(1440,'desktop'),(390,'mobile')]:
            ctx=await b.new_context(viewport={'width':vw,'height':900 if vw>1000 else 844},device_scale_factor=1 if vw>1000 else 2)
            pg=await ctx.new_page()
            for n in PAGES:
                await pg.goto(f'http://localhost:8765/{n}.html',wait_until='networkidle')
                await pg.evaluate("document.querySelectorAll('[loading=lazy]').forEach(e=>e.loading='eager')")
                await pg.evaluate('async()=>{for(let y=0;y<document.body.scrollHeight;y+=600){window.scrollTo(0,y);await new Promise(r=>setTimeout(r,120));}window.scrollTo(0,0);}')
                await pg.wait_for_timeout(3500)
                if n=='index': await pg.screenshot(path=f'/workspace/american-door/site/screenshots/{n}-{tag}-fold.png')
                await pg.add_style_tag(content='.callbar{position:static!important}')
                await pg.screenshot(path=f'/workspace/american-door/site/screenshots/{n}-{tag}-full.png',full_page=True)
        await b.close()
asyncio.run(main())
