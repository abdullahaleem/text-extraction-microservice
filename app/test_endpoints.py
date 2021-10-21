from app.main import app
from fastapi.testclient import TestClient

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

"""
client = TestClient(app) # We can treat the client like python requests


# if we dont call this function test_something its not gonna test it
def test_get_home():
    response = client.get("/") # equivalent to requests.get("")
    assert response.status_code == 200
    assert "text/html" in response.headers["content-type"]


def test_post_home():
    response = client.post("/")
    assert response.status_code == 200
    assert "application/json" in response.headers["content-type"]
    #assert response.json() == {"hello": "world"}

