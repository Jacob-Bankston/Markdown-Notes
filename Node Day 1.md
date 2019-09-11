# Day 22 - Digital Crafts Notes

## Node.js

What is Node?

Now that JavaScript is the most popular language in the world, you can pretty much make anything in the world with JavaScript. Anything you can imagine you can make with JavaScript.

Node allows JavaScript to run on the server.

CLIENT => SERVER => DATABASE

JavaScript => JavaScript => DATABASE with Node.js

Have a client folder and a COMPLETELY SEPARATE server file

Client
* HTML
* CSS
* Images
* JavaScript

Server
* JavaScript

npm = Node Package Manager

To start your node folder use `$ npm init`

For now you can use default values, but later you will want to use descriptive files

It will create a package.json file!
* Used this in the Expo application in the React Native Application
* It will create a main file called index.js
* The index.js file will be the javascript that will run on your code
* This file is more of a configuration file

Use nodemon.io to save yourself some time with rerunning your node code - nodemon = node monitor

Research into npm packages that are available to work with your packages from node

You can run a server without using packages, but it will be very long and difficult to do so. Most people use Express JS.

## Express JS

`npm install express`

This is a way to quickly create your node js server! This is your go to!

Never check in node modules on github!!

If you start checking in the node modules it's way too much data to be including in the project.

Inside of the index.js file you want to add the following

```js
// require means we will be using the express module
const express = require('express')
// creates an instance of express module
const app = express()

// manipulate the urls here!

// 3000 is the default, you're telling the computer which port to listen to
app.listen(3000, () => {
    console.log('Server is running...')
})

```

`node app.js` to run your code.
ctrl-c to kill the application

Error: `Cannot GET /`
The `/` stands for the root of the website

The root would be the index of the website without any extensions after the slash.

These are called __routes__ or __endpoints__.

```js

// using the get function for text
// the first argument is the location
// the second part is an anonymous function that takes in two parameters
app.get('/', (res,req) => {
    res.send("Hello, Welcome to Node!")
})

```

Run `nodemon app.js`

```js

// returning JSON
app.get('/hello', (req,res) => {
    res.json({
        message: 'Hello World'
    })
})

// returning an array of JSON
app.get('/movies',(req,res) =>{
    let movie1 = {
        name: 'Spiderman'
    }
    let movie2 = {
        name: 'Batman'
    }

    let movies = [movie1, movie2]

    res.json(movies)
})

```

Create a common folder

- Movies
  - Client
    - index.html
    - Styles
      - styles.css
    - JS
      - app.js
    - Images
  - Server
    - node_modules
    - app.js
    - package-lock.json
    - package.json

```js

fetch('http://localhost:3000/movies')
    .then(response => response.json())
    .then(json => console.log(json))

```

The CORS issue says you can not do a cross kind of request, your server has to approve it.
The CORS issue can not be solved on the client side, but it can be solved on the server side!

In your directory install the cors package

`npm install cors`

You implement this into your server app.js file

```js

const express = require('express')
const app = express()
const cors = require('cors')

// middleware - a middle man between a request and a response
app.use(cors())

```

This is huge! Now you have created your client side and you have created your server side!

## Routes

You can change the routes with a __Route Parameter__

Example: movies/comedy, movies/action, movies/horror OR movies/:genre

```js

// You have to use the colon to create the parameter, otherwise it's just a normal route
// Make the parameter name descriptive, so when you call it you know what you're talking about
app.get('/movies/:genre' (req, res) => {
    let genre = req.params.genre
    console.log(genre)
    // always remember to respond!
    res.json({genre: genre})
})

app.get('/movies/:genre/year/:year' (req, res) => {
    let genre = req.params.genre
    let year = req.params.year
    console.log(genre)
    // always remember to respond!
    res.send("The genre is " + genre + "year is " + year)
    res.send(`The genre is ${genre} and the year is ${year}`)
})

```


In your client side file.
```js

let genre = 'fiction'
let year = '2019'

fetch(`local:3000/movies/${genre}/year/${year})`)

```

## Post Requests for the Movies

```js

// post and get are completely different
app.post('/movies', (req,res) => {

    let movieName = req.body.movieName
    let movieYear = req.body.movieYear

    // check that your server is running and check in Postman
    // Always a good idea to make sure that your route is running via Postman
    console.log(movieName)
    console.log(movieYear)

    res.send('Movie Saved!')

})
```

In Postman - Put in your url - Select GET or POST - Set your Headers - Insert Your Body - Send

Header - Content-Type: application/json

*Use the exact parameters that are in the server*

Express doesn't know how to parse JSON

Body Parser Package via npm
`npm install body-parser`

Make sure that you're inside the correct directory!! 

```js
const bodyParser = require('body-parser')
app.use(bodyParser.json())
```

```js
app.post('/movies', (req,res) => {

    let movieName = req.body.movieName
    let movieYear = req.body.movieYear

    let movie = {
        name: movieName,
        year: movieYear
    }

    console.log(movieName)
    console.log(movieYear)

    res.send('Movie Saved!')

})
```

`app.use` means we are using a middleware