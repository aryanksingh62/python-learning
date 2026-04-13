from pathlib import Path
import shutil

ext_map= {".jpg":"images",".png":"images",
      ".pdf":"pdf",".csv":"data",".txt":"txtfile"}

def organizer(folder):
    for file in Path(folder).iterdir():
        p= Path(file)
        if p.is_file():
            ext= p.suffix.lower()
            folder_name= ext_map.get(ext,"others")
            dest_folder_path= Path(folder) / folder_name
            dest_folder_path.mkdir(exist_ok=True)
            dest_file= Path(dest_folder_path) / p.name
        
            try:
                if not dest_file.exists():
                    shutil.move(p,dest_file)
                    
                else:
                    counter=1
                    new_name= p.parent / (p.stem + str(counter) + p.suffix)
                    new_dest_file= Path(dest_folder_path) / new_name.name
                    while new_dest_file.exists():
                        counter+=1
                        new_name= p.parent / (p.stem + str(counter) + p.suffix)
                        new_dest_file= Path(dest_folder_path) / new_name.name
                    
                    p.rename(new_name)
                    shutil.move(new_name,new_dest_file)
          
            except Exception as e:
                print(f"failed to moved\n{e}")
    print("folder organized successfully")

if __name__=="__main__":
    folder = input("enter folder  name: ").strip() or Path.cwd()
    if Path(folder).is_dir():
        organizer(folder)
        
    else:
        print("Invalid folder")