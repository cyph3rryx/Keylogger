import time
import keyboard
import datetime
import socket
import getpass

start_time = time.time()
key_press_count = 0

def on_key_press(event):
  global key_press_count
  key_press_count += 1


keyboard.on_press(on_key_press)

def save_record(elapsed_time, key_press_count):
  current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
  username = getpass.getuser()
  hostname = socket.gethostname()
  record = f"{current_time}, Elapsed time = {elapsed_time} seconds, Key press count = {key_press_count}, User = {username}, Host = {hostname}"
  with open("records.txt", "a") as f:
    f.write(record + "\n")
  print("Record saved to records.txt:")
  print(record)

try:
  while True:
    time.sleep(1)
except (KeyboardInterrupt, SystemExit):
  elapsed_time = time.time() - start_time
  save_record(elapsed_time, key_press_count)
