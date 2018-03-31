import json
import urllib2
import math
from fetch_weather import Weather
from config import *

activities = {}
segments = []

def get_activities(per_page):
    if per_page is None:
        per_page = 10
    per_page = str(per_page)
    endpoint = "https://www.strava.com/api/v3/athlete/activities?per_page={}&access_token={}"
    global activities
    activities = json.loads(urllib2.urlopen(endpoint.format(per_page,ACCESS_TOKEN)).read())

def output_fields():
    for field in activities[0]:
        print field,

def output_activities():
    for activity in activities:
        print activity["name"], activity["id"]

def output_segment_ids():
    print [segment["id"] for segment in segments]

def populate_segments():
    for activity in activities:
        if activity["type"] != "Ride" or activity["manual"] is True:
            continue

        activity_id = str(activity["id"])
        endpoint = "https://www.strava.com/api/v3/activities/{}/?per_page=200&access_token={}"
        activity_data = json.loads(urllib2.urlopen(endpoint.format(activity_id, ACCESS_TOKEN)).read())

        segments_visited = []
        for segment in activity_data["segment_efforts"]:
            # For consistency purposes, keep only unique segment efforts
            if segment["id"] not in segments_visited:
                segments.append(segment)
                segments_visited.append(segment["id"])

def generate_segment_latlng_time():
    ans = []
    for segment in segments:
        res = '{},{},{}'
        ans.append(res.format(segment['segment']['start_latlng'][0], str(segment['segment']['start_latlng'][1]), str(segment['start_date'])))
    return ans

def generate_wind_speed_training(datasize, filename):
    get_activities(datasize)
    populate_segments()

    weather_queries = generate_segment_latlng_time()
    weather_data = []
    w = Weather()

    for query in weather_queries:
        weather_data.append(w.make_request(query))
    w.close()

    file = open(filename, "w")

    for x in range(len(segments)):
        segment = segments[x]
        output_str = "{},{},{},{},{},{},{}"
        weather = weather_data[x].split(',')

        wind_speed = weather[0]
        wind_bearing = weather[1]

        start_lat = segment['segment']['start_latlng'][0]
        start_lng = segment['segment']['start_latlng'][1]
        end_lat = segment['segment']['end_latlng'][0]
        end_lng = segment['segment']['end_latlng'][1]
        avg_grade = segment['segment']['average_grade']
        
        ride_bearing = calculate_initial_compass_bearing((start_lat, start_lng),(end_lat, end_lng))

        file.write(output_str.format(segment['id'], segment['distance'], segment['moving_time'], ride_bearing, avg_grade, wind_speed, wind_bearing))
    file.close()

def calculate_initial_compass_bearing(pointA, pointB):
    if (type(pointA) != tuple) or (type(pointB) != tuple):
        raise TypeError('Only tuples are supported as arguments')

    lat1 = math.radians(pointA[0])
    lat2 = math.radians(pointB[0])

    diffLong = math.radians(pointB[1] - pointA[1])

    x = math.sin(diffLong) * math.cos(lat2)
    y = math.cos(lat1) * math.sin(lat2) - (math.sin(lat1) * math.cos(lat2) * math.cos(diffLong))

    initial_bearing = math.atan2(x, y)

    initial_bearing = math.degrees(initial_bearing)
    compass_bearing = (initial_bearing + 360) % 360

    return compass_bearing

def main():
    # output_activities()
    get_activities(14)
    populate_segments()
    # output_segment_ids()
    print generate_segment_latlng_time()
    w = Weather()
    print w.make_request('43.747194,-79.391819,2016-06-05T00:28:22')
    w.close()

generate_wind_speed_training(65, 'training.txt')
