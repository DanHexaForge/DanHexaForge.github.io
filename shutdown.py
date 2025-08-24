import os
import time
import platform

# Wait 45 minutes (45 * 60 seconds)
time.sleep(45 * 60)

# Detect operating system and shutdown accordingly
if platform.system() == "Windows":
    os.system("shutdown /s /t 1")
elif platform.system() == "Linux" or platform.system() == "Darwin":  # Darwin = macOS
    os.system("shutdown now")
else:
    print("Unsupported OS")
