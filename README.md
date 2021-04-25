## About The Project
### IVS - Project 2 - F11 Calculator
![F11 Calculator](screenshot.png?raw=true "F11 Calculator")

Basic mathematical calculator with GUI, mathematical operations, factorials, roots, documentation, manual and math library.

### About
The main point of this project was to learn how to work in a team, use git and to try and create a new software product from scratch. 
This involves: creating a plan of the project, programming individual units that will make up our project, testing them, integrating them and creating one, fully operational software product which should fill the needs of our customer.

### Assignment
The project assignment from BUT FIT - IVS can be found [here](http://ivs.fit.vutbr.cz/projekt-2_tymova_spoluprace2020-21.html)

### Build With
* [Python](https://www.python.org/)
* [PyQt](https://riverbankcomputing.com/software/pyqt)

### System
* Windows 64-bit

## Getting Started
To get a local copy up and running follow these simple steps.
If you want only the calculator not code use installer [here](#install)

**Prerequisites before steps:**
* [Python](https://www.python.org/downloads/windows/) 3.9.1 or greater
* [Git](https://git-scm.com/download/win) 2.31.1 or greater
* [GnuWin](http://gnuwin32.sourceforge.net/packages/make.htm) (make) 3.81 or greater
* [Doxygen](https://www.doxygen.nl/download.html) 1.9.1 or greater

*Don't forget to add directories to the PATH ([tutorial](https://stackoverflow.com/questions/9546324/adding-a-directory-to-the-path-environment-variable-in-windows))*

1. Clone the repo
    ```
    git clone https://github.com/FNewel/floor11_calc.git
    ```
2. Build it (also checks all prerequisites)
    ```
    cd ./floor11_calc/src
    make
    ```
* Or you can only check prerequisites for Python
    ```
    make prerequisites
    ```
3. Run it
    ```
    python calc_main.py
    or
    make run
    ```

### Install
!TODO - až spravíme inštalačku

### Usage
!TODO - neskôr až bude kalkulačka hotova +- dokumentácia
For more examples, please refer to the [Documentation](dokumentace.pdf)

### Authors
* Martin Talajka - [FNewell](https://github.com/FNewel)
* Ondrej Kováč - [MasloJePotravina](https://github.com/MasloJePotravina)

### License
Distributed under the GPL-3.0 License. See [LICENSE](LICENSE) for more information.
