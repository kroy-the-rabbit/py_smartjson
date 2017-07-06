class SmartDevice:
    c_TEMP=194
    c_REALLOC_SECTORS=5
    c_CURRENT_PENDING_SECTORS=197
    c_HOURS=9
    def __init__(self, device):
	self.dev = device.name
	self.model = device.model
	self.serial = device.serial
	self.temp = device.attributes[self.c_TEMP].raw
	self.reallocated_sectors = device.attributes[self.c_REALLOC_SECTORS].raw
	self.capacity =  device.capacity
	self.firmware = device.firmware
	self.smart_status = device.assessment
	self.ssd = device.is_ssd
        self.hours = device.attributes[self.c_HOURS].raw
        self.full_attributes = device.attributes

