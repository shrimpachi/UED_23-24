# How to update your branch to avoid merge conflicts

## \(Updating your branch from main is the **__FIRST__** thing you should do, always, and forever. Before you add anything. Before you even think about adding anything. Before you have your morning coffee.\)

### Pre req's

You should be using a Bash or Bash-like shell like Zsh. Don't have one? **Grow up. You're an adult and it's time you get an OS to match.**\* [At the very least you should have access to the linux sub-sys on your DOS machine to perform the following.](https://learn.microsoft.com/en-us/windows/wsl/install)

You should have already cloned the project to your own computer
Confused? [Don't be!](https://docs.gitlab.com/ee/gitlab-basics/start-using-git.html).


### Let's make a script!

#### [Navigate](https://www.freecodecamp.org/news/command-line-for-beginners/) to the folder **above** your clone. For me it's

    cd ~/Desktop/School/UU/expDsgn/

but you'll have a different spot.
You might need the ls command to list your folders and find your way.


#### Create a new file

    touch syncBranchWithMainScript


#### Edit the file to add the code

    nano syncBranchWithMainScript


#### Now paste the code into the terminal ~ Don't forget to change \<my-clone\> & \<my-branch\> to your own clone's name \(probably ued2023\) and change branch's name

    cd <my-clone>

    git checkout main

    git fetch -p origin

    git merge origin/main

    git checkout <my-branch>

    git merge main -m "updating my branch to avoid merge conflicts"

    git push origin <my-branch>


#### Finally,you can make the file executable so when you type the name in, it automatically runs and does our work for us

    chmod +x syncBranchWithMainScript


#### Now, when you want to mess with your clone you can go back to your clone's containing folder like

    cd ~/Desktop/School/UU/ExpDsgn/

and

    ./syncBranchWithMainScript

to get your branch back up to speed with main.


##### Doesn't work? Check the error. If it's about the first line "line 1: cd: ... No such file or directory" it's because you have a mistake in your path.

##### You might want to use your file browser to graphically navigate to your folder and copy the path from there.




*Don't believe Windows is for children? It's a reskinned copy of Windows NT \(released '93\) which is based on DOS \(released '81\). It has been 12 years old for 30 years now. It's time to grow up, but Microsoft lives in Neverland, so you'll have to grow up without them. You need to get yourself a modern, secure, Unix/Unix-like OS like Fedora, Mint, Ubuntu or macOS. Too scared to install it directly on your computer's default boot disk? [Make a live USB](https://ubuntu.com/tutorials/create-a-usb-stick-on-windows#1-overview)
