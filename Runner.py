#!/usr/bin/python
import Reccomendations
from Reccomendations import critics

#the following routing take each person and finds out its similarity with other person

max=0.0
m_sim=" "


for item in critics:
    max=0.0
    m_sim=" "
    for item1 in critics:
        if item != item1:
            var=Reccomendations.sim_distance(Reccomendations.critics,item,item1)
            if var > max :
                max=var
                m_sim=item1

            print "Similarity Between"
            print ("Person 1:-",item)
            print ("Person 2:-",item1)
            print  var
            print "\n"


    print ("for "+item+ " ")
    print ("The greatest similarity is found with "+m_sim)
    print ("Which is equal to:",max)
    print ("\n\n")

