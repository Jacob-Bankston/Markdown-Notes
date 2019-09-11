# Redux Day 1

Introducing a global state!

## Why

In order to pass around a state you need to pass information up through parents, then down through properties in multiple layers throughout the application depending on what information that you need to pass around. If you store this information in a global state, then you do not have to worry about the flow going up and around the application, or potentially missing one of the steps in the communication process.

## Central Store

The only person that can update the global state is the Reducer

- Receives actions
- Updates state (pure, sync functions, no side-effects!)
- Can be multiple combined Reducers
- You must have a reducer if you want to interact with the global store

## Flow

- The Central Store keeps all of the information of states
- The Store has subscriptions to your components
- Your components dispatch an action to the reducer
- Your reducer dispatches updates to the Central Store which then updates the subscriptions.

This loop keeps everything up to date that has been set up within the components.

## Installation

`npm init`
`npm install redux`

Note: Redux is a standalone library, so you do not need to add in React if you do not want to.

redux-basics.js

```js
// import redux and other imports

// create initial state

// reducer

// store

// dispatch actions

// subscriptions
```

```js
const redux = require("redux");
const createStore = redux.createStore;

// store

// reducer

// dispatch actions

// subscriptions
```

```js
// store
const store = createStore( // pass the reducer

```

```js
// reducer
// if state is undefined then choose the initialState
// else if state is not undefined then just return state
const reducer = (state, action) => {
  // return the updated state
  return state;
};

// this is just the bare bones to barely fulfill the requirements of the reducer
```

```js
// store
const store = createStore(reducer); // now the store is set up!
console.log(store.getState()); // finds out what's in the state! Probably won't use this function in React
```

`console.log(store.getState())` comes up as undefined because we did not declare the state initially!

```js
// create initial state
const initialState = {
  counter: 0
};
```

Application so far!

```js
const redux = require("redux");
const createStore = redux.createStore;

// create initial state
const initialState = {
  counter: 0
};

// reducer
const reducer = (state, action) => {
  return state;
};

// store
const store = createStore(reducer);

// dispatch actions

// subscriptions
```

```js
// dispatch actions
store.dispatch({ type: "INC_COUNTER" });
```

```js
const reducer = (state = initialState, action) => {
  console.log(action.type); // checking to see if we can find the action.types
  return state;
};
```

```js
const redux = require("redux");
const createStore = redux.createStore;

// create initial state
const initialState = {
  counter: 0
};

// reducer
const reducer = (state, action) => {
  console.log(action.type);
  if (action.type == "INC_COUNTER") {
    // update the counter global state
    return {
      ...state, // the spread operator will copy the values of the old values from the state, and put it in the new object
      counter: state.counter + 1
    };
  }

  return state; // in overall code, this is kept to set the initial state while no actions have taken place
};

// store
const store = createStore(reducer);

// dispatch actions
store.dispatch({ type: "INC_COUNTER" });

// subscriptions
```

### Spread Example - ES6 JavaScript Feature

```js
let obj1 = { name: "John", age: 34 };

// when we have to update it we can hard code it like this
let obj2 = { name: obj1.name, age: obj1.age, address: "Richmond Ave" };

// or we can use the spread operator like this!
let obj2 = { ...obj1, address: "Richmond Ave" };

// this saves you a lot of time to update or add new things to objects!
```

Back to the main application!

```js
const redux = require("redux");
const createStore = redux.createStore;

// create initial state
const initialState = {
  counter: 0
};

// reducer
const reducer = (state, action) => {
  console.log(action.type);

  if (action.type == "INC_COUNTER") {
    // update the counter global state
    return {
      ...state, // gives you the old state, and updates with the new updated state!
      counter: state.counter + 1
    };
  }

  return state;
};

// store
const store = createStore(reducer);

// dispatch actions
store.dispatch({ type: "INC_COUNTER" });

// subscriptions
```

