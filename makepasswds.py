import numpy as np
import pandas as pd

res = pd.read_csv("roster.csv")
#names =  [s.split()[0] for s in res["Student Name"].to_numpy().tolist()]
#netids = [s.split("@")[0] for s in res["Preferred Email"].to_numpy().tolist()]
names =  [s.split()[0] for s in res["Name"].to_numpy().tolist()]
netids = [s for s in res["SIS ID"].to_numpy().tolist()]


fin = open("words.txt")
words = [s.split()[0] for s in fin.readlines()[0:50000]]
words = [w for w in words if len(w) < 9 and len(w) > 5]
fin.close()

np.random.seed(1)
s = "students = ["
group_id = "cs174f2023"
for i, (n, id) in enumerate(zip(names, netids)):
    si = "{"
    port = 8082+i
    w1 = words[np.random.randint(len(words))]
    w2 = words[np.random.randint(len(words))]
    w2 = w2[0].upper() + w2[1::]
    passwd = "{}{}{}".format(w1, np.random.randint(100), w2)
    #print("{}:{}::{}::/home/{}:/bin/bash".format(id, passwd, group_id, id))
    si += "name:\"{}\",".format(n)
    si += "\"username\":\"{}\"".format(id)
    si += ",\"passwd\":\"{}\"".format(passwd)
    si += ",\"port\":\"{}\"".format(port)

    si += "}"
    s += "{},".format(si)
s = s[0:-1] + "]"
print(s)
