# React: Vowel Finder

For this challenge, you'll have to create a React application from the ground up. The objective is to create an application that can accept a user inputted word, and display the word back to the user with the vowels highlighted. The goal of this challenge to test your initial React knowledge... good luck!

## Release 0: Create React App

To create a React application, we must run this command in our terminal:

```sh
$> npx create-react-app vowels
$> cd vowels
```

We should begin adding our changes to the `src/App.js` component, and rendering other components (as needed) from within our `App` component's render logic. `App` is the top-level component for our React application. 

And to finally start our app:

```sh
$> npm start
```

## Release 1: Creating Components

Your application should contain:
- An input that allows the user to enter in a word
- A button that allows the user to submit their entered word
- An element that displays the entered word
- Functionality to display the submitted word

Be sure to separate your logic into different components here (i.e. don't put all of your logic in `App.js`)

## Release 2: Finding Vowels
Can you add the following to your application:
- Updated functionality to highlight all vowels in a displayed word, and show the vowel count for each word

HINT: use CSS!
NOTE: `class` is a reserved keyword in JavaScript, so you'll have to use `className` for setting a CSS class property.

## Release 3: Word History

Can you add the following to your application:
- Updated functionality to keep track of all words entered in by the user (and displayed back to the user), with highlighting & counting the vowels as before for each word