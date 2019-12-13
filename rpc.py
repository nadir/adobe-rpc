from pypresence import Presence, activity
import logging
import handler
import time

# Client Setup
client_id = "482150417455775755"
rich_presence = Presence(client_id)

# Logging config
logging.basicConfig(level=logging.INFO, format=('%(asctime)s - %(levelname)s - ' +
                                                '%(funcName)s - %(message)s'),
                    datefmt='%d-%m-%y %H:%M:%S')

def connect():
    logging.info("Connected to rich presence!")
    return rich_presence.connect()


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


def update_loop():
    start_time = int(time.time())
    try:
        while True:
            rpc_data = handler.get_rpc_update()
            rich_presence.update(state=rpc_data['state'],
                                 small_image=rpc_data['small_image'],
                                 large_image=rpc_data['large_image'],
                                 large_text=rpc_data['large_text'],
                                 small_text=rpc_data['small_text'],
                                 details=rpc_data['details'],
                                 start=start_time)
            time.sleep(15)
    except:
        rich_presence.clear()
        logging.warning("Run Adobe/Discord app")
        time.sleep(5)
        update_loop()


try:
    connect_loop()
except KeyboardInterrupt:
    logging.info("Stopped Adobe RPC")
