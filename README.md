# osudata
Scripts for collecting and analyzing osu! game data

## Installing MongoDB
Download and install the latest version of <a href="https://www.mongodb.com/what-is-mongodb">MongoDB</a>.
Current version in use is MongoDB 4.0

## Populating Database
Done through the commandline. Python 3.6+ needs to be installed also with requirements.txt
populate a database by: `python populate.py DatabaseName`
specify mode or modes by `-m`:<br> 
`python populate.py Database -m standard`
Modes: standard, taiko, catch, mania

Databases:<br>
Beatmaps<br>
TopPlays<br>
TopPlayers<br>
TopCountryPlayers<br>


## Beatmap Recommendations
Recommendations are currently done using local database data. Thereby the `TopPlayersAPI`, `TopCountryPlayers`, and `Leaderboard` databases all have to be populated. Not all data for each mode needs to exist, just all the data for the mode that is being recommended. For example, if one wants to only make recommendations for standard osu they don't need to populate the other modes' databases. 

