### Powerplant Challenge Quick Guide

You can access the code challenge downloading the repository:

```
git clone git@github.com:vancasti/powerplant-coding-challenge.git
```

This project was bild using docker, so you have to create the image: 

```
docker build -t powerplant-image .
```

The second step is to run the docker container: 

```
docker run -d --name powerplant-container -p 8888:8888 powerplant-image
```

We have to check that Fast API is running and listening in the 8888 port:

```
INFO:     Uvicorn running on http://0.0.0.0:8888 (Press CTRL+C to quit)
```

You can check the docs API to see an example payload: 

```
http://localhost:8888/docs
```

We can use any API client (f.e. Postman or CURL) to make an API call to /generateplan:

```
curl --location 'http://localhost:8888/productionplan' \
--header 'Content-Type: application/json' \
--data '{
  "load": 910,
  "fuels":
  {
    "gas(euro/MWh)": 13.4,
    "kerosine(euro/MWh)": 50.8,
    "co2(euro/ton)": 20,
    "wind(%)": 60
  },
  "powerplants": [
    {
      "name": "gasfiredbig1",
      "type": "gasfired",
      "efficiency": 0.53,
      "pmin": 100,
      "pmax": 460
    },
    {
      "name": "gasfiredbig2",
      "type": "gasfired",
      "efficiency": 0.53,
      "pmin": 100,
      "pmax": 460
    },
    {
      "name": "gasfiredsomewhatsmaller",
      "type": "gasfired",
      "efficiency": 0.37,
      "pmin": 40,
      "pmax": 210
    },
    {
      "name": "tj1",
      "type": "turbojet",
      "efficiency": 0.3,
      "pmin": 0,
      "pmax": 16
    },
    {
      "name": "windpark1",
      "type": "windturbine",
      "efficiency": 1,
      "pmin": 0,
      "pmax": 150
    },
    {
      "name": "windpark2",
      "type": "windturbine",
      "efficiency": 1,
      "pmin": 0,
      "pmax": 36
    }
  ]
}'
```