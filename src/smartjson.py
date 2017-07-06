from SmartDevice import SmartDevice
from pySMART import DeviceList

import jsonpickle



devlist = DeviceList()

devices = {}


i = 0
while i < len(devlist.devices):
    d = SmartDevice(devlist.devices[i])
    devices[d.dev] = d
    i += 1

print (jsonpickle.encode(devices))
