import json
import sys
from decimal import Decimal
from iotticket.models import device
from iotticket.models import criteria
from iotticket.models import deviceattribute
from iotticket.models import datanodesvalue
from iotticket.client import Client


with open('config.json') as data_file:
    data = json.load(data_file)

username = data["username"]
password = data["password"]
deviceId = data["deviceId"]
baseurl = data["baseurl"]
c = Client(baseurl, username, password)

# ---------- new device
# d = device()
# d.set_name("OPCUA")
# d.set_manufacturer("Toni Hanninen")
# d.set_type("student")
# d.set_description("data from python opcua client")
# d.set_attributes(deviceattribute("a","b"), deviceattribute("c","d"), deviceattribute("key","value"))
# register device demo

# print(c.registerdevice(d))




def send(counter,expression,random):
    nv = datanodesvalue()
    nv.set_name("Counter")
    nv.set_path("Counter")
    nv.set_dataType("double")
    nv.set_value(float(counter))

    nv1 = datanodesvalue()
    nv1.set_name("Expression")
    nv1.set_path("Expression")
    nv1.set_dataType("double")
    nv1.set_value(float(expression))

    nv2 = datanodesvalue()
    nv2.set_name("Random")
    nv2.set_path("Random")
    nv2.set_dataType("double")
    nv2.set_value(float(random))

    print(c.writedata(deviceId, nv, nv1, nv2))