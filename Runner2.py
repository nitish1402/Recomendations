__author__ = 'nitish'

#runner file for Reccomendations using Pearson Correlation Coefficient

#!/usr/bin/python
import Reccomendation1
import Reccomendations
from Reccomendations import critics

#the following routing take each person and finds out its similarity with other person

max = 0.0
m_sim = ' '

print Reccomendation1.sim_person(Reccomendations.critics, 'Lisa Rose', 'Gene Seymour')

for item in critics:
    max = 0.0
    m_sim = ' '
    for item1 in critics:
        if item != item1:
            var = Reccomendation1.sim_person(Reccomendations.critics, item, item1)
            if var > max:
                max = var
                m_sim = item1

           # print "Similarity Between"
           # print ("Person 1:-", item)
           # print ("Person 2:-", item1)
           # print var
           # print "\n"

    print ("for " + item + " ")
    print ("The greatest similarity is found with " + m_sim)
    print ("Which is equal to:", max)
    print ("\n\n")

for item in Reccomendations.critics :
     print ("For " + item)
     print Reccomendation1.top_matches(Reccomendations.critics,item,n=2)


print "------====GETTING RECOMMENDATIONS====----------"
for item in Reccomendations.critics :
    print ("For " + item)
    print Reccomendation1.getrecommendations(Reccomendations.critics, item)
    print Reccomendation1.getrecommendations(Reccomendations.critics, item, similarity=Reccomendations.sim_distance)
###
