#Working with Git in a team

`git status`
`git init`
`git status`
`git add .`
`git commit -m "first message"`

## Set up a repository

`git remote add origin <url>`
When you are creating a new branch you are going to use `checkout -b` then have two branch names.
First is the new branch name,
Second is the branch you are branching from.
We're creating `delete-coffee-order` from the `master` branch
`git checkout -b delete-coffee-order master`
To check the branch you're on.
`git branch`
Creating the new files that you are adding to your directory.
`touch deleteOrderView.swift`
Then you can add the individual file by itself.
`git add deleteOrderView.swift`
`git status`
`git commit -m "deleting coffee order"`
At this point there's not a point for pushing this branch, you really would want to merge it into the master.
`git checkout master`
`git pull`
When you are on the master branch you use git pull to get the most recent updates.
If you do not do a git pull before trying to do a git push it will inform you that you are not in the same number of commits as the origin master.
At this point you will have to solve any issues with merging the files.
`git commit -m "resolving merge conflicts"
This will merge the branch into the master
`git merge delete-coffee-order`
Then you will update the remote repository on GitHub.
`git push`

##Making another branch - The cleaner and recommended approach!

`git status`
`git branch`
`git checkout -b bug-responsive-design delete-coffee-order`
`ls`
`touch bigfixes.txt`
`ls`
`git status`
`git add .`
`git commit -m 'bug fixed'`
`git status`
Here you can do a reverse merge, merging the master into your branch, then merge the branch into the master.
This way if it is broken, then your branch is broken, and the master isn't broken.
First step would be checking that the master is up to date!
`git checkout master`
`git pull`
`git checkout bug-responsive-design`
`git merge master`
`git status`
__In your real job you will then run Unit Tests here!!__
`git checkout master`
`git merge bug-responsive-design`

Once you have merged your branch to the master, go ahead and delete your branch.
This won't do anything, but it will keep your repository clean!

##What is a Fork?

A fork is a clone of the repository, but you are changing the direction that the code is written in!
*An example would be...*
__Google is making an android functionality. Samsung likes the information, and takes their initial information, and modifying it with what they want to do with the information after the fact.__

##Cloning the repository

When working on a group you will have the group clone the repository.
You will not download the zip folder, you wouldn't get any changes from the rest of the group.
One person will be the owner of the repository, and everyone else in the group will clone the repository!
This way if someone will push something and you use git pull you will then get that information.