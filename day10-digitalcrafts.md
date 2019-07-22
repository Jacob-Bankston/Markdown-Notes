#Day 10 - Digital Crafts - Notes

##CSS Box Model, Positioning and Google Chrome Developer Tools

*Life Tip From Azam: The best way to keep up your html/css skills is by replicating websites that you like to visit. The more webpages and techniques you can copy, the more that you can implement in your own projects.*

##CSS

Naming convention for CSS styles you have all lowercase and hyphens in between the words. Make sure your classes and ids are labeled with something related to the project that you’re working on. Don’t name things first-div or all-paragraphs. These naming conventions and labeling processes makes your code more readable and usable by other developers.

Different stylings in css - tag based, class based, id based
```css
		body {
		.classy {
		#identifiable {
```

####Margin versus Padding
The space around the object is the margin
	* This pushes the element away from others

The space inside of the margins is the padding
	* This pushes the content away from the margins

The order! Top Right Bottom Left (Clockwise starting at 12)

`margin: Top Right Bottom Left;`
OR
`margin: 0 auto 0 auto;`

`margin: 50px;` Same margin on all sides, just declare one size

Display Modes
`display: block;` Place an element, then break to the new line

`display: inline-block;` Place an element and place the next one next to it. Does care about the width and the height

`display: inline;` It will wrap container around the content. Doesn’t care about the width and the height, they’re ignored

####Positioning

`position: relative; ` Allows you to declare things relative to parents

`position: absolute;` Put the div where ever you want, even outside of parents! It is moving relative to the body! Including the invisible barriers!

If the parent is denoted with position: relative, then the child will stay relative to the parent instead of the main page.

`position: fixed;` The position is relative to the browser window, not the location on the page. Good for a shopping cart application

`position: sticky;` It will scroll, but once it gets to a certain position it will stay there.

￼

__LIFE TIP FROM AZAM__: Make sure that you are looking up tools to use for your services, that you read into what browsers actually support those features! If you have to reach users using IE10 then you will be limited on some of the newer features.

##Developer Tools

When you are inspecting elements, play around with the different tabs to see the functionality of what’s happening on the page! It will go into complete depth on the webpage even if you’re using shorthand on your code.

When you select something in developer tools and you add something, it will propagate a list of all of the potential things you can add to the css. Similar to vscode and other text editors.

Styles - Shows you more about the styling of that area
Computing - Shows you the margins, padding, etc…
Event Listeners - Shows the things scripts are looking for

You can change your code in the developer tools to see how it will interact with the website! It is not persisted in your code, but it allows you to play and tinker to find solutions to issues.

__AZAM LIFE TIP__: If you’re doing any kind of web development I highly recommend becoming familiar and using Google Chrome Developer Tools!