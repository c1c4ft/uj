import numpy as np
import pandas as pd

df=pd.DataFrame(columns=['n','fib'])

# pd.concat, pd.join, pd.merge, append
row={'n':1.0,'fib':1.0}
row2={'n':2.0,'fib':1.0}

new_df=pd.DataFrame([row,row2])
df=pd.concat([df, new_df], axis=0, ignore_index=True)

print(df)

df2=pd.DataFrame(range(1, 21), columns=['n'])
df2['fib']=np.nan
df2.loc[df2['n']==1, 'fib']=1
df2.loc[df2['n']==2, 'fib']=1

#df2.loc[df2['n'] in [1,2], 'fib'==1]
fib_lag1=0
fib_lag2=0
import sys
for ix, row in df2.iterrows():
    if ix in [0,1]:
        df2.loc[ix, 'fib']=1
    else:
        df2.loc[ix, 'fib']=df2.loc[ix-1, 'fib']+df2.loc[ix-2, 'fib']

print(df2)

#print(ix)
#print(row)
#print(row['n'])



