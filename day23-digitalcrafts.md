#Digital Crafts Notes - Day 23

## Review from Monday!
Step 1: Initialize node
* `npm init`

Step 2: Install Express
* `npm install express`

Step 3: Add Express to your Node.js file
* `const express = require('express')`
* `const app = express()`
* `const PORT = 3000`

Step 4: Set up your host
* `app.listen(3000, () => { console.log("Server is running...") })`
  
Step 5: Create a Get Request
* response: text `res.send`
* response: json `res.json`

Step 6: Adding Routes `/greet/:name`
* The colon will create a dynamic route parameter
* You will have to get the parameter from the user using request `req`
* `let userName = req.params.name`

Step 7: Set up your Middleware
* Install body-parser
  * `npm install body-parser`
  * `const bodyParser = require('body-parser')
* Install cors
  * `npm install cors`
  * `const cors = require('cors')

Step 8: Check Postman
* Set up Headers
  * Key: `Content-Type`
  * Value: `application/json`
* Set up raw Body section
  * Using the same keys that you're expecting in your server!!
  * `{"firstName": "John", "lastName": "Doe"}`

Step 9: Update
* app.put

Step 10: Delete
* app.delete

Step 11: Make sure that you are returning something!!
* `res.json({success: true, message: "User has been created!"})`

Client Side
Step 12: Fetch the information
* `fetch('http://localhost:3000/users', {method: 'POST', body: JSON.stringify({})}).then(json => {if(json.scucess == true) { //update}}
)`

Step 13: You can also send a error message!
* `res.status(//ERROR CODE).json`

## New Information!!

**Utilizing classes!**
```js
// Create a new file for your models!
// Create a models folder

class User {
    constructor(firstName, lastName) {
        this.firstName = firstName
        this.lastName = lastName
    }
}

// exporting means that the User class is now available for the outside world to be used in the other files
module.exports = User

// now you can import it via the require function built in!
```

```js
// in your app.js server
const User = require('./models/user')

let user = new User('John', 'Doe')
```

Now you can manipulate the classes on the server side by creating functions for those classes!
```js
class User {
    constructor(firstName, lastName) {
        this.firstName = firstName
        this.lastName = lastName
    }

    addAddress(address) {
        this.addresses.push(address)
    }
}
```

On the client side there is no `require`

You can export multiple things, it's not the most optimal, but it's how some services and tools use it. This is what you would put in the file to export from!
* `module.exports = User`
* `module.exports = Address`
* `module.exports = {User: User, Address: Address}`
  
```js
// adding the classes into your app.js server file
const Models = require('./models/user')

const user = new Models.User()
const address = new Models.Address()
```

## Server Side Pages

Up until now you've been working on the Client Side and some of the Server Side. The only thing that the server side is doing right now is sending you JSON.

The Client side is doing all of the heavy lifting of converting the JSON into something usable.

If you ever hear about a Web API, they're talking about a server that is sending the client back JSON.

Now we're going to flip that around! We're going to make the Server do all of the hard work! The server will send back a completed HTML page!

Client => Request Information => Server => Response of Completed HTML Page

There will be no client side pages with this mentality! You just create one server folder for everything.

## Template Frameworks

This is when you are getting the framework of the html page from the server side. 

Template Engines: `pug` `jade` `mustache` `handlebars`

Microsoft DotNet: `Razor`

Swift: `Leaf`

Ruby: `Ruby on Rails`

## Mustache Framework

`npm init`
`npm install express`
`npm install body-parser`
`npm install mustache-express`
* Make sure that you install `mustache-express` not just `mustache`
* The documentation for mustache is not that great. Go into Azam's course on Udemy to refine your knowledge base on the material.

## Setting up your Mustache in your app.js

```js
// app.js

const express = require('express')
const app = express()

// add in mustache, don't forget the hyphen!
const mustacheExpress = require('mustache-express')

// removes the need for body-parser
app.use(express.urlencoded())

// tell express to use mustache template engine
app.engine('mustache', mustacheExpress())
// the pages are located in views directory
// views is the standard
app.set('views', './views')
// extension will be .mustache
app.set('view engine', 'mustache')
```

## Adding Mustache Files

Add a views folder!
Add a `index.mustache` file!

All valid `HTML` is valid `mustache`!
If you don't have colorized mustache just look up mustache colorized on vscode!

```html
<html>
    <head></head>
    <body>
      <h1>Hello Mustache!</h1>
    </body>
</html>

```

Goal: When you go to the root `'/'` then you get the `index.mustache`

```js
app.get('/', (req,res) => {
    res.render('index')
})

// remember to start your server or it won't render anything!

// you can restart your server by typing rs!
```

