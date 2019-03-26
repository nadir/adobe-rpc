from window import get_hwnds, get_process_id, get_status
from pypresence import Presence, Activity
import win32gui
import time


client_id = "482150417455775755"
rich_presence = Presence(client_id)
rich_presence.connect()

start_time = int(time.time())

print("Started Photoshop Rich Presence ✓")


try:
    while True:
        process_name = "photoshop.exe"
        pid = get_process_id(process_name)
        if pid == None:
            print(process_name + " is not open!")
            break
        hwnds = get_hwnds(pid)
        window_title = win32gui.GetWindowText(hwnds[-1])
        app_state = "Editing: {}".format(get_status(window_title))
        rich_presence.update(state=app_state,
                             small_image="photoshop_small",
                             large_image="photoshop_large",
                             large_text="Adobe Photoshop",
                             small_text="Editing",
                             details="CC 2018",
                             start=start_time)
        time.sleep(15)
except KeyboardInterrupt:
    print("Stopped Photoshop Rich Presence ✘")
