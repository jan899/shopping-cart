# Grocery Checkout

## Repo Setup

Use the GitHub online interface to create a new remote project repository called something like "rock-paper-scissors-exercise". 

After creating the remote repo, use GitHub Desktop software or the command-line to download or "clone" it onto your computer. Choose a familiar download location like the Desktop.

After cloning the repo, navigate there from the command-line:

```
cd ~/OneDrive/Desktop/GitHub/shopping-cart
```

## Environment Setup

Create and activate a new Anaconda environment

Run the requirements file to install all required third-party packages

```
pip install -r requirements.txt
```

Open up the repository in a text editor, and create a new .env file. Input your desired sales tax with the following variable 

```
TAX_RATE=0.0875
```

## Execute

Within an active virtual environment of choice ("base" or project-specific), run the Python script from the command line:

```
python shopping_cart.py
```