// ES5 Style
// function myFunc(name) {
// 	return 'Hello ' + name + '!';
// }

// ES6
// const myFunc= name => {
// 	return `Hello ${name}`; also template literals used here
// }

// Name is the parameter, after the arrow is the statements
const myFunc = (name) => `Hello ${name}!`;

console.log(myFunc('Oliver'));

// const a = ['tony', 'sara'];
// console.log(a);

----------------------------------------------------------

`this` keyword works differently in arrow functions than regular anonymous
functions.

In arrow functions, `this` refers to the "owner" of the function (like "window")
that created the function (where it was declared).

In regular anonymous functions, `this` refers to whatever called the function.