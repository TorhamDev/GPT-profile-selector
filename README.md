# GPT-profile-selector
let ChatGPT select a profile picture for you!

> this is an assignment but i like the idea!

The idea is you have lots of photos and you don't know which one is good for your profile 😕
So instead of using your brain and choosing a profile picture, you ask ChatGPT to select a photo based on images you have on this platform. After that ChatGPT selects one for you and tells you why he selected this image :)
So now you have a profile picture and we have money 🧠

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