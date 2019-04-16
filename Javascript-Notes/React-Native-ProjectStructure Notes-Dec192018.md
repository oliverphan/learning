## Information Flow
+ Components depend only on its parent and internal state
+ `native modules`: From existing IOS/Android apps

## Architecture
+ Most of React Native App runs on the JavaScript VM
 + Important: The UI is rendered using the platform's (Android/IOS) native UI elements
 + Thus there isn't a virtual DOM like there is in Reactjs
 + How native code is connected to JavaScript code: React Native uses RCTBridgeModule
  + React-native uses a bridge between Javascript and native APIs of a specific platform
+ Structure your shared Components in a folder `./components/*`
 + Then style/divide them into Views in each file
+ Component Structuring: App.js is splash screen, your *prototype*
 + Then make a separate Components folder for your other screens
 + import those components to wherever to be able to pass props to them

## Navigation
+ Add `router.js` to root, then `npm install react-navigation --save`
+ Stack Navigator: Once you make your components folder, import them to App.js
 + Define a const RootStack = createStackNavigator ( {varName1 : Component1, ...})

## Basic Setup/Project Structure
+ Add a folder in root called `app` or `main`
+ Move App.js to root of `app`
+ Update the index.js import statement toimport App from ./app/App.js
+ Shared logic components go into the `components` sub-directory
 + This is where your functional components (to be reused throughout)
  + E.g. Button, GenericTextInput, Avatar, Loading
+ Any images or animations go into the `assets` sub-directory
+ Screens (as export default class extends component) should go into the `views` or `screens` sub-directory
 + Screens are basically just container components that handle data fetching & interaction management - UI is handled in components


## Init Command
+ create-react-native-app `appName`
+ react-native init `appName`
 + cd, react-natve run-android
+ expo init `appName`
 + cd, npm start

## Render
+ index.js is where you install new apps/pages
 + import `App` from './App';
 + And import from the `app.json` file
+ index.js in the root directory holds a file that will render App.js
 + There is no `react-DOM`, `AppRegistry` is your entry point to the app
 + Use `AppRegistry.registerComponent` for native system to load Component bundle & run app with `AppRegistry.runApplication`