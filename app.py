from flask import Flask, render_template, jsonify
import requests 

app = Flask(__name__)

F1_STANDINGS_URL = "https://api.jolpi.ca/ergast/f1/current/driverstandings.json"

@app.route('/')
def index(): 
    #HTML page 
    return render_template('index.html')

@app.route('/api/standings')
def get_standings(): 
    try:
        response = requests.get(F1_STANDINGS_URL, timeout=10)
        response.raise_for_status() 
        data = response.json() 
        
        
        standings_list = data['MRData']['StandingsTable']['StandingsLists'][0]['DriverStandings']
        return jsonify(standings_list)
    except Exception as e: 
        return jsonify({"error": "Αποτυχία αντλησης δεδομένων F1", "details": str(e)}), 500
    

if __name__ == "__main__":
    #Execute
    app.run(debug=True, port=5000)


