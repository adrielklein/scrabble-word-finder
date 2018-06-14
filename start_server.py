import os
import autopy
import datetime
from PIL import Image
import pytesseract

from app.main import create_app
PORT = 5000

def start_server():
    app = create_app()
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', PORT)))

def capture_screen():
    b = autopy.bitmap.capture_screen()
    print(b)
    image_name = "./screenshot" + str(datetime.datetime.now()) + ".png"
    b.save(image_name)
    print (pytesseract.image_to_string(Image.open(image_name)))

if __name__ == '__main__':
    # capture_screen()
    start_server()
    
