# Capstone Project - Raspberry Pi Notes

## Stories and Points

Description: Creating the Hardware side of the solution to connect the application with TVs via bluetooth connection utilizing a microphone and button to control the hardware to ask questions to the Dialogflow project.

- Research Node.js running on a Raspberry Pi
- Have a Node.js server running on the Pi from a project
- Connect with a Microphone
- Connect with a Speaker
- Connect with the files on our github
- Connect the project with Google Cloud Speech to Text API
- Connect the github project into the raspberry pi
- Test the functionality of the Microphone
- Test the functionality of the Speech to Text
- Test the functionality of the Google Assistant
- Test the functionality of the Dialogflow Project
- Research Connecting Screens via Bluetooth extensions
- Find a voice trigger to connect to screens via bluetooth
- Find a potential switch trigger to connect to bluetooth?
- Test connecting to an external screen with the Raspberry Pi
- Test voice trigger to connect to screens
- Research power off functionality with a switch or voice command
- Attach an additional switch command to turn off the pi
- Attach an additional switch or switch command to turn on the pi
- Test Powering off with a voice command
- Test Powering on/off with a switch

## Research Node.js running on a Raspberry Pi

- [Setting up a Node.js server on a pi](https://blog.cloudboost.io/how-to-run-a-nodejs-web-server-on-a-raspberry-pi-for-development-3ef9ac0fc02c)
  - [Download Raspbian](https://thepi.io/how-to-install-raspbian-on-the-raspberry-pi/)
  - Make sure the most recent node is installed
    - _Note: You have to be online for this to work_
    - `sudo su;`
    - `wget -O - https://raw.githubusercontent.com/audstanley/NodeJs-Raspberry-Pi/master/Install-Node.sh | bash;`
    - `exit;`
    - `node -v;`
  - [Set up Postgres on the Raspberry Pi Guide](https://opensource.com/article/17/10/set-postgres-database-your-raspberry-pi)
    - Once installed run these commands to set up the database
      - `psql`
      - `create database quickreact;`
  - Set up React and Extras for the Raspberry Pi
    - `npm install -s express react react-dom pg webpack babel-core babel-loader babel-preset-es2015 babel-preset-react`
    - `npm install nodemon -g`
    - Optional
      - Morgan is a middleware logging package
      - Chalk makes pretty colors on console logs!
      - `npm install -s morgan chalk`
