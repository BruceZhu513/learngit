import PearsonCorrelation
critics={'Lisa Rose':{'Lady in the Water':2.5,'Snakes on a Plane':3.5,
'Just My Luck':3.0,'Superman Returns':3.5,'You,Me and Dupree':2.5,
'The Night Listener':3.0},
         'Gene Seymour':{'Lady in the Water':3.0,'Snakes on a Plane':3.5,
'Just My Luck':1.5,'Superman Returns':5.0,'You,Me and Dupree':3.0,
'The Night Listener':3.5},
         'Michael Phillips':{'Lady in the Water':2.5,'Snakes on a Plane':3.0,
'Superman Returns':3.5,'The Night Listener':4.0},
         'Claudia Puig':{'Snakes on a Plane':3.5,'Just My Luck':3.0,
'Superman Returns':4.0,'You,Me and Dupree':2.5,'The Night Listener':4.5},
         'Mick LaSalle':{'Lady in the Water':3.0,'Snakes on a Plane':4.0,
'Just My Luck':2.0,'Superman Returns':3.0,'You,Me and Dupree':2.0,
'The Night Listener':3.0},
         'Jack Matthews':{'Lady in the Water':3.0,'Snakes on a Plane':4.0,
'Superman Returns':5.0,'You,Me and Dupree':3.5,'The Night Listener':3.0},
         'Toby':{'Snakes on a Plane':4.5,'Superman Returns':4.0,'You,Me and Dupree':1.0}}

def transformPrefs(prefs):
    result={}
    for person in prefs:
        for item in prefs[person]:
            result.setdefault(item,{})
            result[item][person]=prefs[person][item]
    return result


def calculateSimilarItems(prefs,n=10):
    result={}
    itemPrefs=transformPrefs(prefs)
    c=0
    for item in itemPrefs:
        c+=1
        if c%100==0:
            print '%d/%d'%(c,len(itemPrefs))
        scores=PearsonCorrelation.topMatches(itemPrefs,item,n=n,similarity=PearsonCorrelation.sim_pearson)
        result[item]=scores

if __name__=='__main__':
    print calculateSimilarItems(critics)
