from openpyxl import Workbook
from openpyxl.drawing.image import Image

wb = Workbook()
ws = wb.active

img = Image("img.png")

# C3 위치에 img.png 파일의 이미지를 삽입
ws.add_image(img, "C3")

wb.save("sample_image.xlsx")

# Pillow 가 설치 되지 않은 경우 다름 에러 발생할 수 있음
# ImportError : You must install Pillow to fetch image...