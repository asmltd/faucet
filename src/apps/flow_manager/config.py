# Configuration for Flow Manager UI
# Created by Hariharaselvam Balasubramanian
# This will read ../../cfg/etc/ryu/faucet/gauge.conf file and use its configurations for Flow manger UI


def dict_insert_or_append(adict, key, val):
    """Insert a value in dict at key if one does not exist
    Otherwise, convert value to list and append
    """
    if key in adict:
        if type(adict[key]) != list:
            adict[key] = [adict[key]]
        adict[key].append(val)
    else:
        adict[key] = val


def ttree_to_json(ttree, level=0):
    result = {}
    for i in range(0, len(ttree)):
        cn = ttree[i]
        try:
            nn = ttree[i + 1]
        except:
            nn = {'level': -1}

        # Edge cases
        if cn['level'] > level:
            continue
        if cn['level'] < level:
            return result

        # Recursion
        if nn['level'] == level:
            dict_insert_or_append(result, cn['name'], cn['value'])
        elif nn['level'] > level:
            rr = ttree_to_json(ttree[i + 1:], level=nn['level'])
            dict_insert_or_append(result, cn['name'], rr)
        else:
            dict_insert_or_append(result, cn['name'], cn['value'])
            return result
    return result


def get_couch_db_info_from_config_file(config_file_path):
    cf = open(config_file_path, "r")
    conf_text = cf.read()
    pointer = []
    conf_text_rows = conf_text.split("\n")
    for row in conf_text_rows:
        comp = row.lstrip()
        pair = comp.split(":")
        key = pair[0]
        value = pair[1] if len(pair) > 1 else " "
        value = value.rstrip()
        value = value.rstrip("'")
        value = value.lstrip()
        value = value.lstrip("'")
        indent = row.find(comp)
        if key == "":
            continue
        pointer.append({"name": key, "value": value, "level": indent / 4})
    result = ttree_to_json(pointer, 0)
    return result['dbs']['couchdb']


config_file_path = "../../cfg/etc/ryu/faucet/gauge.conf"
couch_config = get_couch_db_info_from_config_file(config_file_path)

couch_db_url = "http://" + couch_config["db_ip"] + ":" + couch_config["db_port"]+"/"
flowsdb = couch_config["flows_doc"]
switches = couch_config["switches_doc"]
flows_design = "flows"
flows_view = "flow"

flask_host = "0.0.0.0"
flask_port = 5000

userdb = "fmusers"
user_design = "users"
user_view = "users"


test_username = "testflowmgr@faucetsdn.org"
test_password = "testflowmgr"
