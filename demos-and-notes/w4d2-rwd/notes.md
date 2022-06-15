# Responsive Web Design

a responsive website 'responds' to various aspects of a user's device to show a more appropriate version of that website
there are many aspects of a device to respond to, such as operating system, input capabilities, javascript availability, etc. for the most part, we're responding to screen size


## two approaches:
    - progressive enhancement: design a website for the smallest screens, and then add non-essential features for larger screens
    - graceful degradation: design for the largest device, and then gracefully remove features for devices that dont support them. example, <noscript>


## responsive meta tag
by default, mobile browsers will scale down content to fit in the screen.
if the content is already designed for phones, we need to prevent the device from scaling our content

breakpoint: specific pixel width at which the layout changes

## responsive units
instead of using fixed units like px, use responsive units
% - usually, 1% means 1% of the parent. this makes it hard to change elements in isolation, since changing an element changes its children. 
in some cases, like transform, % refers to a percentage of the element itself. 

vh, vw
    - viewheight, viewwidth: 1vh is equal 1% of the screen's height
vmin: 1% of the height OR width, whichever is smaller
vmax: 1% of the height OR width, whichever is larger

two responsive units commonly used for fonts:
ems - lets you size an element relative to its parent's font size


rems - root em. lets you size an element relative to the <html> element's font-size.

## flexbox
flexbox is a new display type, other than, block, inline, or inline-block
flexbox is used for solving one-dimensional layout problems.

in contrast, grid is used for solving two-dimensional layout problems


## media queries
a media query is like an if-statement for CSS. you can specify a condition, and if it's true, some other set of styles gets applied to your page

## bootstrap
a very popular CSS framework, written by twitter. essentially just a stylesheet with some class selectors and predefined CSS rules
- provides normalization. applies sensible defaults to every element, so your website looks consistent across browsers
- helps you build a responsive design, using media queries and relative units
- helps you build your layout, using the grid system