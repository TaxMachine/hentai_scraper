import requests
import random
import os
from threading import active_count, Thread

hlist = ["https://api.waifu.pics/nsfw/waifu","https://api.waifu.pics/nsfw/neko","https://api.waifu.pics/nsfw/blowjob"]
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
			

def init():
	count = 0
	hentai = 0
	while count <= 1:
		for stuff in hlist:
			lmao = requests.get(stuff)
			img = lmao.json()
			link = img["url"]
			if link.endswith(".png"):
				download(link, 'png')
			elif link.endswith(".jpg"):
				download(link, 'jpg')
			elif link.endswith(".gif"):
				download(link, 'gif')
		hentai += 1
		print(f"Fetched {hentai} Hentai !")

isDirectory()
for _ in iter(int, 1):
	while True:
		if (active_count() <= threads):
			Thread(target=(init)).start()
			break