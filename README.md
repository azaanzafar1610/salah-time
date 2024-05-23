# salah-time
- A webscraper which scrapes 'prayer times' from a live mosque website. 
- Prayer audio, the 'adhan', is played at each prayer time (total 5 times/day). 
- Live Demo: https://salah-time-ba63813ffa04.herokuapp.com/
# Installation
- 1 - clone repo https://github.com/azaanzafar1610/salah-time
- 2 - create a virtual environment and activate
  - pip install virtualenv
  - virtualenv envname
  - envname\scripts\activate
- 3 - cd into project "cd salah-time"
- 4 - pip install -r requirements.txt
- 5 - python manage.py runserver

- Note: To enable live 'adhan (prayer)' audio, you will need to give your browser permission to autoplay audio/video:
  - https://championcr.com/topic/enable-auto-play/#:~:text=Mac%2C%20and%20Firefox.-,Google%20Chrome,)%E2%80%9D%20to%20%E2%80%9CAllow%E2%80%9C

# Tech Stack
- Django
- JavaScript
- Bootstrap
- others: BeautifulSoup (library) for webscraping

