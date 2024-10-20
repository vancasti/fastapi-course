### Engie Challenge Quick Guide

At first we build the docker image: 

```
docker build -t engie-image .
```

The second step is to run the docker container: 

```
docker run -d --name engie-container -p 8888:8888 engie-image
```

We have to check that fast api is running and listening in the 8888 port:

```
INFO:     Uvicorn running on http://0.0.0.0:8888 (Press CTRL+C to quit)
```

We can use any API client (f.e. Postman or with Curl directly) to make an API call to generateplan endpoint:

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