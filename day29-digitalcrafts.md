#Digital Crafts Notes - Day 29

##ORM - Object Relational Mapper

You can hard code the database information, but if you don't want to, you can use an ORM to help you with the process. There are a lot of these out there for all frameworks and languages.
You will always work with your classes with the ORM!
* Trip
  * Name
  * Description
The name of the class will become the name of the table and the attributes of the class will become the names of the columns.

##Sequelize - NPM

Sequelize has it's own data types that will eventually get to the data types of the database.
`sudo npm install -g sequelize-cli`
`npm init`
`npm install express`
`npm install sequelize pg --save`
At this point you don't really need pg promise anymore because you're going to use the ORM instead.
`sequelize init`
```js
{
    "development": {
        "username": "postgres", // create a username that is unique don't just use postgres
        "password": null,
        "database": "tripsdb",
        "host": "127.0.0.1"
        "dialect": "postgres"
    }
}
```
Don't mess with the Sequelize Table in your Postico because that's Sequelize table that works behind the scenes!
`sequelize model:create --name Trip --attributes 'name:string description:string'`

##Migrations

Migrations are modifying the structure of the database.
If you leave something off, you can edit the javascript first then you can migrate it into the database. This will change the schema of the table from the migration. You will throw off sequelize if you try to edit the table directly in the sequelize table.
The name of the migration should always be unique!

###up Method

This is the method that runs the migration.

###down Method

This is the undo function for the migration. Whatever you do in the up function, you do the reverse in the down function.
It's not required, but it is recommended.

`sequelize db:migrate`
This will run all of the migrations that have not run.
The sequelize table will keep track of what migrations have taken place.

## Adding a Trip

```js
app.post('add-trip', (req,res) => {
    let name = req.body.name
    let description = req.body.description

    // This is a sequelize class object, it has a lot more functions.
    let trip = models.Trip.build({ // Build is a method on a Sequelize Class.
        name: name,
        description: description
    })

    // save is a promise, so you need to use .then() to get the information from it.
    trip.save().then(savedTrip => res.json(savedTrip))
        .catch(error => console.log(error))
    // you can use async await and add a catch for the errors for this.

    console.log(trip)

    res.send('Trip...')
})
```

Remember to use Postman to test the functionality of the database and server routes!

## Finding One Trip

```js
app.get('/trips', (req,res) => {
    // findAll() is a method for the Sequelize model class, and it is a promise
    models.Trip.findAll().then(trips => res.json(trips))

    // How to add a filter to it!
    models.Trip.findAll({
        where: { // Using the Sequelize functions you can filter out your list of models
            id: 1,
            name: 'SF'
        }
    }).then(trips => res.json(trips))
})
```

The findAll function is a static function, and you can define that with `static findAll() {}` instead of `function findAll() {}`

static functions - these functions are common for objects, they do not change the state.
instance functions - these functions will change the state of the object.

## Updating a Trip

```js
app.post('/update-trip', (req,res) => {

    // whenever you are updating or deleting a post, just use everything. It will make it all a lot easier on you in the end.
    let name = req.body.name
    let description = req.body.description
    let tripId = parseInt(req.body.tripId)

    models.Trip.update({
        name: name,
        description: description,
    },{
        where: {
            id: tripId
        }
    }).then(updatedTrip => res.json(updatedTrip))

})
```

You can also use findOne, findNone, and dozens of other operations to work with the same thing.

Patch and Delete methods are used more with web APIs

__Post and Get are the only things you can use with server side pages__

## Migrating a Trip

The name of the migration should be very descriptive of what you're trying to do with the migration.

`sequelize migration:create --name 'adding-username-to-trips'

```js
'use strict';

module.exports = {
    up: (queryInterface, Sequelize) => {
        // add username to Trips table
        return queryInterface.addColumn(
            'Trips', // name of the table
            'username', { // name of the column
                type: Sequelize.STRING // type of the column
            }
        )

    }, 

    down: (queryInterface, Sequelize) => {
        // remove the username from the Trips table
            return queryInterface.removeColumn(
            'Trips', // name of the table
            'username'
        )
    }
}
```
`sequelize db:migrate`
Keep in mind that this runs all of the migrations that are not run yet.
If you are trying to undo a migration it will undo all of the migrations until it gets to the migration you were trying to do.
It will not update your Model file in your .js file. You have to go into the file and update it yourself.
> Tip: It's better to think ahead about what information you want in your program
To undo the recent migration you would run `sequelize db:migrate:undo` and it will run the down function.
