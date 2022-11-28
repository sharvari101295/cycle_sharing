import numpy as np  
import json
import pickle
import config


class CycleSharing():
    def __init__(self,season,holiday,workingday,weather,temp,atemp,humidity,windspeed,hour,day,month,year):
        self.season = season
        self.holiday = holiday
        self.workingday = workingday
        self.weather = weather
        self.temp = temp
        self.atemp = atemp
        self.humidity = humidity
        self.windspeed = windspeed
        self.hour = hour
        self.day = day
        self.month = month
        self.year = year

    def load_model(self):
        with open (config.MODEL_FILE_PATH,'rb') as f:
            self.model = pickle.load(f)

        with open(config.JSON_FILE_PATH,'r') as f:
            self.json_data = json.load(f)


    def get_cycle_share_count(self):
        self.load_model()


        test_array = np.zeros(len(self.json_data['columns']))

        test_array[0] = self.season
        test_array[1] = self.holiday
        test_array[2] = self.workingday
        test_array[3] = self.weather
        test_array[4] = self.temp
        test_array[5] = self.atemp
        test_array[6] = self.humidity
        test_array[7] = self.windspeed
        test_array[8] = self.hour
        test_array[9] = self.day
        test_array[10] = self.month
        test_array[11] = self.year

        print("test_array:",test_array) # 10 values

        cyclesharecount = self.model.predict([test_array])[0]
        return cyclesharecount


if __name__ == "__main__":

    season  = 1
    holiday = 0
    workingday = 1
    weather  = 1
    temp  = 9.84
    atemp = 14.395
    humidity = 81
    windspeed = 6.0032
    hour = 19
    day = 2
    month = 12
    year = 1

    cycle_share = CycleSharing(season,holiday,workingday,weather,temp,atemp,humidity,windspeed,hour,day,month,year)
    cycle_share.get_cycle_share_count()