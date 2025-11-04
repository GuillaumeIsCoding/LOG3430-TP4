import os
import subprocess

bad = os.environ["BADHASH"]
good = os.environ["GOODHASH"]

subprocess.run(["git", "bisect", "start", bad, good])
subprocess.run(["git", "bisect", "run", "python", "manage.py", "test"])