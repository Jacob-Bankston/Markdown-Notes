Notes from CSS Grid - Wes Bos

Hacks

	.item{$}*10

	BECOMES

	<div class="item">1</div>
 	<div class="item">2</div>
  	<div class="item">3</div>
 	<div class="item">4</div>
 	<div class="item">5</div>
 	<div class="item">6</div>
 	<div class="item">7</div>
 	<div class="item">8</div>
 	<div class="item">9</div>
	 <div class="item">10</div>

	.item.item${$}*30

	BECOMES

	<div class="item item1">1</div>
	<div class="item item2">2</div>
  	<div class="item item3">3</div>
	<div class="item item4">4</div>
    	<div class="item item5">5</div>
    	<div class="item item6">6</div>
    	<div class="item item7">7</div>
    	<div class="item item8">8</div>
    	<div class="item item9">9</div>
    	<div class="item item10">10</div>
    	<div class="item item11">11</div>
    	<div class="item item12">12</div>
    	<div class="item item13">13</div>
    	<div class="item item14">14</div>
    	<div class="item item15">15</div>
    	<div class="item item16">16</div>
    	<div class="item item17">17</div>
    	<div class="item item18">18</div>
    	<div class="item item19">19</div>
    	<div class="item item20">20</div>
    	<div class="item item21">21</div>
    	<div class="item item22">22</div>
    	<div class="item item23">23</div>
    	<div class="item item24">24</div>
    	<div class="item item25">25</div>
    	<div class="item item26">26</div>
    	<div class="item item27">27</div>
    	<div class="item item28">28</div>
    	<div class="item item29">29</div>
    	<div class="item item30">30</div>
	
	This is the kind of low key shorthand that I need in my life.

.container {
    display: grid;
    grid-template-columns: auto 500px 100px;
    grid-gap: 20px;
  }
  /* .container {
    display: grid;
    grid-template-columns: repeat(5, 100px); Repeats over 5 columns
    grid-gap: 20px;
  } */
  /* .container {
    display: grid;
    grid-template-columns: 100px 100px 100px;
    grid-gap: 20px;
  } */
  /* .container {
    display: grid;
    grid-template-columns: 200px 500px; This would be 2 columns and 
    grid-template-rows: 200px 100px 400px; 3 rows!
    grid-gap: 20px;
  } */


Implicit Versus Explicit Grids

	Explicit Grids are defined by you, and the implicit grids are implied
		by what you defined before. grid-template-columns 200px
		500px; would imply 5 rows for 10 items.

Functions

	grid-template-columns: (adjusts sizing and adds columns)
		grid-template-columns: repeat(3, 1fr);

	grid-template-rows: (adjusts sizing and manipulates rows)

	grid-gap: (adds spacing between the grid items)
		grid-gap: 20px;

	grid-column: ([item] allows you to set sizing for grid items)
		grid-column: span 2; (spans across 2 item lengths)

PLACING GRID ITEMS

      grid-column-start: 2; /* starts at track 2 in the column area */
      grid-column-end: 5; /* ends at track 5 in the column area */
      grid-column: span 2 / 5; /* spans 2 where it can and stops at 5 */
      grid-column: 1 / -1; /* like weight 100% */
      grid-row: 1 / -1; /* like height 100% Only bottom of explicit grid */
      grid-column: 1 / -2; /* starts at track 1 and ends 1 before the end */
      grid-row: 3 / 5; /* starts at row 3 and ends before row 5 */

SPANNING AND PLACING CARDIO


    .container {
      display: grid;
      grid-gap: 20px;

      /* Make the grid 10 columns wide, every other taking up twice the free space */

      grid-template-columns: repeat(5, 1fr 2fr);

      /* Make the grid have 10 explicit rows, 50px high each */

      grid-template-rows: repeat(10, 50px);
    }

    /* With Item 1, start at col 3 and go until 5 */

    .item1 {
      grid-column: 3 / 5;
    }

    /* With Item 2, start at col 5 and go until the end */

    .item2 {
      grid-column: 5 / -1;
    }

    /* Make Item 5 double span 2 cols and rows */

    .item5 {
      grid-column: span 2;
      grid-row: span 2;
    }

    /* Make Item 8 two rows high */

    .item8 {
      grid-row: span 2;
    }

    /* Make Item 15 span the entire grid width */

    .item15 {
      grid-column: 1 / -1;
    }

    /* Make item 18 span 4 widths, but end 9 */

    .item18 {
      grid-column: span 4 / 9;
    }

    /* Make item 20 start at row 4 and go for 3 */

    .item20 {
      grid-row: 4 / span 3;
    }

