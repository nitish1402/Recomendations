#!/usr/bin/python
import Reccomendations
from Reccomendations import critics

#the following routing take each person and finds out its similarity with other person


for item in critics:
    for item1 in critics:
        if item != item1:
            print "Similarity Between"
            print ("Person 1:-",item)
            print ("Person 2:-",item1)
            print Reccomendations.sim_distance(Reccomendations.critics,item,item1)
            print "\n"



