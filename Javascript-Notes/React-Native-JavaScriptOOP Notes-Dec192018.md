## Note: JavaScript is an event-based language.

 + const: Block scope Variable declaration that makes variable not reassigned/mutable
  + let: Declaring MUTABLE variables, that cannot be reassigned. Also, `let` variables are within block scope, the nearest enclosing block
  + `var`: Can be reassigned, and can be referenced to the nearest function block

## JavaScript Objects
+ Cannot need to be statically delcared, must be initialized
+ e.g. const array = ...
 + Or: const array = () => {return new...}
 + Array keys are indices
## Const, let, or var can be used to declare variables OR functions

+ EVERYTHING is a JavaScript Object
 + Always if they are defined with the `new` keyword
 + All JS Objects inherit from *PROTOTYPE* (a property)
+ Primitive Types
 + string
 + number
 + boolean
 + null
 + undefined
+ Properties go into the curly braces of an Object variable

## JS Promises -> Success & Failure!
+ Used to execute functions after data from an API is fetched
 + Promises can be fulfilled, rejected, pending, or settled (settled is either rejected or fulfilled)
+ var myPromise = new Promise( function (resolve, reject) {
	// do osmething
	if (everything is good) {
	   resolve("It worked!");
	} else {
	reject (Error("It broke"0));
	}
});
 + PARAMETER: Promises are constructed with a callback (two parameters, resolve/reject)

+ Using a Promise object
 + promise.then( function (result) { 
 console.log(result); // Execution when error not thrown
} function (error) {
	console.log(erorr); // Execution when error thrown
})
 ".then" keyword takes the callback for success case & a callback for failure

## Fetch API syntax
+ Returns a Promise object
+ Fetch API uses a GET method
 + fetch(url) // url is for the API you want to access
 .then ( function() {
 	//code for handling stuff from API
 }
 .catch( function() {
 	// code for handling the errors
});

## Simple GET
1. Store URL/end location of info to constants
2. Fetch and THEN convert to JSON
3. THEN do whatever with it
4. The catch the errors

## JavaScript Map function & Arrays: Array.prototype.map()
+ Creates a new array with elements from the result of a function on every element in the previous array
 + E.g. const map1 = array1.map(new element => Function to operate onto elements)
 + A && B Returns `A` if `A` can be coerced into `false`
  + Seeks first falsy value -> If none False return the last one
 + A || B Returns `A` if `A` can be coerced into `true`
  + Seeks first truthy value -> If none True return the last one

+ Empty Strings and null and 0 is False elements

## JavaScript Boolean Operators
+ Logical operators of && and || might (OR MIGHT NOT) return boolean values
 + Used with non-boolean values will return one of the operand expressions
+ Use double negatation on non-boolean values to convert to its boolean value

## Properties
+ The JS Objects have properties you can access in name/value pairs
 + You can assign/add these properties dynamically, without a "template" like in Java
 + E.g. Person.firstName (Object is Person, firstName is name, value is "Oliver")
+ Object Constructors can also be defined
 + function Person(param1, param2, param3...) {
	this.1 = param1;...}
 + var Oliver = new Person("Oliver", "Phan", 21);
 + With Object Constructors, you *can't* dynamically add new properties (unless prototype property used)!

 + Create objects with literals, `new Object();`
 + Garbage Collection: delete Object.property;

## Prototype Inheritance
+ JS Objects inherit methods/properties from a *prototype*
 + A prototype is a property of all functions, and is an object itself
 + Class.prototype can be used to add new properties/methods to the function object
 + *prototype* methods.properties shared between all instances of the function

+ Object.prototype is on top of the prototype inheritance chain
 + Person.prototype inherits from Object.prototype
 + Person objects inherit from Person.prototype

## JavaScript classes
+ Simply a different way to write the function constructor
+ Instead of: function Person(name, age, sex) { }
 + class Person {
 constructor(name, age, sex) {
 ...
}
Methods here -> which are prototype methods!
}
+

## JavaScript Call backs
+ Definition: Functions that are executed after other functions are executed
 + This is allowed since functions are objects in JS, so callbacks are functions that are passed as arguments
+ Because JS is event-based