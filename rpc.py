from pypresence import Presence
import handler
import time


client_id = "482150417455775755"
rich_presence = Presence(client_id)


def connect():
    return rich_presence.connect()


def connect_loop(retries=0):
    if retries > 10:
        return
    try:
        connect()
    except:
        print("Discord is not running, retrying in 10 seconds")
        time.sleep(10)
        retries += 1
        connect_loop(retries)
    else:
        update_loop()


print("Started Photoshop Rich Presence ✓")


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
        print("Make sure Discord/Adobe app is running, retrying in 30 seconds...")
        time.sleep(30)
        update_loop()


try:
    connect_loop()
except KeyboardInterrupt:
    print("Stopped Photoshop Rich Presence ✘")
