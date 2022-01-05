import React from 'react'
import AboutButton from './AboutButton'

const Header = ({onClick}) => {
    return (
        <header>
            <h1 className = "Title">Match Tracker</h1>
            <AboutButton onClick={onClick}/>
        </header>
    )
}

export default Header
