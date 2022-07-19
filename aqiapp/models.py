import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

cred = credentials.Certificate("maapp_cer.json")
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://aqimonitoringsystem-default-rtdb.firebaseio.com/'
})

class MyNode():

    def __init__(self,name):
        self.sensor_name=name
        self.date_time = 0
        self.node_data = []
        self.node_data_pm25 = []
        self.node_data_temp = []
        self.node_data_hum = []

    def get_last_data(self):

        # getting lastest data of sensor
        snapshot = db.reference(self.sensor_name).order_by_key().limit_to_last(1).get()
        #print(snapshot)

        for key,val in snapshot.items():
            self.date_time = key
            self.node_data.append(self.sensor_name)
            self.node_data.append(int(val["pm25"]))
            self.node_data.append(int(val["temp"]))
            self.node_data.append(int(val["hum"]))
            self.node_data.append(key)

    def get_online_chart_data(self):
        snapshot = db.reference(self.sensor_name).order_by_key().limit_to_last(60).get()
        last_pm25 = 0
        for key, val in snapshot.items():
            if int(val['pm25']) < 1000:
                self.node_data_pm25.append(int(val['pm25']))
                last_pm25 = int(val['pm25'])
            else:
                self.node_data_pm25.append(last_pm25)

            self.node_data_temp.append(int(val['temp']))
            self.node_data_hum.append(int(val['hum']))

if __name__=="__main__":
    #for debug only
    node_2 = MyNode('node2')
    node_2.get_last_data()
    print(node_2.node_data)
    node_2.get_online_chart_data()
    print(node_2.node_data_pm25)
