# Steam_API_Data
Our project focuses on Steam which is a game distribution service. The sources of data we extracted were primarily from the Steam API website itself (https://partner.steamgames.com/doc/webapi_overview) and SteamSpy (https://steamspy.com/api.php). These APIs had information that was searchable based on how often games were played, the genre of the game, prices, etc… The data was already formatted in JSON documents from SteamSpy. From the Steam API, we used the splinter library to pull game data such as metacritic scores, reviews, release dates, etc… Due to the enormousness of the Steam website, our group focused on Free-to-play games and top-100 games all-time. We performed two different methods to acquire information on the Free-to-play: api call and web-scraping.

We performed an api call on the Free-to-play games utilizing the base url provided from SteamSpy along with a list of genres, which was indexed within our API request. A list was created in the event we decide to expand our database at a later time. Our API request joins the base url with the desired genre and the response provided in a JSON format. The type of transformation needed for this data (cleaning, joining, filtering, aggregating, etc).

We decided to do a join on the app_id because it is unique to the game itself compared to joining it based on price, developer, and other things. All three datasets have the app_id so it would be the best way to combine all the information together.

We used a non-relational database (MongoDB) because some data will be missing especially when our group focused on different categories. Games that are more popular will have more information about them in the database but one that is not as popular may not show up in the data under top 100 of all time from SteamSpy, but may show up under “Free to Play”. A non-relational database is therefore preferred in this case if we want to grab as much information as we can without having to delete some of the keys.

API Resources:

https://steamcommunity.com/dev

https://partner.steamgames.com/doc/webapi_overview

https://developer.valvesoftware.com/wiki/Steam_Web_API

https://steamspy.com/api.php 
