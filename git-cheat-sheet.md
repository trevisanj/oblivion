

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

