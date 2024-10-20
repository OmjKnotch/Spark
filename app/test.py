import httpx
import asyncio

results =[]
async def work():
	data =await httpx.get('https://stoic.tekloon.net/stoic-quote')
	results.append(data.json)
work()

for i in results:
	print(i)