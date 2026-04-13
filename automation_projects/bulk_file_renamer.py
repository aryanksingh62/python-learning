from pathlib import Path

def renamer(folder,name):
    count=1
    succes=0
    total = sum(1 for f in Path(folder).iterdir() if f.is_file())
    for file in sorted(Path(folder).iterdir()):
        try:
            if file.is_file():
                new_name = Path(folder) / f"{name}_{str(count).zfill(3)}{file.suffix}"
                file.rename(new_name)
                count+=1
                succes+=1
        except Exception as e:
            print(f"Failed to Rename\n{e}")

    print(f"succesfully rename {succes}/{total} files")

if __name__=="__main__": 
    folder= input("Enter the folder name: ").strip()
    name= input("Enter the new file name: ").strip().lower()
    if Path(folder).is_dir():
        renamer(folder,name)
    else:
        print("Inavlid folder")