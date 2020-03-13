from Quartz import CGWindowListCopyWindowInfo, kCGNullWindowID, kCGWindowListOptionAll
import psutil
import json
import logging

# Processes title of application from PID
def get_title(pid):
    logging.debug("Getting title for the application...")

    def callback(hwnd, hwnds):
        if win32gui.IsWindowVisible(hwnd) and win32gui.IsWindowEnabled(hwnd):
            _, found_pid = win32process.GetWindowThreadProcessId(hwnd)
            if found_pid == pid:
                hwnds.append(hwnd)
    hwnds = []
    win32gui.EnumWindows(callback, hwnds)
    window_title = win32gui.GetWindowText(hwnds[-1])
    logging.debug("Title of application: " + window_title)
    return window_title


# Parses metadata for associated applications
with open('meta.json') as f:
    logging.debug("Loading 'meta.json'")
    data = json.load(f)

# Process information of application
def get_process_info():
    logging.debug("Getting process information...")
    for element in data:
        # Finds process name for Adobe applications
        process_name = element['processNameMac']
        for process in psutil.process_iter():
            # Finds pid through iteration
            process_info = process.as_dict(attrs=['pid', 'name'])
            if process_info['name'].lower() in process_name:
                element['pid'] = process_info['pid']
                logging.debug("Process returns with info: " +
                            str(process_info))
                return element

# Status of application
def get_status(app_info, title):
    # Idle detection
    if app_info['largeText'].lower() in title.lower() and app_info['splitBy'] != " - ":
        logging.debug("Returning to Discord that you are detected as idle...")
        return "{}: IDLE".format(app_info['smallText'])
    # Project detection
    else:
        logging.debug("Not idling! Finding project...")
        title_seperated = title.split(app_info['splitBy'])
        if app_info['splitBy'] == " - ":
            title_basename = ntpath.basename(
                title_seperated[app_info['splitIndex']])
            logging.debug("Returning the title of the project")
            return "{}: {}".format(app_info['smallText'], title_basename)
        else:
            return "{}: {}".format(app_info['smallText'], title_seperated[app_info['splitIndex']])
