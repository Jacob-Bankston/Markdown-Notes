#Day 11 - Digital Crafts - Notes

##CSS Flexbox

Mobile Browsers are a little bit behind the desktop browsers. 

Learn the 20% of the thing that will allow you to do 80% of the tasks.

Use Flexbox to put things in a row, use it to put things in a column!

Flexbox => Flexitems
Flexitems can be flex boxes as well!

Flex direction -> row, column

`<link rel=“stylesheet” href=“site.css”></link>`
Memorize this. Just do it!

When you are declaring things in CSS you can add items after to show the order of containing the stylings

The following has check for divs INSIDE of the CONTAINER ID

```css
#container div {
width: 100px
background-color: red;
}
```

`display: flex;`  - This is how you declare a flex box
`flex-direction: column;`
`flex-direction: row;` By default everything is row wise
__RESEARCH__: Look back into `<span>` versus other tags. Useful reasons, etc…

Tackle small problems bit by bit, don’t try to do everything at once! You may know this, but the temptation to do everything is very very real. Don’t stress. It’s okay. Go incrementally! How do you eat an elephant?

__Pro-Tip__: Sketch out what you want the website to look like before you start putting the code in the page. Create the rough draft and plan out the strategy for how to tackle it.

__Pro-Tip__: Think about IDs and Classes as something that when someone else reads your code, you want them to understand what you’re going for! IDs can only be used once, so if you’re not reusing the styling, go with an ID!

Check for your CSS properties in the Google Chrome Developer Tools to see how you like the flex styles.

Workflow for the website should be structured for the big stuff down to the little stuff. Example would be to go with:
Menu => Title => Side Categories => Main Content

Work on getting things displayed before worrying about the positioning.

`justify-content: OPTIONS;` You can adjust to center things in a few ways

Play with justify on the developer tools

`flex-wrap: OPTIONS;` You can wrap the content once it hits window borders

Download the browsers that you’re going to be targeting to, and actually test them on those browsers.

Whatever appears last in the code will overwrite the settings further up in the code, so make sure that you aren’t double declaring things!

Create several files for CSS, Desktop/Mobile/Tablet/Common/etc…

##Mobile

You don’t want the set up for the browser website to look the same on a mobile  website. Go through the planning just like you would for the main browser. Some things you don’t even want displayed on the mobile version because it might be too cluttered.

__Responsive Design__ - Making the website’s code in one setting to respond to the user’s device to adjust the size and format of the site.

__Mobile-Friendly Test__ - put in your url, and it will test out whether your page is good for mobile, and gives you errors on what doesn’t conform to standards. You can also see screenshots of what it looks like on mobile.

__Hamburger Menu__ - Menu that condenses the categories into a dropdown.

It is a good idea to start with a mobile design! It is easier to expand things than to condense things.

Setting the viewport! Adjusts based off of the screen. Required with mobile development. (Your browser won’t know that you are running on a smaller device.)

__Responsive view in Developer Tools__ - You can adjust the size of the screen in the browser, and change to landscape or portrait.

__Media Queries__ - use these to check the size of the display and adjust the settings accordingly. You can have overarching media queries for your big containers in CSS, but you can still use the overall styles in the sheet.

Developer tools will show you in responsive design the break point.

If it’s not showing you can select it in the three dots.

Google Media Queries Sizes - it changes every couple of years…

2 or 3 breakpoints are fairly common. You need as many breakpoints as sizes of things you are developing for.

Use responsive design for everything you make. You only get good at it by continuously working on it.

*Shift-Command-4 Take a Screenshot*

##What the Flexbox

`display: flex;` stretches to the whole width

`display: inline-flex;` goes around the content

__order__ - order’s default is set at 0 advancing the number moves it to the end negative numbers work as well. CAVEAT - You can’t really copy text over because it will be the order they come in.

__wrap__ - You have to have wraps to really be able to adjust containers around

__justify-content__ - Essentially this is to adjust what happens on the main axis.

__align-content__ - Essentially this is to adjust what happens on the cross axis. Only works when we have multiple lines of code.

__align-items__ - can make adjustments on the items

__align-self__ - it will shift the specific container itself. It’s exactly like align-items but you can use it specifically for a single flex container.

__flex__ - The default grow-shrink is to make everything the same size.

__flex-grow__ - When we have extra space, how should we divide it amongst every container on the same line? The default flex-grow is 0. Don’t do anything.

__flex-shrink__ - How do we slim ourselves down when there isn’t enough space for all of the containers.

How much should I give up of myself before other containers.

The default flex-shrink is 1. This is why everything balances without setting this value!!!

__flex-basis__ - sets the base value of what you want from your box along the main axis. 

Examples of flex property with all three abilities: `flex: 1 1 400px;` `flex: 10 5 400px;`

__flex-grow/shrink/basis__ only work on the row they are on, even when wrapping!

`min-height: 100vh;` is magic! `height: 100vh;` is also magic!

Using flex as an intuitive thing with a longer bar is very useful!

In order to force things to wrap, you have to give them some sort of width with the flex-basis property. `Flex: 1 1 50%`

```css
.flex-nav ul {
flex-wrap:wrap;
}
.flex-nav li {
flex:1 1 50%;
}
.flex-nav .social {
flex:1 1 25%;
}
```

Always recommends having a wrapper around all of the containers just in  case you need to alter things when you are changing to a more responsive design later in the developing phase.

The jQuery functions that have toggle do not allow the flex boxes to work properly, so you have to work around that and code it yourself to make it look how you want it to look!