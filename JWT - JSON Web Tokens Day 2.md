# JSON Web Tokens Day 2

## SERVER SIDE

```js
// app.js
const express = require("express");
const app = express();
var jwt = require("jsonwebtoken");
const cors = require("cors");

const users = [{ username: "johndoe", password: "password" }];

app.use(cors());
app.use(express.json());

// MIDDLEWARE IMPLEMENTATION
app.all("/api/*", (req, res, next) => {
  // middle ware
  console.log("middleware called...");
  let headers = req.headers["authorization"];

  if (headers) {
    const token = headers.split(" ")[1];
    var decoded = jwt.verify(token, "someprivatekey");
    if (decoded) {
      const username = decoded.username;
      // check in the database if the user exists
      const persistedUser = users.find(u => u.username == username);
      if (persistedUser) {
        next();
      } else {
        res.json({ error: "Invalid credentials" });
      }
    } else {
      res.json({ error: "Unauthorized access" });
    }
  } else {
    res.json({ error: "Unauthorized access" });
  }
});

app.get("/api/add-books", (req, res) => {
  res.json({ message: "Books added.." });
});

app.get("/api/my-books", (req, res) => {
  res.json([{ title: "Atomic Habits" }]);
});

app.post("/login", (req, res) => {
  const username = req.body.username;
  const password = req.body.password;

  let persistedUser = users.find(
    u => u.username == username && u.password == password
  );

  if (persistedUser) {
    // credentials are valid

    var token = jwt.sign({ username: username }, "someprivatekey");
    res.json({ token: token });
  } else {
    // credentials are not valid
    res.status(401).json({ error: "Invalid credentials" });
  }
});

app.listen(3001, () => {
  console.log("Server is running...");
});
```

```js
// authMiddleware.js

function authenticate(req, res, next) {
  let headers = req.headers["authorization"];

  console.log(headers);

  next(); // proceed to the original request
}

module.exports = authenticate;
```

## CLIENT SIDE

```js
// index.js
import React from "react";
import ReactDOM from "react-dom";
import "./index.css";
import App from "./App";
import * as serviceWorker from "./serviceWorker";
import { BrowserRouter, Switch, Route } from "react-router-dom";
import BaseLayout from "./components/BaseLayout";
import Login from "./components/Login";
import MyBooks from "./components/MyBooks";
import { setAuthenticationHeader } from "./utils/authenticate";

// get the token
let token = localStorage.getItem("jsonwebtoken");
// and attach it to the header
setAuthenticationHeader(token);

ReactDOM.render(
  <BrowserRouter>
    <BaseLayout>
      <Switch>
        <Route path="/" exact component={Login} />
        <Route path="/my-books" component={MyBooks} />
      </Switch>
    </BaseLayout>
  </BrowserRouter>,

  document.getElementById("root")
);

// If you want your app to work offline and load faster, you can change
// unregister() to register() below. Note this comes with some pitfalls.
// Learn more about service workers: https://bit.ly/CRA-PWA
serviceWorker.unregister();
```

```js
// App.js
import React from "react";
import logo from "./logo.svg";
import "./App.css";
import Login from "./components/Login";

function App() {
  return <Login />;
}

export default App;
```

```js
// BaseLayout.js

import React from "react";

function BaseLayout(props) {
  return (
    <div>
      <h1>MENU</h1>
      <div>{props.children}</div>
    </div>
  );
}

export default BaseLayout;
```

```js
// Login.js
import React, { useState } from "react";
import axios from "axios";
import { setAuthenticationHeader } from "../utils/authenticate";

function Login() {
  const [user, setUser] = useState({ username: "", password: "" });

  const handleLogin = () => {
    // perform a login request to the server
    axios
      .post("http://localhost:3001/login", {
        username: user.username,
        password: user.password
      })
      .then(response => {
        const token = response.data.token;
        // save token in local storage
        localStorage.setItem("jsonwebtoken", token);
        // set default axios header
        setAuthenticationHeader(token);
        console.log(response.data);
      });
  };

  const handleTextChange = e => {
    setUser({
      ...user,
      [e.target.name]: e.target.value
    });
  };

  return (
    <div>
      <input type="text" name="username" onChange={e => handleTextChange(e)} />
      <input
        type="password"
        name="password"
        onChange={e => handleTextChange(e)}
      />
      <button onClick={() => handleLogin()}>Login</button>
    </div>
  );
}

export default Login;
```

