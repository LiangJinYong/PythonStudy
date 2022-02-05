import pyautogui
# 스크린 샷 찍기
# img = pyautogui.screenshot()
# img.save("screenshot.png") # 파일로 저장

# pyautogui.mouseInfo()
# 34,17 53,133,187 #3585BB

# try:
# 	px = pyautogui.pixel(34, 17)
# 	print(px)
# except:
# 	px = pyautogui.pixel(34, 17)
# 	print(px)

px = pyautogui.pixel(34, 17)
print(px)

# print(pyautogui.pixelMatchesColor(34, 17, (53, 133, 187)))
# print(pyautogui.pixelMatchesColor(34, 17, px))
print(pyautogui.pixelMatchesColor(34, 17, (53, 133, 188)))