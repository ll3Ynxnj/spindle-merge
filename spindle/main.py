import os
import glob
import argparse


def load_file_paths(file_list_path):
    """
    指定されたファイルリストを読み込む。

    Parameters:
        file_list_path (str): ファイルリストのパス

    Returns:
        list: ファイルパスのリスト
    """
    try:
        with open(file_list_path, 'r', encoding='utf-8') as file:
            # 空行は除外して読み込み
            return [line.strip() for line in file if line.strip()]
    except Exception as e:
        print(f"Error loading file list: {e}")
        return []


def merge_files(file_paths, output_path):
    """
    複数のファイルをマージし、1つの出力ファイルに書き込む。
    各ファイルの内容の前に、ファイルのタイトルとしてヘッダーを挿入する。

    Parameters:
        file_paths (list): マージ対象のファイルパスのリスト
        output_path (str): 出力ファイルのパス
    """
    separator = "=" * 79  # PEP8の最大幅（79文字）の区切り線

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
                            # ファイルタイトル（ヘッダー）の挿入
                            outfile.write(separator + "\n")
                            outfile.write(f"File: {file}\n")
                            outfile.write(separator + "\n\n")

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
    コマンドライン引数を解析し、指定されたファイルリストに基づいてファイルをマージする。
    """
    parser = argparse.ArgumentParser(
        description="ファイルリストに記載されたファイルをマージします。"
    )
    parser.add_argument(
        "file_list",
        help="マージ対象ファイルのパスが記載されたファイルのパス。"
    )
    parser.add_argument(
        "-o", "--output",
        default="merged_output.txt",
        help="出力ファイルのパス。デフォルトは 'merged_output.txt'。"
    )
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
