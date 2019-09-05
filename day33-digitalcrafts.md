# React Day 2!

Everything in a return statement needs to be wrapped in a bigger div!

## Concat

```js
// Stepper.js

// this is making a new array!
incrementCount = () => {
    this.setState({
        counter: this.state.counter + 1,
        // Let's add a history of what states we had in the counter!
        counterHistory: this.state.counterHistory.concat
        (this.state.counter + 1)
    })
}
    // in react you should always make a new object, new array, new everything!

render() {

    let counterHistoryItems = this.state.counterHistory.map(history => {
        return <div>{history}</div>
    })

    return <div>
            <button onClick={this.decrementCount}>-</button>
            {this.state.counter}
            <button onClick={this.decrementCount}>-</button>
            {counterHistoryItems}
            </div>

}
```

Right now the state is contain inside the Stepper.js file, but it is not included in the parent file.

```js
import React from 'react'
import Stepper from './Stepper'

class App extends Component {
    constructor(props) {
        super(props)
        this.state = {
            counter: 0
        }
    }
    handleIncrement = (ctr) => {
        console.log('handleIncrement', ctr)
        this.setState({
            counter: ctr
        })
    }
    render() {
        // adding the function into the props of the Stepper declaration
        return  <div>
                    <h1>{this.state.counter}</h1>
                    <Stepper onIncrement={this.handleIncrement} />
                </div>
    }
}
```

```js
// Stepper.js

incrementCount = () => {
    this.setState({
        counter: this.state.counter + 1,
        counterHistory: this.state.counterHistory.concat
        (this.state.counter + 1)
    }, () => {
        // calling the onIncrement property!
        // you have to wrap this inside it's own anonymous function otherwise it won't wait for the setState to fire
        // completion function fired when the state has been updated successfully
        // this is a callback, not a promise
        this.props.onIncrement()
    })
}
render() {
    let counterHistoryItems = this.state.counterHistory.map(history => {
        return <div>{history}</div>
    })
    return <div>
            <button onClick={this.decrementCount}>-</button>
            {this.state.counter}
            <button onClick={this.decrementCount}>-</button>
            {counterHistoryItems}
            </div>
}
```

Let's add a new component!

```js
//InputName.js
import React, {Component} from 'react'

class InputName extends Component {

    constructor() {
        super()
        this.state = {
            name: ''
        }
    }

    // adding in the function to know what is in .this on our input
    handleNameTextBoxChange = (e) => {
        console.log(e.target.value)
        this.setState({
            name: e.target.value
        })
    }
    render() {
        // using the onChange React event (Synthetic Event) for the input
        return  <div>
                    <hr />
                    <input type="text" onChange={this.handleNameTextBoxChange} />
                    <button>Submit</button>
                    <hr />
                </div>
    }
}
export default InputName
```

```js
//InputName.js
import React, {Component} from 'react'

class InputName extends Component {

    constructor() {
        super()
        this.state = {
            name: '',
            address: ''
        }
    }

    // adding in the function to know what is in .this on our input
    handleTextBoxChange = (e) => {
        this.setState({
            // the target.name refers to the name attribute on the input types
            [e.target.name] : e.target.value
        })
    }

    handleSubmit = () => {
        this.props.onSubmit(this.state.name, this.state.address)
    }

    render() {
        // using the onChange React event (Synthetic Event) for the input
        return  <div>
                    <hr />
                    <input name="name" type="text" onChange={this.handleTextBoxChange} />
                    <input name="address" type="text" placeholder="Enter address" onChange={this.handleTextBoxChange} />
                    <button onClick={this.handleOnClick}>Submit</button>
                    <hr />
                </div>
    }
}
export default InputName
```

```js
// linking the props to the parent from the child

// add to constructor name
this.name = ''
this.address = ''

// add to App
handleSubmit = (name, address) => {
    this.setState({
        name: name,
        address: address
    })
}

// add to return
<InputName onSubmit = {this.handleSubmit} />
```

Reading: React Component Life Cycle!
- constructor()
  - The best place to initialize state
- static getDerivedStateFromProps()
- render()
- componentDidMount()

## Late Review of Assignment

`mkdir server`
`npx create-react-app client`
`cd server`
`npm init`

Client will be your React Project
Server will be your Node.js Project

They are in separate folders, but will have a common parent named Book Barn

Server
`npm install express`
`npm install cors`

Create app.js

*Server app.js*
```js
// simple server!
const express = require('express')
const app = express()
const cors = require('cors')

app.use(cors()) // enable cors

app.get('/books', (req, res) => {
    let books = [
        {title: "Book1"},
        {title: "Book2"}
    ]

    res.json(books)
})

app.post('/books', (req, res) => {
    let title = req.body.title
    books.push({title: title})

})

app.listen(5000, () => {
    console.log("Server is running...")
})
```

Go to app.js in React!

`yarn start`

*Client app.js*
```js
import React, {Component} from 'react';
import './App.css';

class App extends Component {

    constructor(props) {
        super(props)
        this.state = {
            books: []
        }

        this.fetchBooks()
    }

    fetchBooks = () => {

        // http://localhost:5000/books
        fetch("http://localhost:5000/books")
        .then(response => response.json())
        .then(json => {
            this.setState({
                books: json
            })
        })
        // the best way to check if this is correctly tying into the server is to check the chrome developer tools
    }
    render() {

        let bookItems = this.state.books.map(book => {
            return <div>{book.title}</div>
        })

        return  <div>
                    <AddBook />
                    <BookList books = {this.state.books} />
                </div>
    }
}
```

*AddBook.js*
```js
import React, {Component} from 'react';

class AddBook extends Component {

    constructor(props) {
        super(props)
        this.state = {
            title: ''
        }
    }

    handleSave = () => {
        // value is in the state
        fetch('http://localhost:5000/books', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({
                title: this.state.title
            })
        })
    }

    handleTextBoxChange = (e) => {
        this.setState({

        })
    }

    render() {
        return  <div>
                    <input type="text" name="title" onChange={this.handleTextBoxChange} />
                    <button>Save</button>
                </div>
    }
}

export default AddBook
```