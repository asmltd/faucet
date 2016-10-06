#Flow Manager UI


## Reading Real-time Information On Switches

It is difficult to read the real-time information on flows installed on the switches managed by a controller. In addition, it is difficult to efficiently manage the Flow of a switch. 


## Solution Approach

Have developed the User Interface to represent the switch’s data in a legible and readable tables. The UI interface is enhanced with several functionalities like View, Search, and Delete in the interface. 
 
  
## Key functionalities
- Manage flows ( add, edit and delete flows )
- Graphical and Tabulated view of Flows with pagination
- Manage users
- Secure API ( re-usable in other application )
 
## Deployment Details


**Pre-requisites**:  Ubuntu OS,Python2.7,Nginx, and UWSGI


## Folder structure

    faucet
    |
    |
    |---> docker
    |---> src
    |     |
    |     |---> apps
    |     |     |
    |     |     |---> flow_manager  
    |     |     |     |
    |     |     |     |---> docs ( all documents goes here )
    |     |     |     |     |
    |     |     |     |     |---> Angularjs.rst
    |     |     |     |     |---> BootsrtapTemplate.rst
    |     |     |     |     |---> D3jsLibrary.rst
    |     |     |     |     |---> FlaskFramework.rst
    |     |     |     |     |---> RobotFramework.rst
    |     |     |     | 
    |     |     |     |---> ext_libs ( bootstrap and other external libraries )
    |     |     |     |---> images ( logo images )
    |     |     |     |---> modules ( Each page html and js files with in their sub directories )
    |     |     |     |---> onf_libs ( angularjs, and js file, admin lte template files  )
    |     |     |     |---> tests ( robot framework test suite )
    |     |     |     |---> config.py ( fetches config from etc/ryu/faucet/gauge.conf )
    |     |     |     |---> create_user.py ( Creates user database and test user )
    |     |     |     |---> flow_manager_server.py ( Flask server file )
    |     |     |     |---> index.html ( default page from flow manager ui )
    |     |     |     |---> home.html ( home page from flow manager ui )



   






