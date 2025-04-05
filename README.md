# Twitter Like Remover Script

This script automates the process of removing likes (unliking tweets) on Twitter using Selenium and Python. It uses a Chrome WebDriver to navigate through Twitter and removes all likes from the logged-in user's profile.

## Features
- Automatically logs into Twitter using your username and password.
- Finds and clicks the "Unlike" button on tweets.
- Scrolls down the likes page to load more tweets and continues removing likes.
- Supports multiple XPath variations for locating the "Unlike" button.
- User-friendly and easy to use.

## Requirements

Before running the script, ensure you have the following dependencies installed:

- Python 3.x
- Selenium
- ChromeDriver (for Mac, Windows, or Linux depending on your OS)

### Install Selenium

You can install Selenium using pip:

```bash
pip install selenium
