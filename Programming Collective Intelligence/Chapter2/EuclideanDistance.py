from math import sqrt
from recommendations import critics

def sim_distance(prefs,person1,person2):
    #shared_items
    si={}
##    error
##    print [si[item]=1 for item in prefs[person1] if item in prefs[person2]]
    for item in prefs[person1]:
        if item in prefs[person2]:
            si[item]=1
    if len(si)==0:
        return 0

    sum_of_squares=sum([pow(prefs[person1][item]-prefs[person2][item],2)
                        for item in prefs[person1]if item in prefs[person2]])
    return 1/(1+sqrt(sum_of_squares))
    

if __name__=='__main__':
   print sim_distance(critics,'Lisa Rose','Michael Phillips') 
