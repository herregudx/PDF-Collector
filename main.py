import os
import shutil

def copy_pdf_files(src_folder, dest_folder):
    # Create destination folder if it doesn't exist
    os.makedirs(dest_folder, exist_ok=True)

    for root, dirs, files in os.walk(src_folder):
        for file in files:
            if file.lower().endswith('.pdf'):
                src_file_path = os.path.join(root, file)
                dest_file_path = os.path.join(dest_folder, file)

                # Copy the PDF file to the destination folder
                try:
                    shutil.copy2(src_file_path, dest_file_path)
                    print(f"Copied: {src_file_path} to {dest_file_path}")
                except FileExistsError:
                    print(f"File already exists: {dest_file_path}. Skipping.")
                except Exception as e:
                    print(f"Error copying {src_file_path}: {e}")

def main():
    # Start searching from the root of the C: drive
    search_root = "C:\\"
    dest_folder = "C:\\Temp"

    # Walk through all directories looking for "PDF Documents"
    for root, dirs, files in os.walk(search_root):
        if os.path.basename(root) == "PDF Documents":
            print(f"Found: {root}")
            copy_pdf_files(root, dest_folder)

if __name__ == "__main__":
    main()

