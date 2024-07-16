import os
import sys
import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import subprocess

last_save_time = None  # 记录上次保存时间的变量

class MyHandler(FileSystemEventHandler):
    def on_modified(self, event):
        global last_save_time  # 使用全局变量

        current_time = time.time()  # 获取当前时间
        if last_save_time is None or current_time - last_save_time >= 600:  # 10分钟内只监听一次保存
            last_save_time = current_time  # 更新上次保存时间
            print(f"File saved: {event.src_path}")
            script_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "auto_commit.sh")
            subprocess.run(["C:\\Program Files\\Git\\bin\\bash.exe",script_path])

def main():
    directory_path = os.getcwd()  # 获取当前工作目录作为监听的目录

    event_handler = MyHandler()
    observer = Observer()
    observer.schedule(event_handler, directory_path, recursive=True)
    observer.start()

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
        observer.join()

if __name__ == "__main__":
    main()
