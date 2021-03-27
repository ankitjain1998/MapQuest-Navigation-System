# ICS 32 - Fall 2017

# Project #3: Ride Across the River

# Name: Ankit Jain
# ID: 96065117
# UCINetID: jaina2

# User Interface Module

'''
This module is to faciliate
the user interface
'''

# Imported Module(s)

import classes

# Functions

def _invalid_move_message():
    '''
    Message printed when there is an invalid move
    '''
    print('INVALID INPUT!\nTRY AGAIN.')

def _input_locations():
    '''
    Function is used to get the user
    to input the number of locations
    followed by the locations itself.
    Returns a list of the locations.
    '''
    try:
        locations = []
        num_locations = int(input())
        if num_locations >= 2:
            while len(locations)!= num_locations:
                try:
                    location = input()
                    if len(location) == 0:
                        _invalid_move_message()
                    else:
                        locations.append(location.strip())
                except IndexError:
                    _invalid_move_message()
            return locations
        else:
            _invalid_move_message()
            return _input_locations()
    except ValueError:
        _invalid_move_message()
        return _input_locations()

def _input_actions():
    '''
    Function is used to get the user
    to input the number of commands
    followed by the commands itself.
    Returns a list of the commands.
    '''
    try:
        actions = []
        num_actions = int(input())
        assert 1 <= num_actions 
        while len(actions)!= num_actions:
            try:
                action = input()
                if action.strip() in ['STEPS','LATLONG','TOTALTIME','TOTALDISTANCE','ELEVATION']:
                    actions.append(action.strip())
                else:
                    _invalid_move_message()
            except IndexError:
                _invalid_move_message()
        return actions
    except (AssertionError,ValueError):
        _invalid_move_message()
        return _input_actions()

def _user_interface():
    '''
    Function runs the input functions and
    prints the output in the order of how
    the commands are so entered
    '''
    locations = _input_locations()
    commands = _input_actions()
    try:
        working_commands = 0
        for command in commands:
            get = classes.GetType(locations,command).obtain()
            print('')
            if get.get() == None:
                print('NO ROUTE FOUND\n')
                break
            else:
                working_commands += 1
                get.print()
        if working_commands == 0:
            pass
        else:
            print('')
            print('Directions Courtesy of MapQuest; Map Data Copyright OpenStreetMap Contributors')
    except:
        print('MAPQUEST ERROR')


if __name__ == '__main__':
    _user_interface()
    
