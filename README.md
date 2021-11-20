# Text Extraction Microservice

A very light weight microservice that extracts text from images built using Tesseract (by google) and FastAPI. To use the microservice you would need the end_point, image_path and secret_key. The microservice returns all the text in the images split into lines. Please see example below for usage.

``` python
import requests
END_POINT = "https://extract-text-ms-qs6ya.ondigitalocean.app/"
SECRET_KEY = "hmmitsasecret"
response = requests.post(END_POINT, files={"file": open(image_path, "rb")}, headers={"Authorization": f"JWT {SECRET_KEY}"})
```
