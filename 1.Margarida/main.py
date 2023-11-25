import connection
import saveToCsv

#OPEN CSV
saveToCsv.init()

#START RECIEVING MESSAGES
connection.run()

#CLOSE CSV
saveToCsv.close()