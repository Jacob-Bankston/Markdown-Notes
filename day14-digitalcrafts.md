# Day 14 - Digital Crafts - Notes

## Javascript

* If you don't declare something as `var`, `let` or `const` it defaults as a global variable.
* `const`: you can not change the value once it is assigned
* `let`: is a variable that can be changed
* `var`: is a variable that can be changed
* Most of the time you won't see a difference. The only time that there is a difference is when you have some sort of a scope. For the following Example 1, it hoists the same variable name for the temporary variable in the if statement and reassigns the value because it is within the same function area. You would have to use let instead to do what you want to do within the local scope.
```js
// Example 1

function calculateAge() {
    var age = 20

    if(1 == 1) {
        // variable hoisting in JS if you use a var keyword
        var age = 30
    }

    console.log(age)
}
```
```js
// Example 2

function calculateAge() {
    let age = 20

    if(1 == 1) {
        // variable hoisting in JS if you use a var keyword
        let age = 30
    }

    console.log(age)
}
```
* For ES6 and newer platforms for now there is not a really good use case for using `var` anymore. Simply use `const` and `let` instead.
* _Fun Fact: In IOS let is the constant!_

## Document Object Model (DOM)

* The document object model is the reference point for all of the parts of a website.
  
![DOM Model](https://upload.wikimedia.org/wikipedia/commons/thumb/5/5a/DOM-model.svg/800px-DOM-model.svg.png)

* You start the search through the DOM via `<tags>` or classes and ids.

```js
// DOM Document Object Model

// get element by id
// document = Document Object Model
// document = Current DOM of HTML document

// this will grab the single div with the id of myDiv
let someDiv = document.getElementById("myDiv")
console.log(someDiv)

// this will grab the single div with the class of classyDiv
let someDiv2 = document.getElementByClassName("classyDiv")
console.log(someDiv2)

// this will grab all of the paragraphs and place them into an array
let somePara = document.getElementsByTagName("p")
console.log(somePara)

// this will grab all of the "classish" elements and place them into an array
let classes = document.getElementsByClassName("classish")
console.log(classes)
```

#### _When you are going through the Document Object Model (DOM) then you have to have the `<script>` tags in your HTML below what you are trying to search for._

* A quick way to test if javascript commands work is to run them in the console in you Google Developer Tools

## Tying it all together!

* `<input type="text"/>` will create a textbox. There are a lot of ways for the user to input in HTML.

```html
<!-- HTML -->
<input type="text" placeholder="Enter City Name">
<input type="text" placeholder="Enter Image URL Name">
<button id="saveButton">Save</button>
```
```js
//JavaScript
function saveVacationInfo() {
    console.log("saveVacationInfo")
}

// Every time that you search for the element it searches the whole DOM,
// so it's always a good idea to move your elements into a variable 
// so you can use it later on!
let saveButton = document.getElementById("saveButton")

// saveVacationInfo is a new function to handle the save button click
saveButton.addEventListener('click', saveVacationInfo)

// or you can create an anonymous function!
saveButton.addEventListener('click', function() {
    console.log("button click fired...")
})
```
* _Azam Clean Code Tip: When you are manipulating an item, place the name of the item at the end to clearly see what you are manipulating. For example_ `<button id="saveButton">`

* In order to use the debugging tools in Chrome for JavaScript you need to flag in the debugger where you want the script to stop.

## Create Elements in JavaScript

##### This will let you dynamically change your page using JavaScript

```js
saveButton.addEventListener('click', function() {
    console.log("button click fired...")

    let city = cityTextBox.value
    let cityImageURL = cityImageURLTextBox.value

    // create a DIV Element
    let vacationDiv = document.createElement("div")
    // label the inner text for the HTML with the variable city
    // vacationDiv.innerHTML = city

    // create a span tag
    let vacationTitleSpan = document.createElement("span")
    vacationTitleSpan.innerHTML = city

    // create an image tag
    let vacationCityImage = document.createElement("img")
    vacationTitleImage.src = cityImageURL
    // Notice that you use .src - always check back to the HTML procedure!
    // <img src=""> You're filling up the gap!

    // adding a class to an element in JavaScript
    vacationCityImage.className = "vacation-image"

    //Putting it all into a div then appending it to the parent node
    vacationDiv.appendChild(vacationTitleSpan)
    vacationDiv.appendChild(vacationCityImage)

    vacationListDiv.appendChild(vacationDiv)
})
```

* Inner HTML: The stuff between the tags is referred to as inner HTML
* One thing to remember is that the order of your JavaScript does matter! If you're pulling functionality from one js file in another, you have to link that one first!!
    * `<script src="all-my-functions-that-I-need.js" />`
    * `<script src="the-rest-of-my-javascript.js" />`
    * **NOT**
    * `<script src="all-my-functions-that-I-need.js" />`
    * `<script src="the-rest-of-my-javascript.js" />`