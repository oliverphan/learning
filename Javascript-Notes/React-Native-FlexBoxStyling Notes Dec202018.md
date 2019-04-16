## const Style = StyleSheet.create( { } ) ;

## Using curly braces around a variable will embed it into JSX - JSX lets you put any JavaScript expression inside

## Common Properties
+ width
+ height
+ backgroundColor
+ padding{direction}
+ margin{direciton}
+ border{[direction]}{style,color,width}

## Flex Dimensions: Setting sizes based on available space
+ flex: 1 {Fill all available space and share equally with other components under same parent}
 + The flex value is how much the component will take up as a ratio with the other components

## Flexbox - Making layout consistent across different screen sizes
+ Properties
 + flexDirection: Determines primary axis of layout to be stacked: by row or column (Column is default, unlike a Word Processor)
 + justifyContent: Determines distribution of children on primary axis
  + Options: flex-start, center, flex-end, space-around, space-between and space-evenly
 + alignItems: Determines alignment {justification} along the *secondary axis*
  + Options: flex-start, center, flex-end, and stretch

 + And More Properties

## React Elements Defined by the User - Rendering
+ const foo = <Person name="Oliver" />;
+ User-defined components (or variables referring to them) will be passed `props` as a single JSX Attribute object when *rendered*

## Real life CSS defaults to Row as the flexDirection, and uses Main/Cross axis instead of primary/secondary
 + For children: alignSelf will override alignItems

## React Elements reflecting DOM Tags
---
## React Native JSX Wrapper: HTML
+ <View>: <div>
+ <Text>: <p>
+ <Image>: <img>

## Styles: CSS
+ const styles = {
	property: value;
}
 + Assign new style properties dynamically on the fly!

+ React-Native uses CSS in JS, i.e. using JS for our styling of JSX
 + In Reactjs you can use CSS in or out of JS (out of JS means oyu have separate file folders)
 + Also in Reactjs there is a virtual DOM (`react-DOM`) - not in react-native!
 
+ StyleSheet (exclusive to react-native) is a helper passed to a style prop to style components
 + Best Pratice: Make a component accept a style prop which is used to style subcomponents, so that styles "cascade" down