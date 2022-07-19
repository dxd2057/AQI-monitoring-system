from flask import Flask, render_template, request
from models import *

# create an app in flask

app = Flask(__name__)

@app.route("/")
def home():

    pm25 = []
    temp= []
    hum = []
    node_name = 'node6'

    sensor_list = ['node2','node6']
    my_sensor_data = []
    node_name = request.args.get("choose_node")
    #print(node_name)


    for sensor in sensor_list:
        sensor_node = MyNode(sensor)
        sensor_node.get_last_data()
        my_sensor_data.append(sensor_node.node_data)

        if sensor==node_name:
            sensor_node.get_online_chart_data()
            pm25=sensor_node.node_data_pm25
            temp=sensor_node.node_data_temp
            hum=sensor_node.node_data_hum

    print(pm25)

    return render_template("index.html",data=my_sensor_data,pm25=pm25,name=node_name,
                           date_time=sensor_node.date_time,temp=temp,hum=hum)

if __name__=="__main__":
    app.run(debug=True)