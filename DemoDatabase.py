import sqlite3
import os

def run():
    f = open(r'C:\3d-Model\bin\curr_proj.txt','r')
    pathDir = f.readline()
    f.close()
    os.chdir(pathDir)
    paths = pathDir.split('\\')
    index=len(paths)-1
    projName = paths[index] + '.db'
    conn= sqlite3.connect(projName)
     
    cursor = conn.cursor()

    cursor.execute('''CREATE TABLE information
                 (name text, latitude text, longitude text, altitude real)''')




          
