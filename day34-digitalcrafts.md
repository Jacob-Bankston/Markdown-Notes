# React Day 3

## Adding Styles via className=""

**DisplayName.js**

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

**App.js**

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

**App.js**

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

**DisplayName.js**

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

**App.js**

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

**index.js**

```js
ReactDOM.render(<App>MENU</App>, document.getElementById("root"));
```

From here you would need to inject the `{this.props.children}` to add the text `MENU` to the App Component.

**App.js**

```js
class App extends Component {
  render() {
    // then you add className to the .css file and style like normal!
    return (
      <div className="main-content-styles">
        {this.props.children}
        <DisplayName>
          Hey! I am a child of the DisplayName Component
        </DisplayName>
      </div>
    );
  }
}
```

## React Router

`npx create-react-app nameOfApp`
`npm install react-router-dom`

**App.js**

```js
class App extends Component {
  render() {
    return <div>App</div>;
  }
}
```

If you navigate to web pages like Amazon, every page will have a header component, a footer component, and the main component will change depending on the page

You can set up a Base Layout for how you will dictate the overall structure of the application

Base Layout

> Menu
> Main Content
> Footer

**BaseLayout.js**

```js
import React, { Component } from "react";
import App from "./App";

export class Menu extends Component {
  render() {
    return <div>Menu</div>;
  }
}

export class Footer extends Component {
  render() {
    return <div>Footer</div>;
  }
}

export class BaseLayout extends Component {
  render() {
    return (
      <div>
        <Menu />
        <App />
        <Footer />
      </div>
    );
  }
}
```

It's up to you what you would like to display as your home component, it's easy to add it as the App component!

**App.js**

```js
class App extends Component {
  render() {
    return <div>Welcome to my Website...</div>;
  }
}
```

**App.js**

```js
class App extends Component {
  render() {
    return <div>{this.props.children}</div>;
  }
}
```

## Importing the React Router!

**index.js**

```js
import React from "react";
import ReactDOM from "react-dom";
import "./index.css";
import { BaseLayout } from "./components/BaseLayout";
import App from "./components/App";
import { BrowserRouter, Route } from "react-router-dom";

ReactDOM.render(
  <BrowserRouter>
    <BaseLayout>
      <Switch>
        <App />
      </Switch>
    </BaseLayout>
  </BrowserRouter>,
  document.getElementById("root")
);
```

You need to utilize the `<Switch>` to select one of the children to send the page to based on the route.

Then you will identify the `<Route path="" component={} />` to determine which content the application will load.

**index.js**

```js
import React from "react";
import ReactDOM from "react-dom";
import "./index.css";
import { BaseLayout } from "./components/BaseLayout";
import App from "./components/App";
import { BrowserRouter, Route } from "react-router-dom";

ReactDOM.render(
  <BrowserRouter>
    <BaseLayout>
      <Switch>
        <Route path="/" component={App} />
      </Switch>
    </BaseLayout>
  </BrowserRouter>,
  document.getElementById("root")
);
```

The Switch and Route will compare all options based on the url route, then will inject that child option into the BaseLayout.js where it states `{this.props.children}`

**BookList.js**

You should create a separate file for each part of the component, but for demonstrations, we'll just use one file for now.

```js
import React, { Component } from "react";

export class BookList extends Component {
  render() {
    return <div>BookList</div>;
  }
}

export class AddBook extends Component {
  render() {
    return <div>AddBook</div>;
  }
}
```

**index.js**

```js
import React from "react";
import ReactDOM from "react-dom";
import "./index.css";
import { BaseLayout } from "./components/BaseLayout";
import App from "./components/App";
import { BrowserRouter, Route } from "react-router-dom";
import { BookList, AddBook } from "./components/BookList";

ReactDOM.render(
  <BrowserRouter>
    <BaseLayout>
      <Switch>
        <Route path="/" exact component={App} />
        <Route path="/books" component={BookList} />
        <Route path="/addBook" component={AddBook} />
      </Switch>
    </BaseLayout>
  </BrowserRouter>,
  document.getElementById("root")
);
```

