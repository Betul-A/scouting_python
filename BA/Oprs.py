import mysql.connector as mariaDB
import tbapy
import string
tba = tbapy.TBA('Tfr7kbOvWrw0kpnVp5OjeY780ANkzVMyQBZ23xiITUkFo9hWqzOuZVlL3Uy6mLrz')
x = 195
team = tba.team(x)
event = '2019cur'  # This is the key for the event

def sortbyteam(d):
    return d.get('team_number', None)


conn = mariaDB.connect(user='admin',
                       passwd='Einstein195',
                       host='frcteam195.cmdlvflptajw.us-east-1.rds.amazonaws.com',
                       database='team195_scouting')
cursor = conn.cursor()
eventTeams = tba.event_teams(event)
eventOpr = tba.event_oprs(event).get("oprs")
eventoprSorted = [(k[3:], eventOpr[k]) for k in sorted(eventOpr, key=eventOpr.get, reverse=True)]
print(eventoprSorted)

for team in eventoprSorted:
    query = "INSERT INTO BlueAllianceOPR (Team, OPR) VALUES " + "('" + str(team[0]) + "', '" + \
            str(team[1]) + "');"
    cursor.execute(query)
    conn.commit()
