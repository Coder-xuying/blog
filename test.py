import os
import sys
import time

from fsevents import Observer, Stream
import subprocess

last_save_time = None  # 记录上次保存时间的变量

def on_save(event):
    global last_save_time  # 使用全局变量

    current_time = time.time()  # 获取当前时间
    if last_save_time is None or current_time - last_save_time >= 600:  # 10分钟内只监听一次保存
        last_save_time = current_time  # 更新上次保存时间
        print(f"File saved: {event.name}")
        script_path = "/Users/xuying/Desktop/个人/github_pro/blog/auto_commit.sh"  # 外部脚本或程序的路径
        subprocess.run([script_path])

def main():
    if len(sys.argv) < 2:
        print("Usage: python monitor_directory.py /path/to/directory")
        sys.exit(1)

    directory_path = sys.argv[1]

    observer = Observer()
    stream = Stream(on_save, directory_path, file_events=True)
    observer.schedule(stream)
    observer.start()

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
        observer.join()

if __name__ == "__main__":
    main()