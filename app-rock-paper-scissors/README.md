# Rock Paper Scissors

For this project, you'll be asked to create a full-stack "Rock-Paper-Scissors" application using Django + React. This will implement the classic
[Rock, Paper, Scissors](https://en.wikipedia.org/wiki/Rock%E2%80%93paper%E2%80%93scissors) game against an AI opponent.


## Release 1: Django Back-End

Your data model design should allow for the following features:
- A User should be able to play many games
- A Game should last to a certain configurable number of "Throws" won (e.g. first to 3 victories)
- A Throw can be "rock", "paper" or "scissors"

## Release 2: React Front-End

Your front-end site should encorporate the following pages:
- Home Page:
  - Ability to configure and start a new game
- Game Page:
  - Ability to play an AI player in the configured game. The AI should randomly choose their throw value. 
  - Ability for the user to throw out "rock", "paper", or "scissors"
  - Current game score (throws won total, target game throws, etc...) 

## Release 3: User Authentication

Once you have the main features implemented for this project, try to proceed with adding in user authentication functionality. This would include sign-up and login/logout pages on your front-end, and authentication logic in your back-end.

## Release 4: Game History and Scoreboard

Add a couple more pages and features:
- Game History Page:
  - Ability to see the logged-in user's game history on the site
- Leaderboard Page:
  - Ability to see the scores/stats of ALL site users' games (i.e. usernames, total games W/L, total throws W/L)