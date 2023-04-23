import time
import datetime
import socket
import getpass
import logging
import keyboard
import sqlalchemy
from sqlalchemy import create_engine, Column, Integer, String, Float, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from collections import deque
from threading import Timer, Thread
from queue import Queue
from concurrent.futures import ThreadPoolExecutor

# Set up logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s %(levelname)s %(message)s')

# Set up database
engine = create_engine('sqlite:///records.db')
Base = declarative_base()

class Record(Base):
    __tablename__ = 'records'
    id = Column(Integer, primary_key=True)
    timestamp = Column(DateTime, default=datetime.datetime.utcnow)
    elapsed_time = Column(Float)
    key_press_count = Column(Integer)
    username = Column(String)
    hostname = Column(String)

Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)

# Set up variables
recording = False
start_time = None
elapsed_time = 0
key_presses = deque()
record_queue = Queue()
executor = ThreadPoolExecutor()

# Define functions
def on_start_stop_recording():
    global recording, start_time
    if not start_time:
        start_time = time.time()
        timer = Timer(1, update_elapsed_time)
        timer.start()
    recording = not recording
    if recording:
        logging.info('Started recording key presses')
    else:
        save_record(elapsed_time, len(key_presses))
        logging.info('Stopped recording key presses')

def update_elapsed_time():
    global elapsed_time
    elapsed_time = time.time() - start_time
    if recording:
        timer = Timer(1, update_elapsed_time)
        timer.start()

def on_save_record():
    save_record(elapsed_time, len(key_presses))
    logging.info('Saved record')

def on_key_press(event):
    if recording:
        key_presses.append(event)

def save_record(elapsed_time, key_press_count):
    current_time = datetime.datetime.utcnow()
    username = getpass.getuser()
    hostname = socket.gethostname()
    record = Record(elapsed_time=elapsed_time, key_press_count=key_press_count, username=username, hostname=hostname)
    record_queue.put(record)

def record_writer():
    while True:
        records = []
        while not record_queue.empty():
            records.append(record_queue.get())
        if records:
            with Session() as session:
                session.add_all(records)
            logging.info(f'Records saved: {len(records)}')
        time.sleep(1)

keyboard.add_hotkey('ctrl+shift+r', on_start_stop_recording)
keyboard.add_hotkey('ctrl+shift+s', on_save_record)

thread = Thread(target=record_writer, daemon=True)
thread.start()

try:
    while True:
        if key_presses:
            key_press_count = len(key_presses)
            key_presses.clear()
            executor.submit(save_record, elapsed_time, key_press_count)
        time.sleep(0.1)
except KeyboardInterrupt:
    logging.info('Program stopped')
