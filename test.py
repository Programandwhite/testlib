import win32com.client
import pythoncom
import webbrowser

def listdevice():
	mkhalo = r"USB\VID_1A86&PID_7523\5&60E5EF5&0&5"
	meow32_ID = r"USB\VID_F055&PID_9800&MI_01"
	mewbit_ID = r"USB\VID_28E9&PID_018A"
	wmi = win32com.client.GetObject ("winmgmts:")
	usbStatus = []
	for usb in wmi.InstancesOf ("win32_pnpentity"):
	#print(usb.name)
		if usb.PNPDeviceID.find(mkhalo)>-1 or usb.PNPDeviceID.find(meow32_ID)>-1 or usb.PNPDeviceID.find(mewbit_ID) >-1:
			usbStatus.append({
				"name":usb.Name,
				"errCode":usb.ConfigManagerErrorCode,
				"usbsta":usb.Status
				}
				)
	return usbStatus

device = listdevice()
if  len(device):
	for item in device:
		if item["usbsta"] == 'OK':
			webbrowser.open_new(r"http://note.youdao.com/noteshare?id=ae81b2a515c1390f76a3f307e26d32de")
			break
		else:
			if item["errCode"] == 52:
				print("请使用360驱动大师更新驱动")
				webbrowser.open_new("www.baidu.com")
			elif item["errCode"] == 31:
				print("请在设备管理中更改ch340驱动端口")
			elif item["errCode"] ==1 or item["errCode"] ==28:
				print("请安装驱动")
			elif item["errCode"] == 22:
				print("驱动被占用")
			print(item)
else:
	print("没有插如固件")