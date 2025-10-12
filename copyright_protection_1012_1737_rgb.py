# 代码生成时间: 2025-10-12 17:37:47
import hashlib
import time
from gradio import interfaces, Template

"""
版权保护系统
=====
该系统允许用户上传文件，并生成相应的哈希值以验证文件的唯一性。
=====
"""

class CopyrightProtection:
    def __init__(self):
        """初始化版权保护系统。"""
        self.hash_function = hashlib.sha256()

    def generate_hash(self, file):
        """
        为给定的文件生成哈希值。

        参数:
        file -- 要生成哈希值的文件对象
        """
        try:
            self.hash_function.update(file.read())
            file_hash = self.hash_function.hexdigest()
            return file_hash
        except Exception as e:
            # 处理可能的错误
            print(f"An error occurred: {e}")
            return None

    def verify_hash(self, original_hash, new_hash):
        """
        验证两个哈希值是否相同。

        参数:
        original_hash -- 原始哈希值
        new_hash -- 要验证的哈希值
        """
        return original_hash == new_hash

# 创建版权保护系统的实例
copyright_protection = CopyrightProtection()

# 定义Gradio界面
template = Template(title="Copyright Protection System")

# 上传文件并生成哈希值
upload_button = interfaces.File(label="上传文件")
hash_result = interfaces.Textbox(label="文件哈希值")

# 将上传按钮和哈希结果显示添加到界面
template.add(upload_button)
template.add(hash_result)

# 定义上传文件的处理函数
def process_file(file):
    if file is not None:
        hash_result = copyright_protection.generate_hash(file)
        return f"文件哈希值：{hash_result}"
    else:
        return "请上传文件。"

# 将处理函数绑定到上传按钮
upload_button.change(process_file, inputs=upload_button, outputs=hash_result)

# 启动Gradio界面
template.launch()
