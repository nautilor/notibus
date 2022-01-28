
#!/usr/bin/env python3
import gi.repository.GLib
import dbus
from dbus.mainloop.glib import DBusGMainLoop

def notifications(bus, message):
    notification = {}
    args = message.get_args_list()
    for i in range(0, len(args)):
        if i == 4:
            notification['title'] = str(args[i])
        elif i == 3:
            notification['message'] = str(args[i])
    if not notification == {}:
        print(f"{notification['title']} - {notification['message']}")

if __name__ == "__main__":  
    DBusGMainLoop(set_as_default=True)
    bus = dbus.SessionBus()
    bus.add_match_string_non_blocking("eavesdrop=true, interface='org.freedesktop.Notifications', member='Notify'")
    bus.add_message_filter(notifications)
    mainloop = gi.repository.GLib.MainLoop()
    mainloop.run()