## Updating the Menu!

Using NavLink you can update the page very easily with the routes that you have set up!

**BaseLayout.js**

```js
import React, { Component } from "react";
import App from "./App";
import { NavLink } from "react-router-dom";

export class Menu extends Component {
  render() {
    return (
      <ul>
        <li>
          <NavLink to="/">Home</NavLink>
        </li>
        <li>
          <NavLink to="/books">View Books</NavLink>
        </li>
        <li>
          <NavLink to="/add-book">Add Book</NavLink>
        </li>
      </ul>
    );
  }
}

export class Footer extends Component {
  render() {
    return <div>Footer</div>;
  }
}

export class BaseLayout extends Component {
  render() {
    return (
      <div>
        <Menu />
        <App />
        <Footer />
      </div>
    );
  }
}
```

## Handling adding or updating and rerouting from there!

**BookList.js**

```js
import React, { Component } from "react";

export class BookList extends Component {
  render() {
    return <div>BookList</div>;
  }
}

export class AddBook extends Component {
  handleSave = () => {
    this.props.history.push("/"); // using this function with the parameter you can redirect to another route!
  };

  render() {
    return (
      <div>
        <div>AddBook</div>
        <button onClick={this.handleSave}>Save</button>
      </div>
    );
  }
}
```

**index.js**

```js
import React from "react";
import ReactDOM from "react-dom";
import "./index.css";
import { BaseLayout } from "./components/BaseLayout";
import App from "./components/App";
import { BrowserRouter, Route } from "react-router-dom";
import { BookList, AddBook } from "./components/BookList";

ReactDOM.render(
  <BrowserRouter>
    <BaseLayout>
      <Switch>
        <Route path="/" exact component={App} />
        <Route path="/books/:bookId" component={AddBook} />
        <Route path="/books" component={BookList} />
        <Route path="/addBook" component={AddBook} />
      </Switch>
    </BaseLayout>
  </BrowserRouter>,
  document.getElementById("root")
);
```

**BookDetail.js**

```js
export class BookDetail extends Component {

    constructor(props) {
        super(props)

        console.log(props) // checking whether we're at the correct 
    }

  render() {
    return <div>BookDetail</div>;
  }
}
```

In Developer Tools!
* Go to Developer Tools
* Go to file in the component sources
* Select the debugger
* Refresh for the props
* in the console go through to find where you can get the book id!

```js
export class BookDetail extends Component {

    constructor(props) {
        super(props)

        console.log(props.match.params.bookId) // get the bookId from the url
    }

  render() {
    return <div>BookDetail</div>;
  }
}
```

## Next Steps to Deploy!

say `npm run build` from inside your react folder

This will create a build folder for you

That folder will contain everything that you will need to deploy

It will take all of the React stuff that you had, compiles it all together and sets it up to be simple to deploy

## Practice

Make sure that you're spending the time to practice these things! React is very popular, and more so outside of Texas.

## Assignment

Same Assignment with additional features

* Create Separate pages for adding, viewing the books using React Router
* Allow the user to filter books based on the genre

## Staying in Houston - What to Learn

#### Languages or Things to know!
* Angular is important
* DotNet is important
* Machine Learning is a completely different field, but it will be super important over the next 10 years!!


#### Books

Over your career, make sure that you are continuously reading and learning new information from books!

* The Compount Effect - Jumpstart Your Income, Your Life, Your Success By: Darren Hardy
* Essentialism: The Disciplined Pursuit of Less By: Greg McKeown
* The Power of a Positive No: How to Say No and Still Get to Yes By: William Ury and Random House Audio
* Atomic Habits - James Clear

* Robert Martin - Uncle Bob - Clean Code
* Martin Fowler - Always Good Architecture Related Topics - Refactoring: Improving the Design of Existing Code (2nd Edition)

* The 5-Hour Rule Used By Bill Gates, James Ma and Elon Musk
  * They Read 5 hours a week.
  * Reflect on the information.
  * Experiment with what you just read.