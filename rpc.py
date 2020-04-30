from pypresence import Presence
import handler
import sys
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
        print("Error connecting to Discord")
        time.sleep(10)
        retries += 1
        connect_loop(retries)
    else:
        start_time = int(time.time())
        update_loop(start_time)

print("Started Adobe RPC")

def term_check(start_time):
    if (start_time + 80) <= int(time.time()):
        print("Couldn't find Adobe/Discord, exiting")
        sys.exit()

def update_loop(start_time):
    try:
        while True:
            rpc_data = handler.get_rpc_update()
            start_time = int(time.time())
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
        print("Run Adobe/Discord app")
        time.sleep(5)
        term_check(start_time)
        update_loop(start_time)

try:
    connect_loop()
except KeyboardInterrupt:
    print("Stopped Adobe RPC")
