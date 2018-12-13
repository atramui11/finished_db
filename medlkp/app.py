from flask import Flask, render_template, request, Response
import webbrowser
import json
import sqlite3
import socket
from collections import Counter

minage = []
maxage = []
gender = []
paap = []

app = Flask(__name__)

chrome_path = 'open -a /Applications/Google\ Chrome.app %s'

@app.route('/')
def home():
    return render_template('index.html')


@app.route('/receiver1', methods=['GET', 'POST'])
def receiver1():
    temp = request.get_json(force=True)
    temp = format(temp)
    minage.append(temp)
    return "minage"

@app.route('/receiver2', methods=['GET', 'POST'])
def receiver2():
    temp = request.get_json(force=True)
    temp = format(temp)
    maxage.append(temp)
    return "maxage"

@app.route('/receiver3', methods=['GET', 'POST'])
def receiver3():
    temp = request.get_json(force=True)
    temp = format(temp)
    gender.append(temp)
    return "gender"


@app.route('/receiver4', methods=['GET', 'POST'])
def receiver4():
    temp = request.get_json(force=True)
    temp = format(temp)
    paap.append(temp)
    
    #OPEN AND LOOK UP DB  
    # importing the module 
    import sqlite3 

    # connect withe the myTable database    
    connection = sqlite3.connect("medDBFINAL.db3") 

    # cursor object 
    crsr = connection.cursor()  

    locMin = int(minage.pop())
    locMax = int(maxage.pop())
    locGen = gender.pop()
    locGen = locGen.upper()
    locPap = paap.pop()
    locPap = locPap.upper()
    print("'%s', '%s','%d', '%d'" % (locGen, locPap, locMin, locMax))
    
	#new query with two tables
    crsr.execute("SELECT FindingLabels FROM Data_Entry_2017, patientinfo WHERE Data_Entry_2017.PatientID=patientinfo.PatientID AND Data_Entry_2017.ViewPosition='{0}' AND Data_Entry_2017.PatientAge BETWEEN '{1}' AND '{2}' AND patientinfo.PatientGender='{3}';".format(locPap, locMin, locMax, locGen))
	
    ans= crsr.fetchall()  
    
    print("ans after crsr exex is: \n\n")

    listResults = []

    for i,a in enumerate(ans):
        listResults.append(str(ans[i][0]))

    finalResults = ""

    counted = Counter(listResults)
    for diagnosis,count in counted.most_common(30):
        finalResults += diagnosis + " : " + str(count) + "\n"

    print finalResults

    return finalResults

if __name__ == '__main__':
    url = 'http://127.0.0.1:5000/'
    webbrowser.open_new(url)
    app.run(debug=True)
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
