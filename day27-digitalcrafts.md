# Day 27 - Digital Crafts Notes

`CREATE DATABASE databasename;`

Forgetting the semicolon at the end of the terminal command is the most common thing forgotten

Schema - The overall layout of the structure of the database.

There are set commands for databases - Select, Create Table, etc...

Primary Key - This is the unique information for that column
Varchar - Datatype that can hold 50 characters [In other languages this is referred to as strings]
trips - Plural, always use plural when you label the heading

You mostly will use backslashes. Capital letters are reserved for preset Methods.

```
CREATE TABLE trips (
    tripId SERIAL PRIMARY KEY,
    title VARCHAR(50),
    body TEXT
);
\connect databasename;
\dt
\SELECT * FROM trips;
\SELECT tripId, title, body, FROM trips;
```

When you use a star you will see all of the information. This is generally not a good idea for a larger sized database.

`SELECT` selects the information in the Table

`INSERT` puts more information into the Table

`INSERT INTO trips(title,body) VALUES('Houston','A trip to Houston');
The variables need to exactly match the headers on the table.
The values that you enter need to be in the specific spot that is listed as well.

Semicolons at the end tell the terminal that you want to execute the command.

`WHERE` you can use this to select a specific location in the database and it will return a set.
`SELECT title, body FROM trips WHERE title = 'Austin';`

GROUP BY, HAVING...

CRUD operations - CREATE READ UPDATE DELETE

Once you learn one database, 95% of the commands will be the same exact commands.

Whenever you are going to update something you always want to change the primary key!!!

`UPDATE trips SET title = 'Boston', body = 'A trip to Boston' WHERE tripsId = 3;`

`DELETE FROM trips WHERE tripsId = 2;`

Insert, Group, Where, Delete, Update, Create, Select, look up and know at least 10 backwards and forwards

There are nice applications that give you a good interface to work with on your databases. A nice GUI.

Postico is the one that we learned in class.

You have to declare the not null functions for the data that you're storing in your table, primary key for the primary key, and so on...

You can use expressions in the default values and place a current time stamp, or other similar things that you would like to place inside it.

Serial sequence column - the primary key value default values.

`INSERT INTO users(firstname, lastname) VALUES('John','Doe');`
`INSERT INTO users(firstname, lastname) VALUES('','');`

```js
var pgp = require('pg-promis')();
var connectionString = 'postgres://localhost:5432/tripsdb';
var db = pgp(connectionString);

console.log(db)

app.get('/', req,res) => {

    db.any('SELECT tripid, title, body FROM trips;')
        .then(trips => {
            res.render('index',{trips: trips})
        }).catch(error => {
            res.render('/', {message: 'Unable to get trips!'})
        })

    // let trips = await db.any('SELECT tripid, title, body FROM trips;')
    // res.render('index', {trips: trips})

    res.render('index')
}

```

```js
var pgp = require('pg-promis')();
var connectionString = 'postgres://localhost:5432/tripsdb';
var db = pgp(connectionString);

app.post('/add-trip', (req,res) => {
    console.log(req.body.title)
    console.log(req.body.description)
    res.send('add-trip') // if you don't have a response you will have this running forever!
})

app.get('/add-trip', (req,res) => {
    res.render('add-trip')
})
app.get('/', req,res) => {
    db.any('SELECT tripid, title, body FROM trips;')
        .then(trips => {
            res.render('index',{trips: trips})
        }).catch(error => {
            res.render('/', {message: 'Unable to get trips!'})
        })
    res.render('index')
}
```

```html
<form action="/add-trip" method="POST">
    <input type="text" name="title" />
    <input type="text" name="description" />
    <button>Save</button>
</form>
```

```js
var pgp = require('pg-promis')();
var connectionString = 'postgres://localhost:5432/tripsdb';
var db = pgp(connectionString);




app.post('/add-trip', (req,res) => {

    let title = req.body.title
    let body = req.body.description

    // this is going to insert the database and not return anything by declaring none
    db.none('INSERT INTO trips(title,body) VALUES($1, $2)', [title, body])
    .then(() => {
        res.redirect('/')
    }).catch(error => {
        res.render('/', {message: 'Unable to get trips!'})
    })
    // this also works, BUT it is easier to make a mistake that will mess up your database overall.
    // it will be harder to deal with the errors
    db.none(`INSERT INTO trips(title,body) VALUES('${title}', '${body}')`)
    .then(() => {
        res.redirect('/')
    }).catch(error => {
        res.render('/', {message: 'Unable to get trips!'})
    })



    res.send('add-trip')
})




app.get('/add-trip', (req,res) => {
    res.render('add-trip')
})
app.get('/', req,res) => {
    db.any('SELECT tripid, title, body FROM trips;')
        .then(trips => {
            res.render('index',{trips: trips})
        }).catch(error => {
            res.render('/', {message: 'Unable to get trips!'})
        })
    res.render('index')
}
```