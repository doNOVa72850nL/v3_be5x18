# 代码生成时间: 2025-10-23 05:40:47
import os
import shutil
import gr
from gr import *

class DataBackupRestore:
    """Class to handle data backup and restore."""

    def __init__(self, backup_dir, restore_dir):
        """Initialize with backup and restore directories."""
        self.backup_dir = backup_dir
        self.restore_dir = restore_dir

    def backup_data(self, source_path):
        """Backup data from a source path to the backup directory."""
        if not os.path.exists(source_path):
            raise FileNotFoundError(f"The source path {source_path} does not exist.")
        
        backup_path = os.path.join(self.backup_dir, os.path.basename(source_path))
        try:
            shutil.copytree(source_path, backup_path)
            print(f"Data backed up successfully to {backup_path}.")
        except Exception as e:
            raise IOError(f"An error occurred during backup: {e}")

    def restore_data(self, backup_path):
        """Restore data from the backup directory to the restore path."""
        if not os.path.exists(backup_path):
            raise FileNotFoundError(f"The backup path {backup_path} does not exist.")
        
        if not os.path.exists(self.restore_dir):
            os.makedirs(self.restore_dir)
        
        restore_path = os.path.join(self.restore_dir, os.path.basename(backup_path))
        try:
            shutil.copytree(backup_path, restore_path)
            print(f"Data restored successfully to {restore_path}.")
        except Exception as e:
            raise IOError(f"An error occurred during restore: {e}")

# Grail interface
if __name__ == "__main__":
    backup_dir = "backup/"
    restore_dir = "restore/"
    app = DataBackupRestore(backup_dir, restore_dir)

    # Create the backup and restore folders if they do not exist
    os.makedirs(backup_dir, exist_ok=True)
    os.makedirs(restore_dir, exist_ok=True)

    # Define the interface
    with gr.Blocks() as demo:
        gr.Markdown("## Data Backup and Restore Tool")

        with gr.Row():
            source_path = gr.Textbox(label="Source Path")
            backup_button = gr.Button("Backup")
        backup_button.click(lambda x: app.backup_data(source_path.value), inputs=[backup_button], outputs=[gr.Textbox(label="Backup Status")])

        with gr.Row():
            backup_path = gr.Textbox(label="Backup Path")
            restore_button = gr.Button("Restore")
        restore_button.click(lambda x: app.restore_data(backup_path.value), inputs=[restore_button], outputs=[gr.Textbox(label="Restore Status")])

    demo.launch()