from email import message_from_string
import random
import requests
import time

import part_1
import part_2
import part_3
import part_4

header = {
    'authorization': 'ODAzODgyMTM2NzI0OTYzMzYx.GZswE0.QTgfn5dQQXZ4M_eDhSI4FtG91DuyeVx8rQ4UeQ'
}
x = "https://discord.com/api/v9/channels/1030430373206839387/messages"

while True:
    message = {'content': random.choice(part_1.arr) + " " + random.choice(part_2.arr) + ", " + random.choice(part_3.arr) +" " + random.choice(part_4.arr)}
    r = requests.post(x, data=message, headers=header) 
    time.sleep(60 * 60 * random.randrange(6,24))
    