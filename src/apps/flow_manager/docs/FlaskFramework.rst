Faucet Flow Manager UI
Documentation for Flask Framework
Date: October 4th, 2016
Author: Hariharaselvam Balasubramanian

About Flask:
Flask is a micro web framework written in Python and based on the Werkzeug toolkit and Jinja2 template engine. It is BSD licensed.

Host ip and port number are given at config.py file. Host ip "0.0.0.0" will make the application available on public. Host ip "127.0.0.1" will make the application available only on local machin where the flask deployed.
Flask default port is 5000.

How to run:

    python run.py > access.log &

REST API

REST: Representational State Transfer.

    It’s an arrangement of functions on which the testers performs requests and receive responses. In REST API interactions are made via HTTP protocol.
REST also permits communication between computers with each other over a network.
For sending and receiving messages, it involves using HTTP methods, and it does not require a strict message definition, unlike Web services.
REST messages often accepts the form either in form of XML, or JavaScript Object Notation (JSON).

4 Commonly Used API Methods:-

    GET: – It provides read only access to a resource.
    POST: – It is used to create or update a new resource.
    PUT: – It is used to update or replace an existing resource or create a new resource.
    DELETE: – It is used to remove a resource.

In Faucet Flow Manager UI run.py is the flask code it contains following endpoints and annotations:
Annotations:
    1. Cross Origin ( in-build from flask cors origin library )
    2. Login Required ( created at this project )

Endpoints:
    1. home
        url             : /
        method          : GET
        response        : index.html
        parameters      : no
        login required  : no

    2. auth
        url             : auth
        method          : POST
        response        : JSON
        parameters      : username, password
        login required  : no

    3. userlist
        url             : get_all_users
        method          : GET
        response        : JSON
        parameters      : no
        login required  : yes

    4. topology
        url             : get_toplogy
        method          : GET
        response        : JSON
        parameters      : no
        login required  : yes

    5. switch_info
        url             : get_switch_info
        method          : POST
        response        : JSON
        parameters      : page, size
        login required  : yes

    6. switch_tree
        url             : get_switch
        method          : GET
        response        : JSON
        parameters      : no
        login required  : yes

    7. add_flow
        url             : add_flow
        method          : POST
        response        : JSON
        parameters      : {}
        login required  : yes

    8. update_flow
        url             : update_flow
        method          : POST
        response        : JSON
        parameters      : _id,_rev
        login required  : yes

    9. delete_flow
        url             : update_flow
        method          : POST
        response        : JSON
        parameters      : id,rev
        login required  : yes

    10. delete_user
        url             : delete_user
        method          : POST
        response        : JSON
        parameters      : id,rev
        login required  : yes

    11. flows_list
        url             : get_all_flows
        method          : GET
        response        : JSON
        parameters      : no
        login required  : yes

    12. get_flow_info
        url             : get_flow_info
        method          : POST
        response        : JSON
        parameters      : flow_id
        login required  : yes

    13. create_user
        url             : register_user
        method          : POST
        response        : JSON
        parameters      : username,password,role
        login required  : yes

    14. session
        url             : check_session_data
        method          : POST
        response        : JSON
        parameters      : username,password,role
        login required  : no

    15. logout
        url             : logout
        method          : GET
        response        : JSON
        parameters      : no
        login required  : yes
