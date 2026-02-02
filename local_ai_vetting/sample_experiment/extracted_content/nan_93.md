# nan
**URL:** https://www.w3schools.com/jsref/jsref_sort.asp
**Page Title:** JavaScript Array sort() Method
--------------------


## JS Reference

## JavaScript

## Window

## HTML DOM

## HTML Events

## Web APIs

[LINK: API Canvas](api_canvas.asp)
[LINK: API Console](api_console.asp)
[LINK: API Fetch](api_fetch.asp)
[LINK: API Fullscreen](api_fullscreen.asp)
[LINK: API Geolocation](api_geolocation.asp)
[LINK: API History](api_history.asp)
[LINK: API MediaQueryList](api_mediaquerylist.asp)
[LINK: API Storage](api_storage.asp)
[LINK: API Validation](api_validation.asp)
[LINK: API Web](api_web.asp)

## HTML Objects

## Other References

## JavaScript Array sort()

### Examples

More Examples Below !

## Description

The sort() method sorts the elements of an array.
The sort() method sorts the elements as strings in alphabetical and ascending order.
The sort() method overwrites the original array.

## Array Sort Methods:

## Sort Compare Function

Sorting alphabetically works well for strings ("Apple" comes before "Banana").
But, sorting numbers can produce incorrect results.
"25" is bigger than "100", because "2" is bigger 
than "1".
You can fix this by providing a "compare function" (See examples below).

## Syntax

## Parameters

- function(a, b){return a-b}
When sort() compares two values, it sends the values to the compare function,
 and sorts the values according to the returned (negative, zero, positive) value.
Example:
The sort function will sort 40 as a value lower than 100.
When comparing 40 and 100, sort() calls the function(40,100).
The function calculates 40-100, and returns -60 (a negative value).

## Return Value

REMOVE ADS

## More Examples

## Sort Decending

Sort and then reverse the order:

## Numeric Sorts

## Using a Sort Function

Sort numbers in ascending order:
Sort numbers in descending order:
Find the lowest value:
Find the highest value:
Find the highest value:

## Array Tutorials:

Array Tutorial
Array Const
Basic Array Methods
Array Search Methods
Array Sort Methods
Array Iteration Methods

## Browser Support

sort() is an ECMAScript1 (JavaScript 1997) feature.
It is supported in all browsers:
REMOVE ADS

## Contact Sales

If you want to use W3Schools services as an educational institution, team or enterprise, send us an e-mail: sales@w3schools.com

## Report Error

If you want to report an error, or if you want to make a suggestion, send us an e-mail: help@w3schools.com

--------------------