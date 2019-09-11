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
```js
// this code is not complete, just an idea!
bcrypt.hash(password, 10).then(function(hash) {

    db.none('INSERT INTO users(username, password) VALUES($1, $2);', [username, password])
        .then(() => {
            console.log('Success')
            res.send('Take user to login page')
        })
})
```
Once you have set up the bcrypt salt with the password and have checked for the user to exist, add the user to `sessions`
It's your responsibility that you never store sensitive information in clear text.
It's never a good idea to take whatever is in a text box and inject it into your database. People can take those strings and add a method to attack the server. The biggest attack to databases these days is people not encrypting their passwords.
Add a foreign key! You want to set up the foreign key when you set up the table because you will have all of this data set when you start adding information.
The foreign key needs to be something where you can reference a column from each table. This column will join these two tables together.
Then you have to actually join these two tables together!
`SELECT users.userid, users.username AS u FROM users JOIN trips AS t ON t.userid = u.userid`
Table names best practices! Postgres = snake_case, MSSQL = Firstlettercapital, if you use a capital in the middle you have to include quotes around it.
Don't type long aliases, otherwise you are removing the point of using an alias in the first place. `users.username AS u FROM users...`
Join Methods! Inner/Outer/Left/Right/etc...
Add in database layers when you pull it through the server side by layering things in trees via your classes. Created a JSON file that has the data formatted the way that you want it to be structured, then set up your code to create and structure the information in that way.
Planning is key!
Nesting everything is not necessary but it will help you with your structure, and it will help the users and UI people to use the information.
We will learn some ways to have a service work this out for us.
Next step is posting the database somewhere where others can use and access it. Elephant SQL is like Surge but for Databases. Tiny Turtle is the free version of this service.
Create a new instance.
* Fill out the intro information
* You can select your databases through the browser
* Recommended to go through Postico and hte browser
You can use the connectionString connection with the URL from elephant to run it through their instead of your local machine.
There are a lot of different Object Relational Mappers in different frameworks in different roles to look into.