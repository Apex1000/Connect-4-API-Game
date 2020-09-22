# Connect 4 API Game<hr>

## Installation 

### Create an environment
```
python -m venv env
```

```
source env/bin/activate
```

### Clone Repo
```
cd pratilipi_api_task
```

### Install dependencies
```
pip install -r requirements.txt
```
### Run application
```
flask run
```
### API Hits
#### To Enter the game
```
http://127.0.0.1:5000/
```
#### To start the game 
```
http://127.0.0.1:5000/game
```

### Log DB
```
http://127.0.0.1:5000/lgg
```

#### JSON Data format
Player 1
```
{
	"player":"Yellow",
	"move":3
}
```
Player 2
```
{
	"player":"Red",
	"move":3
}
```

Note: - By this time it case sensitive


Hosted on Heroku:- 

```
https://cot-4.herokuapp.com/ 
```

To Start game
```
https://cot-4.herokuapp.com/game 
```
