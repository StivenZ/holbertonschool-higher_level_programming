# JavaScript - Web scraping

### 0.Readme
Reads and prints the content of a file.

#### USAGE: ```$ ./0-readme.js some_file```



### 1.Write me
Script that writes a string to a file.

#### USAGE: ```$ ./1-writeme.js my_file.txt "Python is cool"```



### 2.Status code
Displays the status code of a ```GET``` request. First argument is the URL to request from.

#### USAGE: ```$ ./2-statuscode.js https://intranet.hbtn.io/status```



### 3.Star wars movie title
Requests the title of a Star Wars movie where the episode number matches given parameter.

#### Ednpoint: https://swapi-api.hbtn.io/api/films/:id
#### USAGE: ```$ ./3-starwars_title.js 1```



### 4. Star wars Wedge Antilles
Prints the number of movies where the character “Wedge Antilles” is present.
First argument is the API URL: https://swapi-api.hbtn.io/api/films/
Character's ID is 18 (used to filter)

#### USAGE: ```$ ./4-starwars_count.js https://swapi-api.hbtn.io/api/films```



### 5.Loripsum
Gets the contents of a webpage and stores it in a file.
The first argument is the URL to request.
The second argument the file path to store the body response.

#### USAGE: ```$ ./5-request_store.js http://loripsum.net/api loripsum```



### 6. How many completed?
Write a script that computes the number of tasks completed by user id.
The first argument is the API URL: https://jsonplaceholder.typicode.com/todos

#### USAGE: ```$ ./6-completed_tasks.js https://jsonplaceholder.typicode.com/todos```
