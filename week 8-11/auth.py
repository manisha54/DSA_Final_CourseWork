import json

from requests_toolbelt import user_agent

f = open(r"week 8-11/users.json")

users = json.load(f)


def login(email, password):
    with open(r"week 8-11/users.json", "r") as jsonFile:
        if email in users["users"] and users["users"][email] == password:
            return True
        return False


def signUp(email, password):
    with open(r"week 8-11/users.json", "w") as jsonFile:
        users["users"][email] = password
        json.dump(users, jsonFile)
