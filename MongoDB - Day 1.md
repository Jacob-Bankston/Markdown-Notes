# [MongoDB](https://www.mongodb.com/) - Day 1

## Document Versus Relational

- No SQL
- Schema-less
- Document Database

The Table version would for each particular section of the database

- Customers
  - Customer ID
  - Name
  - Occupation
  - Address
- Books
  - Title
  - Image
  - Author
  - Publisher
  - Year

The Document version would have trees down

- Users

  - User
    - name
    - password
    - books
      - name
      - genre
      - ISBN
      - price

- Posts
  - Title
  - Comments Collections
    - Comment 1
    - Comment 2
    - Comment 3
- Comments

## Mongoose

[Mongoose](https://mongoosejs.com/) is not technically an ORM, it is more like a wrapper to make MongoDB easier to work with. It is more like pg-promise than sequelize.

- npm init
- npm install express
- `npm install mongodb`
- Set up express
  - require express
  - app = express
  - app listen 3000
- `var mongoose = require('mongoose');`
- `mongoose.connect('mongodb://localhost/blogdb', {useNewUrlParser: true}, (error) => { if(!error) { console.log( 'Successfully connected to MongoDB database!' )}})`

## Interacting with Mongo

- Make a new tab in the terminal
  - type `mongo`
  - Now you can use any commands to MongoDB that you are aware of

## Set your schema

- Make a new folder
  - schemas
- Make a new file in the schemas folder
  - post.js

```js
// post.js

const mongoose = require("mongoose");

const postSchema = new mongoose.Schema({
  title: String,
  body: String
});
```

This is very similar to sequelize, but you have to construct it on your own!

```js
// post.js

const mongoose = require("mongoose");

const postSchema = new mongoose.Schema({
  title: String,
  body: String
});

const Post = mongoose.model("Post", postSchema);
// whatever you put in the initial portion of the model it will create that collection in the database

module.exports = Post;
```

The actual collection in the database that will be created will be lower-cased and pluralized.

In the old days you had to use SQL Commands to be able to set any of these up, so these wrappers and ORMs are very helpful.

- Change to the App.js
- get all the posts!

```js
app.get('/posts', (req, res) => {
    Post.find({}, (error, posts) => {
        if(error) {
            res.json({error: 'Unable to fetch posts!'})
        } else {
            res.json(posts)
        }
    })
})
```

- Check in Postman

- Check in Mongo
  - mongo
  - show dbs
  - use booksDB
  - show collections
  - db.books.find()

## Mongo DB UI Package

[mongoui](https://www.npmjs.com/package/mongoui)

`npm i -g mongoui`
`mongoui`

- This will show you an interface that shows you all of your databases for mongodb
- You can interact with the documents in your database!

## Add a Post Request

```js
app.post('/posts', (req, res) => {
    const title = req.body.title
    const body = req.body.body

    // relate this to the schema that you set up!

    let post = new Post({
        title: title,
        body: body
    })
})
```

Finding a post by a title!
Finding a post by an ID!

## Deleting a Post

```js
app.delete('posts/:postID', (req, res) => {

    // get the postID from the route parameter
    const postID = req.params.postID

    Post.remove({
        _id: postID
    }, (error, result) => {
        if(error) {
            res.json({error: 'Unable to delete post'})
        } else {
            res.json(result)
        }
    })
})
```

Check the route on Postman!

## Updating a Post

```js

app.put('/posts', (req, res) => {

    const postID = req.body.postId
    const title = req.body.title
    const description = req.body.description

    // const updatedPost = { title, postId, body }

    const updatedPost = {
        title: title,
        postId: postId,
        body: body
    }

    Post.findByIdAndUpdate(postId, updatedPost, (error, result) => {
        if(error) {
            res.json({error: 'Unable to update'})
        } else {
            res.json({updated: true})
        }
    })

})
```

put is when you want to update the whole document

patch is when you want to update portions of it

