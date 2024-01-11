First run

python makepasswds.py > s2024.jsonThen, runpython makeuserfile.py

This will create a file users.txt, which you can use to create users in batch mode:https://hostingultraso.com/help/ubuntu/creating-ubuntu-user-accounts-batch-mode
You'll then want to run the filepython skel.py

To make sure the user accounts have .bashrc setup so that their terminals have nice formatting when they login.
