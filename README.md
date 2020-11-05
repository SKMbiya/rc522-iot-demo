rc522-iot-demo
==============

A demonstration application that makes use of the rc522-iot API to interface with the mfrc522 RFID card reader and a Raspberry Pi Zero W

Requirements
--------
This code requires you to install the Blynk python library and can be done by running the following command ``pip install blynk-library-python``
You also need to copy the rc522_iot API module into your working directory and then import the rc522_iot API module at the top of your script. It can be found and cloned [here](https://github.com/SKMbiya/rc522-iot).
It is also recommended that you make use of a python virtual environment before installing the libraries, by making use of tools such as venv or virtualenv.

Usage
--------

To use the demonstration application you would need to do the following:
* Connect your Raspberry Pi and RFID card reader as described in Table 1
* Install the Blynk Android or iOS mobile application and create a new project
* Design your application as below:\
[Blynk mobile application layout](https://i.imgur.com/Qaw9UDV.jpg)
* Configure the virtual pins of the application components as follows as described in Table 2
* Enter the authentication code sent to you by Blynk via email in line 8 of the .py script
* Run the rc522_iot.py file in your terminal to start the Blynk server

Table 1:
| Name | Pin # | Pin name   |
|:------:|:-------:|:------------:|
| SDA  | 24    | GPIO8      |
| SCK  | 23    | GPIO11     |
| MOSI | 19    | GPIO10     |
| MISO | 21    | GPIO9      |
| IRQ  | None  | None       |
| GND  | Any   | Any Ground |
| RST  | 22    | GPIO25     |
| 3.3V | 1     | 3V3        |

[Source](https://github.com/mxgxw/MFRC522-python/blob/master/README.md)

Table 2:
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

This demonstration application made use of [Volodymyr Shymanskyy's](https://github.com/vshymanskyy) python blynk client library. It can be found [here](https://github.com/vshymanskyy/blynk-library-python)

Contributors
------------
* EEE3097S Group 19:

Iviwe Malotana: [@IviweMalotana](https://github.com/IviweMalotana)\
Samuel Mbiya: [@SKMbiya](https://github.com/SKMbiya)

License
-------

This project is under the MIT License
