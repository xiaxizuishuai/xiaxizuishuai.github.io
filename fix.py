import subprocess
import os

# Disable git quoting
subprocess.run(["git", "config", "core.quotePath", "false"])

# Get files from git
result = subprocess.run(["git", "ls-files", "img/shellcarvingimages"], capture_output=True, text=True, encoding='utf-8')
files = result.stdout.strip().split('\n')

with open(r'_posts\2026-06-09-shell.md', 'r', encoding='utf-8') as f:
    content = f.read()

count = 1
for filepath in files:
    if not filepath: continue
    filename = filepath.split('/')[-1]
    ext = filename.split('.')[-1]
    new_name = f"media_{count:03d}.{ext}"
    new_filepath = f"img/shellcarvingimages/{new_name}"
    
    # Git mv
    subprocess.run(["git", "mv", filepath, new_filepath])
    
    # Update markdown
    content = content.replace(f"/img/shellcarvingimages/{filename}", f"/img/shellcarvingimages/{new_name}")
    
    count += 1

with open(r'_posts\2026-06-09-shell.md', 'w', encoding='utf-8') as f:
    f.write(content)

print("Fixed images and markdown.")
