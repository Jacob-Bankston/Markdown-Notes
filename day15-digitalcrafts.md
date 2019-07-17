# Day 15 - Digital Crafts - Notes

When you're adding ids to things or classes to things make sure you are very descriptive for what you are doing. You can change up variable names, but keep it consistent so it is readable.

When you are linking your javascript, put it below the `<body>` tag and above the `<html>` tag at the bottom.
  

* **MENTAL NOTE: I need to work on getting a working function and not worrying about it looking pretty. I frequently have been doing the whole project at once, or focusing on the visual components of the site. I need to be more procedural with how I am creating projects. This will have a greater impact if I am working on this early on in the bootcamp rather than trying to catch up later.**
<br>
* **MENTAL NOTE: Just because you can follow along with something doesn't mean you have mastered that thing. It's important to focus on the review and see the common pitfalls with the process to solidfy the learning process and commit that knowledge to long term memory.**

```js
// Arrow Functions - New ES6 Feature
saveTaskButton.addEventListener('click', () => {

})

// The arrow function is an anonymous function, it's just compact

// There is a really big difference when you start using it with classes.
// With the exception of classes, it functions like a normal anonymous function.
```

## Template Literals

ES6 Feature

```html
<button id="saveTaskButton" onClick="alert('ss')">Enter</button>
```

Writing JavaScript inline HTML is not recommended, but possible.

```js
let div = `<div>${name}</div>`
```

To-Do List Simplified with Template Literals

```js
saveTaskButton.addEventListener('click', () => {

    let title = taskTitleTextBox.value

    let taskItemDIV = `<div>
                            <input type ='checkbox' />
                            <label>$(title)</label>
                            <button'>Remove</button>
                        </div>`

    // Not optimal to pull all the lists again
    // pendingTaskList.innerHTML = taskItemDIV

    // More optimal, places it at the end
    pendingTaskList.insertAdjacentHTML('beforeend', taskItemDIV)
})
```

Removing the task with inline HTML using `this` inside the HTML

```js
function removeTask() {
    pendingTaskList.removeChild(btn.parentElement)
}

saveTaskButton.addEventListener('click', () => {

    let title = taskTitleTextBox.value

    let taskItemDIV = `<div>
                            <input type ='checkbox' />
                            <label>$(title)</label>
                            <button onclick='removeTask(this)'>Remove</button>
                        </div>`

    pendingTaskList.insertAdjacentHTML('beforeend', taskItemDIV)
})
```

```js
function removeTask() {
    pendingTaskList.removeChild(btn.parentElement)
}
function removeTask2(e) {
    console.log(e.srcElement.parentElement)
}

saveTaskButton.addEventListener('click', () => {

    let title = taskTitleTextBox.value

    let taskItemDIV = `<div>
                            <input type ='checkbox' />
                            <label>$(title)</label>
                            <button onclick='removeTask(this, event)'>Remove</button>
                            <button onclick='removeTask2(event)'>Remove</button>
                        </div>`

    pendingTaskList.insertAdjacentHTML('beforeend', taskItemDIV)
})
```

You can access from the Elements tab on the developer tools you can access all of the ways that you can interact with that event.

## Array Helpers

If you link to another script in your directory, you just need to load them in order on the html file.

These helpers DO NOT modify the existing array, they will generate a new array!

```js
let numbers = [3, 4, 5, 6, 7]
```

#### forEach

```js
numbers.forEach(function(no) {
    console.log(no)
})
```

#### map

You use this when you have to iterate through the array and manipulate all of the items within it for the new array.

Also called a __transformation operator.__

```js
let numbersDoubled = numbers.map(function(no) {
    return no * 2
})
```

#### Using Arrow Syntax


```js
let numbersDoubled = numbers.map((no) => {
    return no * 2
})
```

*Using the arrow function within one line of code*

```js
let numbersDoubled = numbers.map(no => no * 2)
```

#### filter

*Filters to only what things return true*

```js
let evenNumbers = numbers.filter(function(no) {
    return no % 2 == 0
})
```

*__There are more array helpers out there, do some research!!__*

## Photos Application

__Goal__: You have a giant array of 5000 images. How do you get those to post to the website?

```js
let photosListDiv = document.getElementById("photosListDiv")

photos.map(photo => {
    // place the project goal here!
})
```

__Step by Step__

* Use the array helper map to iterate through the array
* Generate a `<div>` from the array that contains the items from the array
* Create a template literal of the div you would like to create
* Be sure to only use property titles that are available in the array
* Add the title of the image in a `<h3>` tag
* use the `.join` function to add each of the arrays to a big list with `.innerHTML`
* Add the image source in the div

## Dom Manipulation - By Ben

When you're pulling elements then you have to set the index of 0 afterwards to pull the item out of the array that is returned instead of the array with one item in it.