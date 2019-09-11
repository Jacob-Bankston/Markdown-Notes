## Redux Day 3

Side note - when you're using functions you do not have to declare the render method!

## Steps to Set Up React/Redux Connections

- import react and redux via npm
- go to index.js
- `import { createStore } from 'redux'`
- `const store = createStore(reducer)`
- create store folder, create reducers folder, create reducer.js
- `const reducer = (state, action) => { return store }`
- `export default reducer`
- go to index.js
- `import reducer from './store/reducers/reducer'`
- `import { Provider } from 'react-redux'`
- inside of the ReactDOM.render place the Provider
- When you try and run it in the browser and see the Redux dev tools, it will tell you to follow the instructions
  - click the link
  - for a basic store add the following code
    - `const store = createStore(reducer, + window.__REDUX_DEVTOOLS_EXTENSION__ && window.__REDUX_DEVTOOLS_EXTENSION__());`
- inside of the counter.js
  - Import the connect ability `import { connect } from 'react-redux'`
  - Export the connect on the bottom `export default connect()(Counter)`
  - Add the mapDispatchToProps function!
    - `const mapDispatchToProps = (dispatch) => { return { onIncrementCounter: () => dispatch({ type: 'INC_COUNTER' })}}`
    - put this is the first argument in the connect
    - add the dispatch from props to the button click
    - `<button onClick()>
- Add a switch to the reducer!
  - A good use case for a switch is when you know exactly what the input cases are going to be.
    - Compass
    - Game Character Movement Directions
  - Switch works similarly to if/else statements

```js
switch (action.type) {
  case "INC_COUNTER":
    return {
      ...state,
      counter: state.counter + 1
    };
}
```

- Adding the state to a component - DisplayCounter.js
- import connect
- export connect()() on the bottom
- const mapStateToProps
  - add to connect
  - return ctr: state.counter
  - now you can use this in the return as {props.ctr}

In order to use local state you need to import useState from React!

```js
import React, { useState } from "react";

const [taskName, taskSet] = useState("");
```

You create a global state in redux!

## Hooks steps

- import useState
  - gives the local state to a variable
- import useEffect
- create a function to handle changes and assign the target to a value
- create a useState to hold that value
- create a function to update the useState
- create a global state to hold the information
- send the hooked state into the dispatch to update the global state

When you're updating a list in the state, you want to use concat, not push. concat will create a new array.

```js
case 'TASK_ADDED':
    return {
        ...state,
        tasks: state.tasks.concat(action.payload)
    }
```

When your reducer ends up being complicated, you can make multiple reducers to handle one job.

They will all compile to one single reducer.

## Implementing Multiple Reducers

Folders

- store
  - actions
  - reducers

#### Action Types

- create actionTypes.js to create constants for the action types
- `import * as actionTypes from '../store/actions/actionTypes'`
- Why: in the future if you need to change these actions then you have one location to change it.

#### Action Creators

- create actionCreators.js to replace the middle portion of the dispatch.
- import the actionTypes!
  - `import \* as actionTypes from './actionTypes'
- `export const incrementCounter = () => { return { type: actionTypes.INC_COUNTER } }`
- This will change your dispatch call into the following
  - dispatch(actionCreators.incrementCounter())

**Payload** is a non-official, community accepted (de facto) naming convention for the property that holds the actual data in a Redux action object.

#### Combining Reducers

- import { createStore, combineReducers } from 'redux';
- import counterReducer from './store/reducers/counter'
- import tasksReducer from './store/reducers/tasks'
- add a root reducer

```js
const rootReducer = combineReducers({
  ctrRed: counterReducer,
  tasksRed: taskReducer
});
```

- Then you pass the root reducer to the store instead of just reducer!
- Now when you map state to props you would list `tasks: state.tasksRed.tasks`
  - `state.reducername.globalstate`
- You implement props like this now!
  - `{props.tasks.map((task) => { return <div>{task}</div> })}`

## Azam's Notes
