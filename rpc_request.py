#!/usr/bin/env python

import requests
import json
import configparser
import pathlib
from pathlib import Path

def get_config(file=None):
    if (file == None):
        file = str(pathlib.Path.home() / ".bitcoin" / "bitcoin.conf")

    f = open(file,"r")
    data = f.read()
    f.close()

    config=configparser.ConfigParser()
    config.read_string(f"""[default]{data}""")

    return config['default']

def send_request(method="help", params=[]):    
        

    config=get_config()

    testnet=int(config.get('testnet',0))
    port=int(config.get('port',8332 if not testnet else 18332))
    user=str(config.get('rpcuser',''))
    password=str(config.get('rpcpassword',''))

    url = f"http://localhost:{port}/"

    payload = {
        "version" : "1.1",
        "method": method,
        "params": params,
        "id": 0,
    }

    response = requests.post(url, json=payload, auth=(user,password))
    return response
