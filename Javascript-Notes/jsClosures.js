function say667() {
	var num = 42;
	var say = () => console.log(num);
	num++;
	return say;
}

sayNumber = say667(); // log nothing, because say wasn't executed
sayNumber(); // Logs: 43, because num was changed before say was invoked

------------------------------------------------------------------------

var gLogNumber, gIncreaseNumber, gSetNumber;

function setupSomeGlobals() {
	var num = 42;

	gLogNumber = () => console.log(num);
	gIncreaseNumber = () => num++;
	gSetNumber = x => num = x;

}

setupSomeGlobals();
gIncreaseNumber(); // num is 43
gLogNumber(); //logs 43
gSetNumber(5); // num is 5
gLogNumber(); // logs 5

var oldLog = gLogNumber;

setupSomeGlobals();
gLogNumber(); // logs 42

oldLog();
// logs 5, because oldLog contains a reference to the original closure,  and when setupSomeGlobals() was called a second time the global variables were set to a new closure/stack-frame

------------------------------------------------------------------------

function sayAlice() {
    var say = function() { console.log(alice); }
    // Local variable that ends up within closure
    var alice = 'Hello Alice';
    return say;
}
sayAlice()();// logs "Hello Alice", even though function declared before variable!

------------------------------------------------------------------------

// Variable hoisting

function buildList(list) {

	var result = [];
	for (var i = 0; i < list.length; i++) {
		var item = 'item' + i;
		result.push( () => console.log(item + ' ' + list[i] );
	}
	return result;
}

function testList() {
	var fnlist = buildList([1,2,3]); // Should be a list of length 3

	for (var j = 0; j < fnlist.length, j++) {
		fnlist[j]();
	}
}

testList(); // logs "item2 undefined" 3 times
// This is because the buildList function only has one closure
// So when fnlist[j]() functions are invoked, the value of i is 3 and list[i] is undefined

------------------------------------------------------------------------

// Each call to the main function creates a separate closure/stack frame
function newClosure(someNum, someRef) {
	// All these variables are in the closure
	var num = someNum;
	var anArray = [1, 2, 3];
	var ref = someRef;

	return (x) => {
		num += x;
		anArray.push(num);
		console.log(`num: ${num}; anArray ${anArray.toString()}; ref.someVar: ${ref.someVar};`);
	}
}

obj = {someVar: 4};
fn1 = newClosure(4, obj); // Gets a function pointer
fn2 = newClosure(5, obj);

fn1(1); // num: 5; anArray: 1,2,3,5; ref.someVar: 4
// Note how the value in the array is also 5, not 4, even though it was pushed when the value is 4

fn2(1); // num: 6; anArray: 1,2,3,6; ref.someVar: 4

obj.someVar++; // now object is someVar: 5

fn1(2) // num is now 5 + 2, because we add to the same closure, but ref.someVar is 5
fn2(2) // num in this closure is 6 + 2

// OVERALL: NEW CLOSURE SETS ARE ONLY CREATED WHEN THE MAIN FUNCTION IS CHANGED!!