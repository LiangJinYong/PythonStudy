import pyautogui

pyautogui.sleep(3) # 3초 대기
# print(pyautogui.position())

# pyautogui.click(126, 26, duration=1) # 1초 동안 (126, 26) 좌표로 이동 후 마우스 클릭
# pyautogui.click()
# pyautogui.mouseDown()
# pyautogui.mouseUp()

# pyautogui.doubleClick()
# pyautogui.click(clicks=500)

# pyautogui.moveTo(300, 300)
# pyautogui.mouseDown() # 마우스 버튼 누른 상태
# pyautogui.moveTo(400, 400)
# pyautogui.mouseUp() # 마우스 버튼 뗀 상태

# pyautogui.rightClick()
# pyautogui.middleClick()

# print(pyautogui.position())
# pyautogui.moveTo(1222, 189)
# pyautogui.drag(-100, -200, duration=0.25) # 너무 빠른 동작으로 drag 수행이 안될때는 duration 값 설정
# pyautogui.dragTo(1500, 300, duration=0.25) # 절대 좌표 기준으로 드래그

# pyautogui.scroll(300) # 양수이면 위 방향으로 스크롤, 음수이면 아래 방향으로 스크롤
pyautogui.scroll(-800)