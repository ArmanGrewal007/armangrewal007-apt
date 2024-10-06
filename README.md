## Steps to install

> [!Caution]
> This directory still needs to be hosted somewhere. 

Export the hosted URL as a env variable
```
export ARMAN_URL="http://192.168.0.117:8000"
```

You can copy the following commands all at once, and paste in the terminal <br>
Most modern terminals can run them one by one by themselves
```
echo "deb [arch=amd64,arm64] $ARMAN_URL stable main" | sudo tee /etc/apt/sources.list.d/debian_arman.list
sudo apt update --allow-insecure-repositories
sudo apt install armangrewal007 --allow-unauthenticated
```




---------

Typical directory structure of a `Debian package`
```
.
|--<package>-<version>
    |-- debian
    |   |-- changelog
    |   |-- compat
    |   |-- control
    |   |-- copyright
    |   `-- rules
    `-- usr
        `-- local
            |-- bin_aarch64
            |   `-- armangrewal007
            `-- bin_x86_64
                `-- armangrewal007
```
