## Redux Day 3

Side note - when you're using functions you do not have to declare the render method!

## Steps to Set Up React/Redux Connections

* import react and redux via npm
* go to index.js
* `import { createStore } from 'redux'`
* `const store = createStore(reducer)`
* create store folder, create reducers folder, create reducer.js
* `const reducer = (state, action) => { return store }`
* `export default reducer`
* go to index.js
* `import reducer from './store/reducers/reducer'`
* `import { Provider } from 'react-redux'`
* inside of the ReactDOM.render place the Provider
* When you try and run it in the browser and see the Redux dev tools, it will tell you to follow the instructions
  * click the link
  * for a basic store add the following code
    * `const store = createStore(reducer, + window.__REDUX_DEVTOOLS_EXTENSION__ && window.__REDUX_DEVTOOLS_EXTENSION__());`
* inside of the counter.js
  * Import the connect ability `import { connect } from 'react-redux'`
  * Export the connect on the bottom `export default connect()(Counter)`
  * Add the mapDispatchToProps function!
    * `const mapDispatchToProps = (dispatch) => { return { onIncrementCounter: () => dispatch({ type: 'INC_COUNTER' })}}`
    * put this is the first argument in the connect
    * add the dispatch from props to the button click
    * `<button onClick()> 
* Add a switch to the reducer!
  * A good use case for a switch is when you know exactly what the input cases are going to be.
    * Compass
    * Game Character Movement Directions
  * Switch works similarly to if/else statements

```js
switch(action.type) {
    case 'INC_COUNTER':
        return {
            ...state,
            counter: state.counter + 1
        }
}
```

* Adding the state to a component - DisplayCounter.js
* import connect
* export connect()() on the bottom
* const mapStateToProps
  * add to connect
  * return ctr: state.counter
  * now you can use this in the return as {props.ctr}