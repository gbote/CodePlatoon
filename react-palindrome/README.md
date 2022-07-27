Palindrome
===================
In this exercise, I created a component that allows users to input a word and acknowledge to them whether or not the word is a palindrome (spelled the same forward and backwards).

Release 0 - Created the text box
-------------
* Created a UI that has a [text input](http://www.w3schools.com/tags/tag_input.asp) with an onChange event listener attached to it.

Release 1 - Captured what the user typed
---------------
Once a user types something into your text box, it captures what they typed. I saw that referencing the `.value` of the text input field can either be done through the *event* object automatically passed into your event handler function, or via [refs](https://facebook.github.io/react/docs/refs-and-the-dom.html).

 
Release 2 - Wrote my palindrome function
-------------
Based on what a user typed, I set the state on my component to say whether or not the user's input is a palindrome and display that out to the screen. It was useful for me to utilize [ES6 template literals](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Template_literals) to render the acknowledgement like so: `[word] [is/is not] a palindrome`
