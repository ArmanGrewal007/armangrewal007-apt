#! /usr/bin/env bash

# Author: Arman Grewal
#################################################
# Does all the heavy lifting of creating binary
# creating deb package from that binary
# and pushing to github
# NOTE: this must be ran on different archs
# to create different .deb packages
#################################################

PACKAGE_NAME="armangrewal007"
export DEBEMAIL="armansinghgrewal@gmail.com" # For dch command

############ Fetch the latest version from PyPI ############
LATEST_VERSION=$(curl -s "https://pypi.org/pypi/${PACKAGE_NAME}/json" | jq -r .releases | jq -r 'keys | .[]' | sort -V | tail -n 1)
echo "Latest version on PyPI: ${LATEST_VERSION}"


############# Package already created? ############
ARCHITECTURE=$(uname -m)
FICTIONAL_FILE_NAME="armangrewal007_${LATEST_VERSION}_${ARCHITECTURE}.deb"
if [[ -f "$FILE_NAME" ]]; then
    echo "$FILE_NAME exists. so exiting"
    exit 0
fi

############# Update dirname and changelog ############
CURRENT_VERSION="$(ls -d armangrewal007-* | xargs -n 1 basename | awk -F'-' '{print $NF}')"
cd "armangrewal007-${CURRENT_VERSION}"
# # Run this if you are creating the package for first time
# dch --create -v 0.1.3 --package armangrewal007
# Add to changelog for new version/new architecture or both
dch -v "${LATEST_VERSION}" "Added v${LATEST_VERSION} for ${ARCHITECTURE}"
# Just go back and get into the new dir
PACKAGE_DIR="armangrewal007-${LATEST_VERSION}"
cd ..

############# Create a venv and build binary for this architecture #############
echo -e "Creating a venv and building binary for ${ARCHITECTURE}\n"
mkdir temp
cp armangrewal007.py requirements.txt temp/
cd temp
python3 -m venv venv # Even if it exists, it will just overwrite
source venv/bin/activate
pip3 install -r requirements.txt
echo -e "${YELLOW_BOLD}TIP:${RESET} ${YELLOW_IT}can abort this step using ctrl+z, then you can access the terminal${RESET}"
sleep 1
# nuitka --standalone --onefile --include-package=rich ../armangrewal007.py
pyinstaller --onefile armangrewal007.py 
mv "dist/armangrewal007 ../${PACKAGE_DIR}/usr/bin_${ARCHITECTURE}/"
deactivate 
cd ..
rm -rf temp # No need for all the .build, .dist, .onefile-build directories

############# Create the .deb package #############
# Create a orig tarball before building the package
# Required by 3.0 (quilt) format of debuild
tar czf armangrewal007_0.1.3.orig.tar.gz --exclude-vcs --exclude=debian armangrewal007-0.1.3
cd "${PACKAGE_DIR}"
debuild -us -uc
cd ..

############# Push to github #############
git config --global user.name "Arman Grewal"
git config --global user.email "armansinghrewal@gmail.com"

YELLOW_IT="\e[33;3m"
YELLOW_BOLD="\e[33;1m"
RESET="\e[0m"
echo -e "${YELLOW_BOLD}TIP:${RESET} ${YELLOW_IT}can abort this step using ctrl+z, then you can access the terminal${RESET}"
echo -e "${YELLOW_IT}you can run git diff, or anything you deem necessary${RESET}"
echo -e "${YELLOW_IT}further lines are just add, commit and push to git${RESET}"

read -p "Are you sure you want to add and commit v${LATEST_VERSION} for ${ARCHITECTURE}? (y/n): " confirmation
if [[ "$confirmation" != "y" ]]; then
    echo "Operation canceled."
    exit 0
fi

# Commit to git
git add .
git commit -m "Added v${LATEST_VERSION} for ${ARCHITECTURE}"
git push
