from flask import Flask, request, render_template,redirect,url_for
import pymongo 

app = Flask(__name__) 

# root route 
@app.route("/") 
def hello_world(): 
    return render_template('form.html')

# Set up MongoDB connection and collection 
client = pymongo.MongoClient("mongodb+srv://abhi:abhi@cluster0.12iulno.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0") 

# Create database named form_data if they don't exist already 
db = client['pwskills'] 

# Create collection named data if it doesn't exist already 
collection = db['data']

# Add data to MongoDB route 
@app.route('/add_data', methods=['POST']) 
def add_data(): 
    # Get data from request 
    data = dict(request.form) 
    print(data)
    # Insert data into MongoDB 
    collection.insert_one(data) 

    return "Data Submitted Successfully"

if __name__ == '__main__': 
    app.run(host="0.0.0.0")