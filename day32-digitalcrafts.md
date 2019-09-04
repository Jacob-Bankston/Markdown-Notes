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

- Header Component
- Sidebar Component
- Footer Component
- Main Content Component

Everything that you design will be a component.

There is a `<div id="root">` at thee top of the index.html file. The idea is React will render all of the components and inject it into the root div.

## Import

Instead of using the notation of `const express = require('express')` there is a new updated way to import frameworks and files.

```js
import React from "react";
import logo from "./logo.svg";
```

## Example App.js

```js
import React from "react"; // we're importing React from the react framework

class App {} // this app will be a component! It has to first inherit the functionality of a Component via 'extends'
```

```js
import React from "react";
// the App class is inheriting from the Component Class.
class App extends Component {
  // it has to inherit these traits or it can't be displayed.
}

// this makes sure that the App class is accessible from outside of the file.
// making sure that other files can import App into them.
export default App;
```

The components are created with Capital letters by choice, but it is the industry standard. You need to make sure that you capitalize the first letter of all of your components.

The `render` function will tell your application what to render to the screen.

```js
import React from "react";
class App extends Component {
  // html here is called JSX!
  // JSX will allow you to return HTML from JavaScript
  render() {
    return <div></div>;
  }
}

export default App;
```

Install React Developer Tools! New updates are interesting to try and sift through, so let's struggle and learn together!

Without the React Developer Tools you will be "super completely lost"

Whenever you build the UI in react, you will build it in the render function!

```js
import React from "react";
class App extends Component {
  render() {
    return (
      <div>
        <div>Hello World</div>
        <div>Hello World</div>
      </div>
    );
  }
}
export default App;
```

You want to motivate people to not refresh the page. Think about your application in components.

## Greet.js

```js
import React, { Component } from "react";
class Greet extends Component {
  render() {
    return <h1>Greet</h1>;
  }
}
export default Greet;
```

Importing the new component!

```js
import React from "react";
class App extends Component {
  render() {
    // adding the component file in here!
    return (
      <div>
        <div>Hello World</div>
        <div>Hello World</div>
        <Greet />
      </div>
    );
  }
}
export default App;
```

Now you have an App component that has a child component, the Greet component!

React is replacing things in the Virtual DOM, which is how it is able to update quickly for the user.

## Properties - aka props

The parent component can send information to the children!

The children can send information to the parent, or siblings, but they shouldn't talk to each other.

It becomes super complicated.

```js
import React from "react";
class App extends Component {
  render() {
    return (
      <div>
        <div>Hello World</div>
        <div>Hello World</div>
        <Greet name="Mary" catName="Furry" />
      </div>
    );
  }
}
export default App;
```

```js
import React, { Component } from "react";
class Greet extends Component {
  render() {
    return (
      <h1>
        Hello {this.props.name} and the pet name is {this.props.catName}
      </h1>
    );
  }
}
export default Greet;
```

You pass the properties from the App.js and you can insert them in the Greet.js file by using `this.props` functionality.

## State

State is used to control the state of the component.
When you refresh it clears out the local state. The state is only available by the component itself (until we get to Redux and the global state).

Add a constructor inside of the App Component!

```js
import React from 'react';
class App extends Component {

    constructor() {
      // it's a requirement that you have to call the super() class because it has to inherit traits from parents and component
      super(props) // calling the parent class constructor

      // state is nothing more than an empty object
      this.state = {
          counter: 0
          name: "Alex"
      }
    }

    // implementing the counter function!
    // Whenever you are using Reactive programming you will never change the state, you will create a new state!

    // Bad example!
    // incrementCounter() {
    //     console.log('increment counter')
    //     this.state.counter += 1
    // }

    // Bad example 2!
    // If you use normal method like functions it will not know what 'this' is!
    // In this situation 'this' is undefined.
    incrementCounter() {
        console.log('increment counter')
        this.setState({
            counter: 1
        })
    }

    render() {
        return  (
                <div>
                    <div>Hello World</div>
                    <<button onClick={this.incrementCounter}>Increment Counter</button>
                    <Greet name = "Mary" catName = "Furry" />
                </div>
        )
    }
}
export default App
```

