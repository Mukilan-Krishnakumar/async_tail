import time

from channels.generic.websocket import WebsocketConsumer
from .helpers import LogFileHandler

from watchdog.observers import Observer


class MessageConsumer(WebsocketConsumer):
    def connect(self):
        self.accept()
        print("Hold up what!!!")
        file_path = "./tailapp/logfile.txt"
        event_handler = LogFileHandler(file_path)
        print("REad file", event_handler.get_initial_offset())

    def disconnect(self, close_code):
        pass

    def receive(self, text_data):
        pass


def run_watcher():
    file_path = "./tailapp/logfile.txt"
    print("Got file path")
    event_handler = LogFileHandler(file_path)
    observer = Observer()
    print("Observing")
    observer.schedule(event_handler, "./tailapp", recursive=True)
    observer.start()
    try:
        while True:
            print("Watching...")
            time.sleep(1)
    finally:
        observer.stop()
        observer.join()
