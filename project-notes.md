# Notes for our project

It is invaluable to read through the documentation on Firebase to understand how the structures are working. This helps so much to understand what's going on under the hood instead of trying to find a video of someone dulling it down for you!

##Sorting Data and Filtering Data

We're going to have to go through our messages and this is a way for us to limit the number that we pull from the data set. (Think 10,000 posts in the database, we only want to show the last 100 or so...)

```js
// Sorting the list from the specified path
.orderByChlid()
.orderByKey()
.orderByValue()
// Filtering the sorted list
.limitToFirst()
.limitToLast()
.startAt()
.endAt()
.equalTo()
```

## Notes from Firebase Documentation - Realtime Database - Web Section
```js
    // Set the configuration for your app
    // TODO: Replace with your project's config object
    var config = {
        apiKey: "apiKey",
        authDomain: "projectId.firebaseapp.com",
        databaseURL: "https://grocery-list-application.firebaseio.com/",
        storageBucket: "bucket.appspot.com"
    };
    firebase.initializeApp(config);

    // Get a reference to the database service
    var database = firebase.database();

    // Creating/Resetting a node
    // To create new data while deleting all old data at that point use .set()

    function writeUserData(userId, name, email, imageUrl) {
        firebase.database().ref('users/' + userId).set({
            username: name,
            email: email,
            profile_picture : imageUrl
        });
    }

    // Retrieving data continuously
    // Retrieving star count from a post using .on() method for
    // firebase.database().ref and using the value event to take a snapshot
    // of the current data path. You can retrieve the data using the .val() method
    var starCountRef = firebase.database().ref('posts/' + postId + '/starCount');
    starCountRef.on('value', function(snapshot) {
        updateStarCount(postElement, snapshot.val());
    });

    // Retrieving data one time only
    // Retrieving User name for a post with the .once() method
    // instead of the .on() method. This is used for one time pulls.
    var userId = firebase.auth().currentUser.uid;
    return firebase.database().ref('/users/' + userId).once('value').then(function(snapshot) {
        var username = (snapshot.val() && snapshot.val().username) || 'Anonymous';
    // ...
    });

    // Using .update() to update information on children in the database
    // ** Note that the .key method creates a new key for that post.
    // For example, a social blogging app might create a post and simultaneously update it to the recent activity feed and the posting user's activity feed using code like this:
    function writeNewPost(uid, username, picture, title, body) {
        // A post entry.
        var postData = {
          author: username,
          uid: uid,
          body: body,
          title: title,
          starCount: 0,
          authorPic: picture
        };
      
        // Get a key for a new Post.
        var newPostKey = firebase.database().ref().child('posts').push().key;
      
        // Write the new post's data simultaneously in the posts list and the user's post list.
        var updates = {};
        updates['/posts/' + newPostKey] = postData;
        updates['/user-posts/' + uid + '/' + newPostKey] = postData;
      
        return firebase.database().ref().update(updates);
    }

    // Catching an error
    // Add a callback function after the .set() or .update() method to catch what happened.
    firebase.database().ref('users/' + userId).set( {
        username: name,
        email: email,
        profile_picture : imageUrl
        }, function(error) {
            if (error) {
            // There was an error...
            } else {
            // Data saved successfully!
        }
        });
    }

    // Deleting data
    // Use the .remove() method at the location of that data

    // Receiving a Promise
    // Both .set() and .update() return a Promise when the write is committed to the database.

    // Preventing User Input errors
    // Using a 'transaction' method you can check to see if when you're posting the data it has not been changed before you tried to submit to the database by pulling the data and comparing it. If it has changed, it updates the data to the user and tries the function again until it is successful.
    function toggleStar(postRef, uid) {
        postRef.transaction(function(post) {
        if (post) {
            if (post.stars && post.stars[uid]) {
                post.starCount--;
                post.stars[uid] = null;
            } else {
                post.starCount++;
                if (!post.stars) {
                    post.stars = {};
                }
                post.stars[uid] = true;
            }
        }
        return post;
        });
    }

    // Appending Data
    // Using the .push() method you can append data that will generate a unique key every time a new child is added to the Firebase reference. The key is based on a timestamp, so items are automatically ordered chronologically. The reference to the .push() method to get the value of the key or set data for the child.
    // Adding a post to a list of posts in a social application.
    // Create a new post reference with an auto-generated id
    var newPostRef = postListRef.push();
    newPostRef.set({
        // ...
    });

    // Listening to the child nodes
    // child_added
    // child_changed
    // child_removed
    // child_moved
    // These are all pretty self explanatory and listen for what they seem they are listening for.
    // Example for a post on a social media site that listens and responds to an addition, change or removal
    var commentsRef = firebase.database().ref('post-comments/' + postId);

    commentsRef.on('child_added', function(data) {
        addCommentElement(postElement, data.key, data.val().text, data.val().author);
    });

    commentsRef.on('child_changed', function(data) {
        setCommentValues(postElement, data.key, data.val().text, data.val().author);
    });

    commentsRef.on('child_removed', function(data) {
        deleteComment(postElement, data.key);
    });

    // Listening to Entire Lists
    // Listening to the child nodes is recommended, but if you need to listen and loop over everything here is how.
    ref.once('value', function(snapshot) {
        snapshot.forEach(function(childSnapshot) {
            var childKey = childSnapshot.key;
            var childData = childSnapshot.val();
            // ...
        });
    });

    // Sorting Data
    // You can only use one order method at a time!
    // orderByChild() - order by value of child key or child path
    // orderByKey() - order by child keys
    // orderByValue() - order by child values

    // pulling a top post by user example
    var myUserId = firebase.auth().currentUser.uid;
    var topUserPostsRef = firebase.database().ref('user-posts/' + myUserId).orderByChild('starCount');

    // Another example pulling the view count of posts in a data set that looks like this...
    "posts": {
        "ts-functions": {
            "metrics": {
                "views" : 1200000,
                "likes" : 251000,
                "shares": 1200,
            },
            "title" : "Why you should use TypeScript for writing Cloud Functions",
            "author": "Doug",
        },
        "android-arch-3": {
            "metrics": {
                "views" : 900000,
                "likes" : 117000,
                "shares": 144,
            },
            "title" : "Using Android Architecture Components with Firebase Realtime Database (Part 3)",
            "author": "Doug",
        }
    },

    // you can take the "posts" list and then ignore the direct child, and sort through their children like so!
    var mostViewedPosts = firebase.database().ref('posts').orderByChild('metrics/views');

    // Filtering the data
    // You can add a filter to any of the order methods when you form the query
    // You can add more than one filter to any sorted list! Like a limit on where to start and end a list!
    // limitToFirst() - sets the max number of items returned from the beginning of the ordered list
    // limitToLast() - sets the max number of items to return from the end of the ordered list
    // startAt() - returns the items greater than or equal to the specified key or value depending on the sort
    // endAt() - returns the items lesser than or equal to the specified key or value depending on the sort
    // equalTo() - returns the items equal to the specified key or value depending on the sort

    // example - getting a 100 of the most recent posts
    var recentPostsRef = firebase.database().ref('posts').limitToLast(100);

    // Detaching listeners
    // by calling the off() method on your Firebase database reference you will turn off all listeners.
    // if you want to turn off a specific listener add the single listener as a parameter to off().
    firebase.database().ref('posts').off()
```

