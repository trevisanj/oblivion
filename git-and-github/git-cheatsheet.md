# git cheat sheet

### :notes: **Resync repo with new `.gitignore` file**

```shell
git rm -r --cached .
git add . --all
git commit -m ".gitignore is now working"
```
(http://stackoverflow.com/questions/7075923/resync-git-repo-with-new-gitignore-file)

(http://stackoverflow.com/questions/1139762/ignore-files-that-have-already-been-committed-to-a-git-repository)


### :notes: **Create new branch, switch, push**

```shell
git branch --create newbranch
git checkout newbranch
git push --set-upstream origin newbranch
```

### :notes: **Reset local to match origin**

```shell
git fetch origin
git reset --hard origin/master
```

:notes: **Seeing diff**: `git diff b7de eab0 nulbad.f90`

:notes: **Recover deleted file**: `git checkout nulbad.py`

