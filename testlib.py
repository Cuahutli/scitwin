import scitwin
import os

#scitwin.sendMessage()
iconPath = os.path.join(os.path.expanduser('~'),"Desktop","logo-scit.ico")
scitwin.TrayNotification("Notificaciones SCIT", "Somos Grupo SCIT, y te ofrecemos un mundo de soluciones", icon=iconPath)