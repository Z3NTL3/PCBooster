import os
from pathlib import Path
# Get CMD code
HOMEDIR = Path.home()

if os.path.exists(f"{HOMEDIR}\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Startup"):
    print(f"python {__file__}")
    print(f"\n\nAdd the above line into folder: {HOMEDIR}\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Startup")
