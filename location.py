from math import *

# Name: Arti Jain         
# Course: CPE 202
# Instructor: Hatalsky 
# Assignment: Lab 1 Location
# Term: Spring 2019

# represents a location using name, latitude and longitude
class Location: #a location object
    def __init__(self, name, lat, lon):
        self.name = name    # string for name of location
        self.lat = lat      # latitude in degrees (-90 to 90)
        self.lon = lon      # longitude in degrees (-180 to 180)
    #__eq__
    def __eq__(self, other): #overrides what's in python and allows you to compare the data
        return (type(other) == Location and (self.name == other.name) and isclose(self.lat, other.lat) and isclose(self.lon, other.lon))
    #__repr__ = how the object is represented, string representation
    def __repr__(self):
        string = "Location('" + self.name + "', " + str(self.lat) + ", " + str(self.lon) + ")"
        return string

# 4 basic methods every object should have
# init, eq, repr, str

def main():
    loc1 = Location("SLO", 35.3, -120.7)
    loc2 = Location("Paris", 48.9, 2.4)
    loc3 = Location("SLO", 35.3, -120.7)
    loc4 = loc1

    print("Location 1:",loc1)
    print("Location 2:",loc2)
    print("Location 3:",loc3)
    print("Location 4:",loc4)

    print("\nLocation 1 equals Location 2:", loc1==loc2)
    print("Location 1 equals Location 3:", loc1==loc3) #Once the code changed, this went from False to True
    print("Location 1 equals Location 4:", loc1==loc4)

# When the code is changed, instead of True, True, False, True, the output is all True's
    locations = [loc1, loc2]
    print(loc1 in locations)
    print(loc2 in locations)
    print(loc3 in locations)
    print(loc4 in locations)

if __name__ == "__main__":
    main()