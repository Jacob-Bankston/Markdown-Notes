# Day 20 - Digital Crafts - Notes

```js
// REVIEW OF CALLBACK FUNCTIONS

// STEP 1
fetch(url).then(response => {
    console.log(response)
})

// STEP 2
fetch(url).then(response => {
    return response.json()
})

// STEP 3
fetch(url).then(response => {
    return response.json()
}).then(json => {
    console.log(json)
})

// STEP 4
const weatherDiv = document.getElementById("weatherDiv")

fetch(url).then(response => {
    return response.json()
}).then(json => {
    let string = `<span id="tempSpan">Temperature:${json.main.temp}</span>`
    weatherDiv.innerHTML = string
})

// STEP 5
function fetchWeather() {

    feth(url).then(response => {
        return response.json()
    }).then(json => {
        displayWeather(json) // By calling the displayWeather function you have tied these functions together
        // You want to allow other functions to tie together so this is not the optimal method
    })
}

function displayWeather(weather) {

    let spanElement = `<span id="tempSpan">Temperature: ${weather.main.temp}</span>`
    weatherDiv.innerHTML = spanElement
}

fetchWeather()

// STEP 6
function fetchWeather(callback) {

    feth(url).then(response => {
        return response.json()
    }).then(json => {
        callback(json)
    })
}

function displayWeather(weather) {

    let spanElement = `<span id="tempSpan">Temperature: ${weather.main.temp}</span>`
    weatherDiv.innerHTML = spanElement
}


function displayFancyWeather(weather) {
    
    let weatherItem = `<h1>${weather.main.temp}</h1>`
    fancyWeatherDiv.innerHTML = weatherItem

}

fetchWeather(displayWeather)

// OPTION STEP 6 ANONYMOUS FUNCTION
function fetchWeather(callback) {

    feth(url).then(response => {
        return response.json()
    }).then(json => {
        callback(json) // callback can be ANY function which can take one argument
    })
}

function displayWeather(weather) {

    let spanElement = `<span id="tempSpan">Temperature: ${weather.main.temp}</span>`
    weatherDiv.innerHTML = spanElement
}


function displayFancyWeather(weather) {
    
    let weatherItem = `<h1>${weather.main.temp}</h1>`
    fancyWeatherDiv.innerHTML = weatherItem

}

fetchWeather((weather) => { // You do not have to pass in an assigned function you can simply do an anonymous function
    let weatherItem = `<h1>${weather.main.temp}</h1>`
    fancyWeatherDiv.innerHTML = weatherItem
})

// OPTION STEP 7 - AWAIT version of Fetch Weather

async function fetchWeather2() {
    let response = await fetch(url)
    let json = await response.json()
    return json
}

let functional = await fetchWeather2() // assigning the function to a variable and telling it to await
console.log(fetchWeather2())

// OR

async function fetchWeather2() {
    let response = await fetch(url)
    let json = await response.json()
    return json
}

fetchWeather2().then(json => console.log(json)) // using a .then() on the promise to resolve the information

```

Whenever you are doing a fetch request you need to know when it actually returns you something. 

You need to use a callback function or await. 

Check this by putting breakpoints in your debugging.

Debugging will be your lifesaver in this. It will take a lot of practice to fully understand.

##More Firebase - Appending more Objects to nodes

If you don't have any leaves you can't append anything.

```js

let usersRef = database.ref("users")

addUserButton.addeEventListener('click', () => {
    let name = nameTextBox.value
    let age = ageTextBox.value
    saveUser(name, age)
})
```

* Root
  * Users
    * L1234
      * Name
      * Age
      * Hobby - this is an array!!
        * 0
          * name
          * category
        * 1
          * name
          * category

```js

//Hard Coding into to prove concept
function saveUser(name, age) {

    let hobby = {name: 'Golf', category: 'Sports'}
    let hobby2 = {name: 'Hiking', category: 'Outdoors'}

    usersRef.push({ // this .push() function has nothing to do with Array.push()
        name: name,
        age: age
        hobbies: [hobby, hobby2]
    })

}
```

##Adding Classes

New file - hobby.js - You need to load the hobby.js file before the app.js file

