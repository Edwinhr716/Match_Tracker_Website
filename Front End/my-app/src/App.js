import Header from './components/Header'
import Sidepanel from './components/Sidepanel'
import MainPage from './components/MainPage'
import { useState, useEffect, useLayoutEffect } from 'react'

function App() {
  const [allData, setData] = useState(null)
  const [currentData, setCurrentData] = useState(null)



  useEffect(()=>{
    console.log("got here")
      const getData = async() =>{
      const dataFromServer  = await fetchData()
      setData(dataFromServer[0])
      setCurrentData(dataFromServer)
      }  
      getData()
      //setReadyForRender(true)
    }, [])

    const fetchData = async () => {
      let data = new Array()

      let res = await fetch('http://127.0.0.1:8000/get-matches/austin_fc')
      let specificTeam = {
        id : 'austinfc',
        data : await res.json()
      }
      data.push(specificTeam)

      res = await fetch('http://127.0.0.1:8000/get-matches/guatemala')
      specificTeam = {
        id : 'guatemala',
        data : await res.json()
      }
      data.push(specificTeam)

      res = await fetch('http://127.0.0.1:8000/get-matches/honduras')
      specificTeam = {
        id : 'honduras',
        data : await res.json()
      }
      data.push(specificTeam)

      let defaultData = new Array();
      let defaultMessage = "This website was made with ReactJS. Data is taken from https://www.livesoccertv.com. Code for both the backend and the front end is in this Github page https://github.com/Edwinhr716. The API was also created by me"
      defaultData.push(defaultMessage)
      specificTeam = {
        id : 'about',
        data : defaultData
      }

      data.push(specificTeam)
      return data; 
    }

    function onClick(country){
      console.log(currentData)
        switch(country){
          case "Guatemala":
              setData(currentData[1])
              console.log(allData)
            break;
          case "Honduras":
              setData(currentData[2])
              console.log(allData)
            break
          case "Austin FC":
              setData(currentData[0])
              console.log(allData)
            break
          case "about":
              setData(currentData[3])
              console.log(allData)
            break
        }
    }

    return (
      <div className="container">
        <Header onClick={onClick} information={allData}/>
        <div className ="mainLayout">
          <Sidepanel onClick = {onClick} />
          <MainPage information={allData}/>
        </div>
      </div>
    );
}

export default App;
