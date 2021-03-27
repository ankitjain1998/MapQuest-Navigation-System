# ICS 32 - Fall 2017

# Project #3: Ride Across the River

# Name: Ankit Jain
# ID: 96065117
# UCINetID: jaina2

# Classes Module
'''
This module is to extract certain portions
of the information from url and segregate them
separately using classes and class methods
'''

# Imported Module(s)

import api_connect

# Functions, Classes and Class Methods

class Place:
    '''
    Place object is initalized using a string
    and is mainly used to convert the location
    string to url appropriate form to be used
    in the building of the url
    '''
    def __init__(self,location:str):
        '''
        Method to initialize object with
        string as a parameter
        '''
        self._place = location
    def _get_place(self):
        '''
        Attribute used to return the
        location string so used
        '''
        return str(self._place)
    def url_creator(self):
        '''
        Method used to convert the location
        parameter into url appropriate form to
        be used in building the url to extract
        information
        '''
        place = self._get_place()
        while ', ' in place:
            place = place.replace(', ','%2C')
        while ' ' in place:
            place = place.replace(' ','+')
        while ',' in place:
            place = place.replace(',','%2C')
        return place

class RouteFunctions:
    '''
    Class initialized by a list of
    locations which builds the url
    (elevation or route) and returns
    the information so obtained from
    the url
    '''
    def __init__(self,locations:list):
        '''
        Initializes the object taking
        a list of locations as a parameter
        '''
        self._locations = locations

    def _get_locations(self) -> list:
        '''
        Returns the list of locations
        which were entered earlier
        '''
        return self._locations
    def _get_info(self) -> dict:
        '''
        Builds route url and returns
        the information so obtained
        in form of a dictionary 
        '''
        locations = self._get_locations()
        url = api_connect.build_route_url(locations)
        info = api_connect.convert(url)
        if info == None:
            pass
        else:
            exist_route = info['info']['messages']
            if exist_route == []:
                return info
            else:
                return None
    def _get_elevation_info(self) -> list:
        '''
        Builds an elevation url for each
        location in the list and returns
        a list of dictionaries which are
        basically the elevation information
        of each location
        '''
        all_info = []
        locations = self._get_locations()
        urls = api_connect.build_elevation_urls(locations)
        if urls == None:
            return None
        else:
            for url in urls:
                info = api_connect.convert(url)
                exist_route = info['info']['messages']
                if exist_route == []:
                    all_info.append(info)
                else:
                    return None
            if len(all_info) == 0:
                return None
            else:
                return all_info
    
class Steps:
    '''
    Class is used to get the steps to go from
    one location to another
    '''
    def __init__(self,locations:list):
        '''
        Initializes object by taking a list of
        the locations and converting them to a
        RouteFunctions object
        '''
        self._functions = RouteFunctions(locations)
    def get(self) -> list:
        '''
        Extracts the string of the step narrative at
        each point of the journey and returns a list of
        all the steps throughout the entire journey from
        the route url 
        '''
        steps =[]
        functions = self._functions
        info = functions._get_info()
        if info == None:
            return None
        else:  
            num_locations = len(functions._get_locations()) - 1
            for num in range(0,num_locations):
                route_directions = info['route']['legs'][num]['maneuvers']
                num_steps = len(route_directions)
                for index in range(0,num_steps):
                    steps.append(str(route_directions[index]['narrative']))
            return steps
    def print(self):
        '''
        Prints all the direction narratives
        so obtained from the route url
        '''
        steps = self.get()
        if steps == None:
            pass
        else:
            print('DIRECTIONS')
            for step in steps:
                print(step)
        return None

class TotalDistance:
    '''
    Class is used obtain the total distance
    covered between the travelling from
    location to location
    '''
    def __init__(self,locations:list):
        '''
        Initializes object by taking a list of
        the locations and converting them to a
        RouteFunctions object
        '''
        self._functions = RouteFunctions(locations)
    def get(self) -> int:
        '''
        Returns the total distance covered during
        the entire journey rounded to the nearest
        mile obtained from the route url
        '''
        functions = self._functions
        info = functions._get_info()
        if info == None:
            return None
        else:
            distance = info['route']['distance']
            distance = int(round(distance))
            return distance
    def print(self):
        '''
        Prints the total distance covered in
        the complete trip obtained from the route
        url
        '''
        distance = self.get()
        if distance == None:
            pass
        else:
            print('TOTAL DISTANCE: '+ str(distance) + ' miles')
        return None

