# War Card Game / App Builder Project 

## About

This is an application built using Python and Django that simulates the card game War. There is a database that contains a list of all active players. There is functionality to allow for players to be both added and removed from the player list. When players are added the user is prompted to give them a name. Players are stored in the database along with their win/loss record until they are manually deleted. The user is able to select the two players from the database that will play each other and once selected the game of War plays in the background and the winner is displayed on the screen. The entire game play, including which cards were played every round and what each player's hand looked like after each turn is viewable in the console. After the game completes each player's database entry is updated to reflect the win or loss. The user can then select to either view the overall scoreboard or play another game.

I had a previously created Django project I last worked on just a few weeks ago that I've called "The App Builder 9000". This is more-or-less just a collection of a few fun Python projects I've completed recently that I've aggregated together into one project. I will only mention those projects here briefly as I know they aren't what this assignment was about. On the homepage of the project is a list of apps. At this point, only the top 4 apps are actually apps, the rest are just stand-ins for future apps. Besides this War Card Game application, the other 3 apps are a Weather app, a Dog adoption app, and an API that an administrator can upload JSONs to that are formatted with Apples To Apples and Cards Against Humanity cards data. Users can then use the API to play those games.

## Tradeoffs I had to make

The biggest issue I had started because I knew the game of War really well by heart from my memories of playing it as a kid. So because of that, I didn't actually look at the linked instructions until after I had already spent a long time developing the game logic. As it turns out, the War rules I played as a kid are apparently not universal. I'm used to ties resulting in each player needing to lay an additional 3 cards down on the table and then playing a 5th card to decide who wins the war. As I learned, this can result in quite a lot of different end-game scenarios that need to be accounted for in the game logic. I spent a ton of time that ended up being wasted trying to write all that logic. In the end, I couldn't get it to work out because I kept running into edge cases where a player would go into war with 0-4 cards. Because I couldn't get this to work out, I got rid of all that logic and created a more simple end-game scenario where if a player goes into a War with less then the number of cards needed to complete the war ordinarilly (5 cards) the game was awarded to the other player.

The other tradeoff I had to make was that I was hoping to display the game details on the webpage instead of just in the console. In the end, I didn't have the time to do this, so I settled on just displaying a message on the webpage to check the console for game details and included a bunch of print statements to make everything that happened in the game appear there.

## How to run project

#### Download project and create the environment to run it in:

```bash
# Create access project folder
~$  mkdir some_folder
~$  cd some_folder

# Clone or Download Project
~$  git clone https://github.com/brenton26/DjangoProject.git

# Create Python virtual env 
~$  python3 -m venv env

# Activate virtual env
~$  source env/bin/activate

# Install project requirements
~$  cd DjangoProject
~$  pip install -r requirements.txt
```

#### Make any necessary migrations

```bash
# Create Migration files if they aren't already present
~$  python manage.py makemigrations

# Read and apply Migrations
~$ python manage.py migrate
```

#### Start the server

```bash
# Starts server
~$ python manage.py runserver
```

#### Go To Projoect

Paste the URL into your browser: 'http://127.0.0.1:8000/'

#### Other thing to know

On the homepage, you can access the War Game by clicking on the image with playing cards on it. You are more than welcome to explore the other apps as well. Both the Weather app and Dog app are pretty self-explanatory to use. The API one is more complicated because it requires an administrator to upload a JSON to be access at an endpoint. The endpoints wont work until that happens. 
