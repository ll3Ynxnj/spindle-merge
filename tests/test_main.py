# spindle/tests/test_main.py

import unittest
import os
import tempfile
from spindle.main import load_file_paths, merge_files

class TestSpindle(unittest.TestCase):
    def setUp(self):
        # 一時ファイルとディレクトリを作成
        self.temp_dir = tempfile.TemporaryDirectory()
        self.file1 = os.path.join(self.temp_dir.name, "file1.txt")
        self.file2 = os.path.join(self.temp_dir.name, "file2.txt")
        self.output_file = os.path.join(self.temp_dir.name, "merged_output.txt")
        
        # テスト用ファイルを作成
        with open(self.file1, 'w', encoding='utf-8') as f:
            f.write("Content of file1.\n")
        with open(self.file2, 'w', encoding='utf-8') as f:
            f.write("Content of file2.\n")
        
        # ファイルリスト
        self.file_list = os.path.join(self.temp_dir.name, "file_list.txt")
        with open(self.file_list, 'w', encoding='utf-8') as f:
            f.write(f"{self.file1}\n")
            f.write(f"{self.file2}\n")
    
    def tearDown(self):
        # 一時ディレクトリをクリーンアップ
        self.temp_dir.cleanup()
    
    def test_load_file_paths(self):
        from spindle.main import load_file_paths
        paths = load_file_paths(self.file_list)
        self.assertEqual(len(paths), 2)
        self.assertIn(self.file1, paths)
        self.assertIn(self.file2, paths)
    
    def test_merge_files(self):
        file_paths = load_file_paths(self.file_list)
        merge_files(file_paths, self.output_file)
        
        # 出力ファイルの内容を確認
        with open(self.output_file, 'r', encoding='utf-8') as f:
            content = f.read()
        
        expected_content = "Content of file1.\n\nContent of file2.\n\n"
        self.assertEqual(content, expected_content)
    
    def test_no_files_matched(self):
        # 存在しないファイルを追加
        with open(self.file_list, 'a', encoding='utf-8') as f:
            f.write("nonexistent_file.txt\n")
        
        file_paths = load_file_paths(self.file_list)
        merge_files(file_paths, self.output_file)
        
        # 出力ファイルの内容を確認（存在するファイルのみマージされている）
        with open(self.output_file, 'r', encoding='utf-8') as f:
            content = f.read()
        
        expected_content = "Content of file1.\n\nContent of file2.\n\n"
        self.assertEqual(content, expected_content)

if __name__ == '__main__':
    unittest.main()
