**Faucet Flow Manager UI**

Documentation for Robot-Framework

Date: October 4th, 2016

Author: Hariharaselvam Balasubramanian

Robot Framework:
    Robot Framework is a generic test automation framework for acceptance testing and acceptance test-driven development (ATDD). It has easy-to-use tabular test data syntax and it utilizes the keyword-driven testing approach. Its testing capabilities can be extended by test libraries implemented either with Python or Java, and users can create new higher-level keywords from existing ones using the same syntax that is used for creating test cases.


Install required modules:

    pip install robotframework

    pip install -U selenium

    pip install robotframework-selenium2library


How to run:

    pybot -d log_files_path faucet.robot

Requirements:

    Firefox version 45 ( not latest version supports robot framework ) it will have selenium driver.
    Other browsers we should download and install

Variables:
    Flow manager UI's url, username, password can be changed