AUTO-FIT AND AUTO-FILL

.container {
      display: grid;
      grid-gap: 20px;
      border: 10px solid var(--yellow);
      /* grid-template-columns: repeat(auto-fill, 150px); */
      grid-template-columns: repeat(auto-fill, 150px);
    }

    .item4 {
      grid-column-end: -1;
    }

Auto-fill will fill up the entire row with options to place items, while auto fit fits the border of the grid at the last item. You can adjust to use all options in the grid with auto-fill, while you can not use that functionality with auto-fit.

USING MINMAX() FOR RESPONSIVE GRIDS

Type gtc and hit tab to have a shortcut to do grid-template-columns!

    .container {
      display: grid;
      grid-gap: 20px;
      border: 10px solid var(--yellow);
      /* grid-template-columns: repeat(auto-fit, minmax(150px, 1fr)); */
      grid-template-columns: fit-content(100px) 150px 150px 150px;
    }

Using auto-fit will stretch content to fill the rows, while auto-fill will hold it to the original value. Auto-fit works better from a responsive design standpoint.

fit-content(100px) will give that grid-item the auto function while maxing out the content size to 100px.

minmax(150px, 1fr) will give the grid-items the minimum size of 150px while giving them a maximum size of 1fr. This is ideal for responsive design.

GRID TEMPLATE AREAS - AREAS

    .container {
      display: grid;
      grid-gap: 20px;
      grid-template-columns: 1fr 500px 1fr;
      grid-template-rows: 150px 150px 100px;
      grid-template-areas: 
        "sidebar-1 content sidebar-2"
        "sidebar-1 content sidebar-2"
        "footer footer footer"
    }
    .footer {
      grid-area: footer;
    }

    .item1 {
      grid-area: sidebar-1;
    }
    .item2 {
      grid-area: content;
    }
    .item3 {
      grid-area: sidebar-2;
    }

    @media (max-width: 700px) {
      .container {
      grid-template-areas:
        "content content content"
        "sidebar-1 sidebar-1 sidebar-2"
        "footer footer footer"
      }
    }

Grid-template-areas lets you define the sections of the grid area as a variable, then you can set specific classes to have that area. This way you can spread the content in different areas without having to specifically define each zone on the screen. You can also use a media query to shift the grid-template and the classes that were defined as such will simply change to fit the new location of the new assignments. Very good for responsive design!

GRID-TEMPLATE-AREAS - AREA-LINE-NAMES

    .container {
      display: grid;
      grid-gap: 20px;
      grid-template-areas:
        "Tim Tim Tim Tim Bob Bob Bob Bob"
        "Tim Tim Tim Tim Bob Bob Bob Bob"
        "Tim Tim Tim Tim Bob Bob Bob Bob"
        "Tim Tim Tim Tim Bob Bob Bob Bob"
    }
    .item3 {
      grid-column: Tim-start / Bob-end;
      /* grid-column: Tim-start / Tim-end; */
      grid-row-end: Bob-end;
    }

You can select where to place items based on where your areas start and end in the item class itself using the area’s name with the -start or -end functions.

NAMING LINES

    .container {
      display: grid;
      grid-gap: 20px;
      grid-template-columns: 
        [sidebar-start site-left] 1fr 
        [content-start] 500px 
        [content-end] 1fr 
        [site-right];
      grid-template-rows:[content-top] repeat(14, auto) [content-bottom];
    }

    .item3 {
      background: slateblue;
      grid-column: content-start;
      grid-row: content-top / content-bottom;
    }

You can name the lines of the grid between where you are explicitly labeling them in the gtc and gtr declarations. You can also give them multiple names separated by a space. These act as variables that you can use for where you would like things to be placed in the grid-area on the screen.

DENSE

    .container {
      display: grid;
      grid-gap: 20px;
      grid-template-columns: repeat(10, 1fr);
      grid-auto-flow: dense;
    }

    .item:nth-child(6n) {
      background: cornflowerblue;
      grid-column: span 6;
    }
    .item:nth-child(8n) {
      background: tomato;
      grid-column: span 2;
    }
    .item:nth-child(9n) {
      grid-row: span 2;
    }
    .item18 {
      background: greenyellow !important;
      grid-column-end: -1 !important;
    }

