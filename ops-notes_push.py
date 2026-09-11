import subprocess
import sys

PAT = open('/Users/haroonqamer/Swarm/hive/state/secure/github_pat.txt').read().strip()

# Use GIT_ASKPASS to authenticate
env = {'GIT_TERMINAL_PROMPT': '0'}

subprocess.run([
    'git', '-c', f'user.name=Haroon Qamer',
    '-c', f'user.email=haroonqamer@mini-ops.ts.net',
    '-c', f'credential.helper=!f() {{ echo username=haroonq66; echo password={PAT}; }}',
    '-c', 'http.https://github.com/.extraheader=AUTHORIZATION: basic {token}'.format(token=PAT),
    'push', 'origin', 'main'
], env=env, check=True)

print("Pushed to origin/main")