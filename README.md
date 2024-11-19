### FastAPI Doc

```
git clone git@github.com:vancasti/fastapi-api-course.git
```

This project was bild using docker, so you have to create the image: 

```
docker build -t fastapi-image .
```

The second step is to run the docker container: 

```
docker run -d --name fastapi-container -p 8888:8888 fastapi-image
```

We have to check that Fast API is running and listening in the 8888 port:

```
INFO:     Uvicorn running on http://0.0.0.0:8888 (Press CTRL+C to quit)
```

You can check the docs API to see an example payload:

```
http://localhost:8888/docs
```