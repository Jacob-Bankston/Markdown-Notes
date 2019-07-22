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
let req = new XLMHttpRequest()
req.open('GET', url) // first part has to be a GET or a POST request, second thing has to be a url

// load event is next! It means the request has been loaded
// attach load event to the XMLHttpRequest object
req.addEventListener('load', () => {
    console.log(this)
})

// sending the request
req.send()
```