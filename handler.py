import sys
import logging

# Grabs data from applications
def get_rpc_update():
    logging.debug("Checking OS...")
    # Supported operating systems
    if sys.platform in ['Windows', 'win32', 'cygwin']:
        try:
            logging.debug("Importing Windows specific modules...")
            from api.windows import get_title, get_process_info, get_status

            app_info = get_process_info()

            # Information to publically show to Discord
            if app_info != None:
                app_title = get_title(app_info['pid'])
                app_state = get_status(app_info, app_title)

                # Dictionary setup to return application info
                rpc_update = {'state': app_state,
                            'small_image': app_info['smallImageKey'],
                            'large_image': app_info['largeImageKey'],
                            'large_text': app_info['largeText'],
                            'small_text': app_info['smallText'],
                            'details': app_info['largeText']}

                # Returns data from processing the application data
                return rpc_update

            # If 'get_process_info()' doesn't find a proper 'processName' element, stop application
            elif app_info == None:
                logging.error("Unable to find process")

        except ImportError:
            logging.error(
                "Required dependency is not found! Did install all dependencies? Check with the README")
            sys.exit(1)
        except TypeError:
            logging.error("No Adobe Applications running!")

    # Unsupported operating systems for the time being
    elif sys.platform in ['Mac', 'darwin', 'os2', 'os2emx']:
        logging.warning("MacOS support is currently not available. Closing...")
        sys.exit(0)

    else:
        logging.error("Unknown operating system! Exiting...")
        logging.error("If you believe this is an error. Submit a bug report.")

        sys.exit(0)
def exception_handler(exception, future):
    logging.exception("Something bad happened. Printing stacktrace...")