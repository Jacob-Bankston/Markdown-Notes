# JSON Web Tokens

## Authentication between Client and Server

When you are sending data from React/Any Client to a Node/Any Server

1. User will login and you will direct a POST call to /login
2. The server will validate the username and password against the database
3. If the credentials are valid, then the server will generate a return token - (JWT)
4. The client gets the token and saves it in local storage [ and updates the redux flag ]
5. On future requests the client must send the token in the headers
6. The server validates the token and then proceed with the request
   1. The server will validate with a middleware of some sort

## Login Portion

- npm init
- npm install express
- set up express
  - const express
  - const app
  - app listen
- npm install cors
- set up /login route

```js
app.post("/login", (req, res) => {
  const username = req.body.username;
  const password = req.body.password;

  let persistedUser = users.find(
    u => u.username == username && u.password == password
  );

  if (persistedUser) {
    // credentials are valid
  } else {
    // credentials are not valid
  }
});
```

- create database to store users information
- import the json web token library
  - github.com/auth0/node-jsonwebtoken
  - `npm install jswonwebtoken`
- require the token
- sign in the token, and have a unique password! Do not use the default!'

```js
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
```

- create react app
- structure the App.js
- set up the components folder
- Make the Login.js component
- Place the Login component in the App.js render
- Set up the Login button in Login.js
- utilize hooks
  - import { useState }
  - `const [user, setUser] = useState({username: '', password: ''})`
  - `<input type="text" onChange={(e) => handleTextChange()} />`
  - `<input type="password" onChange={(e) => handleTextChange()} />`
  - `<button>Login</button>`

```js
const [user, setUser] = useState({ username: "", password: "" });

const handleTextChange = e => {
    setUser({

    })
};

return (
  <div>
    <input type="text" onChange={e => handleTextChange()} />
    <input type="password" onChange={e => handleTextChange()} />
    <button>Login</button>
  </div>
);
```

* set up handleTextChange function
* Check to make sure that you are grabbing the user properties in the dev tools
* Figure out axios! Install axios.
  * Similar to fetch, but it is less to type
  
```js
axios.post('http://localhost:3001/login', {
    username: user.username,
    password: user.passowrd
})
```

* When we post this, it will invoke the login route and return us the token.
* The token is a promise, so you can grab the value from .then

```js
.then(response => {
    console.log(response.data)
})
```

* `localStorage.setItem('jsonwebtoken': response.data.token)`
* install react router
* On the client side implement the handleLogin() function

* Create the BaseLayout.js component
* import { BroswerRouter, Switch, Route } from 'react-router-dom'
* Insert the BrowserRouter in the ReactDOM.render
* Place the Switch routes inside the BaseLayout component in the ReactDOM

* On the server, create Middleware to authenticate the user when they go through a certain set of routes.
* the function has request, response and next arguments

```js
// authMiddleware.js

function authenticate(req, res, next) {

    let headers = req.headers["authorization"]
    

}

module.exports = authenticate
```

* You need to pass in the token from the client side. If you aren't passing in the token, the server has no way to authenticate.
* Get the token out of the local storage then attach it to the axios header

_One of the nicest things about axios is that it allows you to utilize default headers._

```js
import axios from 'axios'

export function setAuthenticationHeader(token) {

    //set the token in the header
    if(token) {
        // set the headers
        axios.defaults.headers.common['Authorization'] = `Bearer ${token}`
    } else {
        // remove the token
        delete axios.defaults.headers.common['Authorization']
    }
}
```

* import the function into your client route that is sending the post, this will greatly reduce the amount of code you write
* now that the client side is effectively sending the json web token, you want to set up the server accepting the token

* update the middleware so it will do something.
* Add the next() function on the bottom of it
* First check that you're getting the headers `console.log(headers)`
* require the function in the app.js
* `app.all('/api/*', (req, res, next) => { /* middleware */ })`
* put the headers into the route - `let headers = req.headers['authorization']`
* split the headers - `let token = headers.split(' ')[1]

* ERROR - cors was sending a pre-flight check to see if they were linked, and not showing the token
  * the one request was actually sending two requests
    * First request was just validating if it was possible to do the second request
    * Second request was actually checking for authorization

* SOLUTION - if statement - check if headers exist, then take the actions you want.

* decrypt token function to be able to check against the database

DO NOT put the password into the token!

This is only authentication for the server. It does not have the routes set up on the client side, it does not export the users into a database, it does not add salt to put the users into the database. There are still a lot of set up things to do prior to going live with this application.

* in the middleware implementation you want to check several layers.
  * if there are headers
  * if the decoded headers works
  * if the persistUser exists

Assignment
* Books application
  * Add Registration and Login with JSON Web Tokens
  * Do this process two or three times and you will become familiar with all of the moving components.