```js
// MyBooks.js

import React from "react";
import axios from "axios";

function MyBooks() {
  const handleGetMyBooks = () => {
    // get the token out of local storage

    // attach it to the axios header

    axios.get("http://localhost:3001/api/my-books").then(response => {
      console.log(response.data);
    });
  };

  return (
    <div>
      MyBooks
      <button onClick={() => handleGetMyBooks()}>Get My Books</button>
    </div>
  );
}

export default MyBooks;
```

```js
// utils/authenticate.js
import axios from "axios";

// attaches the token to every single request
export function setAuthenticationHeader(token) {
  // set the token in the header
  if (token) {
    // set the headers
    axios.defaults.headers.common["Authorization"] = `Bearer ${token}`;
  } else {
    // remove the token
    delete axios.defaults.headers.common["Authorization"];
  }
}
```

## New Content

- Create Menu.js
- Set Up Redux
  - index.js
    - import Provider
    - import createStore
    - create the store
      - const store...
  - reducer.js
    - The only thing for state now that we're concerned about is whether the user is logged in or not.
    - Set up the initial state
    - Set up the reducer
    - Export the default reducer
  - index.js
    - Pass in the reducer
  - Check for the store
    - Go into the redux dev tools
      - Add the redux dev tools line
      - We're just checking if the isAuthenticated shows up or not
  - Put the Provider in the ReactDOM
    - Place around the BaseLayout or BrowserRouter
- When the person logs in successfully you want to change the state to true
  - Once we set this up the Menu will use this state to change the ability to toggle between different menu items
- Add connection to redux store
  - Login.js
    - import react-redux
    - add connect
    - add mapDispatchToProps
- Add switch to reducer
  - inside reducer add a switch action.type
  - case onAuthenticate change to true
- Check in redux dev tools that the state actually changes
  - the state and difference tabs should show the differences
- Change the Menu to show values when the user is or is not logged in
  - Menu.js
    - react-redux, connect, mapStateToProps
    - check for authentication
    - add props.isAuthenticated as an if statement for the features that do or do not need to show
    - add a sign out button as well
      - set up to show when logged in
      - add onClick function to handle signing out
      - create the sign out function
        - should remove the json web token from local storage
        - should change the state for authentication
    - add mapDispatchToProps
      - add the function on the bottom to use the sign out action
      - add the dispatch to the connect
  - reducer.js
    - add the case for sign out
    - change isAuthenticated to false
- Check in redux dev tools
  - global state starts false
  - login, links should appear, isAuthenticated true
    - login action fired
    - isAuthenticated false
    - links appear
  - sign out
    - sign out action fired
    - isAuthenticated false
    - links disappear
- Different Reducers
  - user reducer - handles authentication
  - book reducer - handles books fetching and updates
- CONGRATS!

  - We can now change states in our application to manipulate the global state, and add differences based on that!

## Environment File - dotenv

- Adding an Environment File
  - When you are using something that is hard coded into your files you can utilize this to change what information is shown to the public, to developers and to the testers.
  - dotenv - npm
  - `npm install dotenv`
  - `require('dotenv').config()`
  - create your .env file like a .gitignore file
    - PORT=3001
    - JWT_SECRET_KEY = "someprivatekey"
  - initialize the .env configuration
- Check to see if the process.env file works
  - console.log(process.env.PORT)
  - console.log(process.env.JWT_SECRET_KEY)
- Create a separate file for the authMiddleware
  - import the necessary functionality needed
  - export the function
  - update the users variable as a global users
- Higher Order Components
  - Protecting the client side urls
  - This is weird. You will create a component that will pass in a component.
- Create requireAuth.js
  - create a component callback situation
  - checks in the constructor if they're authenticated
  - renders the component that was called
- Import into index.js
  - Whatever route you're using with requireAuth has to be wrapped with the function.
  - `component={requireAuth(MyBooks)}`

## Project

- Implement React, Redux, JSON Web Tokens

## Azam's Notes

## SERVER SIDE

```
.env

PORT=3001
JWT_SECRET_KEY= "someprivatekey"
```

