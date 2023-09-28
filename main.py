import string
import pandas as pd
#from postscrape.postscrape.spiders.NFL import NFL

import pandas as pd
import re
data = pd.read_csv("postscrape/postscrape/spiders/Newplayers.csv")
d = data.Year

x = data
for i,l in enumerate(d):
    try:
        lis = list(set(re.findall('....',l.replace(',',''))))
        if('0000' in lis):
            lis.remove('0000')
        x.iloc[i,1] = lis
    except:
        x.drop(labels=i,inplace=False,axis=0)

print(x.iloc[:,1])
x.to_csv ('pretty2.csv', index = False, header=True)






