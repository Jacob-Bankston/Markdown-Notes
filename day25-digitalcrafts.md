#Digital Crafts Notes - Day 25

You can import the fetch tool via node package manager `npm` to be able to pull in other apis to your server side page. Something like...

```js
app.get('/', (req,res) => {

    // fetch the api and pull the image!

    res.render('index', //fetched image )
})
```

You can nest objects inside objects and pull them out in the mustache file by nesting the hashtags!

```html
{{#movies}}

    {{#actors}}
        {{name}}
        {{role}}
        {{awards}}
    {{/actors}}

{{/movies}}

```

You can do conditional statements inside of the mustache files!

linking partials!

```js
app.engine('mustache', mustacheExpress(VIEWS_PATH + '/partials', '.mustache'))
```

Great Review this morning! Refreshed all the material from this week.

## Sessions and Creating your own Middleware

Sessions allow you to pass information to the other pages!

Don't use sensitive information! SSN, Drivers License ID, etc...

```js
const session = require('express-session')

// initialize session
app.use(sessions({
    secret: 'keyboard cat',
    resave: false,
    saveUninitialized: true,
}))

app.use(express.json())
app.use(express.urlencoded())
```

## SALT, SHA256 Encryption, HASH
* The `SHA256` is unique to whatever you put into your black box.
* Then you get the `HASH` code afterwards.
* You input the `SALT` to the black box to create the `HASH`.
* `SALT` is your own personal input code, so don't let anyone know this information.

The way to check if it's working or not is to check the Cookies in the Application Tab.

```js
app.post('/add-info', (req,res) => {

    let name = req.body.tripName

    //put something in the session
    if(req.session) { // check if the session is available first!!
        req.session.tripName = name
    }
})
```

You have to site the session in each area that you want to input the information to.

```js
app.post('/register', (req,res) => {

    let username = req.body.username
    let passowrd = req.body.passowrd

    let user = {username: username, password: password}
    // in a real application you'd check against other usernames
    // in a real application you wouldn't name the variables password!
    // also you would encrypt the password!!

    users.push(user)

    res.redirect('/login')

})
```

You have to create all of the steps for logging in to render the individuals information and propagate that data to the user.

When you go down the ifs/elses then you want to check for the session, then check for a username, then check that the usernames match and have routes to help the user be directed to the appropriate page.

## Middleware

Something between the request and the response firing.

It sounds intimidating, but it's basically a function.

Don't forget to call `next()`, otherwise you will not actually push the request through.

```js

function authenticate(req, res, next) {
    if(req.session) {
        if(req.session.username) {
            //perform the original request
            next()
        } else {
            res.redirect('/login')
        }
    } else {
        res.redirect('/login')
    }
}

app.get('my-trips', authenticate, (req,res) => {
    res.render('my-trips')
})

```

There's a better format to use routes and state that any path going through a particular route will have to use that middleware.

```js
// This works, but will use the middleware on every request
app.use(authenticate) // everything - can't even log in anymore

// This works, but will use the middleware on every route
app.all('*', authenticate) // everything - can't login in either

// This is the recommended way to set this up!
app.all('/trips/*', authenticate) // optimal - only for trips routes

app.use('trips', tripsRouter)
```

You can get more diversity in this functionality by adding in `if` statements in your mustache files.

## Fitz Wisdom Code Snippet

```js
// 
var cb0 = function (req, res, next) {
  console.log('CB0')
  next()
}

var cb1 = function (req, res, next) {
  console.log('CB1')
  next()
}

app.get('/example/d', [cb0, cb1], function (req, res, next) {
  console.log('the response will be sent by the next function ...')
  next()
}, function (req, res) {
  res.send('Hello from D!')
})
```

## Azam Code Snippets

