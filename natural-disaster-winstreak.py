import mss
import time
from PIL import Image
from pytesseract import pytesseract
import mss.tools
import os

survivals = 0
os.system("title Survivals - {}".format(survivals))

while True:
    with mss.mss() as sct:
        monitor_number = 2
        mon = sct.monitors[monitor_number]
        monitor = {"top": mon["top"] + 0,"left": mon["left"] + 0,"width": 1919,"height": 1079,"mon": monitor_number,}
        sct_img = sct.grab(monitor)
        mss.tools.to_png(sct_img.rgb, sct_img.size, output='output.png')
    path_to_tesseract = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
    pytesseract.tesseract_cmd = path_to_tesseract
    text = pytesseract.image_to_string(Image.open('output.png'))
    print("___________________________________________ ",time.strftime("%H:%M:%S"))
    print(text)
    if "InsertYourNameHere" and "Survivors" in text:
        print("Found 2 strings in image, waiting 10 seconds!")
        time.sleep(10)
        survivals = survivals + 1
        os.system("title Survivals - {}".format(survivals))
