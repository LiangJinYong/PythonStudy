from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

browser = webdriver.Chrome()
browser.maximize_window()

url = "https://flight.naver.com/"
browser.get(url) # url 로 이동

# 가는날 선택 클릭
browser.find_element_by_class_name("tabContent_option__2y4c6").click()

time.sleep(1)

# browser.find_elements_by_link_text("27")[0].click() # [0] -> 이번달
# browser.find_elements_by_link_text("28")[0].click() # [0] -> 이번달
browser.find_elements_by_css_selector("b.num")[26].click() # 이번달
browser.find_elements_by_css_selector("b.num")[37].click() # 다음달

# 도쿄 선택
browser.find_element_by_xpath("//*[@id='__next']/div/div[1]/div[7]/div/ul/li[1]").click()
time.sleep(3)
browser.find_element_by_xpath("//*[@id='__next']/div/div[1]/div[10]/div[2]/div[1]/div[2]/ul/li[2]").click()

try:
	# 성공했을 때 동작 수행
	elem = WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.XPATH, "//*[@id='__next']/div/div[1]/div[4]/div/div[3]/div[1]/div/div[1]/div/div[1]")))
	print(elem.text) # 첫번째 결과 출력
except:
	browser.quit()

# 첫번째 결과 출력
# elem = browser.find_element_by_xpath("//*[@id='__next']/div/div[1]/div[4]/div/div[3]/div[1]")
# print(elem.text)

time.sleep(200)