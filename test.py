import os
import sys
import time

from fsevents import Observer, Stream
import subprocess

def on_save(event):
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

