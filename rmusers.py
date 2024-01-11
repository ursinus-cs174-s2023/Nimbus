import json
import subprocess
users = json.load(open("s2023.json"))
for user in users:
    cmd = ["sudo", "deluser", "--remove-home", user["username"]]
    print(cmd)
    subprocess.call(cmd)
