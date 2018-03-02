import scitwin
import scitwin.traynotification
import os

#scitwin.sendMessage()
iconPath = os.path.join(os.path.expanduser('~'),"Desktop","logo-scit.ico")
print(iconPath)
scitwin.WindowsBalloonTip("Notificaciones SCIT", "Somos Grupo SCIT, y te ofrecemos un mundo de soluciones", icon=iconPath)