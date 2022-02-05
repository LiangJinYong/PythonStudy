import pyautogui
# pyautogui.FAILSAFE = False fail-safe 비활성화
pyautogui.PAUSE = 1 # 모든 동작에 1초씩 sleep 적용
# pyautogui.mouseInfo()

for i in range(10):
	pyautogui.move(100, 100)
	# pyautogui.sleep(1)