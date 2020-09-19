#!/bin/bash

git config pull.rebase false
git config user.name "p1ratrulezzz"
git config user.email "git@p1ratrulezzz.me"
KEY_PATH=$(pwd -P)"/deployment-private.key"
KEY_PATH_PUB=$(pwd -P)"/deployment-public.key"
echo "${SSH_PUBKEY}" > "${KEY_PATH_PUB}"
echo "Adding an SSH key to agent"
eval $(ssh-agent -s)
touch "${KEY_PATH}"
chmod 0600 "${KEY_PATH}"
echo "${SSH_PRIVATEKEY}" > "${KEY_PATH}"
ssh-add -t 3600 "${KEY_PATH}"
sudo apt install -y python3-venv git
echo "Checkout master"
git fetch origin
git checkout -b master origin/master
git pull origin master
echo "Deleting words dir"
git rm -r words
mkdir words
echo "Renegerating..."
chmod +x ./regenerate_html.sh
./regenerate_html.sh
echo "Add to git"
git add words
git add index.html sitemap.xml
git commit -m"[skip-ci] Words CI update"
git push -f origin master
rm -f "${KEY_PATH_PUB}"
rm -f "${KEY_PATH_PUB}"
