import React from 'react'

const MainPage  = ({ information }) => {
    if(information === null){
        return (
            <div className = "MainPage">
            </div>

        )
    }

    if(information["id"] === "about"){
        return(
            <div className = "MainPage">
                <h3>{information.data[0]}</h3>
            </div>
        )
    }

    return (

        <div className = "MainPage">
            {information.data.data.map((match) => (
            
                    <div className = "matchLine">
                            <h3 id="Score">{match["score"]}</h3>
                            <h3 id="date">{match["date"]}</h3>
                            <h3 id="competition">{match["competition"]}</h3>
                    </div>
                      
                ) 
            
            )}
        </div>
    )
}


export default MainPage