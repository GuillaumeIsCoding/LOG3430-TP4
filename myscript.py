import os
import subprocess

bad = os.environ["badhash"]
good = os.environ["goodhash"]

subprocess.run(["git", "bisect", "start", bad, good])
subprocess.run(["git", "bisect", "run", "python", "manage.py", "test"])