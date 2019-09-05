# React Day 3

## Adding Styles via className=""

__DisplayName.js__

```js
import React, { Component } from "react";
import logo from "./logo.svg";
import "./App.css";

export const PI = 3.142;

export class DisplayName extends Component {
  render() {
    return <div>DisplayName</div>;
  }
}

export class InputName extends Component {
  render() {
    return <div>InputName</div>;
  }
}
```

__App.js__

```js
import React, { Component } from "react";
import {DisplayName, InputName}
import logo from "./logo.svg";
import "./App.css";

class App extends Component {
    render() { // then you add className to the .css file and style like normal!
        return  <div className="main-content-styles" >
                    <DisplayName />
                </div>
    }
}

export default App;
```

## Comparing HTML versus React

The HTML inside of a `<div>` is known as inner HTML in a standard HTML file

The HTML inside of the `<APP>children</APP>` is defined as `{this.props.children}`

__App.js__

```js
class App extends Component {
  render() {
    // then you add className to the .css file and style like normal!
    return (
      <div className="main-content-styles">
        <DisplayName>
          Hey! I am a child of the DisplayName Component
        </DisplayName>
      </div>
    );
  }
}
```

```js
class App extends Component {
  render() {
    // then you add className to the .css file and style like normal!
    return (
      <div className="main-content-styles">
        <DisplayName>
          Hey! I am a child of the DisplayName Component
        </DisplayName>
      </div>
    );
  }
}
```

__DisplayName.js__

```js
export class DisplayName extends Component {
  render() {
    return (
      <div>
        DisplayName
        <p> {this.props.children}</p>
      </div>
    );
  }
}
```

You can place components inside of other components in the App.js to define them as children.

Using the `{this.props.children}` you can inject different children and it will feel like you are traveling to a different page!