```js
const express = require("express");
const app = express();
require("dotenv").config(); // initialize the dotenv configuration
var jwt = require("jsonwebtoken");
const cors = require("cors");
const authenticate = require("./authMiddleware");

global.users = [{ username: "johndoe", password: "password" }];

app.use(cors());
app.use(express.json());
app.all("/api/*", authenticate);

// MIDDLEWARE IMPLEMENTATION
/*
app.all('/api/*',(req,res,next) => {
    // middle ware 
    console.log('middleware called...')
    let headers = req.headers['authorization']

    if(headers) {
        const token = headers.split(' ')[1]
        var decoded = jwt.verify(token, process.env.JWT_SECRET_KEY);
        if(decoded) {
            const username = decoded.username 
            // check in the database if the user exists 
            const persistedUser = users.find(u => u.username == username)
            if(persistedUser) {
                next() // proceed with the original request
            } else {
                res.json({error: 'Invalid credentials!'})
            }
        } else {
            res.json({error: 'Unauthorized access!'})
        }
    } else {
        res.json({error: 'Authorization header not found!'})
    }
}
) */

app.get("/api/add-books", (req, res) => {
  res.json({ message: "Books added.." });
});

app.get("/api/my-books", (req, res) => {
  res.json([{ title: "Atomic Habits" }]);
});

app.post("/login", (req, res) => {
  const username = req.body.username;
  const password = req.body.password;

  let persistedUser = users.find(
    u => u.username == username && u.password == password
  );

  if (persistedUser) {
    // credentials are valid

    var token = jwt.sign({ username: username }, process.env.JWT_SECRET_KEY);
    res.json({ token: token });
  } else {
    // credentials are not valid
    res.status(401).json({ error: "Invalid credentials" });
  }
});

app.listen(process.env.PORT, () => {
  console.log("Server is running...");
});
```

```js
// authMiddleware.js

const jwt = require("jsonwebtoken");

// MIDDLEWARE IMPLEMENTATION
function authenticate(req, res, next) {
  // middle ware
  console.log("middleware called...");
  let headers = req.headers["authorization"];

  if (headers) {
    const token = headers.split(" ")[1];
    var decoded = jwt.verify(token, process.env.JWT_SECRET_KEY);
    if (decoded) {
      const username = decoded.username;
      // check in the database if the user exists
      const persistedUser = users.find(u => u.username == username);
      if (persistedUser) {
        next(); // proceed with the original request
      } else {
        res.json({ error: "Invalid credentials!" });
      }
    } else {
      res.json({ error: "Unauthorized access!" });
    }
  } else {
    res.json({ error: "Authorization header not found!" });
  }
}

module.exports = authenticate;
```

## CLIENT SIDE

```js
// index.js

import React from "react";
import ReactDOM from "react-dom";
import "./index.css";
import App from "./App";
import * as serviceWorker from "./serviceWorker";
import { BrowserRouter, Switch, Route } from "react-router-dom";
import BaseLayout from "./components/BaseLayout";
import Login from "./components/Login";
import MyBooks from "./components/MyBooks";
import { setAuthenticationHeader } from "./utils/authenticate";
import { Provider } from "react-redux";
import { createStore } from "redux";
import reducer from "./store/reducer";
import requireAuth from "./components/requireAuth";

const store = createStore(
  reducer,
  window.__REDUX_DEVTOOLS_EXTENSION__ && window.__REDUX_DEVTOOLS_EXTENSION__()
);

// get the token
let token = localStorage.getItem("jsonwebtoken");
// and attach it to the header
setAuthenticationHeader(token);

ReactDOM.render(
  <BrowserRouter>
    <Provider store={store}>
      <BaseLayout>
        <Switch>
          <Route path="/" exact component={Login} />
          <Route path="/my-books" component={requireAuth(MyBooks)} />
        </Switch>
      </BaseLayout>
    </Provider>
  </BrowserRouter>,

  document.getElementById("root")
);

// If you want your app to work offline and load faster, you can change
// unregister() to register() below. Note this comes with some pitfalls.
// Learn more about service workers: https://bit.ly/CRA-PWA
serviceWorker.unregister();
```

```js
// App.js
import React from "react";
import logo from "./logo.svg";
import "./App.css";
import Login from "./components/Login";

function App() {
  return <Login />;
}

export default App;
```

```js
// components/BaseLayout.js

import React from "react";
import Menu from "./Menu";

function BaseLayout(props) {
  return (
    <div>
      <Menu />
      <div>{props.children}</div>
    </div>
  );
}

export default BaseLayout;
```