```js
import React from 'react';
class App extends Component {
    constructor() {
      super(props)
      this.state = {
          counter: 0
          name: "Alex"
      }

      // inside the constructor we know that the value of this is defined!
      // we are telling incrementCounter to use the value of 'this' when it was NOT undefined.
      this.incrementCounter = this.incrementCounter.bind(this)

    }

    // because of the set up in the constructor, this is now defined!
    // you can completely bypass this by using an anonymous arrow function.
    incrementCounter() {
        console.log('increment counter')
        this.setState({
            counter: 1
        })
    }

    render() {
        return  (
                <div>
                    <div>Hello World</div>
                    <<button onClick={this.incrementCounter}>Increment Counter</button>
                    <Greet name = "Mary" catName = "Furry" />
                </div>
        )
    }
}
export default App
```

```js
import React from 'react';
class App extends Component {
    constructor() {
      super(props)
      this.state = {
          counter: 0
          name: "Alex"
      }
    }

    // anonymous arrow functions know the correct state of 'this'!
    incrementCounter = () => {
        console.log('increment counter')
        this.setState({
            counter: 1
        })
    }

    render() {
        return  (
                <div>
                    <div>Hello World</div>
                    <<button onClick={this.incrementCounter}>Increment Counter</button>
                    <Greet name = "Mary" catName = "Furry" />
                </div>
        )
    }
}
export default App
```

**Whenever you set the state, it will automatically call the render function.**

You can not set the state inside of the render function because of this! It will crash your app!

```js
import React from 'react';
class App extends Component {
    constructor() {
      super(props)
      this.state = {
          counter: 0
          name: "Alex"
      }
    }

    incrementCounter = () => {
        console.log('increment counter')
        this.setState({
            counter: counter + 1
        })
    }

    // adding in the value of state into the view of the component!

    render() {
        return  (
                <div>
                    <div>Hello World</div>
                    <<button onClick={this.incrementCounter}>Increment Counter</button>
                    <h1>{this.state.counter}</h1>
                    <h3>{this.state.name}</h3>
                    <Greet name = "Mary" catName = "Furry" />
                </div>
        )
    }
}
export default App
```

Adding in APIs to call in!

```js
import React from 'react';
class App extends Component {
    constructor() {
      super(props)
      this.state = {
          counter: 0
          name: "Alex"
          // adding a photos array!
          photos: []
      }
      // adding a this for fetchPhotos
      this.fetchPhotos()
    }

    fetchPhotos = () {
        fetch('https://jsonplaceholder.typicode.com/photos')
        .then(response => response.json())
        .then(photos => {
            // always use setState! Don't use this.state.props, you want to create a new state object!
            this.setState({
                photos: photos
            })
            console.log(photos)
        })
    }

    incrementCounter = () => {
        console.log('increment counter')
        this.setState({
            counter: counter + 1
        })
    }

    // adding in the value of state into the view of the component!
    render() {

        let photoItems = this.state.photos.map(photo => {
            // this looks like template literals, but they're JSX items!
            // try to give each div a unique id to differentiate between them
            return  <div key={photo.id}>
                        <img src={photo.thumbnailURL} />
                        {photo.title}
                    </div>
        })

        // adding photoItems into the return statement!
        return  (
                <div>
                    <div>Hello World</div>
                    <<button onClick={this.incrementCounter}>Increment Counter</button>
                    <h1>{this.state.counter}</h1>
                    <h3>{this.state.name}</h3>
                    <Greet name = "Mary" catName = "Furry" />
                    {photoItems}
                </div>
        )
    }
}
export default App
```

Note: This is going to be super slow because it is doing 5000 requests for each image in the API call.

To improve this code you can break it down into a new component!

PhotoList.js

```js
import React, { Component } from "react";

class PhotoList extends Component {
  render() {
    return <div>PhotoList</div>;
  }
}

export default PhotoList;
```

Remember, the purpose of this component is just to display the photos! It should only have one jo.
If you make it fetch the photos then you can not reuse it!

```js
// App.js return function in the render!
        return  (
                <div>
                    <div>Hello World</div>
                    <<button onClick={this.incrementCounter}>Increment Counter</button>
                    <h1>{this.state.counter}</h1>
                    <h3>{this.state.name}</h3>
                    <Greet name="Mary" catName="Furry" />
                    <PhotoList photos={this.state.photos} />
                </div>
        )
```

```js
import React, { Component } from "react";

class PhotoList extends Component {
  render() {
    let photoItems = this.props.photos.map(photo => {
      return <div>{photo.title}</div>;
    });
    return <div>{photoItems}</div>;
  }
}
export default PhotoList;
```

**SRP Single Responsibility Principal: When you create a function or a component, make sure that it has one and only one job.**

## Concepts that are important!

- Always call setState and make a brand new state object. Never use this.state.props for this
- SRP - Single Responsibility Principal
