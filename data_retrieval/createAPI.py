from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import SQL_Connection


sqlConnection = SQL_Connection.mySQLServer()


app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/get-matches/{item_id}")
def home(item_id):
    return sqlConnection.getMatches(item_id)

@app.get("/get-matches/{item_id}/excluding={competition}")
def exclude(item_id, competition):
    return sqlConnection.getMatchesExcludeCompetition(competition, item_id)

@app.get("/get-matches/{item_id}/from={competition}")
def include(item_id, competition):
    return sqlConnection.getMatchesfromCompetition(competition, item_id)
