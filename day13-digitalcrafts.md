# Day 13 - Digital Crafts - Notes

## JavaScript

Label JavaScript with a `<script>` tag
At the bottom of the html file you link the file using `<script src="js/site.js"></script>`

### Printing

```js
console.log("Hello World");
```

### Variables and Constants

```js
age = 12 // global variable

var age = 23 // if you don't label something with var, it selects the global variable

let age = 34 // Most of the time you will use 'let' because of the scope of the variable

const pi = 3.142 // Constant does not change over time. It will complain if you try to change it.
```

### Functions

```js
// Creating a Function
function greet() {
    console.log("Greetings Planet...");
}

// Calling a Function
greet()


// Adding parameters, returns and calling the function with arguments
function add(a, b) {
    result = a + b;
    return result;
}

let answer = add(3, 5);

console.log(answer);
```

### Loops

```js
// Doesn't have to be named 'index' it can be named 'i' and increment however you want!
for(let index = 1; index <= 10; index++) {
    console.log(index);
}
```

### Arrays

```js
let numbers = [2,3,4,5,6,7];
let names = ["John", "Alex", "Sarah", "Tim"];

for(let index = 0; index < names.length; index++) {
    console.log(names[index]);
}
```

Fun fact, you don't have to add semicolons on things anymore, then language is more aware!

### Adding an item to an array

```js
names.push("George")
```

### Conditions

```js
let version = 3
let os = "macOS"

if(version > 2) {
    console.log("Version is > 2")
}

// And Operator
if(version > 2 && os == "macOS") {
    console.log("version > 2 and macOS")
}

// Or Operator
if(version == 3 || os == "macOS") {
    console.log("One of these!")
}

// Else and Else If
if(version > 2 && os =="macOS") {
    console.log("macOS")
} else if(os == "windows") {
    console.log("windows")
} else {
    console.log("unknown os")
}
```

### Classes and Objects in JavaScript

This programming language was built in 10 days.
There are no actual Classes and Objects, just _fake_ ones. _sugar coating_!

```js
let obj = new Object() // You will probably never do this
obj.model = "Accord" // You are making up these objects on the fly.
obj.make = "Honda" // You'll never really make a base object

console.log(obj)

// Any time you have an object with a class it has the entire prototype functions

Object.prototype.drive = function() {
    console.log("I am driving...")
}
// 99% of times you will not use the Object class, you will define your own class

console.log("Creating a Car Class")


// Defining your own Class - Use a capital letter!
// How to Create a Class
function Car() {
    this.make = "" // 'this' is the same as 'self' in python
    this.model = ""
}

// How to create an object of the class
let car = new Car() // You have to use the 'new' keyword for new objects
car.make = "BMW"
car.model = "Series 3"
// You can create new attributes on the fly! Dynamic Language.
car.isElectric = false
// You should not do this because people will think it's a defined property!

let anotherCar = new Car()

console.log(car)
```

### Adding parameters

```js
// Same thing with parameters to define an attribute
function Car(make, model) {
    this.make = make
    this.model = model
}

let car = new Car("Honda", "Accord")

// Every time that you add a new object to the memory then you HAVE TO put 'new'!!!!


// Not a good approach, but it is feasible to manipulate object attributes later
// You can extend a prototype in the Car function, but just put it in the main 'Class'
car.drive = function() { // anonymous function, they don't have a name
    console.log("Driving...")
}
car.drive()
console.log(car)

// You will see anonymous functions a lot in JavaScript
// It isolates the function to that specific Class Object to not accidentally use elsewhwere
```
### Prototypes

```js
// Adding functions to prototypes

// Not a good use case...
function myDriveFunction() { // only good if you plan on calling this somewhere else.
    console.log("myDriveFunction")
}

//prototype will attach the drive function to every single instance of the Car object
Car.prototype.drive = myDriveFunction
// You can assign an anonymous function but not a function with a name!
let anotherCar = new Car("ddd", "fff")


// You CAN do this when you're using an anonymous function
Car.prototype.drive = function() {
    console.log("Car is driving...")
}

Car.prototype.brake = function() {
    console.log("Car is braking!")
}

// We will use a use a sugar coating later that makes this look cleaner!
```

### Examples

```js
function Customer() {
    this.make = ""
    this.age = ""
}

let steve = new Customer()
steve.payBills = function() { // anonymous function unique to steve!
    console.log("Pay Bills")
}

let john = new Customer()
john.payBills() // This does not work! You only assigned the anonymous function to steve!
```

**MOST of this syntax is referred to as the ES5 Syntax which is the old version of the syntax!**

The new version of the styling and tools is **ES6**, so you have to use a tool _like you do with Sass_ and convert it over to **ES5**. Most of the mobile browsers use **ES6** now, so you'll probably be okay.

### Classes in ES6

```js
class BankAccount {
    constructor() { //the same as the __init__ method in python!
        this.name = ""
        this.accountType = ""
    }

    openAccount() {
        console.log("Open Account")
    }
}

class BankAccount {
    constructor(name, accountType) { //the same as the __init__ method in python!
        this.name = name
        this.accountType = accountType
    }

    openAccount() {
        console.log("Open Account")
    }
}

let bankAccount = BankAccount("John Doe", "Checking")
bankAccount.openAccount()
console.log(bankAccount)
```

This is the same thing that you would do with the prototype functions from before.
**But** it adds sugar coating to make it format nicely.

Realize that JavaScript does not have classes and objects, it's all fake!

_JavaScript also doesn't have Dictionaries!!_

```js
bankAccount.name

// This is the same as

bankAccount["name"] // accesses the name using value of the key - like dictionary
```

It's always good to check if the features you're trying to use on **[caniuse.com](https://caniuse.com)**

### Babel

This tool converts the **ES6** file and converts it to compatible code

## Debugging JavaScript

####Debugging is just trying to solve issues and find the solution to the problem!

####The goal is to focus on one small thing, and then finding the solution to that part of it.

####One of the most important things in this course it to Debug the issue and find the solution to the problem.

### _Google Chrome Developer Tools_

Go to your **Sources** tab in your Developer Tools

Then select your JavaScript file from the drop down column on the left

You can add a `|` to add a break point in the JavaScript to check for things that may or may not be working. It slows things down for you so you can check if things are working how you expect them to.

On the top right you can select **Show Console Drawer** to see the console while you are in the sources tab. To check that as well. _You can type variables into the console to see what value they have been given._

You can use the **Play**, **Step Over** and other tools in the top right to play with the Debugger to show you what stuff is doing.

**_You can also hover over things to see what value they currently have in the script. This includes arrays!!_**

Arrays it will show you the whole array when you hover

Object will show you all of the attributes when you hover

When you use **Step Into** then it will take you into the function to see what's going on internally.

Blue highlighting means that the code will run!

####Debugging allows you to slow things down, and it is the most important thing to learn if you're getting into programming.

* Most of the time you will be working in a job that has legacy code, and you need to know how to fix issues in the code. This is the job.

* Most people don't know how to use the tools in Google Chrome Developer Tools. It can turn a 5 hour issue into a 5 minute issue. - Azam

####Most important tools
* Step Over - Not interested in the details, just step by step
* Step Into - Goes into the details of what happens in functions
* Play - utilize this with break points `|` into the code
  * This is the same functionality as the `debugger` in .js files