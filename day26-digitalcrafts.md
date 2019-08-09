#Digital Crafts Notes - Day 26

## Databases
* MS SQL
* Postgres
* MY SQL
* SRLLITE

#### Relational Databases

It stores all the data. If you want to convert it into an object or make it readable you have to do that yourself.

#### Joins

The heart of relational Databases

Each table is specified, but you can join the content together to be able to compare the information. This is the main strength of relational databases.

If you are joining incorrectly, it will slow down the entire process. You have to be sure about how you approach the pulling of the data to make sure you're keeping everything optimized.

`SELECT street FROM addresses WHERE userID = 1`

When you join the tables it will return you a set.

John Doe 01/01/1982 1200 Something Houston, TX
John Doe 01/01/1982 1344 P39 Houston, TX

Next week we will use SQLize - it has a lot of complexity of using it, but it will return you nested objects.

You can use this or any other ORM - Object Relational Mappers.

You can get more versatility out of coding the raw SQL, but you have to have a lot more layers to the code.

There are also Document Databases, and you can do the same things with either, but you pick one over the other to optimize your use.

One to Many Relationship - A single user to many addresses.

Many to Many Relationship - Recipes that contain multiple ingredients, and ingredients used in multiple recipes
* This will generally make a middle table that will contain the primary keys of the other tables.

#### Foreign Key - A location where you share the primary key information between two tables to relate the items to each other.

Firebase is a Document Database - it saves the information in a document reference format of JSON objects.

## Web Sockets

socket.io
`npm init socket.io`

```html
<html>
    <body>

        <ul id="chatMessagesUL" style="background-color: green">
          Chat messages will display here
        </ul>

        <input type="text" id="chatMessageTextBox" />
        <button id="sendButton">Send</button>

    </body>
</html>
```

```js
// app.js

// npm install express
// npm install socket.io

const express = require('express')
const app = express()

app.get('/', (req,res) => {
    res.sendFile(__dirname + '/chat.html')
})

app.listen(3000, () => {

})

```

```js
// app.js

const express = require('express')
const app = express()
const http = require('http').createServer(app) // http is something that allows you to perform socket operations

app.use('/js', express.static('public'))

// create a socket io instance
const io = require('socket.io')(http)

// has to be labeled connection
io.on('connection', (socket) => {
    console.log("You are connected")
})

app.get('/', (req,res) => {
    res.sendFile(__dirname + '/chat.html')
})

http.listen(3000, () => {  // when you run a socket you have to change app.listen to http.listen

})

```
You can use mustache, but it will be a weird experience if there is a form posting because it will refresh the page every time that a user posts.

```html
<html>
    <body>

        <ul id="chatMessagesUL" style="background-color: green">
          Chat messages will display here
        </ul>

        <input type="text" id="chatMessageTextBox" />
        <button id="sendButton">Send</button>
        <!-- This reference has to be made before the client.js file, otherwise the file won't know about sockets. -->
        <script src="/socket.io/socket.io.js"></script>
        <script src="/js/client.js"></script>
    </body>
</html>
```

```js
// client.js

let socket.io()

let chatMessageTextBox = document.getElementById('chatMessageTextBox')
let sendButton = document.getElementById('sendButton')

sendButton.addEventListener('click', () => {

    let chatMessage = chatMessageTextBox.value
    // emit means to send the current event
    // you can think of this as a channel or event or chat room
    // whoever is listening to this channel is going to get the event
    socket.emit('Houston', chatMessage)
})

```

```js
// app.js

const express = require('express')
const app = express()
const http = require('http').createServer(app)

app.use('/js', express.static('public'))

const io = require('socket.io')(http)

io.on('connection', (socket) => {
    console.log("You are connected")

    // this is how you can make the server care about the client.js user input
    socket.on('Houston', (message) => { 
        console.log(message) // this will take the message from the client and print it to the console

        // Then you have to send the message to the specific event
        // This will send the message back to the client/users
        io.emit('Houston', message)
    })
})

app.get('/', (req,res) => {
    res.sendFile(__dirname + '/chat.html')
})

http.listen(3000, () => {

})

```

```js
// client.js

let socket.io()

let chatMessageTextBox = document.getElementById('chatMessageTextBox')
let sendButton = document.getElementById('sendButton')
let chatMessagesUL = document.getElementById('chatMessagesUL')

sendButton.addEventListener('click', () => {

    let chatMessage = chatMessageTextBox.value
    socket.emit('Houston', chatMessage)
})

socket.on('Houston', (message) => { 
    // inserting the chat message into the index window
    let messageLI = `<li>${message}</li>`
    chatMessagesUL.insertAdjacentHTML('beforeend', messageLI)
})

```

Don't use POST or GET requests because it will refresh every time this happens.

Things to Add!
* Authentication
* User limitations

Sockets are for when you need to be completely connected to the server at all times. `ws`

Examples: Ring Doorbell, Cameras outside, Cars data output, Chat applications, Notification systems, Blockchain

Assignment: Advanced Trips Application - Adding Chat Features!

Look at Azam's Udemy course and check out the section that includes `res.locals.username`

He goes over the conditional statements in mustache as well.
{{#isAuthenticated}}
{{/isAuthenticated}}
{{^isAuthenticated}}