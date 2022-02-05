import re
import requests
from bs4 import BeautifulSoup

# [오늘의 날씨]
# 흐림, 어제보다 00도 높아요
# 현재 00도 (최저 00 / 최고 00)
# 오전 강수확률 00% / 오후 강수확률 00%

# 미세먼지 00 좋은
# 초미세먼지 00 좋은
# ------------------------------

# [헤드라인 뉴스]
# 1. 무슨 무슨 일이...
# 	(링크: https://...)
# 2. 무슨 무슨 일이...
# 	(링크: https://...)
# 3. 무슨 무슨 일이...
# 	(링크: https://...)
# ------------------------------

# [IT 뉴스]
# 1. 무슨 무슨 일이...
# 	(링크: https://...)
# 2. 무슨 무슨 일이...
# 	(링크: https://...)
# 3. 무슨 무슨 일이...
# 	(링크: https://...)

def create_soup(url):
	headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36"}
	res = requests.get(url, headers=headers)
	res.raise_for_status()
	soup = BeautifulSoup(res.text, "lxml")
	return soup

def print_news(index, title, link):
	print("{}. {}".format(index + 1, title))
	print("  (링크) {}".format(link))

def scrape_weather():
	print("[오늘의 날씨]")
	url = "https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=0&ie=utf8&query=%EC%84%9C%EC%9A%B8+%EB%82%A0%EC%94%A8"
	# 맑음
	soup = create_soup(url)
	cast = soup.find("p", attrs={"class", "summary"}).get_text()
	curr_temp = soup.find("div", attrs={"class", "temperature_text"}).get_text().strip()
	min_temp = soup.find("span", attrs={"class", "lowest"}).get_text()
	max_temp = soup.find("span", attrs={"class", "highest"}).get_text()

	rain_rate = soup.find("dl", attrs={"class", "summary_list"}).find("dd").get_text()

	dust = soup.find("ul", attrs={"class", "today_chart_list"})
	pm10 = dust.find_all("li")[0].get_text().strip()
	pm25 = dust.find_all("li")[1].get_text().strip()

	print(cast)
	print(curr_temp)
	print(min_temp)
	print(max_temp)
	print("강수확률:", rain_rate)
	print()
	print(pm10)
	print(pm25)
	print()

def scrape_headline_news():
	print("[헤드라인 뉴스]")
	url = "https://news.naver.com/"
	soup = create_soup(url)
	news_list = soup.find_all("li", attrs={"class", "cjs_headline_item"})
	for index, news in enumerate(news_list):
		title = news.find("div", attrs={"class", "cjs_headline_t"}).get_text().strip()
		link = news.find("a")["href"]
		print_news(index, title, link)
	print()

def scrape_it_news():
	print("[IT 뉴스]")
	url = "https://news.naver.com/main/list.naver?mode=LS2D&mid=shm&sid1=105&sid2=230"
	soup = create_soup(url)
	news_list = soup.find("ul", attrs={"class", "type06_headline"}).find_all("li", limit=3) # 3개 까지 가져오기
	for index, news in enumerate(news_list):
		title = news.find_all("a")[1].get_text().strip()
		link = news.find("a")["href"]
		print_news(index, title, link)
	print()

def scrape_english():
	print("[오늘의 영어회화]")
	url = "https://www.hackers.co.kr/?c=s_eng/eng_contents/I_others_english&keywd=haceng_submain_lnb_eng_I_others_english&logger_kw=haceng_submain_lnb_eng_I_others_english"
	soup = create_soup(url)
	sentences = soup.find_all("div", attrs={"id": re.compile("^conv_kor_t")})
	print("(영어 지문)")
	for sentence in sentences[len(sentences)//2:]: # 8문장이 있다고 가정할 떄, index 기준 4~7까지 잘라서 가져옴
		print(sentence.get_text().strip())
	print("(한글 지문)")
	for sentence in sentences[:len(sentences)//2]: # 8문장이 있다고 가정할 떄, index 기준 4~7까지 잘라서 가져옴
		print(sentence.get_text().strip())

if __name__ == "__main__":
	scrape_weather() # 오늘의 날씨 정보 가져오기
	scrape_headline_news() # 헤드라인 뉴스 정보 가져오기
	scrape_it_news() # IT 뉴스 정보 가져오기
	scrape_english() # 오늘의 영어 회화학습