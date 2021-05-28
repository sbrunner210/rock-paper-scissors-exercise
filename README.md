# rock-paper-scissors-exercise
## First Class Deliverable (5/30/2021)

A game of "Rock, Paper, Scissors" for the user to compete against the computer.

## Prerequisites

  + Anaconda 3.7+
  + Python 3.7+
  + Pip

## Installation

Navigate to the app's folder from the command line.:

```sh
cd rock-paper-scissors-exercise
```

Use Anaconda to create and activate a new virtual environment, perhaps called "my-first-env":

```sh
conda create -n my-first-env python=3.8
conda activate my-first-env
```

After activating the virtual environment, install package dependencies (see the ["requirements.txt"](/requirements.txt) file):

```sh
pip install -r requirements.txt
```

## Setup

In in the root directory of your local repository, create a new file called ".env", and update the contents of the ".env" file to specify your desired username:

    user ="ENTER PLAYER NAME"
    
## Usage

Run the game script:

```py
python game.py
```

> NOTE: if you see an error like "ModuleNotFoundError: No module named '...'", it's because the given package isn't installed, so run the `pip` command above to ensure that package has been installed into the virtual environment.

