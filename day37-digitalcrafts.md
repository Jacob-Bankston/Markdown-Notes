# Redux Day 2

> My forearm has started to hurt on the underside of my arm, so I am trying to limit the amount of excess typing that I will be doing.
> 
> Sorry if the notes are not as dense, but I will still work on creating good markdown content!

local state - state that only pertains to that particular component

useState and useEffect - using hooks to get the information, the set up is a lot more readable and simple.

`import React, { useState } from 'react'`
`const [counter, setCounter] = useState(0)`

Example for today was with a blue and red counter, but because they are using local state, the counter for each component are separate. We need to add Redux to have them work with each other, OR have a lot of links via props and children.

## Redux Diagram

The redux diagram is super important, memorize the Redux Diagram!

![Redux diagram](redux.png)!

## Implementing Redux


* `npm install redux`
* `npm install react-redux`
* Create Store Folder
* Add the reducer
  * reducer.js
    * create the initialState
* Place Store in index.js
  * import Provider from 'react-redux'
* Add the `<Provider store = {store}>` in the ReactDOM.render
  * You can have multiple stores, but we're not diving into that complexity in class
* `import { connect } from 'react-redux'`
  * connect is a function that will connect the component to the global state.
* `export default connect()(RedCounter);`
* Add in the mapStateToProps
  * `const mapStateToProps = (state) => { return ( ctr: state.counter ) }`
  * You are mapping the global state to the properties
  * Then you have to pass the first argument of the connect as mapStateToProps
  * `export default connect(mapStateToProps)(RedCounter);`
* Now you can access the global state in the properties for the component!
  * `{props.ctr}`
* Add in the mapDispatchToProps
  * `const mapDispatchToProps = (dispatch) => { return { onIncrement: () => dispatch({ type: 'INC_COUNTER' })}}
  * `export default connect(mapStateToProps, mapDispatchToProps)(RedCounter);`