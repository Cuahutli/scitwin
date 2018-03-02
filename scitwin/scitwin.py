import ctypes as ct
import win32api
import win32con
#from win32api import Beep, GetCursorPos, SetCursorPos, MessageBox
#from win32con import MB_OK, MB_YESNOCANCEL
#import pywin32
import string

def availableDisksWithCtypes():
    drives = string.ascii_uppercase
    libc = ct.cdll.msvcrt
    driveList = libc._getdrives()
    for n in range(len(drives)):
        mask = 1 << n
        if driveList & mask:
            print(drives[n], 'is available')


"""
    Get list of letter to available disks in your host
"""
def availableDisks():
    drives = win32api.GetLogicalDriveStrings()
    drives = [x[0] for x in drives.split('\0')[:-1]]
    return drives

"""
    send message using windows API
"""
def sendMessage(title="Ejemplo Windows API", message="Listo", type_message=win32con.MB_OK):
    #win32api.Beep(200, 200)
    win32api.MessageBeep(win32con.MB_ICONASTERISK)
    win32api.MessageBox(0, message, title, type_message)

if __name__ == "__main__":

    print(scitwin.availableDisks())
    scitwin.sendMessage("Probando mensajes", "Desde un script con python")