# React: Doors Game

We've coded up a simple 'Choose a door' game using React. To play the game, a player must select a random door, and they win the game if they correctly choose the door that has a prize behind it (otherwise they lose).


## Initial Challenge
Your first challenge is to install this React project (running `npm install`) and to fully understand the code that has been provided. You do not need to change anything right now within the project... just take time to go through the code, and understand how things are connected and working in this React app. Do you understand how all of the functionality in implemented here?

## Main Challenge
 The code is written using functional components. Your task is to convert the following components into a class-based component design:
- src/App.js
- src/components/Game.js
- src/components/Door.js

Once you convert these components, verify that all of the previous functionality of the game remains in tact! Nothing should have changed from the user's perspective.

## Stretch Challenge
There is one piece of functionality that we've not implemented that would be nice to have. Notice that you are able to still open the other doors, even after you make your first door guess. The result of the game remains the same (based on the first door that you opened), but it would be better if we prevented any of the other doors from being opened after the first guess is made. Can you figure out how to implement this desired functionality?