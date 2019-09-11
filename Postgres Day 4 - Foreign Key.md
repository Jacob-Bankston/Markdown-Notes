#Digital Crafts Notes - Day 30

For Posts on a website you will have a one to many relationship

One Post will have many Comments

Strategy: Listen to events on parents then pull the child from the parent so you are not having to worry about new dynamically added children, just worried about listening to an event occurring on the parent.

You want to create both tables separately then after you would set up the foreign key.

If you use `db:migrate:undo` it will remove the last migration, even if you ran multiple migrations previously.

`sequelize migration:create --name 'postid-as-fk-in-comments'` Remember to be as descriptive as possible when you are creating your migrations.
You want your code to be readable to other developers.

```js

// Creating Foreign Key Constraint

module.exports = {
    up: (queryInterface, Sequelize) => {
        return queryInterface.addConstraint(
            'Comments', // table name
            ['postid'], { // column name
                type: 'FOREIGN KEY',
                references: {
                    table: 'Posts', // table referenced
                    field: 'id', // primary key in the referenced table
                    name: 'postid-fk-in-comments' // name of the constraint!
                }
            }
        )
    },

    down: (queryInterface, Sequelize) => {
        return queryInterface.removeConstraint(
            'Comments', // table name
            'postid-fk-in-comments' // name of the constraint!
        )
    }
}
```

```js
// app.js

const express = require('express')
const app = express()

app.use(express.urlencoded())

app.post('/create-post', (req, res) => {

    let title = req.body.title
    let body = req.body.body
    let isPublished = req.body.isPublished == "true" ? true : false

    models.Post.build({
        title: title,
        body: body,
        isPublished: isPublished
    })

    post.save().then(savedPost => res.json(savedPost)) // more likely we'll use a redirect
        .catch(error => res.json({message: "Error saving post!"}))

})


app.listen(3000, () => {
    console.log("Server is running...")
})
```

__To check on Postman use the x-www-form-urlencoded and put in the appropriate key and value pairs to see if it uploads correctly in the database.__

```js
app.post('/create-comment', (req, res) => {

    let subject = req.body.subject
    let body = req.body.body
    let postId = parseInt(req.body.postId)

    let comment = models.Comment.build({
        subject: subject,
        body: body,
        postid: postId // notice that the capitalization matters with the headers in the database!!!
    })

    comment.save().then(savedComment => res.json(savedComment))
    .catch(error => res.json(error))

})
```

```js
app.get('/posts/:postId', (req, res) => {
    
    let postId = parseInt(req.params.postId)

    models.Post.findOne({
        where: {
            id: postId
        }
    }).then(post => res.json(post))
    .catch(error => res.json({message: 'Post not found!'}))

    res.render('post-details', {post: post})
})
```

When you have a foreign key it will error out the system when you try to add a comment to a postId that doesn't exist.

```js
// in module exports for posts!!
Post.associate = function(models) {
    // create one to many relationship between
    // post and comments
    models.Post.hasMany(models.Comment, {as: 'comments', foreignKey: 'postid'})
    // as is an alias into whatever you want. Now you can refer to it as post.comments!
};
```

Once you have created the relationship then you have to specify to sequelize that you want it to include the comments.

```js
app.get('/posts/:postId', (req, res) => {
    
    let postId = parseInt(req.params.postId)

    models.Post.findOne({
        include: [
            {
                model: models.Comment,
                as: 'comments' // this alias has to remain the same
            }
        ],
        where: {
            id: postId
        }
    }).then(post => res.json(post))
    .catch(error => res.json({message: 'Post not found!'}))

    res.render('post-details', {post: post})
})
```

```js
// in module export for comments!!
Comment.associate = function(models) {
    models.Comments.belongsTo(models.Post, {as: 'post', foreignKey: 'postid'})
    // now you can refer to it as comment.post!
};
```

Use Case: Login => Comments => Click on the Comment => Shows you the Post

```js
app.get('/comments/:commentId', (req, res) => {

    let commentId = parseInt(req.params.commentId)

    models.Comment.findOne({
        include: [
            {
                model: models.Post,
                as: 'post'
            }
        ],
        where: {
            id: commentId
        }
    }).then(comment => res.json(comment)).catch(error => res.json({message: "Could not find comment!"}))

})
```

The other relationship that can occur is a many to many relationship. This adds a lot more complexity to the material, and we did not cover it in class today.

glitch.com => Azam's profile = giddy-tower

Deploy node.js server and database online on Heroku and ElephantSQL.