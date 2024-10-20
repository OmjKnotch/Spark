import httpx
import asyncio
from flet import *
from components.viewer import Viewer


async def fetch_quotes(api_url, quotes,names):
    async with httpx.AsyncClient() as client:
        while True:
            try:
                r = await client.get(api_url)
                
                if r.status_code == 200:
                    new_name =r.json()['data']['author']
                    new_quote = r.json()['data']['quote'].strip()
                    new_quote = new_quote.rstrip('@') 
                    if new_quote not in quotes: 
                        quotes.append(new_quote)
                        names.append(new_name)
            except Exception as e:
                print(f"Error fetching quotes: {e}")

            



async def main(page:Page):
    page.fonts ={'playextra_light':'assets/fonts/PlaywriteDEGrund-ExtraLight.ttf',
                  'play_light':'assets/fonts/PlaywriteDEGrund-Light.ttf'
                    }
    page.update()
        

    api_url ='https://stoic.tekloon.net/stoic-quote'

    current_index = 0
    names =["Naval Ravikant"]
    quotes =["If you’re more passionate about founding a business than the business itself, you can fall into a ten year trap. Better to stay emotionally unattached and select the best opportunity that arises. Applies to relationships too."]
    quote_text = Text(value=f'{quotes[current_index]}',text_align='center',size=20,font_family='playwrite_extra_light') 
    author =Text(value =f'{names[current_index]}',size =20) 

    asyncio.create_task(fetch_quotes(api_url, quotes,names))

    def update_content(index):
        quote_text.value = quotes[index]
        quote_text.update()
        author.value =names[index]
        author.update()

    def on_swipe(e:DragUpdateEvent):
        nonlocal current_index
        if e.delta_x < 0:  # Swiped left
            current_index = (current_index + 1) % len(quotes)
        elif e.delta_x > 0:  # Swiped right
            current_index = (current_index - 1) % len(quotes)
        update_content(current_index)

    def on_tap(e: TapEvent):
        nonlocal current_index
        current_index = (current_index + 1) % len(quotes) 
        update_content(current_index)
    
    q =Viewer(page,quotes,on_swipe,on_tap,quote_text,author)
    page.add(q)

app(target=main,assets_dir='assets')
