import json
import urllib2
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

# output_activities()
get_activities(20)
populate_segments()
# output_segment_ids()
print generate_segment_latlng_time()
w = Weather()
print w.make_request('43.747194,-79.391819,2016-06-05T00:28:22')
w.close()