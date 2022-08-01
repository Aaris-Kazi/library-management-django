# import re
# import subprocess
# device_re = re.compile(b"Bus\s+(?P<bus>\d+)\s+Device\s+(?P<device>\d+).+ID\s(?P<id>\w+:\w+)\s(?P<tag>.+)$", re.I)
# df = subprocess.check_output("lsusb")
# devices = []
# for i in df.split(b'\n'):
#     if i:
#         info = device_re.match(i)
#         if info:
#             dinfo = info.groupdict()
#             dinfo['device'] = '/dev/bus/usb/%s/%s' % (dinfo.pop('bus'), dinfo.pop('device'))
#             devices.append(dinfo)
            
# print(devices)
# import win32com.client

# wmi = win32com.client.GetObject ("winmgmts:")
# for usb in wmi.InstancesOf ("Win32_USBHub"):
#     print(usb.DeviceID)

# USB\VID_1BCF&PID_2A02\01.00.00
# USB\ROOT_HUB30\4&29E0B25B&0&0
# USB\ROOT_HUB30\4&365005&0&0

# USB\VID_1BCF&PID_2A02\01.00.00
# USB\ROOT_HUB30\4&29E0B25B&0&0
# USB\VID_0781&PID_5571\4C530001281130122052
# USB\ROOT_HUB30\4&365005&0&0

# wmic logicaldisk where drivetype=2 get deviceid, volumename, description
# Description     DeviceID  VolumeName
# Removable Disk  E:        NIBBI

# import usb.core
# for dev in usb.core.find(find_all=True):
#     print(dev)
import os
# os.system('wmic logicaldisk where drivetype=2 get deviceid, volumename, description')
x = os.system('wmic logicaldisk where drivetype=2 get deviceid, volumename, description')
print(x)
x =os.getcwd()
print(x)
os.chdir('E:/')
# os.system('cd..')
x = os.system('dir')
print(x)