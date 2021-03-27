# ICS 32 - Fall 2017

# Project #3: Ride Across the River

# Name: Ankit Jain
# ID: 96065117
# UCINetID: jaina2

# API - Connect Module

'''
This module is to facilitate the connection
and the interaction with the Open MapQuest API's
and convert the information so received into
a python object. It is also to build the url
from which the information is extracted. 
'''

# Imported Modules

import json
import urllib.parse
import urllib.request
import classes

# Global Constants

MAP_QUEST_API_KEY = 'DznTbSILowpG3mz0bKPFCg0pqYeWVNxm'
RESOURCE_ROUTE_URL = 'http://open.mapquestapi.com/directions/v2/route'
RESOURCE_ELEVATION_URL = 'http://open.mapquestapi.com/elevation/v1/profile'

# Functions

def build_route_url(locations:list) -> str:
    '''
    Function takes a list of locations as a parameter,
    converts them to url appropriate form and returns
    the url as a string. This url is used to get the
    distance, directions, time and latitude-longitude
    for the entered locations.
    '''
    url = ''
    source_location = classes.Place(locations[0])
    destinations = locations[1:]
    url += RESOURCE_ROUTE_URL
    url += '?key=' + MAP_QUEST_API_KEY
    url += '&from=' + source_location.url_creator()
    for destination in destinations:
        place = classes.Place(destination)
        url += '&to=' + place.url_creator()

    return url

def build_elevation_urls(locations:list) -> str:
    '''
    Function takes a list of locations as a parameter,
    uses the latlong of those locations, converts them
    to url appropriate form and returns a list of urls
    as a string. These urls are used to get
    the elevation of the
    required locations in feet. 
    '''
    urls = [] 
    latlong = classes.LatLong(locations)
    parameters = latlong.get_elevation_parameter()
    if parameters == None:
        return None
    else:
        for parameter in parameters:
            parameter = classes.Place(parameter)
            url = RESOURCE_ELEVATION_URL
            url += '?key=' + MAP_QUEST_API_KEY 
            url += '&latLngCollection=' + parameter.url_creator()
            urls.append(url[:-3])

        return urls
  
        
def _make_connection(url:str) -> str:
    '''
    Function takes in a string which is the url,
    and opens that url, decodes the
    information so present in the url
    the entire thing as a string, except
    when there is an error with the connection
    '''
    try:
        connection = urllib.request.urlopen(url)
        all_details = connection.read().decode(encoding = 'utf-8')
        return all_details
    except:
        connection = None
    finally:
        if connection != None:
            connection.close()

        
def convert(url:str) -> dict:
    '''
    Function takes in a string which is the url,
    and converts the information so present in
    the url from json to a python object(dictionary).
    '''
    to_convert = _make_connection(url)
    converted = json.loads(to_convert)
    return converted


    
    

    
