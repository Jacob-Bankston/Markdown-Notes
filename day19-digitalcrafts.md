# Day 19 - Digital Crafts - Notes

## Coffee Review

```html

<!-- HTML Review Portion -->

<html>

<body>

    <input type="text" id="coffeeNameTextBox" required />
    <input type="text" id="emailTextBox" pattern="" />
    <button id="addOrderButton">Order</button>

    <div id="orderList"></div>

    <script src="app.js"></script>
</body>

</html>
```

```js

// JavaScript Review Portion

let coffeeURL = "http://dc-coffeerun.herokuapp.com/api/coffeeorders/"


let orderList = document.getElementById("orderList")
let coffeeNameTextBox = document.getElementById("coffeeNameTextBox")
let emailTextBox = document.getElementById("emailTextBox")
let addOrderButton = document.getElementById("addOrderButton")

addOrderButton.addEventListener('click',() => {
    let coffee = coffeeNameTextBox.value 
    let email = emailTextBox.value 
    placeOrder(coffee,email)
})

function placeOrder(coffee, email) {

    fetch(coffeeURL, {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json'
        },
        body: JSON.stringify({
          emailAddress: email,
          coffee: coffee,
        })
      }).then(response => response.json())
        .then(result => {
            if(result._id) {
                // looks like the order went through 
                displayOrders() 
            } else {
                // show error to the user on the screen 
            }

        })
        
        /*
        {
    "__v": 0,
    "coffee": "Hot Coffee",
    "emailAddress": "johndoe@gmail.com",
    "_id": "5d386d148846d40400f11f5e"
}
        */

}

async function fetchOrders() {
    
    let response = await fetch(coffeeURL)
    return await response.json() // returning a promise 
    //console.log("inside fetch orders function")
    //console.log(json)
    //return json 
}   

function displayOrders() {
    console.log("calling fetch orders")
    fetchOrders().then(orders => {
        let list = Object.values(orders)
        let orderItems = list.map(order => {
            return `<div>${order.coffee} - ${order.email}</div>`
        })
        
        orderList.innerHTML = orderItems 

    })
}

displayOrders()

/*
fetch(coffeeURL)
    .then(response => {
        return response.json()
    }).then(json => {
        console.log(json)
    })
*/
```


in order to display something delayed correctly you have to return a promise to string together instead of returning the json. Json will work immediately and the promise will wait for further instruction.

`return await response.json()`

It's always a good idea to keep what you're pulling from the user in a seperate function to keep the data separate from when you're manipulating it. I did this yesterday when we added the event listener, pulled the information then put it out as parameters in the second function.

```js
fetch('/users', {
    method: 'POST',
    headers: {
        'Content-Type': 'application/json'
    },
    body: JSON.stringify({
        emailAddress: 'whatever@gmail.com',
        coffee: 'carmel frappe',
    })
})  .then(displayOrders())
    .then(result => {
        if(result._id) {
            dsiplayOrders()
        } else {
            //show error to the user on the screen
        })
```

To prevent something from being inserted that you don't want you want to add a `pattern=""` requirement! Google it! Look up form validation.

##Firebase

One of the ways to have your website persist through time is through firebase

Firebase is a platform by google - it allows you to do a lot of services

We're going to focus on Realtime Database

The biggest advantage of using firebase is that you never have to work on a database. You don't have to know how to deal with the backend information.

Behind the scenes it's changing values using something called sockets.

The biggest disadvantage for using firebase is that it is from google. Google is very quick at killing products.

You set up your application in the store then link the script they give you into your body.

Make a separate file to put your api key and whatnot to insert into your index.html

Cloud Firestore and Realtime Database are very very similar

You can allow read/write privledges on the database to allow use of ANYONE that has access to the information to manipulate it, or, of course, you can lock the information.

console.firebase.google.com

This is the developer tool area that you will go through your firebase things

Once you select your services that you want to integrate you link them after the firebase link.

##Inner HTML

Link 1 - link the firebase app
Link 2 - link the firebase app features
Link 3 - script they give you when you created it
Variable - create a variable for firebase.database() || Firebase.database.ref
Link 4 - your personal javascript file

##Database Structure