```js
// components/Login.js
import React, { useState } from "react";
import axios from "axios";
import { setAuthenticationHeader } from "../utils/authenticate";
import { connect } from "react-redux";

function Login(props) {
  const [user, setUser] = useState({ username: "", password: "" });

  const handleLogin = () => {
    // perform a login request to the server
    axios
      .post("http://localhost:3001/login", {
        username: user.username,
        password: user.password
      })
      .then(response => {
        const token = response.data.token;
        // save token in local storage
        localStorage.setItem("jsonwebtoken", token);
        // set default axios header
        setAuthenticationHeader(token);
        // change redux state to isAuthenticated true
        props.onAuthenticated(token);
      });
  };

  const handleTextChange = e => {
    setUser({
      ...user,
      [e.target.name]: e.target.value
    });
  };

  return (
    <div>
      <input type="text" name="username" onChange={e => handleTextChange(e)} />
      <input
        type="password"
        name="password"
        onChange={e => handleTextChange(e)}
      />
      <button onClick={() => handleLogin()}>Login</button>
    </div>
  );
}

const mapDispatchToProps = dispatch => {
  return {
    onAuthenticated: token =>
      dispatch({ type: "ON_AUTHENTICATED", token: token })
  };
};

export default connect(
  null,
  mapDispatchToProps
)(Login);
```

```js
// components/Menu.js

import React from "react";
import { NavLink } from "react-router-dom";
import { connect } from "react-redux";

function Menu(props) {
  const handleSignout = () => {
    // remove the jsonwebtoken from local storage
    localStorage.removeItem("jsonwebtoken");
    // update global state to set isAuthenticated = false
    props.onSignout();
  };

  return (
    <ul>
      <li>
        <NavLink to="/">Login</NavLink>
      </li>
      <li>
        <NavLink to="/register">Register</NavLink>
      </li>
      {props.authenticated ? (
        <li>
          <NavLink to="/my-books">My Books</NavLink>
        </li>
      ) : null}
      {props.authenticated ? (
        <li>
          <NavLink to="/add-book">Add Book</NavLink>
        </li>
      ) : null}
      {props.authenticated ? (
        <li>
          <a href="#" onClick={() => handleSignout()}>
            Sign out
          </a>
        </li>
      ) : null}
    </ul>
  );
}

const mapStateToProps = state => {
  return {
    authenticated: state.isAuthenticated // props.authenticated
  };
};

const mapDispatchToProps = dispatch => {
  return {
    onSignout: () => dispatch({ type: "SIGN_OUT" })
  };
};

export default connect(
  mapStateToProps,
  mapDispatchToProps
)(Menu);
```

```js
// components/MyBooks.js

import React from "react";
import axios from "axios";

function MyBooks() {
  const handleGetMyBooks = () => {
    /*
        // passing headers using fetch api 
        
        fetch('http://localhost:3001/api/my-books',{
            headers: {
                'Authorization': localStorage.getItem('jsonwebtoken')
            }
        }).then(response => response.json()) 
        */

    axios.get("http://localhost:3001/api/my-books").then(response => {
      console.log(response.data);
    });
  };

  return (
    <div>
      MyBooks
      <button onClick={() => handleGetMyBooks()}>Get My Books</button>
    </div>
  );
}

export default MyBooks;
```

```js
// components/requireAuth.js

import React, { Component } from "react";
import { connect } from "react-redux";

// higher order component which takes in another component
export default function(ComposedComponent) {
  class Authenticate extends Component {
    constructor(props) {
      super(props);

      if (!this.props.isAuthenticated) {
        this.props.history.push("/");
      }
    }

    render() {
      return <ComposedComponent {...this.props} />;
    }
  }

  const mapStateToProps = state => {
    return {
      isAuthenticated: state.isAuthenticated
    };
  };

  return connect(mapStateToProps)(Authenticate);
}
```

```js
// store/reducer.js

const initialState = {
  isAuthenticated: false
};

const reducer = (state = initialState, action) => {
  switch (action.type) {
    case "ON_AUTHENTICATED":
      return {
        ...state,
        isAuthenticated: action.token ? true : false
      };
    case "SIGN_OUT":
      return {
        ...state,
        isAuthenticated: false
      };
  }

  return state;
};

export default reducer;
```

```js
// utils/authenticate.js

import axios from "axios";

// attaches the token to every single request
export function setAuthenticationHeader(token) {
  // set the token in the header
  if (token) {
    // set the headers
    axios.defaults.headers.common["Authorization"] = `Bearer ${token}`;
  } else {
    // remove the token
    delete axios.defaults.headers.common["Authorization"];
  }
}
```
