import mysql.connector


class mySQLServer: 

    def __init__(self):
        self.cnx = mysql.connector.connect(user='root', password='Rocco99mascota!',
                              host='127.0.0.1',
                              database='matches')

    def setData(self, table, data):

        cursor = self.cnx.cursor(buffered=True)

        for match in data:
            #Gets the index of the latest element on the table so that the new entry will have a unique id.
            sqlCode = 'SELECT * FROM ' + table + " WHERE match_id = (SELECT max(match_id) FROM " + table + ")"
            cursor.execute(sqlCode)
            self.cnx.commit()
            for row in cursor:
                index = row
            i = index[0] + 1
            #Checks if match is already in the database. If it isn't, it places it in the database
            sqlCode = 'SELECT * FROM ' + table + " WHERE match_name = '" + match['score'] + "' AND competition = '" + match['competition'] + "' AND date_match = '" + match['date'] + "'"
            cursor.execute(sqlCode)
            self.cnx.commit()

            if cursor.rowcount == 0:
                sqlCode = 'INSERT INTO ' + table + " VALUES(" + str(i) + ",'" + match['score'] + "','" + match['competition'] + "','" + match['date'] + "')" 
                cursor.execute(sqlCode)  
                self.cnx.commit() 

    


