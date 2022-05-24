# CLI Intro

`pwd` - print workign directory

`ls` - list
`ls -a` - list all files, including hidden files

`cd` - change directory

`cd ..` - change to parent directory

`cd ~` - change to home folder

`touch filename.txt` - create a new file

`cp file newfile` - copy a file
`cp -r folder newfolder` - copy a folder

`mv oldfile newfile` - move or rename a file or folder

`rm filename` - delete a file
`rm -r folder` - delete a folder
`rm -rf folder` - delete a folder without confirmation. be careful, there's no undo!

if you get an error when running a command, EACCESS - error, access. Try prefixing that command with "sudo" stands for "super user DO". 
the root user can do anything, but this is dangerous. 

vim is a command-line text editor.

vim has multiple modes: insert mode lets you insert text when you press letters
press <Esc> to get into normal mode
type a colon for ex mode:
    `:wq` - save and quit
    `:q!` - quit without saving


# GIT
git is a commandline program for tracking changes to a project
github.com is a website that hosts git repositories, that enables us to collaborate with each other

`git init` create an empty git repo. creates the `.git`. folder. 
`git status` ask git about the current status of the repo
`git add .` (stage) prepare  all files to be committed
`git commit -m "Message"` commit staged files


get started on the homework
- go to the day's curriculum, check out the exercices at the bottom
- fork the repo from romeo's github org to your own github account. (forking copies a repo from a github account to another github account)
- after forking it into your personal account, you can clone the repo, which copies it to your local machine. cloning copies a repo from github.com to your local computer.

- IF YOU CAN'T FORK:
    - clone the repo from romeo's github org to your local machine: `git clone <repo url>`
    - remove the existing remote, disconnecting this repo from romeo: `git remote rm origin`
    - create a new repo in your personal github account
    - set up that new repo in your github account as the remote for your local repo: `git remote add origin <repo url>`
