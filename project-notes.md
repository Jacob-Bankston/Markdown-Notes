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

## Three New Ways to Secure Your App with Firebase Authentication


## Firebase Security Rules

Cloud Firestore and Cloud Storage - Common Expression Language Structure - relies on `match` and `allow` statements
```
service <<name>> {
  // Match the resource path.
  match <<path>> {
    // Allow the request if the following conditions are true.
    allow <<methods>> : if <<condition>>
  }
}
```

Realtime Database - JavaScript like syntax - JSON Structure
```
{
  "rules": {
    "<<path>>": {
    // Allow the request if the condition for each method is true.
      ".read": <<condition>>,
      ".write": <<condition>>
      ".validate": <<condition>>
    }
  }
}
```

Rules are applied as `OR` statements, not `AND` statements.

Implementation Path

1. Integrate the product SDKs
2. Write your Firebase Security Rules
3. Test your Firebase Security Rules - Use the emulators to test the app's behavior and validate them before deploying them
4. Deploy your Firebase Security Rules - Use the firebase console to deploy the rules to production

Warning: If you give access to a higher path level keep in mind that you can not block a subpath later. Structure your rules well!

Realtime Database

There are three basic elements in the rule:
* Path: The database location
* Request: read/write grant broad access while validate acts as a secondary verification based on incoming or existing data.
* Condition: The condition that permist a request if it evaluates to true.

```js
// If your structure in your database looks like this...
  {
    "messages": {
      "message0": {
        "content": "Hello",
        "timestamp": 1405704370369
      },
      "message1": {
        "content": "Goodbye",
        "timestamp": 1405704395231
      },
      ...
    }
  }
```

```js
// Your rules should look like this!
  {
    "rules": {
      "messages": {
        "$message": {
          // only messages from the last ten minutes can be read
          ".read": "data.child('timestamp').val() > (now - 600000)",

          // new messages must have a string content and a number timestamp
          ".validate": "newData.hasChildren(['content', 'timestamp']) &&
                        newData.child('content').isString() &&
                        newData.child('timestamp').isNumber()"
        }
      }
    }
  }
```

*As the example above shows, Realtime Database Rules support a $location variable to match path segments. Use the $ prefix in front of your path segment to match your rule to any child nodes along the path.*

```js
// Another example
  {
    "rules": {
      "rooms": {
        // This rule applies to any child of /rooms/, the key for each room id
        // is stored inside $room_id variable for reference
        "$room_id": {
          "topic": {
            // The room's topic can be changed if the room id has "public" in it
            ".write": "$room_id.contains('public')"
          }
        }
      }
    }
  }
```

You're changing the rules. The above example let's you change the rules on every `'public'` labeled room. As long as the room_id contains `'public'` you can change the topic. I get it.

You can also use the `$variable` in parallel with constant path names.

```js
  {
    "rules": {
      "widget": {
        // a widget can have a title or color attribute
        "title": { ".validate": true },
        "color": { ".validate": true },

        // but no other child paths are allowed
        // in this case, $other means any key excluding "title" and "color"
        "$other": { ".validate": false }
      }
    }
  }
```

## Rule Types

1. .read - describes if and when data is allowed to be read by users.
2. .write - describes if and when data is allowed to be written.
3. .validate - defines what a correctly formatted value will look like, whether it has child attributes, and the data type.
4. By default, if there isn't a rule allowing it, access at a path is denied.

## Building Conditions

#### Pre-defined Variables

* `now` - current time in milliseconds - works well with `firebase.database.ServerValue.TIMESTAMP`
* `root` - a `RuleDataSnapshot` of the root path in the database as it exists before the attempted operation.
* `newData` - a `RuleDataSnapshot` of the data as if it exists after the attempted operation. It includes the new data being written and the existing data.
* `data` - a `RuleDataSnapshot` of the data as it existed before the attempted operation.
* $ variables - a wildcard path used to represent ids and dynamic child keys.
* `auth` - represents an authenticated user's token payload.

These variables can be used anywhere in your rules.

```js
// Example - data written to the /foo/ node must be a string of less than 100 characters
{
  "rules": {
    "foo": {
      // /foo is readable by the world
      ".read": true,

      // /foo is writable by the world
      ".write": true,

      // data written to /foo must be a string less than 100 characters
      ".validate": "newData.isString() && newData.val().length < 100"
    }
  }
}
```

Data Based Rules - Any data that exists in your database can be in your rules!!

Consider this example, which allows write operations as long as the value of the /allow_writes/ node is true, the parent node does not have a readOnly flag set, and there is a child named foo in the newly written data