```js
const redux = require("redux");
const createStore = redux.createStore;

// create initial state
const initialState = {
  counter: 0
};

// reducer
const reducer = (state, action) => {
  console.log(action.type);

  if (action.type == "INC_COUNTER") {
    return {
      ...state,
      counter: state.counter + 1
    };
  } else if (action.type == "ADD_COUNTER") {
    // increment the counter by value
  }

  return state;
};

// store
const store = createStore(reducer);

// dispatch actions
store.dispatch({ type: "INC_COUNTER" });
// increment counter by a certain value
store.dispatch({ type: "ADD_COUNTER", count: 100, something: 9 }); // the only property that is required is type
// all of the other properties can be whatever you want!
// you can pass in objects in the properties and more!

// subscriptions
```

You only want to update the state in small slices. Slice is an important term to remember!

```js
const redux = require("redux");
const createStore = redux.createStore;

// create initial state
const initialState = {
  counter: 0
};

// reducer
const reducer = (state, action) => {
  console.log(action.type);

  if (action.type == "INC_COUNTER") {
    return {
      ...state,
      counter: state.counter + 1
    };
  } else if (action.type == 'ADD_COUNTER') {
      ...state,
      counter: state.counter + action.value
  }

  return state;
};

// store
const store = createStore(reducer);

// dispatch actions
store.dispatch({ type: "INC_COUNTER" });
console.log(store.getState())
store.dispatch({type: 'ADD_COUNTER', value: 100})
console.log(store.getState())


// subscriptions
```

A lot of examples use `switch` instead of using the if, else if statements to simplify the amount of code that you're using.

The final portion of the change is the subscriptions!

```js
// subscription
store.subscribe(() => {
  console.log("Subscription Fired");
});
```

When you are setting a subscription it is asking you to let it know whenever something gets changes.

Note: You want this to be above the dispatches so it is able to pull the information from the updates. It would be like subscribing to something after they have launched something, so you will not get any notifications.

```js
const redux = require("redux");
const createStore = redux.createStore;

// create initial state
const initialState = {
  counter: 0
};

// reducer
const reducer = (state, action) => {
  console.log(action.type);

  if (action.type == "INC_COUNTER") {
    return {
      ...state,
      counter: state.counter + 1
    };
  } else if (action.type == 'ADD_COUNTER') {
      ...state,
      counter: state.counter + action.value
  }

  return state;
};

// store
const store = createStore(reducer);

// subscription
store.subscribe(() => {
    console.log('Subscription Fired')
})

// dispatch actions
store.dispatch({ type: "INC_COUNTER" });
console.log(store.getState())
store.dispatch({type: 'ADD_COUNTER', value: 100})
console.log(store.getState())
```

Assignment - Repeat this process of dispatching, implementing and setting up the reducer at least 3 times.

- Create a node project
- Go through the process of the loop
- Make sure that you understand and know what's going on in the process loop.

## Azam's Notes

```js
/*
let obj1 = {
    name: 'John', 
    age: 34
}

let obj2 = {...obj1, address: 'Richmond Ave'}
*/

/*
this.state = {
    counter: 0 
} */

const redux = require("redux");
const createStore = redux.createStore;

// create initial state
const initialState = {
  counter: 0,
  isLoggedIn: false
};

/*
function orderIcecream(flavor = "vanilla") {

}
orderIcecream("coffee") 
*/

// reducer
// if state is undefined then choose the initialState
// else if state is not undefined then just return state
const reducer = (state = initialState, action) => {
  console.log(action.type);
  if (action.type == "INC_COUNTER") {
    // update the counter global state
    // and returning the updated state
    return {
      ...state, // copy the old state
      counter: state.counter + 1
    };
  } else if (action.type == "ADD_COUNTER") {
    // increment the counter by value
    return {
      ...state, // copy the old state
      counter: state.counter + action.value
    };
  }
  // return the initial state
  return state;
};

// store
const store = createStore(reducer);
console.log(store.getState());

// subscription
store.subscribe(() => {
  console.log("Subscription Fired");
});

// dispatch actions
store.dispatch({ type: "INC_COUNTER" });
console.log(store.getState());

// increment counter by certain value
store.dispatch({ type: "ADD_COUNTER", value: 100 });
console.log(store.getState());
```