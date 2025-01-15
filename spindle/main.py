# spindle/main.py

import os
import glob
import argparse

def load_file_paths(file_list_path):
    """
    指定されたファイルリストを読み込む
    """
    try:
        with open(file_list_path, 'r', encoding='utf-8') as file:
            return [line.strip() for line in file if line.strip()]  # 空行を無視
    except Exception as e:
        print(f"Error loading file list: {e}")
        return []

def merge_files(file_paths, output_path):
    """
    ファイルをマージして出力する
    """
    try:
        with open(output_path, 'w', encoding='utf-8') as outfile:
            for path in file_paths:
                expanded_path = os.path.expanduser(path)
                matched_files = glob.glob(expanded_path)

                if not matched_files:
                    print(f"No files matched: {expanded_path}")
                    continue

                for file in matched_files:
                    if os.path.isfile(file):
                        try:
                            with open(file, 'r', encoding='utf-8') as infile:
                                outfile.write(infile.read())
                                outfile.write("\n")
                            print(f"Merged: {file}")
                        except Exception as e:
                            print(f"Error reading {file}: {e}")
                    else:
                        print(f"Not a valid file: {file}")
        print(f"All files have been merged into {output_path}")
    except Exception as e:
        print(f"Error writing to {output_path}: {e}")

def main():
    """
    コマンドラインからの入力を処理
    """
    parser = argparse.ArgumentParser(description="Merge files specified in a file list.")
    parser.add_argument("file_list", help="Path to the file containing list of files to merge.")
    parser.add_argument("-o", "--output", default="merged_output.txt", help="Output file path.")
    args = parser.parse_args()

    file_list_path = os.path.expanduser(args.file_list)
    output_path = os.path.expanduser(args.output)

    file_paths = load_file_paths(file_list_path)
    if file_paths:
        merge_files(file_paths, output_path)
    else:
        print("No valid file paths found.")

if __name__ == "__main__":
    main()
