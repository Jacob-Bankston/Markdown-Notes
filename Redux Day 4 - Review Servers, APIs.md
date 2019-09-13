# Redux Day 4!

## Review - Server Side Set Up into React/Redux

- Set up Node
- Set up Express
- Set up CORS
- Set up post route
- Use Postman to check routes
- Set up get route
- Use Postman to check route
- Create React App
- import createStore and Provider from redux and react-redux
- create reducer
  - initialState
  - `const reducter - (state = initialState, action => { return state })`
  - `export default reducer`
- import reducer
  - create store const variable
  - add the store variable to Provider
- Add components into app.js
- Add extension to store declaration to be able to use devtools
- import useEffect

```js
useEffect(() => {
  // get the data
  fetchHikingLocations();
}, []);

const fetchHikingLocation = () => {
  fetch("http://localhost:3001/all-locations")
    .then(response => response.json())
    .then(json => {
      console.log(json);
    });
};
```

- mapDispatchToProps
  - We need to dispatch an action and update the global state
- mapStateToProps

payload - any information dispatched (sent) to the reducer that you want to interact with. It is the second argument included in a dispatch statement.

connect - remember to import connect from react-redux to be able to hook up with the store!

- Set up actions
  - Set up actionTypes.js
    - The good thing about setting up the types is you only have to change the information in one area!
  - Set up actionCreators.js

## Explaining useEffect and useState

```js
// local state set up
const [counter, setCounter] = useState(0);
const [name, setName] = useState("");

// componentDidMount - functions would fire when the component rendered
// componentDidUpdate - functions would fire when the state updated
// most of the time these would be the same code used twice,
// so they simplified the code into one function called useEffect!
useEffect(() => {
  // get the data
  fetchHikingLocations();
}, []); // only gets called when the component renders

useEffect(() => {
  // get the data
  fetchHikingLocations();
}); // called any time there is a change to the state

useEffect(() => {
  // get the data
  fetchHikingLocations();
}, [counter]); // called any time there is a change to the counter state
```

## Redux Thunk

[Thunk](https://github.com/reduxjs/redux-thunk): Middleware that will allow you to access dispatch from your action creators

This will allow your actionCreators to be more flexible. If some other component is interested in ~hikingData, they can call ~hikingDataFetch and it will give them that data. This eliminates having to repeat the code in multiple locations.

This doesn't make anything faster, it just allows you to not have to duplicate as much code.

- `npm install redux-thunk`
  - Installed on the client side
- `import thunk from 'redux-thunk';`
- `import { createStore, applyMiddleware } from 'redux';`
- Advanced Store Set up
  - `const composeEnhancers = window.__REDUX_DEVTOOLS_EXTENSION_COMPOSE__ || compose;`
  - `const store = createStore(reducer, composeEnhancers( applyMiddleware(thunk) )`
- Now you can access the dispatch inside the action creators!

This will not be helpful in the short run, but it will be very helpful in the long run.

## Azam's Class Notes

### Hiking Server

##### app.js

```js
const Express = require("express");
const Coordinate = require("./coordinate");
const cors = require("cors");
const app = Express();

app.use(Express.json());
app.use(cors());

let locations = [];

app.post("/save-location", (req, res) => {
  const latitude = req.body.lat;
  const longitude = req.body.long;

  let coordinate = new Coordinate(latitude, longitude);

  locations.push(coordinate);

  res.status(200).send();
});

app.get("/all-locations", (req, res) => {
  res.json(locations);
});

const PORT = 3001;
app.listen(PORT, () => {
  console.log("Server is running");
});
```

##### coordinate.js

```js
class Coordinate {
  constructor(lat, lng) {
    this.latitude = lat;
    this.longitude = lng;
  }
}

module.exports = Coordinate;
```

### Hiking Client

##### index.js

```js
import React from "react";
import ReactDOM from "react-dom";
import "./index.css";
import App from "./App";
import * as serviceWorker from "./serviceWorker";
import { createStore, applyMiddleware, compose } from "redux";
import { Provider } from "react-redux";
import reducer from "./store/reducer";
import thunk from "redux-thunk";

const composeEnhancers = window.__REDUX_DEVTOOLS_EXTENSION_COMPOSE__ || compose;

const store = createStore(reducer, composeEnhancers(applyMiddleware(thunk)));

ReactDOM.render(
  <Provider store={store}>
    <App />
  </Provider>,
  document.getElementById("root")
);

// If you want your app to work offline and load faster, you can change
// unregister() to register() below. Note this comes with some pitfalls.
// Learn more about service workers: https://bit.ly/CRA-PWA
serviceWorker.unregister();
```

##### App.js

```js
import React from "react";
import logo from "./logo.svg";
import "./App.css";
import HikingList from "./components/HikingList";

function App() {
  return (
    <div>
      <HikingList />
    </div>
  );
}

export default App;
```

##### components/HikingList.js

```js
import React, { useEffect, useState } from "react";
import { connect } from "react-redux";
import * as actionCreators from "../store/actions/actionCreators";

function HikingList(props) {
  // local state
  const [counter, setCounter] = useState(0);
  const [name, setName] = useState("");

  // componentDidMount
  // componentDidUpdate
  useEffect(() => {
    // get the data

    props.onHikingLocationsLoaded();

    //fetchHikingLocations()  // moved into action creators
  }, []); // empty array as second argument is saying that there are no
  // dependencies fro teh useEffect to be called again.

  /* deleted becasue we moved it into the action creators 

    const fetchHikingLocations = () => {
        fetch('http://localhost:3001/all-locations')
        .then(response => response.json())
        .then(json => {
            props.onHikingLocationsLoaded(json)
        })
    } */

  return (
    <div>
      {props.hikingLocations.map(location => {
        return (
          <div>
            {location.latitude}, {location.longitude}
          </div>
        );
      })}
    </div>
  );
}

const mapDispatchToProps = dispatch => {
  return {
    onHikingLocationsLoaded: () => dispatch(actionCreators.hikingDataFetched())
  };
};

const mapStateToProps = state => {
  return {
    hikingLocations: state.locations // props.hikingLocations
  };
};

export default connect(
  mapStateToProps,
  mapDispatchToProps
)(HikingList);
```

##### store/reducer.js

```js
const initialState = {
  locations: []
};

const reducer = (state = initialState, action) => {
  switch (action.type) {
    case "HIKING_DATA_LOADED":
      return {
        ...state,
        locations: action.payload
      };
  }

  return state;
};

export default reducer;
```

##### store/actions/actionCreators.js

```js
import * as actionTypes from "./actionTypes";

export const hikingDataFetched = () => {
  return dispatch => {
    // fetch all hiking locations
    fetch("http://localhost:3001/all-locations")
      .then(response => response.json())
      .then(json => {
        dispatch({ type: actionTypes.HIKING_DATA_LOADED, payload: json });
      });
  };
};
```

##### store/actions/actionTypes.js

```js
export const HIKING_DATA_LOADED = "HIKING_DATA_LOADED";
```
