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
```

