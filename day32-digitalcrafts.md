# React Beginning!

## SPA (Single Page Application)

Examples: Gmail, Facebook, Twitter

## React

Just the UI. It only pertains to the user interface on the screen. Just like with anything else, if you learn 20% of the knowledge then you will be able to use 80% of the features.

Once you learn React, you will feel right at home learning other frameworks like Flutter or Swift UI or other declarative UI frameworks.

There are many ways that you can start up a React application, but one of the best ways is to use Create React App.

## Create React App

npx create-react-app hello-react

yarn is a faster version of npm but you can use npm instead.

One of the coolest features of testing React applications is that it will load the application immediately.

## Components

Each different aspect of the application are components.
* Header Component
* Sidebar Component
* Footer Component
* Main Content Component

Everything that you design will be a component.

There is a `<div id="root">` at thee top of the index.html file. The idea is React will render all of the components and inject it into the root div.

## Import

Instead of using the notation of `const express = require('express')` there is a new updated way to import frameworks and files.

```js
import React from 'react';
import logo from './logo.svg';
```

## Example App.js

```js
import React from 'react'; // we're importing React from the react framework

class App { }// this app will be a component! It has to first inherit the functionality of a Component via 'extends'
```

```js
import React from 'react';
// the App class is inheriting from the Component Class.
class App extends Component { // it has to inherit these traits or it can't be displayed.

}

// this makes sure that the App class is accessible from outside of the file.
// making sure that other files can import App into them.
export default App
```

The components are created with Capital letters by choice, but it is the industry standard. You need to make sure that you capitalize the first letter of all of your components.

The `render` function will tell your application what to render to the screen.

```js
import React from 'react';
class App extends Component { 

    // html here is called JSX!
    // JSX will allow you to return HTML from JavaScript
    render() {
        return <div></div>
    }

}

export default App
```

Install React Developer Tools! New updates are interesting to try and sift through, so let's struggle and learn together!

Without the React Developer Tools you will be "super completely lost"

Whenever you build the UI in react, you will build it in the render function!

```js
import React from 'react';
class App extends Component { 
    render() {
        return  (
                <div>
                    <div>Hello World</div>
                    <div>Hello World</div>
                </div>
        )
    }
}
export default App
```

You want to motivate people to not refresh the page. Think about your application in components.

## Greet.js

```js
import React, {Component} from 'react';
class Greet extends Component {
    render() {
        return (
            <h1>Greet</h1>
        )
    }
}
export default Greet
```

Importing the new component!

```js
import React from 'react';
class App extends Component { 
    render() {
        return  (
                <div>
                    <div>Hello World</div>
                    <div>Hello World</div>
                    <Greet />
                </div>
        )
    }
}
export default App
```

Now you have an App component that has a child component, the Greet component!

React is replacing things in the Virtual DOM, which is how it is able to update quickly for the user.

## Properties - aka props

