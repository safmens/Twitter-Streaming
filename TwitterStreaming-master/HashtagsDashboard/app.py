import html
from flask import Flask,jsonify,request
from flask import render_template
import ast

from pyspark import RDD


import requests

app = Flask(__name__)
global label

label = str
labels = []
values = []



@app.route("/")
def chart1():
    global labels,values
    labels = []
    values = []
    return render_template('home.html', values=values, labels=labels)


@app.route("/top_hashtags")
def chart2():
    global labels,values
    labels = []
    values = []
    return render_template('chart.html', values=values, labels=labels)

@app.route("/search_by_word")
def chart3():
    global labels,values
    labels = []
    values = []
    return render_template('search_by_word.html', values=values, labels=labels)

@app.route("/dashboard")
def chart4():



    global labels1,values1
    labels1 = []
    values1 = []
    return render_template('dashboard.html', values1=values1, labels1=labels1)



@app.route('/refreshData')
def refresh_graph_data():
    global labels, values
    print("labels now: " + str(labels))
    print("data now: " + str(values))
    return jsonify(sLabel=labels, sData=values)


@app.route('/updateData', methods=['POST'])
def update_data_post():
    global labels, values
    if not request.form or 'data' not in request.form:
        return "error",400
    labels = ast.literal_eval(request.form['label'])
    values = ast.literal_eval(request.form['data'])
    print("labels received: " + str(labels))
    print("data received: " + str(values))
    return "success",201




@app.route('/refreshData1')
def refresh_graph_data1():
    global labels, values
    print("labels now: " + str(labels))
    print("data now: " + str(values))
    return jsonify(sLabel=labels1, sData=values1)





@app.route('/updateData1', methods=['POST'])
def update_data_post1():
    global labels1, values1
    if not request.form or 'data1' not in request.form:
        return "error",400
    labels1 = ast.literal_eval(request.form['label1'])
    values1 = ast.literal_eval(request.form['data1'])
    print("labels received: " + str(labels1))
    print("data received: " + str(values1))
    return "success",201




if __name__ == "__main__":
    app.run(host='localhost', port=5001)

