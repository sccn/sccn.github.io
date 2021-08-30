### Installation Steps
https://github.com/OpenNeuroOrg/openneuro/tree/master/packages/openneuro-cli

1. Check to make sure bash is used (nemar-dev defaults to tcsh) and change if necessary
```sh
echo $SHELL
chsh --shell /bin/bash <username>
```
2. Install nvm 
```sh 
curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.38.0/install.sh | bash
```
3. Install nodejs@14 through nvm
```sh
nvm install 14
```
4. Install openneuro-cli
```sh
npm install -g @openneuro/cli
```
5. Follow **Setup** guide [here](https://github.com/OpenNeuroOrg/openneuro/tree/master/packages/openneuro-cli) to login, then check **Usage**.


### Troubleshoot
* If you encounter "Error: Cannot find module 'react'", manually install react locally where openneuro-cli is located.
```sh
cd /home/<username>/.nvm/versions/node/<v#>/lib/node_modules/openneuro-cli
npm install react
```

* To update the OpenNeuro client:
```sh
npm update openneuro-cli
```
