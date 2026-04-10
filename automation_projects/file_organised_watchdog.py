import os
import shutil
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

WATCH_FOLDER = os.path.expanduser(r"~\OneDrive\Pictures\Screenshots")
file_dest = {'.pdf':'PDFs',".jpg":"Images",".png":"Images"
             ,".zip":"Zipped"}

class MyFileHandler(FileSystemEventHandler):
    def on_created(self,event):
        if event.is_directory:
            return
        file_path= event.src_path
        ext= os.path.splitext(file_path)[1].lower()

        dest_folder= file_dest.get(ext,"Others")
        dest_path= os.path.join(WATCH_FOLDER,dest_folder)
        os.makedirs(dest_path,exist_ok=True)   
        move_to= os.path.join(dest_path,os.path.basename(file_path))

        try:
            shutil.move(file_path,move_to)
            print(f"{os.path.basename(file_path)} succesfully moved to {dest_folder} folder")
        except:
            print("Failed to move")

if __name__=="__main__":
    print(f"Wactching Folder:{WATCH_FOLDER}")
    if not os.path.isdir(WATCH_FOLDER):
        print("Invalid folder path")
    else:
        event_handler= MyFileHandler()
        observer= Observer()
        observer.schedule(event_handler,path=WATCH_FOLDER,recursive=False)
        observer.start()

    try:
        while True:
            pass
    except KeyboardInterrupt:
        observer.stop()
    observer.join()