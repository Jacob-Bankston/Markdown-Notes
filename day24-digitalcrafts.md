#Digital Crafts Notes - Day 23

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

