# React Day 3

DisplayName.js

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

App.js

```js
import React, { Component } from "react";
import {DisplayName, InputName}
import logo from "./logo.svg";
import "./App.css";

class App extends Component {
    render() {
        return  <div className="main-content-styles" >
                    <DisplayName />
                </div>
    }
}

export default App;
```
