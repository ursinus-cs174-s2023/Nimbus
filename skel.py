import json
import subprocess
users = json.load(open("s2024.json"))
for user in users:
    username = user["username"]
    cmd = ["sudo", "cp", "-r", "/etc/skel/.", "/home/{}".format(username)]
    print(cmd)
    subprocess.call(cmd)
    # chown -R $i /home/$i
    cmd = ["sudo", "chown", "-R", username, "/home/{}".format(username)]
    print(cmd)
    subprocess.call(cmd)
