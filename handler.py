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

            # Information to publically show to Discord
            app_info = get_process_info()
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

        except ImportError:
            logging.error(
                "Make sure you have 'pywin32' installed, for more info read README.md")
            sys.exit(1)
        except TypeError:
            logging.error("No Adobe Applications running!")
        except (KeyboardInterrupt, SystemExit):
            logging.info("Stopped Adobe RPC!")
            sys.exit(0)

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