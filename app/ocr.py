import os
import pytesseract
from PIL import Image

BASE_DIR = "app"
IMAGE_DIR = os.path.join(BASE_DIR, "images")

image_path = os.path.join(IMAGE_DIR, "image2.png")

image = Image.open(image_path)

preds = pytesseract.image_to_string(image)
predictions = [text for text in preds.split("\n")]

print(preds)