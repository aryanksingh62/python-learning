import schedule
import logging
import time
from datetime import datetime
import shutil
from pathlib import Path

Path("logs").mkdir(exist_ok=True)

logging.basicConfig(
    filename= "logs/app.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)
logging.info("scheduler started")


def copy_to_backup(input_folder,output_folder):

    if not input_folder.exists():
        logging.error(f"Invalid folder")
        return
    
    try:     
        shutil.copytree(input_folder,output_folder,dirs_exist_ok=True)
        logging.info(f"Backup complete: {input_folder} → {output_folder.name}")

    except Exception as e:
        logging.error(f"failed to moved on {e}")

def job():
    timestamp= datetime.now().strftime("%Y-%m-%d")
    INPUTFILE= Path("some")
    OUTPUTFILE=  Path.cwd().parent / f"backup_{timestamp}"
    copy_to_backup(INPUTFILE,OUTPUTFILE)

schedule.every().day.do(job)

while True:
    schedule.run_pending()
    time.sleep(60)