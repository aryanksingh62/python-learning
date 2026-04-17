from pathlib import Path

def detect_dup(input_folder):
    data={}
    size_data={}
    for file in Path(input_folder).rglob("*"):
            
            if file.is_file():
                data.setdefault(file.name, []).append(file)
                size_data.setdefault(file.stat().st_size,[]).append(file)

    #detect by name
    if any(len(value)>1 for value in data.values()):
        for key,value in data.items():
            if len(value)>1:
                print(f"Duplicate: {key}")
                for path in value:
                    print(path) 
                print()
    else:
        print(f"No duplicate found by file name")

    #detect by size            
    if any(len(value)>1 for value in size_data.values()):
        for key,value in size_data.items():
            if len(value)>1:
                print(f"Duplicate (same size: {key} bytes)")
                for path in value:
                    print(path) 
                print()
    else:
        print("No duplicate found file size")

if __name__=="__main__":
    folder=input("Enter the folder name: ").strip()
    if Path(folder).is_dir():
        detect_dup(folder)
    else:
        print("Invalid Folder")