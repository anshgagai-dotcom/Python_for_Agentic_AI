# subprocess.run se python --version chalao (list form) aur output print karo.
# 1. Run python --version using subprocess.run in list form and print the output.


import subprocess

r = subprocess.run(
    ["python", "--version"],
    capture_output=True,
    text=True
)

print(r.stdout.strip())

