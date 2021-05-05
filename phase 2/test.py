import pandas as pd
df = pd.read_csv('account.csv')

uu = df['username']
pp = df['password']
rr = df['roll']
for u,p ,r in zip(uu,pp ,rr):
    print(u,p,r)
