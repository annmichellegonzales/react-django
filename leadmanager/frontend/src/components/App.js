import React, { Component } from 'react'
import ReactDOM from 'react'

import Header from './layout/Header'

class Apps extends Component {
    render() {
        return (
            <Header />
        )
    }
}

ReactDOM.render(<App />, document.getElementById('app'));