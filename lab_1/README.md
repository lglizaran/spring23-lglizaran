# Lab 1: Containerizing a Basic API

<p align="center">
    <!--FAST API-->
        <img src="https://user-images.githubusercontent.com/1393562/190876570-16dff98d-ccea-4a57-86ef-a161539074d6.svg" width=10%>
    <!--PLUS SIGN-->
        <img src="https://user-images.githubusercontent.com/1393562/190876627-da2d09cb-5ca0-4480-8eb8-830bdc0ddf64.svg" width=10%>
    <!--POETRY LOGO-->
        <img src="https://python-poetry.org/images/logo-origami.svg" width=7%>
    <!--PLUS SIGN-->
        <img src="https://user-images.githubusercontent.com/1393562/190876627-da2d09cb-5ca0-4480-8eb8-830bdc0ddf64.svg" width=10%>
    <!--DOCKER-->
        <img src="https://user-images.githubusercontent.com/1393562/209759111-3e98226d-d2ed-47c1-85c4-c96c7a3fbf3b.svg" width=12%>
</p>

- [Application](#app)
  - [How to build the app](#build)
  - [How to run the app](#run)
  - [How to test the app](#test)
- [Questions](#questions)

---

# Application

There has been developed a `FastAPI` application that:  
- Returns the inputted name passed to the `/hello` endpoint `(http://127.0.0.1:8000/hello?name=your-name)`.  
This endpoint should always be used with the `name` parameter.
- Serves the `OpenAPI` documentation `(http://127.0.0.1:8000/docs)`
- Serves a json object that meets the OpenAPI specification version `3+` `(http://127.0.0.1:8000/openapi.json)`


## How to build the app

The app has been containerized using `Docker`. To build the container run the following command (make sure your working directory is `lab_1/lab1`):  
`docker build . -t <name>`

## How to run the app

To run the app, simply run the container you have created:  
`docker run --name lab1_container -d -p 8000:8000 name`  
The application will startup and listen on port `8000` (make sure you don't have that port already in use)  
What the app really does inside the container is to launch the application with uvicorn `uvicorn src.main:app --host 0.0.0.0 --port 8000`


THere is also a shell script included `run.sh` that builds the image, launches the app, make some tests and close and delete the container. To run this script, run `sh run.sh` in the main directory `(lab_1)`.

## How to test the app

For testing, we recommend using `Poetry`, a python packaging and dependency management system. [Follow the instructions](https://python-poetry.org/docs/#installation) in case you don't have it installed.  
To test the app, run `poetry run pytest`.

# Questions

- What status code should be raised when a query parameter does not match our expectations?  
If a query parameter does not match our expectations, we should receive a `400 Bad Request` error code, which is a client error.  
In the app, this will happen if we do not pass the parameter `name` to the `/hello` endopoint.

- What does Python Poetry handle for us?  
Poetry is helping us manage the enviroment (packages, versions, dependencies, app versions) and the testing phase. 

- What advantages do multi-stage docker builds give us?  
With multi-stage docker builds you can create an image with just the packages needed for the application you want to use. The most important advantage is disk space and simplicity, because the final image that you use to execute your application can contain only the files (packages, configs) needed.  
In the case of this app, we are building a `build` image with python and poetry which, along with the `.toml` and `.lock` files serve us to create the virtual environment. In the `runner` image, the final that we use to run the application, we just bring a base python image and add the virtual enviromnent created with poetry.
