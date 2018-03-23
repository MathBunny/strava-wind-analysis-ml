from config import *
import json, ast, urllib2


activities = {}
segments = []

def get_activities(per_page):
    if per_page == None:
        per_page = 10
    per_page = str(per_page)
    contents = urllib2.urlopen("https://www.strava.com/api/v3/athlete/activities?include_all_efforts=true&per_page=" + per_page + "&access_token=" + ACCESS_TOKEN).read()
    global activities
    activities = json.loads(contents)

def output_fields():
    for field in activities[0]:
        print field,

def output_activities():
    for activity in activities:
        print activity["name"], activity["id"]

def output_segment_ids():
    for segment in segments:
        print segment["id"]

def populate_segments():
    for activity in activities:
        if activity["type"] != "Ride" or activity["manual"] == True:
            continue
        activity_id = str(activity["id"])
        activity_data = json.loads(urllib2.urlopen("https://www.strava.com/api/v3/activities/" + activity_id + "?per_page=200&access_token=" + ACCESS_TOKEN).read())
        segments_visited = []
        for segment in activity_data["segment_efforts"]:
            if segment["id"] not in segments_visited:
                segments.append(segment)
                segments_visited.append(segment["id"])


# output_activities()
get_activities(20)
populate_segments()
output_segment_ids()