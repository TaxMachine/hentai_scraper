import requests
import random
import os
from threading import active_count, Thread

hlist = ["https://api.waifu.pics/nsfw/waifu","https://api.waifu.pics/nsfw/neko","https://api.waifu.pics/nsfw/blowjob", "https://nekobot.xyz/api/image?type=hentai", "https://nekobot.xyz/api/image?type=hboobs", "https://nekobot.xyz/api/image?type=hanal"]
threads = int(input("Threads: "))

def isDirectory():
	if not os.path.exists("./hentai"):
		print("Hentai directory not found, creating one...")
		os.mkdir("./hentai")
		print("directory successfully created")

def hashed():
	hash = random.getrandbits(128)
	return str("%032x" % hash)

def download(url, end):
	with open(f"./hentai/{hashed()}.{end}", "wb") as handle:
		r = requests.get(url, stream=True)
		if not r.ok:
			print("Rate Limit Detected")

		for block in r.iter_content(1024):
			if not block:
				break

			handle.write(block)

def waifupics():
	count = 0
	hentai = 0
	while count <= 1:
		for stuff in hlist:
			lmao = requests.get(stuff)
			img = lmao.json()
			if 'i.waifu.pics' in stuff:
				if img["url"]:
					link = img["url"]
					ending = link.split('.')[3]
					match ending:
						case "jpg":
							download(link, 'jpg')
							hentai += 1
							print(f'Fetched {hentai} hentai !')
						case "png":
							download(link, 'png')
							hentai += 1
							print(f'Fetched {hentai} hentai !')
						case "gif":
							download(link, 'gif')
							hentai += 1
							print(f'Fetched {hentai} hentai !')
						case _:
							print('Something went wrong')
			else:
				if img["success"] == True:
					link = img["message"]
					ending = link.split('.')[3]
					match ending:
						case "jpg":
							download(link, 'jpg')
							hentai += 1
							print(f'Fetched {hentai} hentai !')
						case "png":
							download(link, 'png')
							hentai += 1
							print(f'Fetched {hentai} hentai !')
						case "gif":
							download(link, 'gif')
							hentai += 1
							print(f'Fetched {hentai} hentai !')
						case _:
							print('Something went wrong')

isDirectory()
for _ in iter(int, 1):
	while True:
		if (active_count() <= threads):
			Thread(target=(waifupics)).start()
			break
