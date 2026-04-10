import os

def preview(folder, base_name, ext):
    i = 1
    for file in os.listdir(folder):
        file_path = os.path.join(folder, file)
        if os.path.isfile(file_path):
            if ext == os.path.splitext(file)[1].lower():
                print(f"{file} → {base_name}_{i}{ext}")
                i += 1

def rename(folder, base_name, ext):
    i = 1
    for file in os.listdir(folder):
        file_path = os.path.join(folder, file)
        if os.path.isfile(file_path):
            if ext == os.path.splitext(file)[1].lower():
                dest_path = os.path.join(folder, f"{base_name}_{i}{ext}")
                os.rename(file_path, dest_path)
                i += 1

if __name__ == "__main__":
    folder = input("Enter the folder you want to organize: ").strip()
    if not os.path.isdir(folder):
        print("Invalid folder path")
    else:
        base_name = input("Enter the base name for the files: ").strip().lower()
        ext = input("Enter the extension to filter (e.g. .jpg): ").strip().lower()
        while True:
            print("1. Do you want to Preview before renaming enter (1)")
            print("2. Rename")
            print("3. cancel")

            choice = input("Enter the option: ").strip()
            if choice == "1":
                preview(folder, base_name, ext)
            elif choice == "2":
                rename(folder, base_name, ext)
                print("✅ Renaming complete.")
            elif choice== "3":
                print("renaming canceled...")
                break
            else:
                print("Invalid choice")