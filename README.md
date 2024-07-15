## adbPullNExLocal

- fileName: adbPull_ifexistnotPull.py
- By: Ealsen HuangFu
- Date: 2024-07-15-22:12
- Version: 1.0

### Description:
- This script checks if files in a remote directory exist in a local directory. 
- If not, it pulls the files from the remote directory to the local directory using adb pull command.
- Usage: Set the remote directory and local directory, then run the script in the command line.
- Note: The script does not support directories with spaces in their names (adb will throw an error).
- Make sure adb is installed and configured, and the device is connected and developer mode is enabled.
- The device should also have USB debugging or remote debugging enabled.

### Following
- The script is based on the following assumptions:
- - adb is installed and configured
- - the device is connected
- - developer mode is enabled
- - USB debugging or remote debugging is enabled
- - the remote directory and local directory paths are correct

### Statement
- This software is provided "as is" without any warranty or guarantee of any kind,
- either express or implied. The author disclaims all liability and responsibility
- for any errors or omissions in the content of this software, and any damages
- (direct, indirect, incidental, or consequential) that may result from the use of
- this software.
