from pypresence import Presence, activity
import logging
import handler
import time
import sys

# Client Setup
client_id = "482150417455775755"
rich_presence = Presence(client_id)

# Logging config
logging.basicConfig(level=logging.INFO, format=('%(asctime)s - %(levelname)s - ' +
                                                '%(funcName)s - %(message)s'),
                    datefmt='%d-%m-%y %H:%M:%S')

# Binds RPC connection to Discord
def connect():
    logging.info("Connected to rich presence!")
    return rich_presence.connect()

# Attempts to find Discord
def connect_loop(retries=0):
    if retries > 10:
        return
    try:
        logging.info("Connecting rich presence...")
        connect()
    except:
        logging.error("Error connecting to Discord, retrying...")
        time.sleep(10)
        retries += 1
        connect_loop(retries)
    else:
        update_loop()


logging.info("Started Adobe RPC")

# Updates Discord of current activity
def update_loop():
    # Sets current time
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
            time.sleep(15)
    # When either Discord or a supported Adobe product is not detected...
    except:
        # Clear rpc_data
        rich_presence.clear()
        logging.warning("Not detecting Discord/Adobe application! Are the applications running?")
        time.sleep(5)
        # Update Discord
        update_loop()


try:
    logging.info("Starting rich presence...")
    connect_loop()
except KeyboardInterrupt:
    logging.info("Stopped Adobe RPC!")
    sys.exit(0)
