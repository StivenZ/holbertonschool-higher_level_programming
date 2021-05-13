$.get("https://swapi-api.hbtn.io/api/films/?format=json", function(data){
    for (movies of data.results) {
        $("#list_movies").append(`<li>${ movies.title }</li>`);
    }
});
