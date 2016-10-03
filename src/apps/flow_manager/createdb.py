import requests
import json

dbhost = "localhost"
dbport = "5984"
dbuser = "root"
dbpass = "asm123"
database = "faucet"
userdatabase = "users"
username = "testflowmgr@faucetsdn.org"
password = "testflowmgr"
role = "1"
data = {"username": username, "password": password, "role": role}
createdb = requests.put("http://"+dbuser+":"+dbpass+"@"+dbhost+":"+dbport+"/"+userdatabase+"/")
print createdb
view_data = {'_id': '_design/users','views': {'users': {'map': 'function(doc){ emit(doc._id, doc)}'}}}
view_data = json.dumps(view_data)
createvw = requests.put(url="http://" + dbuser + ":" + dbpass + "@" + dbhost + ":" + dbport + "/" + userdatabase + "/_design/users/",
    data=view_data)

print createvw
createuser =requests.post(url="http://"+dbhost+":"+dbport+"/"+userdatabase+"/", json={"username": username, "password": password, "role": role})
print createuser
