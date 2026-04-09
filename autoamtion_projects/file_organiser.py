import os
import shutil

ext_map = {"Image":[".jpg",".jpeg",".png"],
"TxtFiles":[".pptx",".txt",".docx"],
"PDFs":[".pdf"]
}

def destination_folder(filename):
    ext = os.path.splitext(filename)[1].lower()

    for folder,extension in ext_map.items():
        if ext in extension:
            return folder
    return "Others"

def sort_files(folder_path):
    for file in os.listdir(folder_path):
        full_path= os.path.join(folder_path,file)

        if file == os.path.basename(__file__):
            continue

        if os.path.isfile(full_path):
            dest_folder= destination_folder(file)
            dest_path= os.path.join(folder_path,dest_folder)
            new_path= os.path.join(dest_path,file)

            os.makedirs(dest_path,exist_ok=True)
            shutil.move(full_path,new_path)
            print(f"Moved :{file} -> {dest_folder}/")

if __name__=="__main__":
    folder= input("Enter the folder path or leave blank:").strip()
    folder=  folder or os.getcwd()

    if not os.path.isdir(folder):
        print("Invalid directory")
    else:
        sort_files(folder)
        print("✅Sorting completed")