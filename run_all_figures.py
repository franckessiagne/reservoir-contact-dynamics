import subprocess
import sys
from pathlib import Path

scripts = [f"figure{i}.py" for i in range(1, 13)]

for script in scripts:
    print(f"Running {script}...")
    result = subprocess.run([sys.executable, script], cwd=Path(__file__).parent)
    if result.returncode != 0:
        raise RuntimeError(f"{script} failed with return code {result.returncode}")

print("All figure scripts completed successfully.")
