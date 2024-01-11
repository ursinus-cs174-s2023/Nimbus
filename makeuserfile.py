import json
import subprocess
users = json.load(open("s2024.json"))
group = "cs174s2024"
fout = open("users.txt", "w")
for user in users:
    username = user['username']
    passwd = user['passwd']
    fout.write("{}:{}::{}::/home/{}:/bin/bash\n".format(username, passwd, group, username))
fout.close()