## Notes from Firecast Auth Basic Login and Signup Video

```js
// Get elements
const txtEmail = document.getElementById('txtEmail');
const txtPassword = document.getElementById('txtPassword');
const btnLogin = document.getElementById('btnLogin');
const btnSignUp = document.getElementById('btnSignUp');
const btnLogout = document.getElementById('btnLogout');

// Add login event
btnLogin.addEventListener('click', e => {
    // Get email and pass
    const email = txtEmail.value;
    const pass = txtPassword.value;
    const auth = firebase.auth();
    // Sign in
    const promise = auth.signInWithEmailAndPassword(email, pass);
    promise.catch(e => console.log(e.message));
})

// Add signup event
btnSignUp.addEventListener('click', e => {
    // Get email and pass
    // TODO: CHECK FOR A REAL EMAIL
    const email = txtEmail.value;
    const pass = txtPassword.value;
    const auth = firebase.auth();
    // Sign in
    const promise = auth.createUserWithEmailAndPassword(email, pass);
    promise.catch(e => console.log(e.message));
})

btnLogout.addEventListener('click', e => {
    firebase.auth().signOut();
});

// Add a realtime listener
firebase.auth().onAuthStateChanged(firebaseUser => {
    if(firebaseUser) {
        console.log(firebaseUser);
        btnLogout.classList.remove('hide');
    } else {
        console.log('not logged in');
        btnLogout.classList.add('hide');
    }
});

// auth.signInWithEmailAndPassword(email, pass); // Returns and existing user and returns a promise to resolve that user

// auth.creatUserWithEmailAndPassword(email, pass); // Creates the user and signs them in

// auth.onAuthStateChanged(firebaseUser => { // This parameter will be populated with a the current user's information - no user equal 'null'

// });
```