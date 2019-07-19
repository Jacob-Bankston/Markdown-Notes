Notes from Day 9 of Digital Crafts Bootcamp

HTML5 - This language is used for structuring out your pages.

	You usually learn tags and features on a as needed basis.

	Hyper Text Markup Language

	For Development use Google Chrome
		There are a lot of features in Google Chrome Browser that are great
		for developers that are only on Chrome.

	When you name a file index.html it is the industry standard as the main
		page. It will be the home page of the site. It is not required, but
		everyone will look for that page to find your homepage.

	When you start a tag, you better close the tag also.

	<html><head></head><body></body></html>

	HTML is not as picky as other languages, it will probably still run with
		bugs, so be aware of that when debugging. It doesn’t complain or
		bug out.

	Convention is to use lowercase lettering when you are writing tags.

	Open up html files in any browser.

	You can wrap tags inside of each other like <b><I></I></b>

	<html> tells the browser that the file is an html site, not an image or mp3.

	<head> tag helps search functions know what your website is about. It
		can be used to tie your CSS, JavaScript, Mobile site etc… The
		information below the website links on google are usually from the
		header tag in the html from the website.

	<body> where everything should go, the actual content of the page.

	<meta> Describes what your website Is about in your head tag.

	<div> A division tag. A container. Other tags can be held inside a div tag.
		You don’t have to put everything inside of a div, but it’s
		recommended so you can break things into sections.

	<ul> and <ol> An unordered list tag and an ordered list tag.You’re
		building a list.

	<li> A list item in the <ul> or <ol> tags

	<p> paragraph tag

	<br> line break tag - not recommended. There are better ways to add
		spacing.

	<b> bold - probably do this in CSS instead

	<I> italics - probably do this in CSS instead
	
	<h1><h2><h3><h4><h5><h6> different heading sizes to make different
		sized heading texts.

	<img src=“image_file.png”></img>
		You can reference image urls or you can save them to your folder to
		reference them.

	<a> anchor tag. This is how you can link to other sites
		<a href=“index.html”></a>
		<a href=“https://www.google.com”></a>
		href - hyperlink reference
		<a href=“/“></a> - takes you to the root of the website

	attributes - the additional tags inside of a tag like src=“” or class=“”

	Self Closing Tags - If you don’t think that you are going to place anything
		in between the tags you can you this format to close the tag within
		the declaration of the tag.
	
		<img src=“image_file.png” />

	Organize your structure of files!
		Store the images in an images folder - images
		Store the CSS in the CSS folder - css
		Store the JavaScript in the JavaScript folder - js
		Have all of the HTML files in the root folder

	style attribute - you can pass in a valid css to pass in a style
		<div style=“background-color: orange”>

	inline - code that is written into the HTML file, you don’t want to do this.

CSS - Used for styling your webpages to make them nicer.

	You have to pass in a valid CSS style otherwise it will show up as an
		error.

	Use the semicolon to separate the values
		<div style=“background-color: red; color: white”>

	If google overrides a style, you can define the style of the specific tag.

	Classes in CSS are not the same as Python!

	You will link the styles in the <head> tag like the following code!
		<head>
			<style> 				.menu {
					background-color: orange;
					color: white;
					font-family: Arial, Helvetica, sans-serif;
					font-weight: bold;
				}

				.featured-image {
					width: 100px;
					height: 100px;
				}
				a { /* All anchor tags */
					color: white;
					text-decoration: none; /* No underline. */
					font-size: 17;
				}
			</style>
		</head>

	Then you link it in the code in the HTML
		<div class=“menu”></div>

	For width/height/etc… you can list as pixels “px”, or percentage “%” (The
		percentage is in reference to the parent!) One of the benefits can be
		that it will resize with your window or with your device. There are
		other adjustments to sizes, but there are some ways to optimize
		better when we get to flex box.

	*You can optimize a lot of the sizing and issues with mobile development
		with media queries.

	You want to make a habit of putting the styles in the <head> tag because
		it will load first in the webpage, rather than loading after the fact.

	The best approach to implement styles will be to create a separate file
		for CSS. “styles.css” The reason for this is because the styles will be
		saved to the person’s computer, and you can use the styles for each
		page on the website. The same thing happens with images on
		websites.

	<link> tag is to link to the CSS or JS or whatever
		<link rel=“stylesheet” href=“css/site.css”></link>

	Priority! The overall style for <p> or <div> will be overwritten with a
		specified class. Highest priority is the inline style.

	id attribute - Each of id in the html document needs to be unique. Works
		in the same way as a class, but it is unique to that one location.

		id=“store-heading”

		#store-heading {
			background-color: black;
			font-size: 15;
		}

Chrome Developer Tools

	Whenever you are having issues, ALWAYS CHECK THE INSPECT
		CHROME DEVELOPER TOOSL!! It will show the errors, where the
		errors are, what the error type is. ALWAYS KEEP THIS OPEN.

	In the console it will show you the error. If you hover over the error you
		can see the file where the error is occurring. If you click it, it will
		highlight the line of code that the error is occurring in!

	Inspect as a Mobile Application
		Right Click
		Inspect
		Select Mobile Device with a dropdown on the top left corner
		Several options of phones to choose from!!

	The number one thing that you should master is the google chrome
		developer tools! Go through and really get a deeper understanding
		of what functionality you can use to help you.

	The network tab will show you all the files that have been downloaded
		when you go to the html page.

Requests

	The fewer requests that your website is the faster that it will load. If it
		takes longer than 2 seconds for your page to come up, the person
		will probably give up on waiting for it.

	Obviously it depends on the website, but as a general try for fewer
		requests.
	

HOMEWORK:
	- Twitter Bot Project
	- Update Linked In with more features from the blog post
	- Update the Resume to have the good good qualities that people look for
	- Send the email to Kristin along with a reference to my linked in
	- Edit and improve the Python Dictionaries Blog Post
	- #100DaysOfCode Post for the day [Blog, Twitter, Facebook]
	- Research how to play pitch files from python, look into how to
		implement this into the raspberry pi project to make the game using
		text to speech.
	- JavaScript 30 10th video
	- Watch the C# Video Online:
		https://www.youtube.com/watch?v=GhQdlIFylQ8&t=171s
