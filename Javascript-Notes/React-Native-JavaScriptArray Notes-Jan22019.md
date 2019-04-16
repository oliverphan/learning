## Javascript Arrays
+ Declaration:
 + Preferred literal: var myArray = [];
 + Verbose: var myArray = new Array();
+ JavaScript Arrays have a key index, usually numeric (0-9...) unless custom properties have been added to the array with array['custom'] = 'someValue' syntax. 

+ You can add JavaScript objects {"objectProperty": "valueOfAttribute"}
 + Either with push({objectHere}) or directly assigning key: array[0] = {objectHere}
 + Be warned: you might open up new space with numeric keys!

+ .splice manipulates new array and returns elements
+ .slice does the same without modifying original array

## More on Map functions - Important!
+ Works like a for loop, going through each object
+ While you shouldn't loop through arrays with an enhanced for loop (use index counter instead with length property), you can for object properties!

+ When mapping through objects in an Array the order of parameters:
+ Example: let newArr = oldArr.map( (val, index, arr) => {
	// return element to new Array
});
+ newArr: the new Array that is returned
+ oldArr: the Array to run the map function on
+ val: The value to be processed
+ index: The index of the value being processed
+ arr: the original array

## Useful operators
typeof

p instanceof q