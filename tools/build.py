"""Validate and package the dependency-free static website."""
import shutil
import subprocess
import sys
from pathlib import Path

root = Path(__file__).resolve().parents[1]
subprocess.run([sys.executable, str(root / 'tools/check.py'), str(root / 'public')], check=True)
output = root / '_site'
if output.exists():
    shutil.rmtree(output)
shutil.copytree(root / 'public', output)
print(f'Static website built: {output}')
