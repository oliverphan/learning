## TextInput Component
+ *onChangeText* prop: Takes a function (callback) to call when text changed
 + Arrow function to manipulate

+ *onSubmitEditing* prop that takes a function to be called when the text is submitted

+ render() { 
return (
	<View style={styles.container}>
		<TextInput
		style = {{backgroundColor: "green"}}
		placeholder = "Sample render() function!"
		onChangeText={(text) => this.setState({text})}
	/>
)

+ then you do something with the Map function
 + Remember map function operates on ALL variables in the array