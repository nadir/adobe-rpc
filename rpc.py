from pypresence import Presence
from pypresence.exceptions import InvalidID, InvalidPipe
import handler
import time
import sys


client_id = "482150417455775755"
rich_presence = Presence(client_id)


def connect():
    rich_presence.connect()


try:
    connect()
except (InvalidID, InvalidPipe):
    print("Discord is not running...")
    sys.exit(0)


start_time = int(time.time())

print("Started Photoshop Rich Presence ✓")


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
except KeyboardInterrupt:
    print("Stopped Photoshop Rich Presence ✘")
