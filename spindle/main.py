import os
import glob
import argparse
import sys

try:
    import pyperclip
except ImportError:
    print("Error: pyperclip モジュールが必要です。'pip install pyperclip' を実行してください。")
    sys.exit(1)


def load_file_paths(file_list_path):
    """
    指定されたファイルリスト (SpindleLists.txt) を読み込む。
    - 空行や '#' で始まるコメント行は無視する。

    Parameters:
        file_list_path (str): SpindleLists.txt のパス

    Returns:
        list: 有効なファイルパスのリスト
    """
    try:
        with open(file_list_path, 'r', encoding='utf-8') as file:
            paths = []
            for line in file:
                stripped = line.strip()
                # 空行またはコメント行はスキップ
                if not stripped or stripped.startswith("#"):
                    continue
                paths.append(stripped)
            return paths
    except Exception as e:
        print(f"Error loading file list: {e}")
        return []


def merge_files(file_paths, output_path):
    """
    複数のファイルをマージし、1つの出力ファイルに書き込む。
    各ファイルの内容の前に、ファイル名を含むヘッダーを挿入し、
    さらに最終結果をクリップボードへコピーする。

    Parameters:
        file_paths (list): マージ対象のファイルパスのリスト
        output_path (str): 出力ファイルのパス
    """
    separator = "=" * 79  # 区切り線（79文字）
    merged_content = ""   # クリップボードへコピーするために全内容を保持
    try:
        with open(output_path, 'w', encoding='utf-8') as outfile:
            for path in file_paths:
                # ユーザー展開 (~ など) を実施
                expanded_path = os.path.expanduser(path)
                # recursive=True を指定して再帰検索を有効にする
                matched_files = glob.glob(expanded_path, recursive=True)

                if not matched_files:
                    print(f"Warning: No files matched: {expanded_path}")
                    continue

                for file in matched_files:
                    if os.path.isfile(file):
                        try:
                            header = separator + "\n" + f"File: {file}\n" + separator + "\n\n"
                            outfile.write(header)
                            merged_content += header

                            with open(file, 'r', encoding='utf-8') as infile:
                                content = infile.read()
                                outfile.write(content)
                                merged_content += content
                                outfile.write("\n")
                                merged_content += "\n"
                            print(f"Merged: {file}")
                        except Exception as e:
                            print(f"Error reading {file}: {e}")
                    elif os.path.isdir(file):
                        # ディレクトリの場合は警告を出さず無視する
                        continue
                    else:
                        print(f"Warning: Not a valid file: {file}")
        print(f"All files have been merged into {output_path}")

        # マージした結果をクリップボードへコピー
        pyperclip.copy(merged_content)
        print("Merged content has been copied to clipboard.")
    except Exception as e:
        print(f"Error writing to {output_path}: {e}")


def main():
    """
    コマンドライン引数を解析し、実行ディレクトリに配置された
    SpindleLists.txt を基にファイルをマージする。
    """
    parser = argparse.ArgumentParser(
        description="Spindle: SpindleLists.txtに記載されたファイルをマージします。"
    )
    parser.add_argument(
        "-o", "--output",
        default="spindle_output.txt",
        help="出力ファイルのパス。デフォルトは 'spindle_output.txt'。"
    )
    args = parser.parse_args()

    file_list_path = "SpindleLists.txt"
    if not os.path.exists(file_list_path):
        print(f"Error: '{file_list_path}' が存在しません。")
        sys.exit(1)

    file_paths = load_file_paths(file_list_path)
    if file_paths:
        merge_files(file_paths, os.path.expanduser(args.output))
    else:
        print("Error: 有効なファイルパスが見つかりません。")


if __name__ == "__main__":
    main()
