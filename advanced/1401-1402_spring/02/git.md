Download git for windows
Create an account on github
Create a new repository

…or create a new repository on the command line
echo "# test-python2" >> README.md
git init
git add README.md
git commit -m "first commit"
git branch -M master
git remote add origin https://github.com/mohammadmasoumi/test-python2.git
git push -u origin master

…or push an existing repository from the command line
git remote add origin https://github.com/mohammadmasoumi/test-python2.git
git branch -M master
git push -u origin master