import React from 'react'

const AboutButton = ({onClick}) => {

    return (
        <button className= "aboutButton" onClick={()=>onClick("about")}>About</button>
    )

}



export default AboutButton