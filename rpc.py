from pypresence import Presence, activity
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

# Binds RPC connection to Discord
def connect():
    return rich_presence.connect()

# Attempts to find Discord
def connect_loop(retries=0):
    logging.info("Connecting rich presence...")
    if retries > 10:
        return
    try:
        logging.info("Conneting to RPC...")
        connect()
    except:
        logging.error("Error connecting to Discord! Retrying")
        time.sleep(10)
        retries += 1
        connect_loop(retries)
    else:
        update_loop()

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
    # When either Discord or a supported Adobe product is not detected...
    except:
        # Clear rpc_data
        rich_presence.clear()
        logging.warning(
            "Not detecting Adobe applications! Are you sure your running a compatible application?")
        # Update Discord
        update_loop()

# Main instance
def main():
    logging.info("Started Adobe RPC, starting rich presence...")
    connect_loop()

if __name__ == "__main__":
    try:
        main()
    except (KeyboardInterrupt, SystemExit):
        logging.info("Stopped Adobe RPC!")
        sys.exit(0)
