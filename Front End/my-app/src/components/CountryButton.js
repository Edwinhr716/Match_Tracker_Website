import React from 'react'

const CountryButton = ({image, onClick, country}) => {

    var modalButton = {
        backgroundImage : 'url(' + image + ')', 
        backgroundPosition : 'center',
        backgroundSize : 'cover'
    }


   
    

    return (
       <button className = "btn" style={modalButton} onClick={()=> onClick(country)} >Test</button>
    )
}



export default CountryButton