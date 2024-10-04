import os
from flask import Flask, Request, Response, json
from flask_sqlalchemy import SQLAlchemy
import pymysql
from dotenv import load_dotenv

load_dotenv()
port = int(os.getenv('port', 12951))

db = pymysql.connect(
    host=os.getenv('host'), 
    port=port,  
    user=os.getenv('user'),  
    password=os.getenv('password'), 
    database=os.getenv('database')
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
    # app.run(debug=True)
    app.run(host='0.0.0.0', port=5000)