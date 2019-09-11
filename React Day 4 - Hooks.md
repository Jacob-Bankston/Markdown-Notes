# React Hooks

Create React App!

You'll notice that there is not a class or anything in the default Create React application, it's more of a functional based programming method.

```js
import React from "react";
import logo from "./logo.svg";
import "./App.css";

function App() {
  // this is the name of the component!
  return (
    // this is the render function!
    <div>Hello World</div>
  );
}

export default App;
```

The notation for the onclick is written this way because you are wanting the program to wait until it is clicked to take an action.

```js
function App() {
  return (
    <div>
      Hello World
      <button onClick={() => incrementCount()}>Increment</button>
    </div>
  );
}
```

```js
function App() {
  const incrementCount = () => {
    // you have to declare it as a variable, otherwise you need a class and a constructor
    // a variable can be assigned a simple or complex structure like an integer, or a function!
    console.log("increment count..."); // checking to see if increment count is even firing...
  };

  return (
    <div>
      Hello World
      <button onClick={() => incrementCount()}>Increment</button>
    </div>
  );
}
```

This is a functional oriented component rather than utilizing object oriented components

We still haven't gotten into hooks! Let's do that now!

```js
import React, { useState } from "react"; // you need to import useState from react
import logo from "./logo.svg";
import "./App.css";

// this is how we used to utilize state with object oriented programming

// class App extends Component {
//     constructor() {
//         this.state = {
//             counter = 0
//         }

//         this.setState({
//             counter:this.state.counter + 1
//         })
//     }
// }

function App() {
  // First argument - The value that you want to put in the state
  // Second argument - The method or function which will update the state

  const [counter, setCounter] = useState(0); // for useState(0) - this will set the initial value of the counter to 0

  // we simplified the 7 lines of code into one line!

  const incrementCount = () => {
    setCounter(counter + 1); // you will use setCounter to change the state of counter
  };

  const decrementCount = () => {
    setCounter(counter - 1); // you will use setCounter to change the state of counter
  };

  const decrementCount = () => {
    setCounter(counter - counter); // you will use setCounter to change the state of counter
  };

  // in order to call the counter you just call the counter! No having to worry about setting the state.

  return (
    <div>
      <h1>{counter}</h1>
      <button onClick={() => incrementCount()}>Increment</button>
      <button onClick={() => decrementCount()}>Decrement</button>
      <button onClick={() => clearCount()}>Clear</button>
    </div>
  );
}

export default App;
```

Cleaned Up App.js!

```js
import React, { useState } from "react";
import logo from "./logo.svg";
import "./App.css";
function App() {
  const [counter, setCounter] = useState(0);
  const incrementCount = () => {
    setCounter(counter + 1);
  };
  const decrementCount = () => {
    setCounter(counter - 1);
  };
  const decrementCount = () => {
    setCounter(counter - counter);
  };
  return (
    <div>
      <h1>{counter}</h1>
      <button onClick={() => incrementCount()}>Increment</button>
      <button onClick={() => decrementCount()}>Decrement</button>
      <button onClick={() => clearCount()}>Clear</button>
    </div>
  );
}
export default App;
```

PostList.js! _Be sure to change the index.js to reflect the addition of PostList._

How to Fetch!

```js
// to fetch things you can't put the fecthPosts() function outside of the class
// you have to add the useEffect - which is just like componentDidMount and componentDidUpdate
import React, { useState, useEffect } from "react";
import logo from "./logo.svg";

function PostList() {
  // name of the component

  const [posts, setPosts] = useState([]); // remember to set the state!
  const [counter, setCounter] = useState(0); // remember to set the state!

  useEffect(() => {
    // load the data!!
  });

  return <div>PostList</div>;
}
```

```js
const [posts, setPosts] = useState([]);
useEffect(() => {
  fetch("http://fetchlibrary.url")
    .then(response => response.json())
    .then(json => {
      console.log(json); // checking to see if you're getting the data!
    });
});
```

```js
const [posts, setPosts] = useState([]);
useEffect(() => {
  fetch("http://fetchlibrary.url")
    .then(response => response.json())
    .then(json => {
      setPosts(json);
    });
});
```

Before, we were in the render function when we fetched the information, now we have to inject it in our return.

```js
import React, { useState, useEffect } from "react";
import logo from "./logo.svg";

function PostList() {

    const [posts, setPosts] = useState([]);
    const [counter, setCounter] = useState(0);

    // you can create a functional variable to run the fetch function for you
    const fetchPosts = () => {
        fetch()
        .then(response => response.json())
        .then(json => {
            setPosts(json)
        })
    }

    useEffect(() => {
        fetchPosts()
    });

    // this will return you a div per post!
  return (
      <div>
      {posts.map((post) => {
          return <div><div>
      })}
      </div>
  )
}

export default PostList
```

The purpose of hooks is to reduce the amount of code that you need to actually utilize in your code.

(**Look into the life cycles of React for interview and legacy code situations just to be familiar with it!**)[https://medium.com/react-ecosystem/react-components-lifecycle-ce09239010df]

- initializing
- mounting
- updating
- unmounting
- What is a Virtual DOM

## Why would you use Redux?

Technically you can use a global hook with a reducer with React, but many companies are already invested and using Redux!

Use Case: Communicating across states across components!

You will create a separate location for a Global State, and any time you need to query against any state, the Global State will be where you send all queries to.

Redux is a Global State maintainer library that is independent.

What should you put in a global state?

- Things that several components want
  - User names
  - Number of items searched, or generated by user

## Azam's Notes

App.js

```js
import React, { useState } from "react";
import logo from "./logo.svg";
import "./App.css";

/*
class App extends Component {

  constructor() {

    this.state = {
      counter: 0 
    }

    // this.setState({
        counter: this.state.counter + 1 
    })

  }

} */

function App(props) {
  // name of the component

  //1 ) the value that you want to put in state
  // 2) the method/function which will update the state
  // useState(0) means the initial value of the counter
  const [counter, setCounter] = useState(99);

  const incrementCount = () => {
    // increment the state counter
    setCounter(counter + 1);
    console.log(props);
  };

  const decrementCounter = () => {
    setCounter(counter - 1);
  };

  return (
    // this is the render function
    <div>
      <h1>{counter}</h1>
      <button onClick={() => incrementCount()}>Increment</button>
      <button onClick={() => decrementCounter()}>Decrement</button>
    </div>
  );
}

export default App;
```

index.js

```js
import React from "react";
import ReactDOM from "react-dom";
import "./index.css";
import App from "./App";
import PostList from "./PostList";
import * as serviceWorker from "./serviceWorker";

ReactDOM.render(<PostList />, document.getElementById("root"));

// If you want your app to work offline and load faster, you can change
// unregister() to register() below. Note this comes with some pitfalls.
// Learn more about service workers: https://bit.ly/CRA-PWA
serviceWorker.unregister();
```

PostList.js

```js
import React, { useState, useEffect } from "react";
import logo from "./logo.svg";

function PostList() {
  // name of the component

  const [posts, setPosts] = useState([]);
  const [counter, setCounter] = useState(0);

  const fetchPosts = () => {
    // load the data
    fetch("https://jsonplaceholder.typicode.com/posts")
      .then(response => response.json())
      .then(json => {
        setPosts(json);
      });
  };

  // similar to componentDidMount
  useEffect(() => {
    fetchPosts();
  });

  return (
    <div>
      {posts.map(post => {
        return <div>{post.title}</div>;
      })}
    </div>
  );
}

export default PostList;
```
