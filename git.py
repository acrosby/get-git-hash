#
# Copyright 2013 A.Crosby
# See LICENSE for license information
#
import subprocess, os

def subs(cmd):
    p = subprocess.Popen(cmd, shell=True,
                         stdout = subprocess.PIPE,
                         stderr = subprocess.PIPE)
    out = p.communicate()
    if len(out[1])>0:
        raise ValueError("Error using git through subprocess: %s" % (out[1],))
    else:
        return out[0]
        
def check(repo):
    cmd = "cd %s && git status | grep 'modified:'" % (repo,)
    modified = subs(cmd)
    cmd = "cd %s && git status | grep 'new file:'" % (repo,)
    new = subs(cmd)
    if len(modified) > 0 or len(new) > 0:
        raise ValueError("Please commit the changes to the repository '%s'" % (repo,))

def current_hash(repo):
    check(repo)
    cmd = "cd %s && git log | head -n 1" % (repo,)
    out = subs(cmd)
    out = out.strip("commit").strip(" ").strip("\n")
    return out

def current_branch(repo):
    check(repo)
    cmd = "cd %s && git status | grep 'On branch'" % (repo,)
    out = subs(cmd)
    out = out.strip("# On branch ").strip(" ").strip("\n")
    return out

def unique(repo):
    check(repo)
    branch = current_branch(repo)
    hash = current_hash(repo)
    return branch + "-" + hash

def prepend_unique(repo, filename):
    path = os.path.abspath(filename)
    fnames = os.path.split(path)
    this = unique(repo)
    return os.path.join([fnames[0], this+"_"+fnames[1]])
