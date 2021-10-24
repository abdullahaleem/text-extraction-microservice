import os
import io
import shutil
import time

from requests.api import request
from app.main import app, BASE_DIR, UPLOAD_DIR, get_settings
from fastapi.testclient import TestClient
from PIL import Image, ImageChops

import requests

"""
We will include the files to pytest.ini that we dont want to test on

We want our tests to be run before we do anything meaningful with git and version control and we will use pre-commit for that
This defines a bunch of steps / hooks that we want our system to take prior to doing a commit
we can use the pre-commit sample-config to get a template and put it in the .pre-commit-config.yaml files. We can the install it pre-commit install...
and then run it using pre-commit run --all-files.
Now once we add everything to git and run commit, it will will run all of these things and it will it every single time we commit
It is really nice as it ensures atleast these things are being handled before we commit
We can also add pytest to that file too se it would check all test before commiting (we need to install and run all-files once we make changes)

The reason we do this: 1. code is well tested 2. make sure its tested when we try to push it 3. make sure its ready when going to production
It can also be done one github (you dont necessiarily have to run these on your local machine) using github actions
Its safe to have autodeploy once we have added the testing part in pre-commit.

If we dont call this function test_something its not gonna test it
"""

END_POINT = "https://extract-text-ms-qs6ya.ondigitalocean.app/"


def test_get_home():
    response = requests.get(END_POINT) # equivalent to client.get("/") from local
    assert response.status_code == 200
    assert "text/html" in response.headers["content-type"]


def test_invalid_file_upload():
    response = requests.post(END_POINT)
    assert response.status_code == 422
    assert "application/json" in response.headers["content-type"]


def test_prediction_upload_without_auth():
    images_path = os.path.join(BASE_DIR, "images")

    for image_name in os.listdir(images_path):
        image_path = os.path.join(images_path, image_name)
        response = requests.post(END_POINT, files={"file": open(image_path, "rb")})
        assert  response.status_code == 401
    

def test_prediction_upload():
    settings = get_settings()
    images_path = os.path.join(BASE_DIR, "images")

    for image_name in os.listdir(images_path):
        image_path = os.path.join(images_path, image_name)
        try:
            image = Image.open(image_path)
        except:
            image = None

        response = requests.post(END_POINT, files={"file": open(image_path, "rb")}, headers={"Authorization": f"JWT {settings.app_auth_token_prod}"})
        
        if image is not None:
            assert response.status_code == 200
            #response_stream = io.BytesIO(response.content)
            data = response.json()
            assert len(data.keys()) == 2
        else:
            assert response.status_code == 400
            
        # Clearing space on server. Added time so we can see what is being dont while in development.
        if os.path.exists(UPLOAD_DIR):
            # time.sleep(3)
            shutil.rmtree(UPLOAD_DIR)