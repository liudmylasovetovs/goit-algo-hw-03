import os
import shutil
import argparse

def copy_and_sort(src_dir, dest_dir='dist'):
    try:
        os.makedirs(dest_dir, exist_ok=True)
        for root, dirs, files in os.walk(src_dir):
            for file in files:
                file_path = os.path.join(root, file)
                extension = file.split('.')[-1]
                dest_subdir = os.path.join(dest_dir, extension)
                os.makedirs(dest_subdir, exist_ok=True)
                dest_path = os.path.join(dest_subdir, file)
                shutil.copy2(file_path, dest_path)
    except Exception as e:
        print(f"An error occurred: {e}")

def main():
    parser = argparse.ArgumentParser(description='Recursively copy and sort files by extension.')
    parser.add_argument('source_dir', help='Path to the source directory')
    parser.add_argument('dest_dir', nargs='?', default='dist', help='Path to the destination directory (default is "dist")')

    args = parser.parse_args()
    source_dir = args.source_dir
    dest_dir = args.dest_dir

    if not os.path.exists(source_dir):
        print(f"Source directory '{source_dir}' does not exist.")
        return

    copy_and_sort(source_dir, dest_dir)
    print(f"Files copied and sorted from '{source_dir}' to '{dest_dir}'.")

if __name__ == "__main__":
    main()
