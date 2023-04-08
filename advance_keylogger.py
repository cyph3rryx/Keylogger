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
start_time = time.time()
key_press_count = 0

# Define functions
def on_start_stop_recording():
    global recording
    recording = not recording
    if recording:
        logging.info('Started recording key presses')
    else:
        elapsed_time = time.time() - start_time
        save_record(elapsed_time, key_press_count)
        logging.info('Stopped recording key presses')

def on_save_record():
    elapsed_time = time.time() - start_time
    save_record(elapsed_time, key_press_count)
    logging.info('Saved record')

def on_key_press(event):
    global key_press_count
    if recording:
        key_press_count += 1

def save_record(elapsed_time, key_press_count):
    current_time = datetime.datetime.utcnow()
    username = getpass.getuser()
    hostname = socket.gethostname()
    record = Record(elapsed_time=elapsed_time, key_press_count=key_press_count, username=username, hostname=hostname)
    session = Session()
    session.add(record)
    session.commit()
    logging.info(f'Record saved: {record}')

# Register hotkeys
keyboard.add_hotkey('ctrl+shift+r', on_start_stop_recording)
keyboard.add_hotkey('ctrl+shift+s', on_save_record)

# Main loop
try:
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    logging.info('Program stopped')
