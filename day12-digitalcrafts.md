#Day 12 - Digital Crafts - Notes

##Review of Basic CSS/HTML

`<nav><header><footer>` tags are more modern HTML tags

*Fitz-wisdom*: Right click an image in vscode to copy the src of it.

DON’T FORGET THE VIEWPORT TAG! Necessary for Responsive Design.

__Greenfield__ - Brand New Project

Mostly in the start up realm.

__Brownfield__ - Maintenance of Old Projects

Mostly in the enterprise realm.

*Azam - 10 years, 4 Greenfield projects*

You will spend an equal amount of time in Chrome Developer Tools as you will be actually coding.

`align-content` - is more for wrapped content

##Bootstrap

Bootstrap is an open source toolkit for developing HTML, CSS, and JS. Quickly build out an app that functions as a framework to build off of.

Keep in mind, a lot of stuff built off of bootstrap looks the same.

get bootstrap.com => Getting Started => Starter Template

Notice: It pulls from bootstrap cdn, and if bootstrap is down, your site is down…

GCDT - Network Tab - Displays everything downloaded

the min (minification) file will take away all the space to save storage for CSS.

If you don’t like the styles of bootstrap, you have to override the bootstrap inline. It depends on who loads first if you’re adding your own file and leaving it up to global declarations. You just make sure that your file is loaded after the bootstrap file - aka - link your file below the bootstrap file.

There are a lot of bootstrap theme builders, you can google them, use bootstrap for a minimal amount of your code, whatever you want!

__GCDT__ - You can select to see the media queries in the responsive section

Go through the components in bootstrap to find different things to pull from.
__Card__
__Badge__
__Button__

__Integrity Tag__ - Doesn’t allow you to change the CSS. It’s a new tag. If it is pointing to this algorithm, then it will not load the file. Mostly about the security of the application then anything else.

Bootstrap is mostly experimental, just play around with it.

##Themes!

[themeforest](themeforest.net) - website themes.

__Recommendation__: Spend your time creating things for your portfolio rather than creating your own.

GitHub should be up to date!! It is your resume + your portfolio!!

##Sass

sass-lang.com

Sass is like CSS with more features. It’s not CSS, but you have to write in the language, then convert it into CSS so the browser can understand it.

Nesting in Sass is a lot more readable. It helps with some missing features that are not included in CSS now, but will probably be implemented in the future.

Has a .scss file type

You will not type anything into the CSS file, you’ll just type things into the sass file, and it will convert and transport it into the css file.

Terminal Command to write over your code to your CSS

`sass my-site.scss sit.css`

__Partials__ - you can create a partial sass file, and implement that into the CSS. This is when you only need sass for a certain part of your site, and then to apply that to your overall site.

__Inheritance__ - Same as in python, you can inherit from the parent class. You can create shared styles, and then give them to other classes and ids