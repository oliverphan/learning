# New React Items I don't know:
## ES2015/ES6 (Cool new Syntax!)
 + const: Block scope Variable declaration that makes variable not reassigned/mutable
  + let: Declaring MUTABLE variables, that cannot be reassigned. Also, `let` variables are within block scope, the nearest enclosing block
  + `var`: Can be reassigned, and can be referenced to the nearest function block
  + With no modifier, variable is completely global

 + Arrow syntax: Basically uses => to replace return statement
  + const functionName = (param1 [= default1], param2 [= default2],...) => {statement};
  + Left side is your parameters, right side is the JavaScript return statement

 + Template string literals: insert into a `string` with ${varName}

 + Export Keyword: So the module (which is just a block of JS code in a file) can be used in other components
  + Import: So we can use other components
 + Default Keyword: You can refer to the module literally instead of using brackets
 
## JSX
 + Elegant way to embed XML/markup in Javascript code
 + Putting JS variables back in JSX need braces {varName}
 
## Web Development:
+ Keep presentation, functionality/content, and styling all SEPARATE

## Components
+ Similar to JS Functions: Accept Prop inputs and return React elements to display on screen
+ Everything is a component! And all components need is a render(), sometimes a constructor()
+ Declaration: export default class __ extends Component {} (Then all the other components can call on this class!) {class Comp extends React.Component {render() {this.props.name}}}
 + *OR*: Declared as a function (instead of class) to receive *props* if it doesn't need to manage state! {function Component(`props`){return `props.name`}}

 
## Props
+ Props are just parameters to creating components, used to customized re-usable components
+ {this.props.___ }
 
## State
+ State allows React components to change their output over time in response to user actions, network responses, and anything else. Doesn't let React components change its own props!
+ this.state = {isSomething : true};, this.setState(previousState => ( return {JS LOGIC};))
 + When setState is called in a component, that component will re-render

### Adding a Local State to a Class
+ Make sure whatever you're changing is a this.state.whatEver
+ Add a class constructor to initialize `this.state` with a curly bracket literal
 + constructor(props) {
   super(props);
   this.state = {something : new Something()};
  }