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
- `npm install mongoose`
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
app.get("/posts", (req, res) => {
  Post.find({}, (error, posts) => {
    if (error) {
      res.json({ error: "Unable to fetch posts!" });
    } else {
      res.json(posts);
    }
  });
});
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
app.post("/posts", (req, res) => {
  const title = req.body.title;
  const body = req.body.body;

  // relate this to the schema that you set up!

  let post = new Post({
    title: title,
    body: body
  });
});
```

Finding a post by a title!
Finding a post by an ID!

## Deleting a Post

```js
app.delete("posts/:postID", (req, res) => {
  // get the postID from the route parameter
  const postID = req.params.postID;

  Post.remove(
    {
      _id: postID
    },
    (error, result) => {
      if (error) {
        res.json({ error: "Unable to delete post" });
      } else {
        res.json(result);
      }
    }
  );
});
```

Check the route on Postman!

## Updating a Post

```js
app.put("/posts", (req, res) => {
  const postID = req.body.postId;
  const title = req.body.title;
  const description = req.body.description;

  // const updatedPost = { title, postId, body }

  const updatedPost = {
    title: title,
    postId: postId,
    body: body
  };

  Post.findByIdAndUpdate(postId, updatedPost, (error, result) => {
    if (error) {
      res.json({ error: "Unable to update" });
    } else {
      res.json({ updated: true });
    }
  });
});
```

put is when you want to update the whole document

patch is when you want to update portions of it

## Adding a Comment Schema

```js
// schemas/comment.js

const mongoose = require("mongoos");

const Schema = mongoose.Schema;
const ObjectId = Schema.ObjectId;

const commentSchema = new mongoose.Schema({
  postId: ObjectId,
  title: String,
  body: String
});

// mongoose will create a comments collection in the database
const Comment = mongoose.model("Comment", commentSchema);

module.exports = Comment;
```

Update the Post Schema with comments!

```js
const postSchema = new mongoose.Schema({
  title: String,
  body: String,
  comments: [Comment.schema]
});
```

You can directly inject a schema into another schema!

- When adding a comment inside of the schema you need to embed it in the post request
- app.post comments
- add the normal posting things
- Then find the post by Id
- Once found inject the comment into the comments section of the post schema

When you are pulling from parameters, 99% of the time it is a get request
If you are using a post request, then you should be getting the information from the body

## Azam's Notes

```js
// app.js
const express = require("express");
const app = express();
var mongoose = require("mongoose");
const Post = require("./schemas/post");
const Comment = require("./schemas/comment");

app.use(express.json());

// connecting to the MongoDB database
mongoose.connect(
  "mongodb://localhost/blogdb",
  { useNewUrlParser: true },
  error => {
    if (!error) {
      console.log("Successfully connected to MongoDB database!");
    }
  }
);

// ADDING A COMMENT INSIDE OF THE POST SCHEMA

app.post("/comments", (req, res) => {
  const postId = req.body.postId;
  const title = req.body.title;
  const body = req.body.body;

  const comment = new Comment({
    title: title,
    body: body
  });

  Post.findById(postId, (error, post) => {
    post.comments.push(comment);
    post.save(error => {
      if (!error) {
        res.json({ success: true });
      } else {
        res.json({ error });
      }
    });
  });
});

// UPDATING A POST

app.put("/posts", (req, res) => {

  // note that the postId is listed as _id in MongoDB

  const postId = req.body.postId;
  const title = req.body.title;
  const body = req.body.body;

  //const updatedPost = { title, postId, body }

  const updatedPost = {
    title: title,
    postId: postId,
    body: body
  };

  Post.findByIdAndUpdate(postId, updatedPost, (error, result) => {
    if (error) {
      res.json({ error: "Unable to updated" });
    } else {
      res.json({ updated: true });
    }
  });
});

// DELETING A POST

app.delete("/posts/:postId", (req, res) => {
  // get the postId from the route parameter
  const postId = req.params.postId;

  Post.remove(
    {
      _id: postId
    },
    (error, result) => {
      if (error) {
        res.json({ error: "Unable to delete post" });
      } else {
        res.json(result);
      }
    }
  );
});

// FINDING A POST BY AN ID

//  /posts/5d8246dcd94aa228362d1e33
app.get("/posts/:postId", (req, res) => {
  // get the postId from the route parameter
  const postId = req.params.postId;

  Post.findById(postId, (error, post) => {
    if (error) {
      res.json({ error: "Unable to get post" });
    } else {
      res.json(post);
    }
  });

  // finding the post by title
  /*
    Post.findOne({
        title: 'Hello Python'
    }, (error, post) => {
        res.json(post)
    }) */
});

// ADDING A POST

app.post("/posts", (req, res) => {
  const title = req.body.title;
  const body = req.body.description;

  let post = new Post({
    title: title,
    body: body
  });

  post.save(error => {
    if (error) {
      res.json({ error: "Unable to save" });
    } else {
      res.json({ success: true, message: "Saved new post!" });
    }
  });
});

// VIEW ALL POSTS!error

// get all posts
app.get("/posts", (req, res) => {
  Post.find({}, (error, posts) => {
    if (error) {
      res.json({ error: "Unable to fetch posts!" });
    } else {
      res.json(posts);
    }
  });
});

app.listen(3000, () => {
  console.log("Server is running...");
});
```

### schemas Folder

```js
// comment.js

const mongoose = require("mongoose");
//const Schema = mongoose.Schema
//const ObjectId = Schema.ObjectId

const commentSchema = new mongoose.Schema({
  title: String,
  body: String
});

// mongoose will create a posts collection in the database
const Comment = mongoose.model("Comment", commentSchema);

module.exports = Comment;
```

```js
// post.js

const mongoose = require("mongoose");
const Comment = require("./comment");

const postSchema = new mongoose.Schema({
  title: String,
  body: String,
  comments: [Comment.schema]
});

// mongoose will create a posts collection in the database
const Post = mongoose.model("Post", postSchema);

module.exports = Post;
```
