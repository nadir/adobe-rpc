from pypresence import Presence
import logging
import handler
import time
import sys

# Client Setup
client_id = "482150417455775755"
rich_presence = Presence(client_id)

# Logging config
logging.basicConfig(level=logging.DEBUG, format=('%(asctime)s - %(levelname)s - ' +
                                                 '%(funcName)s - %(message)s'),
                    datefmt='%d-%m-%y %H:%M:%S')

# Attempts to find Discord
def connect_loop(retries=0):
    logging.info("Connecting rich presence...")
    
    # Retry limit of 10 attempts
    if retries < 10:
        try:
            logging.info("Conneting to RPC...")
            rich_presence.connect()
            update_loop()
        except:
            logging.error("Error connecting to Discord! Retrying...")
            retries += 1
            connect_loop(retries)
    else:
        logging.exception("Failed to connect to Discord! Printing stacktrace and exiting...")


# Updates Discord of current activity
def update_loop():
    # Sets startup time for the application
    start_time = int(time.time())
    try:
        while True:
            # Creates rpc_data dictionary to parse data to handle
            rpc_data = handler.get_rpc_update()
            # 'handler.py' data is imported into here
            rich_presence.update(state=rpc_data['state'],
                                 small_image=rpc_data['small_image'],
                                 large_image=rpc_data['large_image'],
                                 large_text=rpc_data['large_text'],
                                 small_text=rpc_data['small_text'],
                                 details=rpc_data['details'],
                                 start=start_time)
    # When either Discord or a supported Adobe product is not detected...
    except:
        # Clear rpc_data
        rich_presence.clear()
        logging.warning(
            "Not detecting Adobe applications! Are you sure your running a compatible application?")
        # Update Discord
        update_loop()

# Main instance
if __name__ == "__main__":
    try:
        logging.info("Started Adobe RPC!")
        connect_loop()
    except:
        logging.info("Stopped Adobe RPC!")
        sys.exit(0)
