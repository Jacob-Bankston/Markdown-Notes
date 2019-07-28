# Day 21 - Digital Crafts - Notes

## Kelsey

* Great Projection
* Very familiar with slides
* A lot of research went in to this presentation
* Very comfortable speaking to the group, normal speaking tone instead of a "presentation voice"
* Awesome idea to use technology in your presentation!!
* You really sold yourself to the group as a valuable resource as a user experience expert! Be prepared to have everyone go through you to test out their products next week!
* Happy Path First is a great mindset! Thanks for sharing this with us!!
* Things Organized Neatly

## Carine

* I love your smile! Very positive throughout the presentation
* You warmed everyone up by having them share about themselves. It made the room more comfortable :]
* I love your topic, happiness is so important in the world!
* You're a great public speaker, great projection, expressive gestures and good inflection in your voice.
* You seem very comfortable in front of an audience!

## Git Branches

The purpose for branches is to protect you from messing up the project.

The other benefit is it is only working on small versions of the stuff.

You have a main master branch to merge, and you can merge branches together without going to the master.

Merging two branches creates a new branch.

Commit changes frequently to have a up to date history.

Be very descriptive and punctual in your commit messages so we know what you're doing

#### Merge Conflicts

* Should I take John's menu or Sally's menu?

You have to get together and discuss what you're putting together and solve the issue then try again.

#### Master Branch

The main branch for all the commits.

You have to refer your branch back with the master and pull the information for it to see how your feature interacts with the rest of the code.

You do not want to work in isolation.

__Merge Master into Filter Branch__
* You check to make sure your thing doesn't break the master branch BEFORE you push to the master file.
* You check this by making unit tests to check the code.

checkout - moving around inside of the git folder
pull request - you request for your branch changes to go to the master
add - adding files to your current section of the git (branch or master)
commit - committing your changes of what you added to the git (branch or master)
*checkout the local master - pull from the remote master to make sure your code still works with the master*

git checkout master
git pull origin master
git checkout -b 'change greeting function' - *this creates a new branch with the -b*
git checkout -b 'change greeting'
git branch
git merge __(whatever your merging to goes here)__ - *it will default to whatever branch you're on currently*

## Software Development Principles

#### Waterfall

Step by step process to go through all of the process to create an application. Can take a long time to construct the entire system.

#### Agile

Also known as Pair Programming, Scrum, Deloyment, Continuous Development, Continuous Testing

## Sprints in Agile

Find out the task list of everything that you need ot add.

A normal sprint is 2 weeks. (There's a lot of flexibility on this topic in the indsutry)

#### Stories

When you have a story from a business person you have to be able to break down what things you have to break down and implement to create that thing. All of the points then can break down into their own points. It is your job as a developer to convert the story into the action items of what you need to construct and work on in the work flow. __THIS IS NOT A TIME FRAME, THESE ARE ACTION ITEMS WITHOUT A TIME FRAME.__

* Overall Example:
  * Login Page
  * Sign Up Page
  * Display Products
  * Search Products
  * Shopping Cart

__PLANNING POKER__ - Everyone will try and convince each other that their evaluation of action items is more accurate and to defend the amount of points to cross. When something has too many points, split it into multiple sections to work on.

* Overall Example:
  * Login Page [Guesses - 5, 8, 8, 8]
  * Sign Up Page [Guesses - 5, 5, 3, 6]
  * Display Products [Guesses - 9, 8, 10, 7]
  * Search Products 
  * Shopping Cart

* Example: The user should be able to login on the login page
  * Text input from user
  * Button interactivity
  * Styling of page
  * Connecting to database
  * Pulling authentication from database
  * Set up a database to store the data
  * Etc...

#### Sticky Notes
You take a sticky note with an action item, put your name on it with extra information as it moves down the chart.

The main goal is to finish each story! Help push all of the sticky notes to the end of the list.

* Story
  * Used to list out the task items on each story to work on.
* Doing
  * Who is doing the task - How much time it will take
* Done
  * Who did the thing and is it finished - How long it actually took - Ready to Test
* Testing
  * Put the code through Unit Testing and actual Testing
* Completed
  * List of all of the completed task lists

__At the end of the two week sprints you have to deploy the application to demo the product to the business team. Everyone will be there, you may be presenting this to 30+ members of your team.__

#### Velocity

Then it's not over!! At this point you should determine how many action items that you can handle within a given time period by determining your average velocity of productivity.

#### Scrum Meetings

__A morning meeting where they answer three questions.__

*This should last less than 2 minutes.*

1. What you did yesterday
2. What are your goals for today
3. What is going to be the challenges that will inhibit you in those goals.

#### Retrospective

* After the sprint you have a meeting to discuss what worked well and what did not work well. This is something to reflect on the team work and how to improve the team in the future.

## Authentication

Grabe the script for the firebase auth in the documentation

Available web libraries in web - step 5 - authentication

Authentication tab in firebase - add a sign-in method

Users does not auto refresh, you have to do that manually to check

```js

// Sign up a new user code! Documentation has other code to manipulate other things!
registerButton.addEventListener('click', () = {
    let email = registerEmailTextBox.value

        firebase.auth().createUserWithEmailAndPassword(email, password).catch(function(error) {
        // Handle Errors here.
        var errorCode = error.code;
        var errorMessage = error.message;
        // ...
        });
})
```

__Check the Firebase Authentication tab in the docs. Google the terms and read!__

When you get the object for the user you want to know what the `uid` is. 
It is the __unique__ ID code for that user to separate them from the other users.

Know the difference between `type="text"` and `type="password"`!

*For a work-around for now add js files for separate html files to work around an issue with errors popping up when you change pages.*

* Application Tab Google Chrome Developer Tools
  * Go into Databases and find Firebase

```js
let currentUser = firebase.auth().currentUser
console.log(currentUser)
```

You can always check for the current user to get their information from the authentication firebase data to pull their uid to manipulate it.