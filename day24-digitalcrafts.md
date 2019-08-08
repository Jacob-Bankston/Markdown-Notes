#Digital Crafts Notes - Day 24

## Router

This can simplify your main page set of routes to limit how big the main `app.js` file is, and to make your code more readable.


Router File Example
```js
// trips.js the Router file

const express = require('express')
const router = express.Router()

// localhost:3000/trips
router.get('/trips', (req,res) => {
    res.render('trips')
})

// Once you direct the main route you can add other layers below the higher order router!

// localhost:3000/trips/my-trips
router.get('/my-trips', (req,res) => {
    res.render('trips')
})

module.exports = router
```


Sourcing the Router file in your app.js
```js
const express = require('express')
const app = express()
const mustacheExpress = require('mustache-express')
const tripsRouter = require('./routes/trips')

// /trips => tripsRouter
// /trips/houston => tripsRouter
app.use('/trips', tripsRouter)

// Once you do this you don't need any of the routes that get the /trips page
// it is now the job of the router
```


Use case!
```js
// instead of coding this in the app.js you can use a Router to simplify the main app.js page

app.get('/users', (req,res) => {
    res.send('All users')
})

app.get('/users/:userId', (req,res) => {
    res.send(`The user id ${userId}`)
})

app.get('/users/profile', (req,res) => {
    res.send('All users')
})
```

```js
// source the usage in your app.js file!
app.use('/users', usersRouter)
```

```js
// add the routes in your users.js router file

const express = require('express')
const router = express.Router()

// Top Tier

router.get('/users', (req,res) => {
    res.send('ROOT ROUTE')
})

// Second Tier

// this route is specific
// if it does not match this it will go down the file and find an acceptable route
router.get('/profile', (req,res) => {
    res.send('User profile page')
})

// this route is taking in a parameter
// if it does not match a specific route above, it will go to this route instead
router.get('/:userId', (req,res) => {
    res.send(`The user id ${req.params.userId}`)
})
```

__The overall goal of using the router is to simplify your app.js page!__

Use Case: Check for authentication, if they are not authenticated then they can't access certain pages.

## Azam Gist - app.js and users.js examples

```js
// app.js

const express = require('express')
const app = express() 
const mustacheExpress = require('mustache-express')

const tripsRouter = require('./routes/trips')
const usersRouter = require('./routes/users')

// /trips -> tripsRouter 
// /trips/houston -> tripsRouter
app.use('/trips',tripsRouter)
app.use('/users',usersRouter)

// tell express to use mustache templating engine
app.engine('mustache',mustacheExpress())
// the pages are located in views directory
app.set('views','./views')
// extension will be .mustache
app.set('view engine','mustache')

app.get('/',(req,res) => {
    res.render('index')
})

app.get('/login',(req,res) => {
    res.render('login')
})

app.listen(3000,() => {})
```

```js
//users.js

const express = require('express')
const router = express.Router() 

// localhost:3000/users 
router.get('/',(req,res) => {
    res.send('ROOT ROUTE')
})

// localhost:3000/users/profile
router.get('/profile',(req,res) => {
    res.send('THIS IS PROFILE SCREEN')
})

// localhost:3000/users/12
router.get('/:userId',(req,res) => {
    res.send(`The user id ${req.params.userId}`)
})





module.exports = router
```

## Global additions

```js
// instead of using trips = [] you would have to make the variable global
// this way you can access it in your router file

global.trips = []
```

## Partials

Adding content that you use to inject into the main html files.

You have to tell mustache that you are using partials.

__Partials Set Up!__
```js
// Using __dirname

console.log(__dirname) // Users/jacobbankston/Desktop/node-200
```

```js
const path = require('path')

// this will give us a path to the views folder
const VIEWS_PATH = path.join(__direname, '/views')

app.engine('mustache', mustacheExpress(VIEWS_PATH + '/partials', '.mustache'))

// setting the views path with the variable
app.set('views', VIEWS_PATH)
```

```html
<!-- This is the .mustache file -->
<!-- Inject the partials with this syntax -->

{{> menu}}

```

Partials are really useful to develop your pages in multiple sections!

## Static files

Went through and added this to the project yesterday!

Getting started Express JS - Static files

This is how you can source css and other files into your server side file.

```js
// '/tripStyles' is the alias, you don't need to include the alias.
//localhost:3000/site.css
app.use(express.static('css'))

// localhost:3000/tripStyles/site.css
app.use('/tripStyles', express.static('css'))
```

```js
// localhost:3000/css/site.css
app.use('/css', express.static('css'))
```

```js
// localhost:3000/img/site.img
app.use('/img', express.static('img'))
```

## Assignment

/api/movies - returns an array of movies in JSON

You can expose GET or POST methods if you choose. You can limit it if you would like.

