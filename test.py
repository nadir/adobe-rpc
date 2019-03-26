from api.windows import get_title, get_process_id, get_status
import time


while True:

    process_name = "afterfx.exe"
    pid = get_process_id(process_name)
    window_title = get_title(pid)
    print(window_title)
    time.sleep(6)
