import sys
import json
from pypresence.exceptions import InvalidID, InvalidPipe


def get_rpc_update():
    if sys.platform in ['Windows', 'win32', 'cygwin']:
        try:
            from api.windows import get_title, get_process_id, get_status

            process_name = "photoshop.exe"
            pid = get_process_id(process_name)
            window_title = get_title(pid)
            app_state = "Editing: {}".format(get_status(window_title))

            rpc_update = {'state': app_state,
                          'small_image': "photoshop_small",
                          'large_image': "photoshop_large",
                          'large_text': "Adobe Photoshop",
                          'small_text': "Editing",
                          'details': "CC 2018"}
            return rpc_update

        except ImportError:
            print("Make sure you have pywin32 installed, for more info read README.md")

    elif sys.platform in ['Mac', 'darwin', 'os2', 'os2emx']:
        print("Macos support is currently not available.")
        sys.exit(0)


def exception_handler(exception, future):
    print("")
