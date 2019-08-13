#Digital Crafts Notes - Day 28

## Encryption versus Encoding

An encrypted password doesn't have a way to reverse the encryption and can't be broken. 

The encoding can be run through an algorithm and be solved.

**Look up code snippets**

```js

app.use(express.urlencoded())

app.post('/register') => {
    let username = req.body.username
    let password = req.body.password

    db.none('INSERT INTO users(username, password) VALUES($1, $2);', [username, password])
        .then(() => {
            console.log('Success')
            res.send('Take user to login page')
        })

    // INSERT INTO users(username, password) VALUES ('johndoe', 'password');

    // Make sure you add a response!!

}

```

[INSERT with result!!]()

It's a good idea to always use Postman first to check if your server is working! Then you can check your front end portion. This is what I should have done yesterday when I didn't know what to look for!

In postman you want to send the request with form encoded values!

You have to check to make sure that everything is actually encrypted!! Double check that you're not saving the passwords by themselves, you need to encrypt all of the sensitive data.

This is where you go into the bcrypt library!
* Salt rounds - how much salt (additional rounds will make the encryption harder to crack) do you want to add?
* It will return a callback function of an error or a hash!
* It can also return a version with promises as well!
* Don't use the synchronous things when you can use asynchronous methods instead!

```js
bcrypt.hash(password, 10).then(function(hash) {
    // the more salt rounds you do, the more time it will take the user to load up the information
    console.log(hash)
})
```

