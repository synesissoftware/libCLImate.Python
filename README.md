# libCLImate.Python <!-- omit in toc -->

Command-Line Interface boilerplate mini-framework, for Python

![Language](https://img.shields.io/badge/Python-3776AB?style=flat&logo=python&logoColor=white)
[![License](https://img.shields.io/badge/License-BSD_3--Clause-blue.svg)](https://opensource.org/licenses/BSD-3-Clause)
[![PyPI](https://img.shields.io/pypi/v/libclimate.svg)](https://pypi.org/project/libclimate/)
[![GitHub release](https://img.shields.io/github/v/release/synesissoftware/libCLImate.Python.svg)](https://github.com/synesissoftware/libCLImate.Python/releases/latest)
[![Last Commit](https://img.shields.io/github/last-commit/synesissoftware/libCLImate.Python)](https://github.com/synesissoftware/libCLImate.Python/commits/master)
[![CI](https://github.com/synesissoftware/libCLImate.Python/actions/workflows/python-package.yml/badge.svg)](https://github.com/synesissoftware/libCLImate.Python/actions/workflows/python-package.yml)
![Python](https://img.shields.io/badge/Python-2.7%20%7C%203.8+-lightgrey)


## Table of Contents <!-- omit in toc -->

- [Introduction](#introduction)
- [Installation](#installation)
- [Components](#components)
- [Project Information](#project-information)
  - [Where to get help](#where-to-get-help)
  - [Contribution guidelines](#contribution-guidelines)
  - [Dependencies](#dependencies)
    - [Efferent (fan-out)](#efferent-fan-out)
    - [Development Dependencies](#development-dependencies)
    - [Afferent (fan-in)](#afferent-fan-in)
  - [Related projects](#related-projects)
  - [License](#license)


## Introduction

**libCLImate** is a portable, lightweight mini-framework that encapsulates the common aspects of **C**ommand-**L**ine **I**nterface boilerplate, including:

* command-line argument parsing and sorting, into flags, options, and values;
* validating given and/or missing arguments;
* a declarative form of specifying the CLI elements for a program;
* provision of de-facto standard CLI facilities, such as responding to '--help' and '--version';

**libCLImate.Python** is the **Python** version. It wraps [**CLASP.Python**](https://github.com/synesissoftware/CLASP.Python) (**pyclasp**). This repository is a packaging skeleton; the **Climate** API is not implemented yet.


## Installation

Install via **pip**:

```
pip install libclimate
```

Use via **import**:

```Python
import libclimate

print(libclimate.__version__)
```


## Components

Skeleton; **Climate** API not yet implemented.


## Project Information


### Where to get help

[GitHub Page](https://github.com/synesissoftware/libCLImate.Python "GitHub Page")


### Contribution guidelines

Defect reports, feature requests, and pull requests are welcome on https://github.com/synesissoftware/libCLImate.Python.


### Dependencies


#### Efferent (fan-out)

* [**CLASP.Python**](https://github.com/synesissoftware/CLASP.Python/) (**pyclasp**);
* [**Diagnosticism.Python**](https://github.com/synesissoftware/Diagnosticism.Python/) (**diagnosticism**);
* [**woad.Python**](https://github.com/synesissoftware/woad.Python/) (**woad**);


#### Development Dependencies

* [**pytest**](https://docs.pytest.org/);


#### Afferent (fan-in)

None (currently).


### Related projects

* [**CLASP**](https://github.com/synesissoftware/CLASP/);
* [**CLASP.Go**](https://github.com/synesissoftware/CLASP.Go/);
* [**CLASP.js**](https://github.com/synesissoftware/CLASP.js/);
* [**CLASP.NET**](https://github.com/synesissoftware/CLASP.NET/);
* [**CLASP.Python**](https://github.com/synesissoftware/CLASP.Python/);
* [**CLASP.Ruby**](https://github.com/synesissoftware/CLASP.Ruby/);
* [**libCLImate** (C/C++)](https://github.com/synesissoftware/libCLImate);
* [**libCLImate.Go**](https://github.com/synesissoftware/libCLImate.Go);
* [**libCLImate.NET**](https://github.com/synesissoftware/libCLImate.NET);
* [**libCLImate.Ruby**](https://github.com/synesissoftware/libCLImate.Ruby);


### License

**libCLImate.Python** is released under the 3-clause BSD license. See [LICENSE](./LICENSE) for details.


<!-- ########################### end of file ########################### -->
