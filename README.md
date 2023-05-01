# dictionary

Its a simple python app which helps in understanding how to build Docker fastapi app and then  push this docker image in Github Container Registry ghcr.io

You can pull this docker package directly into your terminal through  the docker pull command.

$ docker pull ghcr.io/thevineet/dictionary:v1

This app returns the meaning of any word whenever any api request is made.
There are two api routes
-http://localhost:8000/{word}
  It returns the meaning of the word passed to it through the path variable 'word'
  
-http://localhost:8000/closed/{word}
  It returns 3 closedly matches words for the word passed through it through the path variable 'word'. This could be useful to show the meanings of wrongly spelled
  words as well.
  
 Examples
 -http://localhost:8000/bird 
   {
   "success":1,
    "data":
      ["Any of the bipedal, warm-blooded vertebrates that lay eggs having wings which, 
       for most species, enables them to fly.","A powered heavier-than-air aircraft with fixed wings that 
       obtains lift by the Bernoulli effect and is used for transportation.","Badminton equipment consisting
       of a ball of cork or rubber with a crown of feathers."]
    }
  
 -http://localhost:8000/teamm
  {"success":0,"data":"Word not found"}
 
 -http://localhost:8000/closed/teamm
  {"success":1,"data":["team","steam","tea"]}
 
 -http://localhost:8000/closed/tkttktkt
 {"success":0,"data":"Word not found"}
 
