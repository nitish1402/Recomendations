#!usr/bin/python

from math import sqrt
#using pearson correlation coefficient to calculate similarity between two critics


def sim_person(names, person1, person2):
    si = {}

    for item in names[person1]:
        if item in names[person2]:
            si[item] = 1

    if len(si) == 0:
        return 0

    n = len(si)

    #calculating sums for each person
    sum1 = sum([names[person1][item] for item in si])
    sum2 = sum([names[person2][item] for item in si])

    #calculating square sum for each person
    sum1Sq = sum([pow(names[person1][item], 2) for item in si])
    sum2Sq = sum([pow(names[person2][item], 2) for item in si])

    #taking products for each item they have in common and calculating the products sum
    psum = sum([names[person1][item] * names[person2][item] for item in si])

    #calculation for pearson correlation coefficient
    num = psum - (sum1 * sum2 / n)

    den = sqrt((sum1Sq - pow(sum1, 2) / n) * (sum2Sq - pow(sum2, 2) / n))

    if den == 0:
        return 0

    r = num / den

    return r


def top_matches(names, person1, n=5, similarity=sim_person):

    scores = [(similarity(names, person1, other), other)
              for other in names if other != person1]

    scores.sort()

    scores.reverse()

    return scores[0:n]


#the following function calculate the rating for the movies which i have not rated yet

def getrecommendations(names, person, similarity=sim_person):

    m_item={}  #dictionary for each movie and cummulative ratings
    sim_sum={}  #getting the sum of similarity for each movie

    #getting the other persons
    for others in names:
        #we have exclude the person it self
        if others == person: continue

        #get the similarity
        sim = similarity(names, others, person)

        #got the similarity here
        #if its comes out to be less than 0 than no mean of it because ultimately
        #the result is going out to be 0
        if sim <= 0 :continue

        #taking the particular user at a time

        for item in names[others]:

            #we want only those movies which the given user hasn't rated
            if item not in names[person] or names[person][item] == 0:

                #defining a list  to carry out the calculation per movie
                m_item.setdefault(item,0)
                m_item[item] += names[others][item]*sim

                sim_sum.setdefault(item,0)
                sim_sum[item] += sim

                #ending for loop here


    #ending for loop here
    #now we have two list and only normalistaion is left

    ranking = [(total/sim_sum[item],item) for item,total in m_item.items() ]

    ranking.sort()
    ranking.reverse()

    return ranking



