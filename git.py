import subprocess, os

def subs(cmd):
    p = subprocess.Popen(cmd, shell=True,
                         stdout = subprocess.PIPE,
                         stderr = subprocess.PIPE)
    if len(communicate[1])>0:
        raise ValueError("Error using git through subprocess")
    else:
        out = p.communicate()[0]
    
def current_hash(repo):
    cmd = "cd %s && git log | head -n 1" % (repo,)
    out = subs(cmd)
    out = out.strip("commit").strip(" ").strip("\n")
    return out

def current_branch(repo):
    cmd = "cd %s && git status | grep 'On branch'" % (repo,)
    out = subs(cmd)
    out = out.strip("# On branch ").strip(" ").strip("\n")
    return out

def unique(repo):
    