```js

// hobby.js
class Hobby {
    constructor(name, category) {
        this.name = name
        this.category = category
    }
}

```

```js

// Updating app.js
function saveUser(name, age) {

    let hobby1 = new Hobby('Golf', 'Sports')
    let hobby2 = new Hobby('Hiking', 'Outdoors')

    usersRef.push({ // this .push() function has nothing to do with Array.push()
        name: name,
        age: age
        hobbies: [hobby1, hobby2]
    })

}
```

Creating a User Class! New file - user.js

```js

// user.js
class User {
    constructor(name, age) {
        this.name = name
        this.age = age
        this.hobbies = []
    }
}

```

```html
<script src="user.js"></script>
<script src="hobby.js"></script>
<script src="app.js"></script>
```

```js

// Updating app.js
function saveUser(name, age) {

    let hobby1 = new Hobby('Golf', 'Sports')
    let hobby2 = new Hobby('Hiking', 'Outdoors')

    let user = new User(name, age)
    user.addHobby(hobby1)
    user.addHobby(hobby2)
    //user.hobbies = [hobby1, hobby2]

    usersRef.push(user)

}
```

```js
// Updating to add a Hobby Function
// user.js
class User {
    constructor(name, age) {
        this.name = name
        this.age = age
        this.hobbies = []
    }

    addHobby(hobby) {
        // validate the hobby so that you are not adding duplicates
        this.hobbies.push(hobby)
    }
}
```

Now we have to get the input from the users!

```js
// Updating to add the userId
// user.js
class User {
    constructor(name, age) {
        this.name = name
        this.age = age
        this.userId = ''
        this.hobbies = []
    }

    addHobby(hobby) {
        // validate the hobby so that you are not adding duplicates
        this.hobbies.push(hobby)
    }
}
```

```js
usersRef.on('value', (snapshot) => {
    console.log(snapshot.val())

    let users = []

    snapshot.forEach(item => {  // You can use any variable for snapshot, but if any value is changed under the users reference then it will contain the snapshot
        console.log(item.key)
        console.log(item.val())
        let userItem - item.val()
        let user = new User(userItem.name, userItem.age)
        user.userId = item.key // unique key from firebase database

        user.hobbies = userItem.hobbies

        console.log(item.val())

        users.push(user) // adding to array
    })

    displayUsers(users)

})

function displayUsers(users) {

    users.map(user => {

        let hobbyItems = user.hobbies.map(hobby => {
            return `<p>${hobby.name}</p>`
        }).join('')

        return `<div>
                    ${user.name}
                    <input type="text" placeholder="name goes here"><input>
                    <button onclick'addHobby("${user.userId}")'>Add User</button><br>
                    ${hobbyItems}
                </div>`
    })

    userList.innerHTML = userItems.join('')

}

function addHobby(userId) {
    let hobby = obj.previousElementSibling.value
    usersRef.child(userId).set({
        hobbies: hobbies.concat(hobby)
    })
}
```

Make sure that the snapshot function runs on load of the page while it's wrapped in the function.

* Root
  * Stores
    * Walmart
      * Address: "222 Wally Ln."
      * Name: "Walmart"

```js
let storesRef = database.ref('stores').child('Walmart').set( {
    name: 'Walmart',
    address: '222 Wally Ln.'
})

let storesRef = database.ref('stores').child('HEB').set( {
    name: 'HEB',
    address: '333 HEB St.'
})

let storesRef = database.ref('stores').child('Krogers').set( {
    name: 'Krogers',
    address: '222 Krogie Pl.'
})
```

Make sure that the name of all of the nodes are unique!

```js
// creating a unique key for the store
let storesRef = database.ref('stores').push({
    name: 'Walmart',
    address: '1200 Studemont Dr.'
})
```

```js
// accessing the child using the key
let storesRef = database.ref('stores').child().set({
    name: 'Walmart'
    address: '1200 Gessner Rd.'
})
```

```js
database.ref('value', (snapshot) => {
    console.log("VALUE EVENT FIRED...")
    for(key in snapshot.val) {
        console.log(key)
    }
})
```