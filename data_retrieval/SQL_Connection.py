from fastapi.params import Query
import mysql.connector
#Always returns dictionaries
class mySQLServer:

    def __init__(self):
        self.cnx = mysql.connector.connect(user='root', password='',
                              host='127.0.0.1',
                              database='matches')

    
    def query(self, cursor, sqlCode):
        cursor.execute(sqlCode) 
        self.cnx.commit()
        matchData = {}
        matches = []
        matchData["data"] = matches
        for match in cursor:
            infoMatch = {}
            infoMatch["score"] = match[1]
            infoMatch["competition"] = match[2]
            infoMatch["date"] = match[3]
            matchData["data"].append(infoMatch)
        return matchData

    def getMatches(self, table):
        cursor = self.cnx.cursor(buffered=True)
        sqlCode = "SELECT * FROM " + table
        return self.query(cursor,sqlCode)

    def getMatchesExcludeCompetition(self , competition, table):
        cursor = self.cnx.cursor(buffered=True)
        sqlCode = " SELECT * FROM " + table + " WHERE competition NOT IN (SELECT competition FROM " + table + " WHERE competition = '" + competition +"')"
        return self.query(cursor, sqlCode)
    
    def getMatchesfromCompetition(self, competition, table):
        cursor = self.cnx.cursor(buffered=True)
        sqlCode = "SELECT * FROM " + table + " WHERE competition = '" + competition + "'"
        return self.query(cursor, sqlCode)
