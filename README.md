# Grocery Checkout

## Repo Setup

Use the GitHub online interface to create a new remote project repository. Give it the name: "shopping_cart". 

After creating the remote repo, use GitHub Desktop software or the command-line to download or "clone" it onto your computer

After cloning the repo, navigate there from the command-line. For example:

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

## Sendgrid Setup 

Sign up for a SendGrid account, and complete your "Single Sender Verification." Check your email to verify your account. 

Create a SendGrid API Key with "full access" permissions. 

In your .env file, create a variable for your SendGrid API Key:

```
SENDGRID_API_KEY =
```

Additionally create a variable for your SENDER_ADDRESS. This should be the same email address as the single sender address you just used in your SendGrid account. 

```
 SENDER_ADDRESS =
```
