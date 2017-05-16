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

### :notes: **Resolve conflicts**

```shell
git branch --create newbranch
git checkout newbranch
git push --set-upstream origin newbranch
```



# Communicating with GitHub _via_ SSH

This will configure automatic authentication and transfer to GitHub _via_ SSH, so `git push` will no longer ask
for user name and password.
 
The steps involved are roughly summarized below. For full details, please follow the
links provided.

:one: Generate a SSH key

```shell
ls -al ~/.ssh  # Check existing SSH keys
ssh-keygen -t rsa -C "your@email.com"
ssh-add ~/.ssh/id_rsa
```

**Note** if `ssh-add ...` above fails: run 

```
eval `ssh-agent -s`
```

and retry.

(https://help.github.com/articles/generating-ssh-keys/)

:two: Open file _~/.ssh/id_rsa.pub_ using any text editor and copy its contents to the clipboard (Ctrl+C)

:three: Go to GitHub, personal settings, look for "SSH and GPG keys", click on "New SSH key", and paste the contents of _~/.ssh/id_rsa.pub_ into the appropriate box.

After you do this, you can test if it works:

```shell
ssh -T git@github.com
 ```
 
:four: Change the remote URL that git uses

```shell
git remote set-url origin git@github.com:user-name/repository-name.git
```

(https://help.github.com/articles/changing-a-remote-s-url/)
