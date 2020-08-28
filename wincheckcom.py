import win32com.client
import pythoncom
import webbrowser
import platform

DOM =[r"USB\VID_1A86&PID_7523\5&60E5EF5&0&5",r"USB\VID_F055&PID_9800&MI_01",r"USB\VID_28E9&PID_018A"]

def listdevice(COM):
	wmi = win32com.client.GetObject ("winmgmts:")
	usbStatus = []
	for usb in wmi.InstancesOf ("win32_pnpentity"):
	#print(usb.name)
		if usb.PNPDeviceID.find(COM)>-1:
			usbStatus.append({
				"name":usb.Name,
				"errCode":usb.ConfigManagerErrorCode,
				"usbsta":usb.Status
				}
				)
	return usbStatus
def CheckCOM(device):
  if(platform.system()=='Windows'):
      #device = listdevice()
      if  len(device):
        for item in device:
          if item["usbsta"] == 'OK':
            print("驱动正常")
            break
          else:
            if item["errCode"] == 52:
              print("请使用360驱动大师更新驱动")
              webbrowser.open_new(r"http://note.youdao.com/noteshare?id=ae81b2a515c1390f76a3f307e26d32de")
            elif item["errCode"] == 31:
              print("请在设备管理中更改ch340驱动端口")
              webbrowser.open_new(r"http://note.youdao.com/noteshare?id=3506c58851ef078b4c5e75717d54b550")
            elif item["errCode"] ==1 or item["errCode"] ==28:
              print("请安装驱动")
              webbrowser.open_new(r"http://www.wch.cn/download/CH341SER_EXE.html")
            elif item["errCode"] == 22:
              print("驱动被禁用")
            else:
                print("未知错误："+item["errCode"])
      else:
          print("没有插设备")
    			
if __name__ == "__main__":
  for i in DOM:
    Com = listdevice(i)
    CheckCOM(Com)
