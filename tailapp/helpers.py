from watchdog.events import FileSystemEventHandler


class LogFileHandler(FileSystemEventHandler):
    def __init__(self, file_path):
        self.file_path = file_path
        self.offset = self.get_initial_offset()

    def get_initial_offset(self):
        with open(self.file_path, "rb") as file:
            file.seek(0, 2)
            return file.tell()

    def on_modified(self, event):
        if not event.is_directory and event.src_path.endswith(
            self.file_path.split("/")[-1]
        ):
            print("FILE CHANGED!!!")
