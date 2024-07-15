# fileName: adbPull_ifexistnotPull.py
# By: Ealsen HuangFu
# Date: 2024-07-15-22:12
# Version: 1.0

# Description: This script checks if files in a remote directory exist in a local directory. 
# If not, it pulls the files from the remote directory to the local directory using adb pull command.
# Usage: Set the remote directory and local directory, then run the script in the command line.
# Note: The script does not support directories with spaces in their names (adb will throw an error).
# Make sure adb is installed and configured, and the device is connected and developer mode is enabled.
# The device should also have USB debugging or remote debugging enabled.

# The script is based on the following assumptions:
# - adb is installed and configured
# - the device is connected
# - developer mode is enabled
# - USB debugging or remote debugging is enabled
# - the remote directory and local directory paths are correct

# This software is provided "as is" without any warranty or guarantee of any kind,
# either express or implied. The author disclaims all liability and responsibility
# for any errors or omissions in the content of this software, and any damages
# (direct, indirect, incidental, or consequential) that may result from the use of
# this software.


""" 前提条件:adb 已经安装并且配置好环境变量 且连接好设备
代码功能：检查远程目录中的文件是否已经存在于本地目录中，如果不存在则执行 adb pull 命令将文件拉取到本地目录中。
使用方法：设置好远程目录和本地目录，然后在命令行中运行 python adbPull_ifexistnotPull.py 即可。
注意事项：不支持文件夹名带空格（adb会报错），请确保远程目录和本地目录的路径正确，并且设备已经连接并且已经
开启开发者模式和 USB 调试或 远程调试。 """


''' 要实现这个脚本，我们需要考虑几个关键点：

列出远程目录中的文件：通常，adb 命令本身并不直接支持列出设备上的目录内容，但我们可以
使用 adb shell ls 命令来实现这一点。
比较文件是否存在：在本地目录中检查每个远程文件是否已存在。
执行 adb pull：对于不存在的文件，执行 adb pull 命令。
统计文件：记录未复制和已复制的文件数量。
由于 adb shell ls 命令的输出需要被解析，我们可以使用 Python 的 subprocess 模块来执行这些命令，
并使用标准库中的其他功能来处理文件和目录。
 '''	


import subprocess  
import os  
  
def list_remote_files(remote_dir):  
    """列出远程目录中的文件"""  
    cmd = f"adb shell ls {remote_dir}"  
    result = subprocess.run(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)  
    if result.returncode != 0:  
        print(f"Error listing remote files: {result.stderr}")  
        return []  
    return [line.strip() for line in result.stdout.splitlines() if not line.startswith('.')]  # 忽略隐藏文件  
  
def check_local_file(local_dir, filename):  
    """检查本地文件是否存在"""  
    return os.path.exists(os.path.join(local_dir, filename))  
  
def adb_pull_file(remote_file, local_dir):  
    """执行 adb pull 命令"""  
    local_file = os.path.join(local_dir, os.path.basename(remote_file))  
    cmd = f"adb pull {remote_file} {local_file}"  
    subprocess.run(cmd, shell=True)  
  
def main():
    # 设置远程目录和本地目录
    remote_dir = "/sdcard/Plus/"

    # 注意Windows的路径分隔符是反斜杠，而Python的字符串转义字符也是反斜杠，所以需要使用双反斜杠或者原始字符串
    local_dir = "G:\\Multimedia\\the_mix_hide\\XXXOOO\\videospicturesmix20240630start\\Plus"
    remote_files = list_remote_files(remote_dir)
    skipped_count = 0
    pulled_count = 0

    if not os.path.exists(local_dir):
        os.makedirs(local_dir)

    for remote_file in remote_files:
        remote_path = os.path.join(remote_dir, remote_file)
        if check_local_file(local_dir, remote_file):
            print(f"Skipping: {remote_path} (already exists locally)")
            skipped_count += 1
        else:
            print(f"Pulling: {remote_path}")
            adb_pull_file(remote_path, local_dir)
            pulled_count += 1

    print(f"Skipped {skipped_count} files.")
    print(f"Pulled {pulled_count} files.")
    input("Press Enter to continue...")

if __name__ == "__main__":
    main()


	
	
'''注意：
这个脚本假设 adb 已经在你的 PATH 环境变量中，或者你可以修改 adb 命令的路径。
脚本使用 shell=True 来运行命令，这在某些情况下可能不是最佳实践，因为它可能使脚本容易受到注入攻击。然而，在这个脚本中，
我们直接控制传递给 subprocess.run 的命令字符串，所以风险较低。
脚本还假设所有文件都可以直接通过 adb pull 复制，没有考虑文件权限或特殊字符的问题。
input("Press Enter to continue...") 代替了 pause 命令，因为它在 Python 中是跨平台的。在 Windows 命令行中，你可以
使用 os.system('pause') 来代替，但这不是跨平台的。'''
