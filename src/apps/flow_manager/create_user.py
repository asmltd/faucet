# Create User for Flow Manager UI
# This will create User dcoument in couch db and create test user
# It wont affect couch db's default user database

import requests
import json
import config

dbhost = config.couch_config["db_ip"].strip()
dbport = config.couch_config["db_port"].strip()
dbuser = config.couch_config["db_username"].strip()
dbpass = config.couch_config["db_password"].strip()
userdatabase = config.userdb
username = config.test_username
password = config.test_password
role = "1"


user_db_with_credentials="http://" + dbuser + ":" + dbpass + "@" + dbhost + ":" + dbport + "/" + userdatabase + "/"
print "Create User Database for Flow Manager UI"
print "__________________________________________"

print "Delete user database ( if exists )"
deletedb = requests.delete(user_db_with_credentials)
print deletedb.content
print "__________________________________________"


print "Create user database"
createdb = requests.put(user_db_with_credentials)
print createdb.content
print "__________________________________________"


print "Create view for user database"
view_data = {'_id': '_design/users', 'views': {'users': {'map': 'function(doc){ emit(doc._id, doc)}'}}}
view_data = json.dumps(view_data)
createvw = requests.put(
    url=user_db_with_credentials + "_design/users/",
    data=view_data
)
print createvw.content
print "__________________________________________"


print "Create Test user"
createuser = requests.post(
    url=user_db_with_credentials,
    json={"username": username, "password": password, "role": role}
)
print createuser.content
print "__________________________________________"
