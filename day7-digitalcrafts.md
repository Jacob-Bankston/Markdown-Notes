#Day 7 - Digital Crafts - Notes

##Importing
To import a file you can say - import file

To import a class/function you can say - from file import class/function

*LIFE TIP - Code incrementally, go step by step, the smaller the step the better.*

Snake case versus Camel Case

snake_case vs camelCase

Python uses Snake Case and JavaScript uses Camel Case

If you don’t want to include something as required in the init method, you can still put it in the file, just not as a required input

```css
def __init__(self, name, title)
    self.name = name
    self.title = title
    self.price = 0.0
    self.color = gray
```

##RESEARCH - one to one, one to many, many to many

One to Many - Shopping List, Posts on a Website

DO NOT TAKE INPUT IN YOUR CLASS - It’s not the job of the input to ask for the information. It should be only responsible for the domain

*RESEARCH - Domain objects, Model Classes*

Ask for input in the main.py file

*You want to create code that can be shared with others, otherwise it is unusable.*

*Make sure that the classes are nice and lean*

**C# has heavy use of classes**

*Shortcut in terminal - “code .” Opens the current folder in vs code.*

*RESEARCH - Persistence, writing files in python*

##Files

You have to `open(“filename.txt”)` then `fileobject.close()` the file

reading the file is the default code in the open function

Remove white space from right side - `contents.rstrip()`

If you forget to close the file, it takes up resources, no one else can open it or interface with it.

Automatically close the file when done using the with operator with `open(“todo.txt”)` as `file_object:`

Uses the normal indentation syntax of python to automatically close the file at the end of the usage. This is the preferred method.

Read a file - `file_object.read()`

Read a file line by line - `for line in file_object: print(line)`
This way is only available in the with function it adds a \n function at the end of each line

Read the lines line by line - `file_object.readlines()`
`[‘Wash the car \n’, ‘Feed the dog \n’]`
returns an array of each line

Write to the file using the following syntax:
`with open(“customers.txt”, “w”) as file_object:
file_object.write(“johndoe@gmail.com”)`
This writes over the file with the new contents

Append Mode! Adding the contents to the next line
`with open(customers.txt”, “a”) as file_object:
file_obect.write(“johndoe@gmail.com”)`

*RESEARCH - JSON Files versus just simple text files*

**DEBUGGED - Be sure that you are in the appropriate directory when running the file in the terminal!**

##JSON

JavaScript Object Notation - saved structured data

Nothing more than a key value pair! Kind of like a dictionary.

A valid JSON document has only one root level. (One Parent Level)

You can always check the validity of a JSON file by googling a JSON validator.

If you have multiple ‘dictionary’ like sets you can place them in an array, or larger dictionary to nest everything in.

You have to import the json module in the python file: `import json`

Same way to WRITE to json files like any other files:
```python
names = [“Mary”, “John”, “Steve”, “Phil”]
with open(“filename.json”, “w”) as file_object:
    json.dump(names, file_object)
```

Same way to READ from son files like any other files:

```python
with open(“filename.json”) as file_object:
    new_list = json.load(file_object)
```

When you are utilizing JSON you will most likely just write the information again to not have an error pop up with having more than one root. You will probably never use the append method for this.

The json module does not know how to import an object from your class, only the base structural objects built into python.

The prebuilt method in python to convert a class object to dictionary:

`__dict__`

To tie that to an object with the name customer you would state:

`customer.__dict__`

*RESEARCH - `@staticmethod`*

You can call the Static Methods on the class itself

With static method you don’t have to create an init to call the function:
```python
@staticmethod
def from_dictionary(dict):
return Customer(dict[“name”], dict[“age”])
```

Calling the static method would look like this:
```python
c = Customer.from_dictionary(dict)
```

You can convert the JSON information back into an object, or keep it as the data. It depends on what you’re doing with the information. If you need to access a method of the class then you would need to convert it back.

A practical example of JSON - A movie website has a dictionary with a key of the dictionary of the list of movies to search through

JSON is used as the primary means of sending you data, nothing to do with html, css, interactivity, etc…

Chrome Browser - JSON VIEW formatting for json files

JSON Lint - validate your JSON files!

Shift+Tab will take the tabs to the left
Tab will shift the tabs to the right