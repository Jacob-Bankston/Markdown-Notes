# Day 16 - Digital Crafts - Notes

##jQuery

api.jquery.com

It is a javascript library that was made in 2006

If you are going into the petroleum industry you will probably still have some work with jQuery, even though it is very out of date.

cdnjs.com has most of the sources of the libraries that you can use for jQuery

If you want to link the jQuery library you can just copy past the code and use it in your code

*Place this above your coded javascript code so you can access it!*

`<script src="jQeury.js"></script>`

jQuery syntax begins with a $ sign.

```js
let div1 = document.getElementById("div1")

let div2 = $("#div1") // search using id jQuery

// this will return a jQuery object of the div
// this allows you to chain operations together

console.log(div1)
console.log(div2)
```

When you create a jQuery object it creates a lot of pre-built in functionality!!

`$("#div1").css('background-color', 'yellow').show().hide().show(100)`

You can chain things at the end. It will always return with a jQuery object!

You can check out the [jquery](www.jquery.com) website to find all of the functions that you can utilize with the object!

`$(document).ready(function(){`

You can attach stuff to it, it's ready, the DOM has been loaded!

The documentation for jQuery is pretty good since it has been around for so long! Spend some time looking through it.

Most of the things are pretty simple, just a more compact way of using javascript.

Lots of options of what you can do with jQuery!!

jqueryui.com is another resource for jquery options

## Validation

`<form></form>`

It automatically adds features to make sure that the form has content and that the form is submitting.

If you wrap everything in the form tags, all of the information is sent to a server.

To have a form submit you have to have `name` properties on the input tags.

If you're looking for a pattern you can identify it with `pattern=""`
* With this you can add a regular expression

Validation should always be on the server side and client side

`.checkValidity()` will check the validity of the form being submitted. This is also available on single items like checkboxes and textboxes.

`.setCustomValidity()` to give a custom message for a validity check.

`.preventDefault()` will prevent some of the default functionality built into the `<form>`

__From now on you ALWAYS have to have form validity on your user input, otherwise you will have garbage in your database.__

Think about what kind of forms would be the best use case for certain UI decisions.

####Regex language

regexlib.com if you search through this you can find out whether something follows the pattern or not.
