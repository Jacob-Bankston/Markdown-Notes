# React/Redux Review

## Server

- npm init
- npm install express
- require express
- app = express()
- app.use(express.json())
- npm install cors
- require cors
- app.use(cors())
- set up app listening
- set up post route
  - pull from the body
  - add a class
  - push the class to the array
  - send a response
- set up a get route
  - send the json
- check using postman
  - set the appropriate headers
    - content type application json
  - put the json in the raw body
    - quotes around everything

## Client

- create react app
- set up redux, actions, reducers, thunk, etc...
- set up post route

```js
function AddHike() {
  const handleAddHikeButtonPressed = () => {
    fetch("http://localhost:3001/", {
      method: "POST",
      headers: {
        "Content-Type": "application/json"
      },
      body: JSON.stringify({
        latitude: 33.45,
        longitude: 45.67
      })
    });
  };

  return (
    <div>
      <button onClick={() => handleAddHikeButtonPressed()}>Add Hike</button>
    </div>
  );
}
```

Side Note: **Search source files with CMD+'O', that's the letter not the number.**

## Adding navigator.geolocation!

```js
function AddHike() {
  const getUserLocation = () => {
    // before calling it, we are going to check if it exists.
    if (navigator.geolocation) {
      navigator.geolocation.getCurrentPosition(coords => {
        recordHike(coords.coords.latitude, coords.coords.longitude);
      });
    }
  };

  const recordHike = (latitude, longitude) => {
    fetch("http://localhost:3001/", {
      method: "POST",
      headers: {
        "Content-Type": "application/json"
      },
      body: JSON.stringify({
        latitude: latitude,
        longitude: longitude
      })
    });
  };

  return (
    <div>
      <button onClick={() => handleAddHikeButtonPressed()}>Add Hike</button>
    </div>
  );
}
```

- function DisplayHikes component set up
  - set up list of mapping the list to return the component
    - `{props.myHikes.map(hike => { return (<div><a href={`https://www.latlong.net/c/?lat=${hike.latitude}&long=${hike.longitude}`}></a></div>)})}
    - `{this.props.hike.latitude}, {this.props.hike.longitutde}`
- fix up App.js to display the list and the add button
  - set up useEffect and useState
    - useState - `[hikes, setHikes] = useState([])`
    - useEffect - fetchHikes() set up the fetch to the server
  - function fetchHikes() - fetch the get for the hikes
  - pass hikes prop to children `<DisplayHikes hikes={hikes} />`

## Azam's Notes

#### server side

```js
const express = require("express");
const cors = require("cors");
const app = express();

app.use(cors());
app.use(express.json());

let hikes = [];

app.get("/hikes", (req, res) => {
  res.json(hikes);
});

app.post("/add-hike", (req, res) => {
  let latitude = req.body.latitude;
  let longitude = req.body.longitude;

  // create a class called Hike

  // I am going to use anonymous objects
  let hike = { latitude: latitude, longitude: longitude };
  hikes.push(hike);

  res.status(200).send();
});

app.listen(3001, () => {});
```

#### Client Side React

```js
// App.js
import React, { useEffect, useState } from "react";
import logo from "./logo.svg";
import "./App.css";
import AddHike from "./components/AddHike";
import DisplayHikes from "./components/DisplayHikes";

function App() {
  const [hikes, setHikes] = useState([]);

  useEffect(() => {
    fetchHikes();
  });

  const fetchHikes = () => {
    fetch("http://localhost:3001/hikes")
      .then(response => response.json())
      .then(json => {
        setHikes(json);
      });
  };

  return (
    <div>
      <AddHike />
      <DisplayHikes myHikes={hikes} />
    </div>
  );
}

export default App;
```

```js
// AddHike.js

import React from "react";

function AddHike() {
  const getUserLocation = () => {
    if (navigator.geolocation) {
      navigator.geolocation.getCurrentPosition(coords => {
        recordHike(coords.coords.latitude, coords.coords.longitude);
      });
    }
  };

  const recordHike = (latitude, longitude) => {
    fetch("http://localhost:3001/add-hike", {
      method: "POST",
      headers: {
        "Content-Type": "application/json"
      },
      body: JSON.stringify({
        latitude: latitude,
        longitude: longitude
      })
    });
  };

  const handleAddHikeButtonPressed = () => {
    getUserLocation();
  };

  return (
    <div>
      <button onClick={() => handleAddHikeButtonPressed()}>Add Hike</button>
    </div>
  );
}

export default AddHike;
```

```js
import React from "react";

function DisplayHikes(props) {
  return (
    <div>
      {props.myHikes.map(hike => {
        return (
          <div>
            <a
              href={`https://www.latlong.net/c/?lat=${hike.latitude}&long=${hike.longitude}`}
            >
              {hike.latitude}, {hike.longitude}
            </a>{" "}
          </div>
        );
      })}
    </div>
  );
}

export default DisplayHikes;
```
