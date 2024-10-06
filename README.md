<div align="center">
  <h1>armangrewal007</h1>
  <img src="armangrewal007-aarch64-v0.1.3.gif" /> <br>
  (This GIF demonstrates version <code>v0.1.3</code> running on an <code>aarch64</code> Docker container, along with another Docker container acting as a Debian repository hosting the package. <a href="https://www.github.com/ArmanGrewal007/debian_arman">Link to my debian repository</a>)
</div>

-------------

<div align="center"><h4><a href="Contributing.md">Click here</a> if you want to know how I built it, or you want to contribute ❤️</h4></div>


## Steps to install

> [!Caution]
> The Debian repo still needs to be hosted somewhere. 😭

Assuming the repo has been hosted on this URL, export the hosted URL as a env variable
```
export ARMAN_URL="http://192.168.0.117:8000"
```

You can copy the following commands all at once, and paste in the terminal <br>
Most modern terminals can run them one by one by themselves
```bash
echo "deb [arch=amd64,arm64] $ARMAN_URL stable main" | 
sudo tee /etc/apt/sources.list.d/debian_arman.list
sudo apt update --allow-insecure-repositories
sudo apt install armangrewal007 --allow-unauthenticated
```




---------

Typical directory structure of a `Debian package`
```ruby
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
            |   `-- <package-binary>
            `-- bin_x86_64
                `-- <package-binary>
```


