# [MongoDB](https://www.mongodb.com/) - Day 2

## Review

- `mongod` starts the database
- `mongoui` starts the user interface in the browser
- Compass is the tool that MongoDB provides to have a similar user interface

- MongoDB Commands in Terminal

  - show dbs
  - use blogdb
  - db.posts.find()

- Check for server routes in Postman

- What to Run

  - MongoDB
  - Node Server
  - React Client Server
  - Mongo UI

- Reminders
  - Include Cors in the server!
  - Use express json!

## Promises

```js
app.get('/posts', (req, res) => {

    Post.find({}).then((posts)) => {
        res.json(posts)
        }.catch(error => {
            res.json({error: "Unable to get all posts!"})
        })
})
```

```js
app.get("/posts", async (req, res) => {
  try {
    const posts = await Post.find({});
    res.json(posts);
  } catch (error) {
    res.json({ error: "could find posts!" });
  }
});
```

## How to Create Multiple Documents

Posts - Collection

- Post
  - title
  - body
  - comments - Sub documents
    - comment 1
    - comment 2
    - comment 3

A more optimized method would be to split the Posts and Comments from each other

Posts - Collection

- Post
  - title
  - body
  - comments

Comments - Collection

- Comment
  - User
  - Body
  - PostID

```js
// comment.js
const mongoose = require('mongoose')
const Schema = mongoose.Schema
const ObjectId = Schema.ObjectId

const commentSchema = new mongoose.Schema({
    postId: ObjectId,
    title: String,
    body: String
})

const Comment = mongoose.model('Comment', commentSchema)

module.exports Comment
```

### Creating a New Comment

```js
app.post("/comments", async (req, res) => {
  // Pull the post id from the post on the client side to create a relationship between them!

  const postId = req.body.postId;
  const commentTitle = req.body.title;
  const commentBody = req.body.body;

  const comment = new Comment({
    postId: postId,
    title: commentTitle,
    body: commentBody
  });

  // Saving the comment to the database!!

  try {
    await comment.save();
    res.json({ success: true });
  } catch (error) {
    res.json({ error: "Unable to add comment!" });
  }
});
```

### Getting the Post with Comments!

```js
app.get("/posts/:postId", async (req, res) => {
  const postId = req.params.postId;
  const post = await Post.findById(postId);
  const comments = await Comment.find({
    postId: postId
  });

  // "Well this is JavaScript, you can just create objects on the fly!"

  res.json({ post: post, comments: comments });
});
```

### Benefits of the API

The great thing about the API that you create with the Server is if you change the Database in the background, the user will not experience any changes on the client side.

## Client Side React

```js
function App() {
  // set up the states for the posts and comments

  const [post, setPost] = useState({ post: {}, comments: [] });
  const [comments, setComments] = useState([]);

  useEffect(() => {
    fetchPost();
  }, []);

  // The second parameter of the useEffect is saying that you should refresh
  // when the array is changed. If the array had post in it, it would fire whenever
  // post was updated.

  const fetchPost = () => {
    const url = "http://localhost:3000/posts/";
    fetch(url)
      .then(response => response.json())
      .then(json => {
        setPost(json.post);
        setComments(json.comments);
      });
  };

  // check the loading slowly
  // first check the post.title
  // second set up the post.body
  // third check if the comments load
  // fourth set up the map for the comment.title
  // fifth set up the containers for title and body

  return (
    <div>
      <h1>{post.title}</h1>
      <p>{post.body}</p>

      <b>Comments</b>
      {comments.map(comment => {
        return (
          <div>
            <h3>{comment.title}</h3>
            <p>{comment.body}</p>
          </div>
        );
      })}
    </div>
  );
}
```

## Data Validation

**Before we get into the specifics of validation syntax, please keep the following rules in mind:**

- Validation is defined in the SchemaType
- Validation is middleware. Mongoose registers validation as a pre('save') hook on every schema by default.
- You can manually run validation using doc.validate(callback) or doc.validateSync()
- Validators are not run on undefined values. The only exception is the required validator.
- Validation is asynchronously recursive; when you call Model#save, sub-document validation is executed as well. If an error occurs, your Model#save callback receives it
- Validation is customizable

#### [Using Mongoose to Validate](https://mongoosejs.com/docs/validation.html)

Inside of the Schema you will add the required attribute so the person can not add a post/comment without including that information

```js
title: {
    type: String,
    required: [true, 'Please provide the title of the comment!'] // add a message to the validation error
}
```

```js
console.log(error.message["title"]);
```

### Using 'unique'

Technically unique is not a validator, it's just a tool to add in to make each of that type of thing unique.

```js
var uniqueUsernameSchema = new Schema({
  username: {
    type: String,
    unique: true
  }
});
var U1 = db.model("U1", uniqueUsernameSchema);
var U2 = db.model("U2", uniqueUsernameSchema);

var dup = [{ username: "Val" }, { username: "Val" }];
U1.create(dup, function(error) {
  // Race condition! This may save successfully, depending on whether
  // MongoDB built the index before writing the 2 docs.
});

// Need to wait for the index to finish building before saving,
// otherwise unique constraints may be violated.
U2.once("index", function(error) {
  assert.ifError(error);
  U2.create(dup, function(error) {
    // Will error, but will *not* be a mongoose validation error, it will be
    // a duplicate key error.
    assert.ok(error);
    assert.ok(!error.errors);
    assert.ok(error.message.indexOf("duplicate key error") !== -1);
  });
});

// There's also a promise-based equivalent to the event emitter API.
// The `init()` function is idempotent and returns a promise that
// will resolve once indexes are done building;
U2.init().then(function() {
  U2.create(dup, function(error) {
    // Will error, but will *not* be a mongoose validation error, it will be
    // a duplicate key error.
    assert.ok(error);
    assert.ok(!error.errors);
    assert.ok(error.message.indexOf("duplicate key error") !== -1);
  });
});
```

