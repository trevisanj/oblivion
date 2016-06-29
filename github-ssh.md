# Communicating with GitHub _via_ SSH

This will configure automatic authentication and transfer to GitHub _via_ SSH, so `git push` will no longer ask
for user name and password.
 
The steps involved are roughly summarized below. For full details, please follow the
tutorials referenced below.
1. Generate a SSH key. I followed the tutorial at
   https://help.github.com/articles/generating-ssh-keys/,
   but the commands are roughly as follows:
   ```shell
   ls -al ~/.ssh  # Check existing SSH keys
   ssh-keygen -t rsa -C "your@email.com"
   ssh-add ~/.ssh/id_rsa
   <your_text_editor>  ~/.ssh/id_rsa.pub
   ```
2. Copy-paste the key to a box at a settings page at GitHub.
   After you do this, you can test if it works:
   ```shell
   ssh -T git@github.com
   ```
3. Change the remote URL that git uses. Tutorial at
   https://help.github.com/articles/changing-a-remote-s-url/
   ```shell
   git remote set-url origin git@github.com:user-name/repository-name.git
   ```
