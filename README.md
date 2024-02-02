# networkScan
# github configuration
echo "# networkScan" >> README.md
git config --global user.email xxxxx
git config --global user.name mdxxxx
git config --global core.excludefile ~/.gitignore_global

  git init
  git add README.md
  git commit -m "first commit"
  git branch -M master
  git remote add origin git@github.com:mdengapa/networkScan.git
  git remote add origin https://github.com/mdengapa/networkScan.git
  git push -u origin master

git rm -r --cached . && git add .
git commit -m "new devices in file" && git push -u origin master

