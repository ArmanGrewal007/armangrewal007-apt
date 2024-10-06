# Steps to contribute

...

## Notes for myself
### 1. Create a docker image and setup git in that 
This script will pull the images, tag them appropriately, and run the docker containers in detached mode. <br>
You can do `docker logs -f <container>` to see if it has been installed or not.

```
./start_services.sh
```

> Need to put the latest python file  (`cli.py`) here as `armangrewal007.py`

### 2. Creating binary and packaging it according to debian standards
1. Add ssh key of that machine to this account, so that you can push to this repo.
2. Clone this repo, and run `_automate.sh` to
    1. Automatically build binary from the python file.
    2. Place it in appropriate directory.
    3. Build the package using `debuild -us -uc`.
    4. Commit to repo with all the changes.

```
git clone git@github.com:ArmanGrewal007/armangrewal007-apt.git
```       

```
./_automate.sh
```

### 3. Publishing to deb repo
Deb repo is at `https://www.github.com/ArmanGrewal007/debian_arman`


### 4. This repo was getting to large, so here is a fix 

```bash
du -sh .git # More than 150<b
# Unstages all changes while preserving working directory
git reset --soft $(git rev-list --max-parents=0 HEAD)
git commit -m "Pushed all commits to one"
git push origin master --force
# Remove all old reflog entries and unnecessary files
git reflog expire --expire=now --all
git gc --prune=now --aggressive
du -sh .git # 32Mb only
```