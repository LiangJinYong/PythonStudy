import pyautogui

# file_menu = pyautogui.locateOnScreen("file_menu.png")
# print(file_menu)
# pyautogui.click(file_menu)

# plus_icon = pyautogui.locateOnScreen("plus_icon.png")
# pyautogui.moveTo(plus_icon)

# screen = pyautogui.locateOnScreen("screenshot.png")
# print(screen)

# for i in pyautogui.locateAllOnScreen("checkbox.png"):
# 	print(i)
# 	pyautogui.click(i, duration=0.25)

# checkbox = pyautogui.locateOnScreen("checkbox.png")
# pyautogui.click(checkbox)

# plus_icon = pyautogui.locateOnScreen("plus_icon.png")
# pyautogui.moveTo(plus_icon)

# 속도 개선
# 1. GrayScale
# plus_icon = pyautogui.locateOnScreen("plus_icon.png", grayscale=True)
# pyautogui.moveTo(plus_icon)

# 2. 범위 지정
# pyautogui.mouseInfo()
# plus_icon = pyautogui.locateOnScreen("plus_icon.png", region=(2153, 1013, 400, 200))
# pyautogui.moveTo(plus_icon)

# 3. 정확도 조정
# run_btn = pyautogui.locateOnScreen("run_btn.png", confidence=0.9) # 90%
# pyautogui.moveTo(run_btn)

# 자동화 대상이 바로 보여지지 않는 경우
# 1. 계속 기다리기
# file_menu_notepad = pyautogui.locateOnScreen("file_menu_notepad.png")
# if file_menu_notepad:
# 	pyautogui.click(file_menu_notepad)
# else:
# 	print("발견 실패")
# while file_menu_notepad is None:
# 	file_menu_notepad = pyautogui.locateOnScreen("file_menu_notepad.png")
# 	print("발견 실패")

# pyautogui.click(file_menu_notepad)

# 2. 일정 시간동안 기다리기 (Timeout)
import time
import sys

# timeout = 10 # 10초 대기
# start = time.time() # 시작 시간 설정
# file_menu_notepad = None

# while file_menu_notepad is None:
# 	file_menu_notepad = pyautogui.locateOnScreen("file_menu_notepad.png", confidence=0.9)
# 	end = time.time() # 종료 시간 설정
# 	if end - start > timeout: # 지정한 10초를 초과하면
# 		print("시간 초과")
# 		sys.exit()

# pyautogui.click(file_menu_notepad)

def find_target(img_file, timeout = 30):
	start = time.time()
	target = None
	while target is None:
		target = pyautogui.locateOnScreen(img_file, confidence=0.9)
		end = time.time()
		diff = end - start
		print(f"==> {diff:.2f}s passed")
		if diff > timeout:
			break
	return target

def my_click(img_file, timeout=30):
	target = find_target(img_file, timeout)
	if target:
		pyautogui.click(target)
		print("Target found and clicked!")
	else:
		print(f"[Timeout {timeout}s] Target not found ({img_file}). Terminate program.")
		sys.exit()

my_click("file_menu_notepad.png", 10)