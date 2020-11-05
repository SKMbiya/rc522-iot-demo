rc522-iot-demo
==============

A demonstration application that makes use of the rc522-iot API to interface with the mfrc522 RFID card reader and a Raspberry Pi Zero W

Requirements
--------
This code requires you to install the Blynk python library and can be done by running the following command ``pip install blynk-library-python``
You also need to copy the rc522_iot API module into your working directory and then import the rc522_iot API module to at the top of your script. It can be found and cloned [here](https://github.com/SKMbiya/rc522-iot).
It is also recommended that you make use of a python virtual environment before installing the libraries, by making use of tools such as venv or virtualenv.

Usage
--------

To use the demonstration application you would need to do the following:
* Install the Blynk Android or iOS mobile application and create a new project
* Design your application as below:\
[Blynk mobile application layout](https://imgur.com/Qaw9UDV)
* Configure the virtual pins of the application components as follows as described in Table 1
* Enter the authentication code sent to you by Blynk via email in line 8 of the .py script
* Run the rc522_iot.py file in your terminal to start the Blynk server

Table 1:
| Name | Component Type | Virtual Pin #  |
|:------:|:-------:|:------------:|
| SPI | Styled Switch Button | 2 |
| Prompt | Value Display Label | 10 |
| Response | Value Display Label | 9 |
| NameAndID | Styled Push Button | 0 |
| Add Member | Styled Push Button | 1 |
| Reset | Styled Push Button | 3 |

Credits
-------

This demonstration application made use of [Volodymyr Shymanskyy's](https://github.com/vshymanskyy) class to interface with the NFC reader Module MFRC522 on the Raspberry Pi. It can be found [here](https://github.com/vshymanskyy/blynk-library-python)

Contributors
------------
* EEE3097S Group 19:

[@IviweMalotana](https://github.com/IviweMalotana)\
[@SKMbiya](https://github.com/SKMbiya)

License
-------

This project is under the MIT License
