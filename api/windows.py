import win32gui
import win32process
import psutil


def get_process_id(processName):
    for process in psutil.process_iter():
        try:
            processinfo = process.as_dict(attrs=['pid', 'name'])
            if processinfo['name'].lower() in processName.lower():
                return processinfo['pid']
        except psutil.NoSuchProcess:
            return None


def get_title(pid):
    def callback(hwnd, hwnds):
        if win32gui.IsWindowVisible(hwnd) and win32gui.IsWindowEnabled(hwnd):
            _, found_pid = win32process.GetWindowThreadProcessId(hwnd)
            if found_pid == pid:
                hwnds.append(hwnd)
    hwnds = []
    win32gui.EnumWindows(callback, hwnds)
    window_title = win32gui.GetWindowText(hwnds[-1])
    return window_title


def get_status(title):
    if "Adobe Photoshop".lower() in title.lower():
        return "IDLE"
    else:
        title_seperated = title.split(" @ ")
        return title_seperated[0]
