import requests
from bs4 import BeautifulSoup

lyric_list_url = "https://j-lyric.net/artist/a001fed/"

res = requests.get(lyric_list_url)
res.raise_for_status()

soup = BeautifulSoup(res.text, "lxml")

titles = soup.find_all("p", attrs={"class": "ttl"})

for t in titles:
	song_title = t.text
	song_link = "https://j-lyric.net/" + t.find("a")["href"]

	lyric_res = requests.get(song_link)
	lyric_res.raise_for_status()

	lyric_soup = BeautifulSoup(lyric_res.text, "lxml")
	content = lyric_soup.find("p", attrs={"id": "Lyric"})

	final_content = str(content).replace("<br/>", "\n")\
			.replace('<p id="Lyric">', "")\
			.replace('</p>', '') # 줄 바꿈, p 태그 치환


	print(f"Processing: {song_title}")
	with open(f"./SukumaSwitch2/{song_title}.txt", "w", encoding="utf8") as f:
		f.write(song_title)
		f.write("\n\n\n")
		f.write(final_content)

print("Finished!")