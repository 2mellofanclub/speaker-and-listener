# speaker and listener (old)

uses selenium and pychrome

sets up two browsers: the selenium browser does the actual browsing, the pychrome browser uses DevTools to listen to the sent network requests. this example just opens pages and prints out request urls and query strings to the command line. an actual use case could, for example, involve manual operation of the selenium browser window and have the request data tabled in csvs.

shutting down the browsers produces an error, but it should be fine

this was adapted from a tutorial i can no longer find :(