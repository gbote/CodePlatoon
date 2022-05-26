## Making a circle

You may have previously seen the property `border-radius`, If not [check it out](http://cssreference.io/property/border-radius/). We'll use this to make a circle.

### Release 0 - Make a Square.
First, make a square.

```HTML
<style>
/* CSS EMBEDDED INTO HTML PAGE */
  .box {
    height: 100px;
    width: 100px;
    border: 2px solid aqua;
    line-height: 100px;
    text-align: center;
  }
</style>

<!-- HTML -->
<div class="box">Box</div>
```

### Release 1 - Make a Circle!
Then, all you need to do is set the `border-radius` of the square to `50%`.

### Release 2 - Mold the Circle!
* Can you make an oval?
* Inspect your circle and look at the box model within the inspector. Is it rendered as a circle?
* Change the `background-color` to something more desirable to your eyes.
* Change the color of the font to something else.
* Change the font family to something else.
* Play with the HTML and the styles! If you nest another element in the circle, what happens?

### Release 3 - Stack the Circles
Want a challenge? Make a few more `.box` divs, and play with their `display` and `position` properties.
