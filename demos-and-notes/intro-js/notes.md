# Javascript

- the only language available on the front-end
- as of recently, javascript can also be used for servers, in node.js


In english, a sentence is composed of multiple words. each word has a part-of-speech, such as noun, verb, or adjective, which determines how you can combine words with other words.

In javascript, a STATEMENT is composed (mostly) of VALUES. each VALUE has a TYPE, such as primitive types (number, string, boolean, null, undefined) , or complex types (object, array, function) complex

# Primitive types

## Numbers
- a number LITERAL is the simplest, most straightforward way to write a number
8 // number literal
var theNumber = 10
theNumber // non-literal number

### arithmetic operators
+, -, *, /, % - binary operators. operate on two operands
every type in Javascript has different operators that can operate on its values

3.14 // floating point number
55 // integer
PEMDAS applies to mathematical operations. if it's unclear, add parentheses

## Strings
'literal string'
"this is also a string"
`this string
can span
multiple lines`

-escaping can mean one of two different things
    - turn a character with a special meaning into just a regular character: 'Don\'t do that!'
    - turn a regular character into one with a special meaning: \n, \t

## string operator
"hello " + "world" - string concatenation
the '+' sign is OVERLOADED, it behaves differently when its operands are different types. 


## variable declaration
- three ways to declare a variable
    - var - originally the only option. 
    - const - create a variable that cannot be reassigned
    - let - create a variable that can be reassigned


## Booleans
- true or false

- logical operators
&& || - binary operators
! - unary operator

## null
has no value. it is never created automatically, it only exists because a programmer decided something should have a null value.

## undefined
has no value. javascript will sometimes create an undefined value when it needs to give you something, but doesn't know what. 


## Arrays
- an ordered list of values

## Object
- an unordered list of key-value pairs. keys in javascript objects are strings

## Function
- a reusable set of logic
- normally returns a value

a function that is attached to an object is called a method.