```js
".write": "root.child('allow_writes').val() === true &&
          !data.parent().child('readOnly').exists() &&
          newData.child('foo').exists()"
```

Query Based Rules - Use `query.` expressions in your rules to grand read or write access based off of the query parameters.

```js
"baskets": {
  ".read": "auth.uid != null &&
            query.orderByChild == 'owner' &&
            query.equalTo == auth.uid" // restrict basket access to owner of basket
}
```

Based off of the rule above this query would succeed because it has all of the parameters required.

```js
db.ref("baskets").orderByChild("owner")
                 .equalTo(auth.currentUser.uid)
                 .on("value", cb)                 // Would succeed
```

Based off of the rule above this query would fail with a `PermissionDenied` error.

```js
db.ref("baskets").on("value", cb)                 // Would fail with PermissionDenied
```

You can also limit how much a user is allowed to see with the `query` operation.

```js
// this limiits the read access to only the first 1000 results of a query as ordered by priority
messages: {
  ".read": "query.orderByKey &&
            query.limitToFirst <= 1000"
}

// Example queries:

db.ref("messages").on("value", cb)                // Would fail with PermissionDenied

db.ref("messages").limitToFirst(1000)
                  .on("value", cb)                // Would succeed (default order by key)
```

## Query Based Rule Expressions

* query.orderByKey - Boolean - True for queries ordered by key. False otherwise.
* query.orderByPriority - Boolean - True for queries ordered by priority. False otherwise.
* query.orderByValue - Boolean - True for queries ordered by value. False otherwise.

* query.orderByChild - string/null - use a string to represent the path to a child node. EX: `query.orderByChild == "address/zip"` If the query isn't ordered by a child node, this value is null.

* query.startAt -  string/number/boolean/null - Retrieves the bounds of the executing query, or returns null if there is no bound set.
* query.endAt -  string/number/boolean/null - Retrieves the bounds of the executing query, or returns null if there is no bound set.
* query.equalTo - string/number/boolean/null - Retrieves the bounds of the executing query, or returns null if there is no bound set.

* query.limitToFirst -  number/null - Retrieves the limit on the executing query, or returns null if there is no limit set.
* query.limitToLast - number/null - Retrieves the limit on the executing query, or returns null if there is no limit set.

## How Security Rules Work

The following may not seem immediately intuitive, but it is a powerful assistant in the setting up of rules.

```js
// This security structure allows /bar/ to be read whenever /foo/ contains a child 'baz' with value 'true'

{
  "rules": {
     "foo": {
        // allows read to /foo/*
        ".read": "data.child('baz').val() === true",
        "bar": {
          // ignored, since read was allowed already
          ".read": false
        }
     }
  }
}
```

The `".read": false"` rule under `/foo/bar/` has no effect here, since access cannot be revoked by a child path.

__This is a method in which you could give an administrator access to read data, but not a user__

`.validate` rules do not cascade like this. They have to work at all levels to function properly.

WARNING: You have to give explicit permission to a path otherwise the priveleges will be denied by default. Check out this example!

```js
// Rules
{
  "rules": {
    "records": {
      "rec1": {
        ".read": true
      },
      "rec2": {
        ".read": false
      }
    }
  }
}

// the parent records was not defined explicitly as having read access, therefore calling it results in an error.
var db = firebase.database();
db.ref("records").once("value", function(snap) {
  // success method is not called
}, function(err) {
  // error callback triggered with PERMISSION_DENIED
});

// in order to actually get the value we want we'd have to access it directly
var db = firebase.database();
db.ref("records/rec1").once("value", function(snap) {
  // SUCCESS!
}, function(err) {
  // error callback is not called
});
```












## Database Security Regex

Require a string to be a date formatted as YYYY-MM-DD between 1900-2099:
`".validate": "newData.isString() && newData.val().matches(/^(19|20)[0-9][0-9][-\\/. ](0[1-9]|1[012])[-\\/. ](0[1-9]|[12][0-9]|3[01])$/)"`

Require string to be an email address:
`".validate": "newData.isString() && newData.val().matches(/^[A-Z0-9._%+-]+@[A-Z0-9.-]+\\.[A-Z]{2,4}$/i)"`

Require string to be a basic URL:
`".validate": "newData.isString() && newData.val().matches(/^(ht|f)tp(s?):\\/\\/[0-9a-zA-Z]([-.\\w]*[0-9a-zA-Z])*((0-9)*)*(\\/?)([a-zA-Z0-9\\-\\.\\?\\,\\'\\/\\\\+&=%\\$#_]*)?$/)"`

