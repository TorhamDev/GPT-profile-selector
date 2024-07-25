# GPT-profile-selector
let ChatGPT select a profile picture for you!

## How to run?
```bash

# clone repo
git clone https://github.com/TorhamDev/GPT-profile-selector.git

cd GPT-profile-selector

# install packages
pip install -r requirements.txt

# Setup database
python manage.py makemigrations 
python manage.py migrate

# Run basic development server
python manage.py runserver
```