grid-auto-flow: dense; makes it to where all of the gaps in your grid are filled up with anything that can fit into its space. This is very good when you have a lot of irregular fitting spans in your grid to keep everything where it needs to be in the website.

ALIGNMENT AND CENTERING

    /*
      justify-items: stretch, center, start, end [Horizontal]
      align-items: stretch, center, start, end [Vertical]
      place-items: stretch, center, start, end [Both Axis!]

      justify-content: start, end, space-around, space-between, center [Horizontal]
      align-content: start, end, space-around, space-between, center [Vertical]
      place-content: start, end, space-around, space-between, center [Both Axis!]

      align-self:
      justify-self:

      justify-* is row axis
      align-* is column axis
    */

    .container {
      display: grid;
      grid-gap: 20px;
      grid-template-columns: repeat(10, 1fr);
      grid-template-rows: repeat(5, 100px);
      /* place-items: center center; */
      justify-content: space-between;
      align-content: space-between;
    }

    .itm {
      background: white;
    }

    .itm5 {
      justify-self: center;
      align-self: center;
    }

Keep in mind that for grid the axis never changes, so justify will always be manipulating the horizontal axis while align will always be manipulating the vertical axis. One newer feature to CSS is to allow the place function such as place-content: center; to center both axis instead of having to break it into two separate lines of code. Check to be sure that it is supported in the browsers before jumping in and using this feature.

    /* display: grid;
    justify-content: center;
    align-items: center; */

This is a really simple way to go ahead and make sure that any text in the class is centered vertically and horizontally! It’s a great simple set of boilerplate to use for anything that you want centered like that.

RE-ORDERING GRID ITEMS

    .container {
      display: grid;
      grid-gap: 20px;
      grid-template-columns: repeat(10, 1fr);
    }

    .logo {
      grid-column: span 2;
      order: 2;
    }
    .nav {
      grid-column: span 8;
      order: 1;
    }
    .content {
      grid-column: 1 / -1;
      order: 3;
    }

With the order property you can set which grid-item will appear in what order in your grid. Be careful with this because this will throw off screen-readers or selecting the text in those areas since the html has the order set up different when it combs through the content from the raw html file.

NESTING GRID WITH ALBUM LAYOUTS

Grid-items can also have a grid inside of them, and this is a super common thing to have. When your images don’t want to play with the value of the grid, then set their width to 100%, and they will readjust. There is some funny business going on with the natural width/height wanting to throw off your overall site.

Img {
	width: 100%;
	height: 100%;
	object-fit: cover;
}

This was another solution placed on stack overflow to address reshaping it in an area of a grid to adjust vertically and horizontally.

CSS GRID IMAGE GALLERY

Very cool way to layer a lot of images using CSS Grid and grabbing a lot of randomness from the image gallery from javascripting. I’m starting to understand pulling data from the DOM and going through the JS stuff as well. I’m looking forward to diving into that material in class to have a better handle on the ninja-like stuff that we’ll be able to do with the interactivity of the sites.

FLEXBOX VERSUS CSS GRID

In general CSS Grid can do everything that Flexbox can do.

Flipper - able to flip between rows and columns in css grid [Flexbox Easier]
Controls on Right - able to put icons on the right side of a row [Same]
Flex on Items - adds a long bar between items [Flexbox Easier]
Perfectly Centered - Puts the contents in the center of the grid [Same]
Self Control - Can move things to corners [Can only do in Grid]
Stacked Layout - Can adjust centered items when wrapped in rows [Flexbox only]
Unknown Content Size - When you know the # of columns but don’t know the size of content
Unknown Number of Items - Can fit as many items as you want, then they wrap [Grid]
Variable Widths on Rows - Can fill up the rows on screen. [Flexbox only]

Grid-template: 1fr 1fr / 1fr 1fr;

Same as

Grid-template-columns: 1fr 1fr;
Grid-template-rows: 1fr 1fr;
Grid-template-areas: none;

RECREATING CODEPEN

Super cool foundation to recreate something that is complex with grid

BOOTSTRAPPY

setting an .item {} class to a min-width: 0; or a  minimal (0, 1fr) and set the width to 100%

You can set variables in CSS by defining them in a var() function — var(—hello)

You can utilize a negative margin!

RESPONSIVE WEBSITE

Great use cases for different facets of a website!

Aria-controls - gives you options on altering controls for hiding/showing things! No scripting.

You use auto-fit a lot on in the real world case! And minmax as well!

	grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));

FULL BLEED BLOG LAYOUT

Grid is inherently good at spacing out text within a website.












