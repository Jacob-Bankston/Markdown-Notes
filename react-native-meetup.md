# React Native Weekend Bootcamp Notes

## expo

Creates a template for a React Native Application

## styled components

Splits off the styling into creating customized components

## react native paper

A UI Kit for different things to include in your application

## redux

A wrapper to allow more interactions and calls for specific sections of your application. Allows you do compartmentalize the different portions of your application.

## Expo Tabs

Gives you a template with multiple pages on your application with tabs on the bottom of the application.

## AWS Amplify

There are a lot of features to the web services that are similar to the services from Google like Firebase

> Remember `amplify init` and `amplify whatever the hell you want to add`

Follow the steps through the get started
* [docs](https://aws-amplify.github.io/docs/)
* Install the CLI
* Configure the Amplify
* Once you're finished jump into the React Native [docs](https://aws-amplify.github.io/docs/js/start?ref=amplify-rn-btn&platform=react-native) for AWS Amplify
    * Go through the process to pull the GraphQL api to integrate a schema
    * generate a code for the graphQL api for the schema
    * You can adjust the schema later once you set it up
* Set up your aws amplify relay
  * aws-appsync-relay
  * create an environment from the github
  * This will create a wrapper around the relay service which will handle the realtime updates to and from the database for us.
* set up your amplify configuration in the main application file
* import amplify from aws-amplify
* import aws from aws-exports
* Implement the authenticator tool with aws

Once you finish with setting up go back through the query documentation on react relay - useQuery information
* get the query information for the application from react relay
* get the specific list query and import that as well

## React Relay

The service to communicate from our application to the database.

Follow the steps to get started in the [docs](https://relay.dev/docs/en/introduction-to-relay)

## Web Sockets

The features we worked with today handle a lot of the issues that you would have with web sockets for you.