### Built-in Validators

Mongoose has several built-in validators.

- All SchemaTypes have the built-in required validator. The required validator uses the SchemaType's `checkRequired()` function to determine if the value satisfies the required validator.
  Numbers have `min` and `max` validators.
- Strings have `enum`, `match`, `minlength`, and `maxlength` validators.
- Each of the validator links above provide more information about how to enable them and customize their error messages.

```js
var breakfastSchema = new Schema({
  eggs: {
    type: Number,
    min: [6, "Too few eggs"],
    max: 12
  },
  bacon: {
    type: Number,
    required: [true, "Why no bacon?"]
  },
  drink: {
    type: String,
    enum: ["Coffee", "Tea"],
    required: function() {
      return this.bacon > 3;
    }
  }
});
var Breakfast = db.model("Breakfast", breakfastSchema);

var badBreakfast = new Breakfast({
  eggs: 2,
  bacon: 0,
  drink: "Milk"
});
var error = badBreakfast.validateSync();
assert.equal(error.errors["eggs"].message, "Too few eggs");
assert.ok(!error.errors["bacon"]);
assert.equal(
  error.errors["drink"].message,
  "`Milk` is not a valid enum value for path `drink`."
);

badBreakfast.bacon = 5;
badBreakfast.drink = null;

error = badBreakfast.validateSync();
assert.equal(error.errors["drink"].message, "Path `drink` is required.");

badBreakfast.bacon = null;
error = badBreakfast.validateSync();
assert.equal(error.errors["bacon"].message, "Why no bacon?");
```

## Azam's Notes

```js
// app.js Server Side

const express = require("express");
const app = express();
const cors = require("cors");
var mongoose = require("mongoose");
const Post = require("./schemas/post");
const Comment = require("./schemas/comment");

app.use(cors());
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

app.post("/comments", async (req, res) => {
  const postId = req.body.postId;
  const commentTitle = req.body.title;
  const commentBody = req.body.body;

  const comment = new Comment({
    postId: postId,
    //title: commentTitle,
    body: commentBody
  });

  try {
    await comment.save();
    res.json({ success: true });
  } catch (error) {
    console.log(error);
    console.log(error.errors["title"].message);
    res.json({ error: error });
  }
});

/*
app.post('/comments',(req,res) => {

    const postId = req.body.postId 
    const title = req.body.title 
    const body = req.body.body 

    const comment = new Comment({
        title: title, 
        body: body 
    })

    Post.findById(postId,(error, post) => {
        post.comments.push(comment)
        post.save(error => {
            if(!error) {
                res.json({success: true})
            } else {
                res.json({error})
            }
        }) 
    })


}) */

app.put("/posts", (req, res) => {
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

//  /posts/5d8246dcd94aa228362d1e33
app.get("/posts/:postId", async (req, res) => {
  const postId = req.params.postId;
  const post = await Post.findById(postId);
  const comments = await Comment.find({
    postId: postId
  });

  res.json({ post: post, comments: comments });
});

app.post("/posts", (req, res) => {
  const title = req.body.title;
  const body = req.body.description;

  let post = new Post({
    body: body
  });

  post.save(error => {
    if (error) {
      console.log(error);
      res.json({ error: "Unable to save" });
    } else {
      res.json({ success: true, message: "Saved new post!" });
    }
  });
});

// get all posts
app.get("/posts", async (req, res) => {
  // Using Promises with async and await
  try {
    const posts = await Post.find({});
    res.json(posts);
  } catch (error) {
    res.json({ error: "Unable to get all posts" });
  }

  /* Using Promises
    Post.find({}).then((posts) => {
        res.json(posts)
    }).catch(error => {
        res.json({error: 'Unable to get all posts!'})
    }) */

  /* Using Callbacks 

    Post.find({},(error,posts) => {
        if(error) {
            res.json({error: 'Unable to fetch posts!'})
        } else {
            res.json(posts)
        }
    }) */
});

app.listen(3002, () => {
  console.log("Server is running...");
});
```

```js
// schemas/comment.js Server Side

const mongoose = require("mongoose");
const Schema = mongoose.Schema;
const ObjectId = Schema.ObjectId;

const commentSchema = new mongoose.Schema({
  postId: ObjectId,
  title: {
    type: String,
    required: [true, "Please provide the title of the comment!"]
  },
  body: String
});

// mongoose will create a posts collection in the database
const Comment = mongoose.model("Comment", commentSchema);

module.exports = Comment;
```

```js
// schemas/post.js Server Side

const mongoose = require("mongoose");

const postSchema = new mongoose.Schema({
  title: String,
  body: String
});

// mongoose will create a posts collection in the database
const Post = mongoose.model("Post", postSchema);

module.exports = Post;
```
