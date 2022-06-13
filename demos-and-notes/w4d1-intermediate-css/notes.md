# Intermediate CSS

learning about the most fundamental CSS properties:
- display
- box-sizing
- position
- z-index
- float
- overflow
- pseudo classes




## display

- display:block - takes up the full width of the page, with a line break before and after. can have height and width
    - most html elements are block-level by default: div, h1, p,

- display:inline - neatly wraps its children. it has no dimensions of its own. can sit horizontally next to other inline elements
    - some html elements are inline by default: a, em, strong,
- display:none - an element with display none is not visible, doesn't take up space, cannot be interacted with

- display:inline-block -  best of both worlds, combining inline and block. an inline-block element can have dimensions (height/width), but it can also be placed inline with other inline-block elements
    - few elements are inline-block by default: img


## box-sizing

- box-sizing: 
    - content-box. by default, border and padding are not included in an element's specified width, they are added to the width
    - border-box. border and padding are included in an element's specified width


## position

by default, all elements have position:static 
    - elements with position:static are considered NOT POSITIONED
    - elements with ANY OTHER VALUE for position are considered POSITIONED

the next simplest value for position is position:relative
mostly the same as position:statice, except,
    - is technically POSITIONED
    - an element with position:relative can be nudged in any direction using properties top, left, bottom, and right
        - for example, setting top:20px pushes the element DOWN 20px
    - moving a position:relative element doesn't change how it takes up space, it only changes where is visually appears

position:fixed
    - it is POSITIONED
    - set top/left/bottom/right to position the element relative to the window
    - no longer takes up space

position:absolute
    - an element with position:absolute is positioned relative to its closest POSITIONED parent


z-index:
    controls the stacking order of positioned elements, when multiple elements are stacked on top of each other
    recommendation: set z-index to a high number, at least 100 (not 999999), and use increments of 10 for your z-index, so other elements can be inserted in between your layers
    z-index is not global to the whole page, it is relative to a stacking-context


float:
    use float to wrap text around images
    for other layout problems, consider using position:absolute or position:fixed instead.

overflow:
    if an element has a specific height, and has too much content to fit that height, overflow affects what happens to the extra content
    overflow:visible means that overflowing content can be visible, as if it wasn't overflowing. 
    overflow:hidden means that overflowing content cannot be seen
    overflow:scroll creates a scrollbar to access overflowing content
    overflow:auto will create a scrollbar only if there is too much content


use a `:` to target elements with a pseudoclass, like a class
    common pseudoclasses:
        anchors:
            - a:link
            - a:visited
            - a:active
            - a:hover
        inputs:
            - checked,
            - valid, invalid - useful for form validation
            - focus - click on an input so it gets that blue border. the opposite of focus is 'blur'
        relative children:
            - li:first-child - applies to the first list item in any list
            - li:nth-child(5) - applies to the fifth child in any list