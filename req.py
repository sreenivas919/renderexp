import pkg_resources
import subprocess

# Get user-installed packages (excluding system dependencies)
installed_packages = {pkg.key for pkg in pkg_resources.working_set}

# Get raw pip freeze output
pip_freeze_output = subprocess.run(["pip", "freeze"], capture_output=True, text=True).stdout

# Process lines to remove unnecessary entries
cleaned_requirements = []
for line in pip_freeze_output.splitlines():
    package = line.split(" @ ")[0]  # Remove file paths
    if package.lower() in installed_packages:  # Keep only user-installed packages
        cleaned_requirements.append(package)

# Write to requirements.txt
with open("requirements.txt", "w") as f:
    f.write("\n".join(cleaned_requirements) + "\n")

print("Clean minimal requirements.txt generated successfully!")
