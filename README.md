# unminipy

A small utility for unminifying minified JSON to assist with readability.

<p align="center">
  <img width="300" height="300" src="./assets/logo.png" alt="focus"/>
</p>

## Usage

To install unminipy, visit the [releases](https://github.com/steebe/unminipy/releases) page and install the latest.

### Warning

Presently, unminipy is only supported on MacOS. Soon, I will release versions compatible with Windows and Linux.

---

### Manual setup

#### script/

##### Using the venv

To initialize the venv:
```shell
[unminipy]$ script/init.sh
```

To activate the venv:
```shell
[unminipy]$ source script/env-up.sh
```

To deactivate the venv:
```shell
(unminipy-env)[unminipy]$ deactivate

# OR

(unminipy-env)[unminipy]$ source script/env-down.sh
```

##### Building
```shell
# (with the venv active)
[unminipy]$ script/build.sh
```