app.js
```js
const express = require('express')
const mustacheExpress = require('mustache-express')
const app = express() 
const path = require('path')
const Trip = require('./models/trip')
// express session 
const session = require('express-session')

// initialize session 
app.use(session({
    secret: 'keyboard cat',
    resave: false,
    saveUninitialized: true,
  }))

app.use(express.json())
app.use(express.urlencoded())
// require authentication for all routes for GET/POST 
// which are inside /trips route 
app.all('/trips/*',authenticate)

const VIEWS_PATH = path.join(__dirname,'/views')
// /Users/azamsharp/Desktop/trips/views
console.log(VIEWS_PATH)

// tell express to use mustache templating engine
app.engine('mustache',mustacheExpress(VIEWS_PATH + '/partials','.mustache'))

// the pages are located in views directory
app.set('views',VIEWS_PATH)
// extension will be .mustache
app.set('view engine','mustache')

let users = [{username: 'johndoe', password: 'password'}] 

let trips = []
let trip1 = new Trip('Houston', '08/11/2010', 'houston.png')
let trip2 = new Trip('Denver', '10/21/2019', 'denver.png')
trips.push(trip1)
trips.push(trip2)

// create an authentication middleware 
function authenticate(req,res,next) {

    if(req.session) {
        if(req.session.username) {
            // perform the original request 
            next()
        } else {
            res.redirect('/login')
        }
    }
}

app.get("/", (req, res) => {

    if(req.session) {
        let name = req.session.tripName 
        console.log(name)
    }

    res.render("index", {trips : trips})
})

app.get('/login',(req,res) => {
    res.render('login')
})

app.get('/trips/my-trips',(req,res) => {
   res.render('my-trips')
})

app.get('/delete-trip',authenticate,(req,res) => {
    res.render('delete-trip')
})

app.get('/logout',(req,res) => {
    if(req.session) {
        req.session.destroy(error => {
            if(error) {
                next(error)
            } else {
                res.redirect('/login')
            }
        }) 
    }
})

app.post('/login',(req,res) => {
    
    let username = req.body.username 
    let password = req.body.password 

    let persistedUser = users.find(user => {
        return user.username == username && user.password == password
    })

    if(persistedUser) {
        // user is authenticated successfully 
        if(req.session) {
            req.session.username = persistedUser.username
            // where should we redirect 
            res.redirect('/my-trips') 
        }
    } else {
        // user is not authenticated successfully 
        res.render('login',{message: 'Invalid username or password'})
    }

})

app.post('/register',(req,res) => {

    let username = req.body.username 
    let password = req.body.password 

    let user = {username: username, password: password}

    users.push(user)

    res.redirect('/login')

})

app.get('/register',(req,res) => {
    res.render('register')
})

app.post('/add-trip',(req,res) => {


    let name = req.body.tripName 
    let date = req.body.tripDate 
    let imageURL = req.body.tripImageURL 

    let trip = new Trip(name,date,imageURL)
    trips.push(trip)

    // put something in the session
    if(req.session) { // check if session is available 
        req.session.tripName = name 
    }


    res.redirect('/')
})

app.get('/add-trip',(req,res) => {
    res.render('add-trip')
})

app.use(express.static('static'))



app.listen(3000,() => {})
```

index.html

```html
<html>
<head>
<link rel="stylesheet" href="/css/styles.css">
</head>
<body>

    {{> menu}}

    {{#trips}}
        {{name}}
        {{date}}
        <img src='/images/{{url}}'/>
    {{/trips}}

<script src="/js/client.js"></script>
</body>
</html>
```

login.mustache

```html
<html>
<head>
<link rel="stylesheet" href="/css/styles.css">
</head>
<body>

    {{> menu}}

    <h1>Login</h1>

   <form action="/login" method="POST">

    <input type="text" name="username" placeholder="Enter username"/>
    <input type="password" name="password" placeholder="Enter password" />
   
    <input type="submit" />

   </form>

   {{message}}

<script src="/js/client.js"></script>
</body>
</html>
```

register.mustache

```html
<html>
<head>
<link rel="stylesheet" href="/css/styles.css">
</head>
<body>

    {{> menu}}

    <h1>Register</h1>

   <form action="/register" method="POST">

    <input type="text" name="username" placeholder="Enter username"/>
    <input type="password" name="password" placeholder="Enter password" />
   
    <input type="submit" />

   </form>

<script src="/js/client.js"></script>
</body>
</html>
```

add-trip.mustache

```html

<html>
<head>
<link rel="stylesheet" href="/css/styles.css">
</head>
<body>

    {{> menu}}

   <form action="/add-trip" method="POST">

    <input type="text" name="tripName" placeholder="Enter name"/>
    <input type="text" name="tripDate" placeholder="Enter date" />
    <input type="text" name="tripImageURL" placeholder="Enter image url" />
    <input type="checkbox" name="favouriteTrip" />
    <input type="submit" />

   </form>

     {{> menu}}

<script src="/js/client.js"></script>
</body>
</html>

```

delete-trip.mustache

```html

```

my-trips.mustache

```html
<html>
<head>
<link rel="stylesheet" href="/css/styles.css">
</head>
<body>

    {{> menu}}


    <h1>My Trips</h1>

<script src="/js/client.js"></script>
</body>
</html>
```

partials/menu.mustache

```html
<header>
    <p><a href="/">Home</a></p>
    <p><a href="/add-trip">Add Trip</a></p>
</header>
```

## Assignment


* Main Project - Week after Next - Back End Project - Randomized Team

* Mini Project - Next Wed. and Thurs.
  * Something fun and useless
  * Criteria
    * Full Stack Application - Team of 2
    * Mini Prize