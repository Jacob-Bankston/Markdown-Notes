# Day 18 - Digital Crafts - Notes

##Review

```js
let req = new XMLHttpRequest()
req.open('GET', url)

// using the function knows that it is inside this XMLHttpRequest
req.addEventListener('load', function() {
    console.log('function()')
    console.log(this) //this is an XMLHttpRequest object
})

// using the arrow function looks to the parent scope like a class or the window
req.addEventListener('load', () => {

    console.log(event)
    
    console.log('arrow function')
    console.log(this) // this is a window object
})

req.send()
```

If you can not access XMLHttpRequest you can not access the property responseText - which means you can not get the content that you need.

When you're working with http you can not pass objects you can only pass text, integers, dictionaries, and other primitive types.

##Events

Inside of an arrow function it creates something called an event. When you console.log() this event it comes out as a ProgressEvent. This is the way to get the properties from an arrow function!

```js
req.addEventListener('load', () => {

    // event.currentTarget is XMLHttpRequest object
    let request = event.currentTarget

    let movies = JSON.parse(request.responseText.Search)

    // a common problem that you will have with map is it does not work
    // if the object is not an array!
    let movieItems = movies.map(movie => {
        return `<span>${movie.Title}</span>`
    })

    movieList.innerHTML = movieItems.join('')
})
```

`JSON.parse()` - This will take your dictionary or array and turn it back into the dictionary or array.

__Callback Function__ - Use the callback function as a parameter so you can choose different functions to run through the main function. Pulling different sorting methods or different sections to sort.

JavaScript will rush through everything that it can quickly, so you have to design your javascript to account for this tendency.

##Process

1. Write your code to test if it works
2. Write out the same code as functions that each do one step
   
This process will make your code a lot more flexible.

Your function should always only do one thing. If it does more than one, stop and figure out how to make it separate functions.

##Promises

```js
let promise = new Promise((resolve, reject) => {
    resolve()
})

promise.then(() => {
    console.log("resolved")
})
```

You can change the events together with `.then`

```js
let promise = new Promise((resolve, reject) => {
    setTimeout(() => {
        resolve("Spiderman", "Batman")
    }, 5000)    
})

promise.then((movies) => {
    console.log(movies)
    return movies
}).then((movies) => {
    console.log("Filter the movies based on rating")
    return movies
}).then((m) => {
    console.log("Filter on fav movies")
    console.log(m)
})
```

`.catch` is when something bad happens. Just like a try/catch

```js
.catch((error) => {
    console.log(error)
})
```

Promises are like a sugar coating for callbacks!

##Fetch Library

```js

let moviesURL = url

fetch(moviesURL)
    .then(response => {
        return (response.json()) // response.json() returns a promise
    }).then(json => {
        console.log(json)
    })
```

```js
async function fetchMovies() {
    let response = await fetch(moviesURL) // you must use await inside a function marked async
    let json = await response.json()
    console.log(json)
}
```

`await` does the evaluation of the promise for you!