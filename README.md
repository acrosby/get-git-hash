get-git-hash
============

Get repository hash and branch name

```python
import git

git.current_hash("/my/repo")
git.current_branch("/my/repo")
git.unique("/my/repo")
```

Build a filename based on the version of code you are using

```python
path = "/this/is/my/figure.png"

git.unique_path("/my/repo", path)
```
