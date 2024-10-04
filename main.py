from flask import Flask, Request, Response, json
from flask_sqlalchemy import SQLAlchemy
import pymysql

db = pymysql.connect(
    host="localhost",  # or the IP address of the server where your database is hosted
    port=3306,  # default MySQL port
    user="root",  # MySQL username
    password="root",  # MySQL password
    database="pandeyji_eatery"  # The database name
)

cursor = db.cursor()
cursor.execute("SELECT VERSION()")
data = cursor.fetchone()
print(f"Database version: {data}")
app = Flask(__name__)
# app.config['MYSQL_USER'] = 'root'
# app.config['MYSQL_DATABASE'] = 'pandeyji_eatery'
# mysql = MySQL(app)


@app.route('/')
def defaulut_page():
    return {"message":"Hello world"}

@app.route('/')
async def handle_request(request:Request):
    payload=await request.json()
    # Extract the necessary information
    intent=payload['queryResult']['intent']['displayName']
    parameters=payload['quesryResult']['parameters']
    output_contexts=payload['queryResult']['outputContexts']

    if(intent == "track.order"):
        return handle_track_order(parameters)
    return {"message":"in transit"}
 
def handle_track_order():
      return Response(
        json.dumps({"fulfillmentText": "Tracking order for the backend"}),
        mimetype='application/json'
    )

if __name__ == '__main__':
    app.run(debug=True)