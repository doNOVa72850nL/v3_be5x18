# 代码生成时间: 2025-10-01 20:26:35
import subprocess
import gr
import shlex
"""
A simple package manager using Gradio framework.
This program allows users to install, uninstall, and list packages.
"""

class PackageManager:
    def __init__(self):
        """Initialize the package manager."""
        pass

    def install_package(self, package_name):
        """Install a package using the package manager."""
        try:
            # Use subprocess to run the package installation command
            subprocess.run(f"apt-get install {shlex.quote(package_name)} -y", shell=True, check=True)
            return f"Package '{package_name}' installed successfully."
        except subprocess.CalledProcessError as e:
            # Handle errors during package installation
            return f"Failed to install package '{package_name}': {e}"

    def uninstall_package(self, package_name):
        """Uninstall a package using the package manager."""
        try:
            # Use subprocess to run the package uninstallation command
            subprocess.run(f"apt-get remove {shlex.quote(package_name)} -y", shell=True, check=True)
            return f"Package '{package_name}' uninstalled successfully."
        except subprocess.CalledProcessError as e:
            # Handle errors during package uninstallation
            return f"Failed to uninstall package '{package_name}': {e}"

    def list_packages(self):
        """List all installed packages."""
        try:
            # Use subprocess to run the package listing command
            output = subprocess.check_output("dpkg --get-selections", shell=True).decode("utf-8")
            return output
        except subprocess.CalledProcessError as e:
            # Handle errors during package listing
            return f"Failed to list packages: {e}"

# Create a Gradio interface for the package manager
iface = gr.Interface(
    fn=PackageManager().install_package,
    inputs=[gr.Textbox(label="Package Name")],
    outputs=[gr.Textbox(label="Result")],
    title="Package Manager - Install Package"
).launch()

iface = gr.Interface(
    fn=PackageManager().uninstall_package,
    inputs=[gr.Textbox(label="Package Name")],
    outputs=[gr.Textbox(label="Result")],
    title="Package Manager - Uninstall Package"
).launch()

iface = gr.Interface(
    fn=PackageManager().list_packages,
    inputs=[],
    outputs=[gr.Textbox(label="Installed Packages")],
    title="Package Manager - List Packages"
).launch()