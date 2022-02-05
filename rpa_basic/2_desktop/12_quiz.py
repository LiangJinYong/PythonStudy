# 퀴즈
# Quiz) 아래 동작을 자동으로 수행하는 프로그램을 작성하시오.

# 1. 그림판 실행 (단축키 : win + r, 입력값 : mspaint) 및 최대화
# 2. 상단의 텍스트 기능을 이용하여 횐 영역 아무 곳에다가 글자 입력
# 입력 글자 : "참 잘했어요"
# 3. 5초 대기 후 그림판 종료

# 이때, 저장하지 않음을 자동으로 선택하여 프로그램이 완전 종료되도록 함

import pyautogui
import pyperclip
import sys
print('자동 프로그램 실행 시작...')

pyautogui.hotkey('winleft', 'r') # 단축키 : win + r 입력
pyautogui.sleep(0.25)
pyautogui.write('mspaint')
pyautogui.press('enter') # 엔터 키 입력

# 그림판 나타날 때 까지 2초 대기
pyautogui.sleep(2)

window = pyautogui.getWindowsWithTitle("제목 없음 - 그림판")[0] # 그림판 1개만 띄워져 있다고 가정

if window.isMaximized == False:
	window.maximize() # 최대화


# 글자 버튼 클릭
txt_btn = pyautogui.locateOnScreen("text_mspaint.png", confidence=0.9)
if txt_btn:
	pyautogui.click(txt_btn, duration=0.5)
else:
	print("찾기 실패")
	sys.exit()

pyautogui.click(300, 300, duration=0.5)

def my_write(text):
	pyperclip.copy(text)
	pyautogui.hotkey('ctrl', 'v')

my_write("참 잘했어요.")

pyautogui.sleep(5) # 5초 대기

window.close() # 프로그램 종료
pyautogui.sleep(1)
pyautogui.press('n') # 저장하지 않음
