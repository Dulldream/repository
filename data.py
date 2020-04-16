class Location :
    def __init__(self, location_name=None, lat=None,
                 lon=None, station_id=None, time=None,
                 weather_element=None):
        self.location_name = location_name
        self.lat = lat
        self.lon = lon
        self.station_id = station_id
        self.time = time
        self.weather_element = weather_element

    def from_json(self, json_data):
        self.lat = json_data.get('lat')
        self.lon = json_data.get('lon')
        self.location_name = json_data.get('locationName')
        self.station_id = json_data.get('station_id')
        time1 = json_data.get('time')
        self.time = time.get('obsTime')


        weather_element_json = json_data.get('weatherElement')
        element = WeatherElement()
        element.from_json(weather_element_json)
        self.weather_element = element


class WeatherElement :
    def __init__(self, wdir=None, wdsd=None, temp=None, humd=None, h_24r=None):
        self.wdir = wdir
        self.wdsd = wdsd
        self.temp = temp
        self.humd = humd
        self.h_24r = h_24r

    def from_json(self, json_data):
        for element in json_data:
            element_name = element.get('elementName')
            element_value = element.get('elementValue')
            if element_Name == 'WDIR'
                self.wdir = element_value








