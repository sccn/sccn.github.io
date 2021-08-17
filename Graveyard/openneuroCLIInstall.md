https://github.com/OpenNeuroOrg/openneuro/tree/master/packages/openneuro-cli

Check to make sure bash is used (nemar-dev defaults to tcsh) and change if necessary
```sh
echo $SHELL
chsh --shell /bin/bash <username>
```
Install nvm 
```sh 
curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.38.0/install.sh | bash
```
Install nodejs@14 through nvm
```sh
nvm install 14
```
Install openneuro-cli
```sh
npm install -g @openneuro/cli
```
Follow **Setup** guide [here](https://github.com/OpenNeuroOrg/openneuro/tree/master/packages/openneuro-cli) to login, then check **Usage**.

If you encounter "Error: Cannot find module 'react'", manually install react locally where openneuro-cli is located.
```sh
cd /home/<username>/.nvm/versions/node/v14.16.1/lib/node_modules/openneuro-cli
npm install react
```
