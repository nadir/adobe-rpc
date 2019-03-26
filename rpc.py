from pypresence import Presence
import handler
import time


client_id = "482150417455775755"
rich_presence = Presence(client_id)
rich_presence.connect()

start_time = int(time.time())

print("Started Photoshop Rich Presence ✓")


try:
    while True:
        rpc_data = handler.get_rpc_update()
        rich_presence.update(state=rpc_data['state'],
                             small_image="photoshop_small",
                             large_image="photoshop_large",
                             large_text="Adobe Photoshop",
                             small_text="Editing",
                             details="CC 2018",
                             start=start_time)
        time.sleep(15)
except KeyboardInterrupt:
    print("Stopped Photoshop Rich Presence ✘")
