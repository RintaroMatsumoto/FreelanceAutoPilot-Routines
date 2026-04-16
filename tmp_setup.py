import sys, subprocess, os
sys.stdout.reconfigure(encoding='utf-8')
os.chdir(r'C:\Users\GoldRush\Documents\MyProject\FreelanceAutoPilot-Routines')

def run(cmd):
    r = subprocess.run(cmd, capture_output=True, text=True, encoding='utf-8', shell=True)
    if r.stdout.strip(): print(r.stdout.strip())
    if r.stderr.strip(): print(r.stderr.strip())
    return r.returncode

# Create GitHub repo
run('gh repo create RintaroMatsumoto/FreelanceAutoPilot-Routines --public --description "Claude Routines driven freelance automation. No code, just prompts and state."')

# Git setup
run('git add -A')

# Commit via file to avoid encoding issues
with open('commit_msg.txt', 'w', encoding='utf-8') as f:
    f.write('init: FreelanceAutoPilot-Routines - prompts + state architecture')
run('git commit -F commit_msg.txt')

# Push
run('git branch -M main')
run('git remote add origin https://github.com/RintaroMatsumoto/FreelanceAutoPilot-Routines.git')
run('git push -u origin main')

# Cleanup
os.remove('commit_msg.txt')
print('\n--- Done ---')