class TotalTime:
    '''
    Class is used to obtained the
    total estimate of the time to
    complete the journey from one
    location to another 
    '''
    def __init__(self,locations:list):
        '''
        Initializes object by taking a list of
        the locations and converting them to a
        RouteFunctions object
        '''
        self._functions = RouteFunctions(locations)
    def get(self) -> int:
        '''
        Returns the estimate of the total time
        to complete the entire trip rounded to
        the nearest minute obtained from the route
        url
        '''
        functions = self._functions
        info = functions._get_info()
        if info == None:
            return None
        else:
            time = float(info['route']['time'])
            minutes = int(round(float(time/60)))
            return minutes
    def print(self):
        '''
        Prints the estimated total time obtained
        from the route url
        '''
        time = self.get()
        if time == None:
            pass
        else:
            print('TOTAL TIME: ' + str(time) + ' minutes')
        return None

class LatLong:
    '''
    Class is used to obtain the latitude
    and longitude of each location so
    covered in the journey 
    '''
    def __init__(self,locations:list):
        '''
        Initializes object by taking a list of
        the locations and converting them to a
        RouteFunctions object
        '''
        self._functions = RouteFunctions(locations)
    def get(self) -> tuple:
        '''
        Returns a tuple of the latitude and
        longitude of each location extracting
        it from the route url
        '''
        functions = self._functions
        info = functions._get_info()
        if info == None:
            return None
        else:
            lat = []
            lng = []
            lat_lng = []
            locations = info['route']['locations']
            num_locations = len(locations)
            for index in range(0,num_locations):
                lat_lng_dict = info['route']['locations'][index]['latLng']
                _lng_ = lat_lng_dict['lng']
                _lat_ = lat_lng_dict['lat']
                lat.append(_lat_)
                lng.append(_lng_)
            lat_lng.append(lat)
            lat_lng.append(lng)
            lat_lng = tuple(lat_lng)
            return lat_lng
    def _print_lat(self,lat:float) -> str:
        '''
        Returns a printing appropriate string
        of the latitudes of the location
        '''
        if lat > 0:
            to_print = '{:.2f}N'.format(float(lat))
        else:
            to_print = '{:.2f}S'.format(float(abs(lat)))
        return to_print
    def _print_lng(self,lng:float) -> str:
        '''
        Returns a printing appropriate string
        of the longitudes of the location
        '''
        to_print = ''
        if lng > 0:
            to_print = '{:.2f}E'.format(float(lng))
        else:
            to_print = '{:.2f}W'.format(float(abs(lng)))
        return to_print
    def get_elevation_parameter(self) -> str:
        '''
        Returns a string by obtaining the latlong of the
        locations and making them appropriate for
        building the elevation url
        '''
        parameters = []
        latlng = self.get()
        if latlng == None:
            pass
        else:
            for index in range(len(latlng[0])):
                lat = str(latlng[0][index])
                lng = str(latlng[1][index])
                parameter = lat +',' + lng + ','
                parameters.append(parameter)
            return parameters
    def print(self):
        '''
        Prints the latitude and longitude of the
        locations obtained from the route url
        '''
        lat_lng = self.get()
        if lat_lng == None:
            pass
        else:
            index  = len(lat_lng[0])
            print('LATLONGS')
            for num in range(0,index):
                print('{} {}'.format(self._print_lat(lat_lng[0][num]),self._print_lng(lat_lng[1][num])))
            return None

class Elevation:
    '''
    Class is used to get the elevation of
    each location so covered in the journey
    '''
    def __init__(self,locations:list):
        '''
        Initializes object by taking a list of
        the locations and converting them to a
        RouteFunctions object
        '''
        self._functions = RouteFunctions(locations)
    def get(self):
        '''
        Returns a list of the elevation
        of each location extracting
        it from the elevation url
        '''
        functions = self._functions
        info = functions._get_elevation_info()
        elevations = []
        if info == None:
            return None
        else:
            for location in info:
                elevation = float(location['elevationProfile'][0]['height']*3.28084)
                elevation = round(elevation)
                elevations.append(str(elevation))
            return elevations
    def print(self):
        '''
        Prints the elevation of each
        location extracted from the
        elevation url
        '''
        elevations = self.get()
        if elevations == None:
            pass
        else:
            print('ELEVATIONS')
            for elevation in elevations:
                print(elevation)
            return None
    
class GetType:
    '''
    Class is used to get a certain type of
    object as per the command so entered
    '''
    def __init__(self,locations:list,command:str):
        '''
        Class is initialized by a list of locations
        and a string which is the entered command
        '''
        self._locations = locations
        self._command = command
    def obtain(self):
        '''
        Method uses the command string
        on basis of which it returns
        the type of object so needed
        to get the output
        '''
        locations = self._locations
        command = self._command
        if command == 'TOTALDISTANCE':
            return TotalDistance(locations)
        elif command == 'TOTALTIME':
            return TotalTime(locations)
        elif command == 'STEPS':
            return Steps(locations)
        elif command == 'LATLONG':
            return LatLong(locations)
        elif command == 'ELEVATION':
            return Elevation(locations)
        else:
            return None

            
            

    
