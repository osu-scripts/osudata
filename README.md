# osudata
Python scripts for collecting and analyzing osu! game data

## Installing MongoDB
Download and install the latest version of <a href="https://www.mongodb.com/what-is-mongodb">MongoDB</a>. Current version in use is 4.0

## Populating Database
Populating is done through the command line. Python 3.6+ is needed along with requirements.txt
Once in the project directory with python and the other requirements installed use ```python populate.py Database``` to populate a database. By default data for all games modes is populated. You can choose specific game mode(s) by using ```-m ``` followed by the the name of the mode or modes. Game mode are standard, taiko, mania, and catch. 

Populating TopPlays data base for osu!standard only 
```python populate.py TopPlays -m standard```

Populating Beatmaps database for taiko and catch
```python populate.py Beatmaps -m taiko catch```

Databases:<br>
Beatmaps<br>
TopPlays<br>
TopPlayers<br>
TopCountryPlayers<br>


## Beatmap Recommendations
Recommendations are currently done using local database data. Thereby the `TopPlayersAPI`, `TopCountryPlayers`, and `Leaderboard` databases all have to be populated. Not all data for each mode needs to exist, just all the data for the mode that is being recommended. For example, if one wants to only make recommendations for standard osu they don't need to populate the other modes' databases. 

