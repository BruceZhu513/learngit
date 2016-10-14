from recommendations import critics
from math import sqrt

def sim_pearson(prefs,p1,p2):
    si={}
    for item in prefs[p1]:
        if item in prefs[p2]:
            si[item]=1
    n=len(si)
    if len(si)==0:
        return 0
    sum1=sum(prefs[p1][i] for i in si)
    sum2=sum(prefs[p2][i] for i in si)

    sum1Sq=sum(pow(prefs[p1][i],2) for i in si)
    sum2Sq=sum(pow(prefs[p2][i],2) for i in si)

    pSum=sum([prefs[p1][i]*prefs[p2][i]for i in si])

    num=pSum-(sum1*sum2/n)
    den=sqrt((sum1Sq-pow(sum1,2)/n)*(sum2Sq-pow(sum2,2)/n))
    if den==0:return 0
    r=num/den
    return r

def topMatches(prefs,person,n=5,similarity=sim_pearson):
    scores=[(sim_pearson(prefs,person,other),other) for other in prefs if other!=person]
    scores.sort()
    scores.reverse()
    return scores[0:n]

def getRrcommentdations(prefs,person,similarity=sim_pearson):
    totals={}
    simSums={}
    for other in prefs:
        print other
        if other==person:
            continue
        sim=similarity(prefs,person,other)

        if sim<0:
            continue
        for item in prefs[other]:
            if item not in prefs[person] or prefs[person][item]==0.0:
                totals.setdefault(item,0.0)
                totals[item]+=sim*prefs[other][item]
                simSums.setdefault(item,0)
                simSums[item]+=sim

    rankings=[(total/simSums[item],item) for item,total in totals.items()]
    rankings.sort()
    rankings.reverse()
    return rankings

if __name__=='__main__':
##    print sim_pearson(critics,'Lisa Rose','Gene Seymour')    
##    print topMatches(critics,'Toby',n=3)
    print getRrcommentdations(critics,'Toby')
