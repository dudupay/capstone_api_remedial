################ Trips ################

from flask import Flask, request
import sqlite3
import requests
from tqdm import tqdm
import json 
import numpy as np
import pandas as pd

app = Flask(__name__) 

@app.route('/')
@app.route('/homepage')
def home():
    return 'Hello World'

@app.route('/trips/')
def route_all_trips():
    conn = make_connection()
    trips = get_all_trips(conn)
    return trips.to_json()

@app.route('/trips/<id>') # rute dinamis
def route_id(id):
    conn = make_connection()
    trips = get_id(id, conn)
    return trips.to_json()

@app.route('/trips/add', methods=['POST']) 
def route_add_trips():
    # parse and transform incoming data into a tuple as we need 
    data = pd.Series(eval(request.get_json(force=True)))
    data = tuple(data.fillna('').values)
    
    conn = make_connection()
    result = insert_into_trips(data, conn)
    return result

@app.route('/json', methods=['POST']) 
def json_example():
    
    req = request.get_json(force=True) # Parse the incoming json data as Dictionary
    
    name = req['name']
    age = req['age']
    address = req['address']
    
    return (f'''Hello {name}, your age is {age}, and your address in {address}
            ''')


################ Functions ################

def get_all_trips(conn):
    query = f"""SELECT * FROM trips"""
    result = pd.read_sql_query(query, conn)
    return result

def get_id(id, conn):
    query = f"""SELECT * FROM trips WHERE id = {id}"""
    result = pd.read_sql_query(query, conn)
    return result 

def make_connection():
    connection = sqlite3.connect('austin_bikeshare.db')
    return connection

def insert_into_trips(data, conn):
    query = f"""INSERT INTO trips values  {data}"""
    try:
        conn.execute(query)
    except:
        return 'Error'
    conn.commit()
    return 'OK'

if __name__ == '__main__':
    app.run(debug=True, port=5000)

################ Static and Dynamic Endpoints and Handling JSON ################

from flask import Flask, request
import sqlite3
import requests
from tqdm import tqdm
import json 
import numpy as np
import pandas as pd

app = Flask(__name__) 

# example of analytical static endpoint
@app.route('/trips/average_duration')
def route_all_trips_average_duration ():
    conn = make_connection()
    trips_average_duration = get_all_trips_average_duration(conn)
    return trips_average_duration.to_json()

@app.route('/trips/average_duration/<duration_minutes>') #rute dinamis
def route_duration_minutes(duration_minutes):
    conn = make_connection()
    trips_average_duration = get_duration_minutes(duration_minutes, conn)
    return trips_average_duration.to_json()

@app.route('/trips/add', methods=['POST']) 
def route_add_trips():
    # parse and transform incoming data into a tuple as we need 
    data = pd.Series(eval(request.get_json(force=True)))
    data = tuple(data.fillna('').values)
    
    conn = make_connection()
    result = insert_into_trips(data, conn)
    return result

@app.route('/json', methods=['POST']) 
def json_example():
    
    req = request.get_json(force=True) # Parse the incoming json data as Dictionary
    
    id = req['id']
    bikeid = req['bikeid']
    duration_minutes = req['duration_minutes']
    
    return (f'''Hello {id}, your bikeid is {bikeid}, and the length of your cycling time is {duration_minutes}
            ''')

################ Functions Static and Dynamic Endpoints and Handling JSON ################

def get_all_trips_average_duration(conn):
    query= f"""SELECT * FROM trips"""
    result = pd.read_sql_query(query, conn)
    return result

def get_duration_minutes(duration_minutes, conn):
    query = f"""SELECT * FROM trips WHERE duration_minutes = {duration_minutes}"""
    result = pd.read_sql_query(query, conn)
    return result

def make_connection():
    connection = sqlite3.connect('austin_bikeshare.db')
    return connection

def insert_into_trips(data, conn):
    query = f"""INSERT INTO trips values {data}"""
    try:
        conn.execute(query)
    except:
        return 'Error'
    conn.commit()
    return 'OK'

