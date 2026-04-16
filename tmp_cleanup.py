import os, subprocess, sys
sys.stdout.reconfigure(encoding='utf-8')
os.chdir(r'C:\Users\GoldRush\Documents\MyProject\FreelanceAutoPilot-Routines')
os.remove('tmp_setup.py')

with open('commit_msg.txt', 'w', encoding='utf-8') as f:
    f.write('chore: remove setup script')
subprocess.run(['git', 'add', '-A'], capture_output=True)
subprocess.run(['git', 'commit', '-F', 'commit_msg.txt'], capture_output=True, text=True)
subprocess.run(['git', 'push'], capture_output=True, text=True)
os.remove('commit_msg.txt')
print('Cleaned up.')
