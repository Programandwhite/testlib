import serial
import serial.tools.list_ports as list_ports
import platform
def serialList():
  if platform.system() == 'Windows':
    import win32com.client
    import re
    wmi = win32com.client.GetObject ("winmgmts:")
    for usb in wmi.InstancesOf ("win32_pnpentity"):
      deviceId = usb.PNPDeviceID
      m = re.search(r'VID_([0-9a-f]{4})(&PID_([0-9a-f]{4}))?(&MI_(\d{2}))?(\\(\w+))?', deviceId, re.I)
      if m:
        vid = int(m.group(1), 16)
        pid = int(m.group(3), 16)
        if (usb.name.find('COM') > -1 or usb.name.find('CDC') > -1):
          if ((pid == 38912 and vid == 61525) or (pid == 394 and vid == 10473)):
            return {
              'deviceConnect': 1,
              'comStatus': usb.ConfigManagerErrorCode,
              'portList': [{
                'name': 'meowbit',
                'type': 'serial',
                'peripheralId': 'usb_meowbit',
                'pid': pid,
                'vid': vid
              }]
            }
    return {
      'deviceConnect': 0
    }
  else:
    serialPortList = []
    for port in list_ports.comports():
      if port.pid and port.vid:
        serialPortList.append({'name': port.description, 'type':'serial', 'peripheralId': port.device, 'pid': port.pid, 'vid': port.vid})
    if serialPortList:
      return {
        'deviceConnect': 1,
        'portList': serialPortList
      }
    else:
      return {
        'deviceConnect': 0
      }
print(serialList())