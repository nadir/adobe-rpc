import win32gui
import win32process
import psutil
import json
import ntpath


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


with open('meta.json') as f:
    data = json.load(f)


def get_process_info():
    for element in data:
        process_name = element['processName']
        for process in psutil.process_iter():
            process_info = process.as_dict(attrs=['pid', 'name'])
            if process_info.get('name') and process_info.get('name').lower() in process_name:
                element['pid'] = process_info['pid']
                return element


def get_status(app_info, title):
    if app_info['largeText'].lower() in title.lower() and app_info['splitBy'] != " - ":
        return "{}: IDLE".format(app_info['smallText'])
    else:
        title_seperated = title.split(app_info['splitBy'])
        if app_info['splitBy'] == " - ":
            title_basename = ntpath.basename(
                title_seperated[app_info['splitIndex']])
            return "{}: {}".format(app_info['smallText'], title_basename)
        else:
            return "{}: {}".format(app_info['smallText'], title_seperated[app_info['splitIndex']])
