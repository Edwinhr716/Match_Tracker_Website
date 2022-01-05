import React from 'react'
import CountryButton from './CountryButton'

const Sidepanel = ({onClick}) => {
    return (
        <div className = "sidePanel">
            <CountryButton image='https://upload.wikimedia.org/wikipedia/commons/thumb/e/ec/Flag_of_Guatemala.svg/510px-Flag_of_Guatemala.svg.png' onClick={onClick} country="Guatemala" />
            <CountryButton image='https://upload.wikimedia.org/wikipedia/commons/thumb/c/c7/Flag_of_Honduras_%283-2%29.svg/750px-Flag_of_Honduras_%283-2%29.svg.png' onClick={onClick} country = "Honduras" />
            <CountryButton image = 'https://www.si.com/.image/t_share/MTY4MDI4OTI4OTg0NTU2ODE3/austin-fc-logojpg.jpg' onClick={onClick} country = "Austin FC" />
        </div>
    )
}


export default Sidepanel