Putting double brackets around something in the mustache file is the way that mustache files inject a variable.

```html
<!-- Adding variables! -->
<html>
    <head></head>
    <body>
      <h1>Hello {{name}}!</h1>
      <h3>Age is {{age}}</h3>
    </body>
</html>

```
```js
// insert the object into the response render!
app.get('/', (req,res) => {
    res.render('index', {name: 'John Doe', age: 30})
})
```

## Lists

```js
// insert the object into the response render!
app.get('/animals', (req,res) => {
    let animals = ['cat', 'dog', 'lion', 'tiger']
    res.render('animals', {animals: animals})
})
```

There's not a way to make a master page, there will be a lot of copy pasting.

```html
<!-- animals.html! -->
<html>
    <head></head>
    <body>
        <!-- This makes a comma separated version of the list -->
        {{animals}}
    </body>
</html>
```

```html
<!-- animals.html! -->
<html>
    <head></head>
    <body>
        <!-- This is like a mustache forEach loop -->
        {{#animals}}
            <!-- Whatever the value is inside of the array, inject that value. -->
            <div style="background-color: yellow">
              {{.}}
            </div>

        {{/animals}}
    </body>
</html>
```

The dot syntax only injects the value as it is. It only really works for text, and you won't really use it.

## Handling Objects/Classes to loop over

```js
app.get('/users', (req,res) => {
    let users = [{name: 'John', age: 45}, {name: 'Mary', age: 34}]
    res.render('users', {users: users})
})
```

```html
<!-- users.html! -->
<html>
    <head></head>
    <body>
        {{#users}}
            <!-- Instead of the . property, you declare which property you want! -->
              {{name}} - {{age}}

        {{/users}}
    </body>
</html>
```

## Forms

```html
<!-- addUser.html! -->
<html>
    <head></head>
    <body>
        <!-- Form is a very special event that allows you to input values -->
        <form action="/add-user" method="POST">
        <!-- You need to clarify that you're posting the information -->
            <input type="text" />
            <input type="text" />
            <!-- You need a button or submit input to send the data -->
            <button>Save</button>
        </form>
    </body>
</html>
```

```js
// navigating to the form
app.get('/add-user', (req, res) => {
    res.render('add-user')
})
```

Use the Network Tab in your Google Chrome Developer Tools to figure out what's going on with the form.

Network Tab => Console => Headers Tab
* Check if it's sent to the server!
* You can check from this tab what information was passed in the request!
* Scroll to the bottom of the Headers to check what was passed in.

```html
<html>
    <head></head>
    <body>
        <form action="/add-user" method="POST">
        <!-- You have to add the name to the inputs to pass the info -->
            <input type="text" name="fullName" />
            <input type="text" name="age" />
            <button>Save</button>
        </form>
    </body>
</html>
```

Add the Post!

```js
// removes the need for body-parser
app.use(express.urlencoded())

let users = []

app.post('add-user', (req,res) => {
    let fullName = req.body.fullName
    let age = parseInt(req.body.age)

    let user = {name: fullName, age: age}
    users.push(user)
    // This will redirect the get route to the users page entered earlier
    res.redirect('/users')

    // res.json({success: true})
})

app.get('/users', (req,res) => {
    res.render('users', {users: users})
})
```

If you're sending someone for a redirect, you can render the page, but redirection will allow you inject things from the defined injection method you defined earlier.

__Common Server Side Frameworks__
`Django` - Python
`ASP.net` - Microsoft
`PHP` - WordPress
`Ruby on Rails` - Ruby

__Udemy Course__
Today's Material was Section 6 and Section 7

## Assignment: Trips

* App should allow user to add a new trip
  * title
  * image
  * date of departure
  * date of return
* App should allow user to View all trips
* App should allow user to Delete all trips
* App should allow user to Update all trips
* App should allow user to sort trips by date
* App should allow user to sort trips by city
* Responsive for Mobile

Think about :routes for checking out specific trips and isolating a trip

## Tips on Deleting Files

Inside the `{{#trips}}` you are displaying the information from the trips.

Place a form inside of each trip area! This way you can isolate each of the items in the list.

```html

{{#trips}} <!-- Assuming that we have 5 trips, each trip will have their own form -->
  <form action="/delete-trip" method="POST">
    <div>
      <img src="" />
      <label>{{name}}</label>
      <button>Delete</button>
      <!-- You can add a hidden field to not display something, but carry the data -->
      <input type="hidden" name="tripName" value="{{name}}" />
    </div>
  </form>
{{/trips}}

```

```js
let tripName = req.body.tripName
trips = trips.filter(trip => {
    trip.name != tripName
})

res.redirect('/')
```

extra credit! look into `node uuid`