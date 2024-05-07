# Import the FastAPI class from the fastapi package
from fastapi import FastAPI

# Create an instance of the FastAPI class
# This instance will be responsible for handling routing, responding, and other FastAPI functionalities
# All methods and attributes of FastAPI can be accessed using this `app` object
app = FastAPI()  # Object of the FastAPI class

# Define route 1
# The `@app.get()` decorator registers a GET endpoint with the specified path ("/" in this case)
# When a request is made to the specified path with the GET method, this function will be executed
@app.get("/")  # Decorator function (@) calls the `app.get()` function
def index():
    # This function returns a dictionary containing a simple JSON response
    # The response will have the key "Hello" and the value "World"
    return {"Hello": "World"}

# Define route 2
# Similar to route 1, this function defines another GET endpoint with the path "/piaic/"
@app.get("/piaic/")
def piaic():
    # This function returns a dictionary containing information about an organization
    # The response will have the key "Organization" and the value "piaic"
    return {"Organization": "piaic"}