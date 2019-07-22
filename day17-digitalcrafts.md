# Day 17 - Digital Crafts - Notes

### Understanding GET and POST, Consuming Web API using XMLHttpRequest

You can see the specific type of request in the developer tools network tab.

Selecting them you can get the information about them as well

Read more about GET and POST requests

Without post requests you can not create any data

GET requests are in JSON

if it is in an older format it will be in XML

OMDb API - The Open Movie Database

News API

The company that creates the API is incentivized by being able to have one source to pull all of their data from for all of their products.

In the real world every API should be connected to a database

github public apis!!

APIs are created by the backend developers

Test your json skills with jsonplaceholder!

```js
let url = 'https://jsonplaceholder.typicode.com/posts'


```

asynchronous requests - this means that the bigger stuff will happen in the background and not mess up the user's interface

// XLMHttpRequest

```js
let req = new XMLHttpRequest()
req.open('GET', url) // first part has to be a GET or a POST request, second thing has to be a url

// load event is next! It means the request has been loaded
// attach load event to the XMLHttpRequest object
req.addEventListener('load', function() {

    // Using JSON.parse function to parse JSON string to a JavaScript Object
    let user = JSON.parse("{'name':'John'}")
    console.log(user)
    // whenever you're writing JSON style you will always have quotes around the key and value items, normal JavaScript doesn't have quotes around the key!
    // if you are passing in a JSON string it has to be in JSON format or it will return an error!

    let posts = JSON.parse(this.responseText)
    console.log(posts)

    posts.map(post => {
        return `<div>
                    <h4>${post.title}</h4>
                    <p>${post.body}</p>
                </div>`
    })


    
    console.log(this.responseText) // this is a way to grab the text from the XMLHttpRequest
})

// sending the request
req.send()
```

when you are talking about urls and apis then they can also be referred to as endpoints

The mozilla developers website has a lot of information on XMLhttpRequests

reqres.in

download postman

```js

// app.js file from Azam

let postList = document.getElementById("postList")

let url = 'https://jsonplaceholder.typicode.com/posts'

// XMLHttpRequest 
let req = new XMLHttpRequest() 
req.open('GET',url)
// attach load event to the XMLHttpRequest object 
req.addEventListener('load',function() {

    // Using JSON.parse function to parse 
    // JSON string to JavaScript object
    //let user = JSON.parse('{"name":"John"}')

    let posts = JSON.parse(this.responseText)

    let postItems = posts.map(post => {
        return `<div>
                    <h4>${post.title}</h4>
                    <p>${post.body}</p>
                </div>`
    })

    postList.innerHTML = postItems.join('')


    console.log(posts)
})

// sending the request 
req.send() 
```

```html

<!-- Example html stuff -->

    <head></head>

<body>

    <div id="movieList">

    </div>

    <script src="movies.js"></script>
</body>
</html>
```

```js

// movies example

let movieList = document.getElementById("movieList")

let moviesURL = "http://www.omdbapi.com/?s=Batman&page=2&apikey=564727fa"

let req = new XMLHttpRequest()
req.open('GET',moviesURL)
req.addEventListener('load',() => {
    let movies = JSON.parse(event.currentTarget.responseText) // 
    
    let movieItems =  movies.Search.map(movie => {
        return `<div>
                    <h2>${movie.Title}</h2>
                    <img src='${movie.Poster}' />
                </div>`
    })

    movieList.innerHTML = movieItems.join('')
    
    //event is available automatically 
    console.log(movies.Search)
}) 

// make the actual request...
req.send() 
```