* Root (root of the tree)
  * Users (branch of the tree)
    * User1 (branch of the tree)
      * name (leaf of the tree)
        * "John" (value of the leaf)
      * age (leaf of the tree)
        * "30" (value of the leaf)
    * User2 (branch of the tree)
      * name (leaf of the tree)
        * "Sarah" (value of the leaf)
      * age (leaf of the tree)
        * "28" (value of the leaf)

```js
let usersRef = database.ref("users")
usersRef.child("user1").set({
    name: 'John'
    age: 23
})
usersRef.child("user2").set({
    name: 'Mary'
    age: 25
})
```

You can not have an empty child, they need to have leaves to show up!

Whenever you are thinking about storing data in the database, think about that data times 1 million users or 10 million, etc...

```js
let usersRef = database.ref('users')

usersRef.on('value', (snapshot) => { // Any values that are changed in the database 
// it will reload EVERYTHING, not the best for big apps

    let users = []

    console.log("VALUE CHANGE EVENT OCCURED")
    for(key in snapshot.val()) {
        let user = snapshot.val()[key]
        user.key = key
        console.log(user)
        users.push(user) // normal array functionality
    }

    displayUsers(users)

})

function displayUsers(users) {
    users.map(user => {
        return `<div>
                    ${user.name} - ${user.age}
                </div>`
    })

    userList.innerHTML = usersItems.join('')
}
```

```html
<!-- HTML Firebase Azam Notes Portion -->

<html>
    <body>

        <h2>Add User</h2>
        <input type="text" id="nameTextBox" />
        <input type="text" id="ageTextBox" />
        <button id="addUserButton">Add User</button>

        <div id="userList" />

        <!-- The core Firebase JS SDK is always required and must be listed first -->
<script src="https://www.gstatic.com/firebasejs/6.3.1/firebase-app.js"></script>
<script src="https://www.gstatic.com/firebasejs/6.3.1/firebase-database.js"></script>

<!-- TODO: Add SDKs for Firebase products that you want to use
     https://firebase.google.com/docs/web/setup#config-web-app -->

<script>
  // Your web app's Firebase configuration
  var firebaseConfig = {
    apiKey: "AIzaSyDB6hPm3tGd5R1BNQQn24KDcNFQ7tuidoc",
    authDomain: "groceryapp-30a4d.firebaseapp.com",
    databaseURL: "https://groceryapp-30a4d.firebaseio.com",
    projectId: "groceryapp-30a4d",
    storageBucket: "",
    messagingSenderId: "343565691441",
    appId: "1:343565691441:web:98d85fb6daa7e62c"
  };
  // Initialize Firebase
  firebase.initializeApp(firebaseConfig);
  // create an object of firebase database 
  var database = firebase.database() 
</script>
    <script src="app.js"></script>
    </body>
</html>
```

```js

// Firebase app.js Azam Notes

let nameTextBox = document.getElementById("nameTextBox")
let ageTextBox = document.getElementById("ageTextBox")
let addUserButton = document.getElementById("addUserButton")
let userList = document.getElementById("userList")


let usersRef = database.ref('users')

// setup observation 
/*
commentsRef.on('child_changed', function(data) {
    setCommentValues(postElement, data.key, data.val().text, data.val().author);
  }); */

usersRef.on('value',(snapshot) => {

    let users = [] 

    console.log("VALUE CHANGED EVENT OCCURED")
    for(key in snapshot.val()) {
        let user = snapshot.val()[key]
        user.key = key 
        console.log(user)
        users.push(user)
    }

    displayUsers(users)
    //let users = Object.values(snapshot.val())
    //console.log(users)
})

function deleteUser(key) {
    usersRef.child(key).remove() 
}

function displayUsers(users) {
    let userItems = users.map(user => {
        return `<div>${user.name} - ${user.age} <button onclick='deleteUser("${user.key}")'>Delete</button> </div>`
    })

    userList.innerHTML = userItems.join('')
}

addUserButton.addEventListener('click',() => {

    let name = nameTextBox.value 
    let age = parseInt(ageTextBox.value) 
    saveUser(name, age)
})

function saveUser(name, age) {
    usersRef.push({ // use push to create a random id for the node
    name: name, 
    age: age
})
}

/*
- Root 
    - Users 
         - User 
             - name 
             - age 
         - User 2
             - name 
             - age 
*/

// users node 
/*
let usersRef = database.ref('users')
usersRef.child("user2").set({
    name: 'Mary', 
    age: 23
}) */
```