if __name__ == '__main__':
    app.run(debug=True, port=5000)

################ Stations ################

from flask import Flask, request
import sqlite3
import requests
from tqdm import tqdm
import json 
import numpy as np
import pandas as pd

app = Flask(__name__) 

@app.route('/')
@app.route('/homepage')
def home():
    return 'Hello World'

@app.route('/stations/')
def route_all_stations():
    conn = make_connection()
    stations = get_all_stations(conn)
    return stations.to_json()

@app.route('/stations/<station_id>') # rute dinamis
def route_station_id(station_id):
    conn = make_connection()
    stations = get_station_id(station_id, conn)
    return stations.to_json()

@app.route('/stations/add', methods=['POST']) 
def route_add_stations():
    # parse and transform incoming data into a tuple as we need 
    data = pd.Series(eval(request.get_json(force=True)))
    data = tuple(data.fillna('').values)
    
    conn = make_connection()
    result = insert_into_stations(data, conn)
    return result

@app.route('/json', methods=['POST']) 
def json_example():
    
    req = request.get_json(force=True) # Parse the incoming json data as Dictionary
    
    name = req['name']
    age = req['age']
    address = req['address']
    
    return (f'''Hello {name}, your age is {age}, and your address in {address}
            ''')


################ Functions ################

def get_all_stations(conn):
    query = f"""SELECT * FROM stations"""
    result = pd.read_sql_query(query, conn)
    return result

def get_station_id(station_id, conn):
    query = f"""SELECT * FROM stations WHERE station_id = {station_id}"""
    result = pd.read_sql_query(query, conn)
    return result 

def make_connection():
    connection = sqlite3.connect('austin_bikeshare.db')
    return connection

def insert_into_stations(data, conn):
    query = f"""INSERT INTO stations values  {data}"""
    try:
        conn.execute(query)
    except:
        return 'Error'
    conn.commit()
    return 'OK'

if __name__ == '__main__':
    app.run(debug=True, port=5000)

################ Static and Dynamic Endpoints and Handling JSON ################

from flask import Flask, request
import sqlite3
import requests
from tqdm import tqdm
import json 
import numpy as np
import pandas as pd

app = Flask(__name__) 

# example of analytical static endpoint
@app.route('/stations/average_council')
def route_all_stations_average_council ():
    conn = make_connection()
    stations_average_council = get_all_stations_average_council(conn)
    return stations_average_council.to_json()

@app.route('/stations/average_council/<council_district>') #rute dinamis
def route_council_district(council_district):
    conn = make_connection()
    stations_average_council = get_council_district(council_district, conn)
    return stations_average_council.to_json()

@app.route('/stations/add', methods=['POST']) 
def route_add_stations():
    # parse and transform incoming data into a tuple as we need 
    data = pd.Series(eval(request.get_json(force=True)))
    data = tuple(data.fillna('').values)
    
    conn = make_connection()
    result = insert_into_stations(data, conn)
    return result

@app.route('/json', methods=['POST']) 
def json_example():
    
    req = request.get_json(force=True) # Parse the incoming json data as Dictionary
    
    station_id = req['station_id']
    name = req['name']
    council_district = req['council_district']
    
    return (f'''Hello {station_id}, your bike is on {name}, and the council district is {council_district}
            ''')

################ Functions Static and Dynamic Endpoints and Handling JSON ################

def get_all_stations_average_council(conn):
    query= f"""SELECT * FROM stations"""
    result = pd.read_sql_query(query, conn)
    return result

def get_council_district(council_district, conn):
    query = f"""SELECT * FROM stations WHERE council_district = {council_district}"""
    result = pd.read_sql_query(query, conn)
    return result

def make_connection():
    connection = sqlite3.connect('austin_bikeshare.db')
    return connection

def insert_into_stations(data, conn):
    query = f"""INSERT INTO stations values {data}"""
    try:
        conn.execute(query)
    except:
        return 'Error'
    conn.commit()
    return 'OK'

if __name__ == '__main__':
    app.run(debug=True, port=5000)




