# 0x00. AirBnB clone - The console
This project creates a command line interpreter that will run the whole cloned app. The user will be able to run the console in interactive and non-interactive modes.
The console will;

  - Create the data model for the whole project
  - manage (create, update, destroy etc) objects via the command interpreter
  - store and persist objects to a JSON file


## Concepts
- Group Project Collaboration using Git and Github
- Python Backend Development
- Object Oriented Programming
- JSON files manipulation
### Key Concept

 >***Write a Python command interpreter (Console)***

**Command Line Interpreter / Console**
---
The Console will manage the creation and manipulation is objects in the app. It will also be a connection point to the storage and serve the API for data manipulation. The design will look as shown below;

![system design diagram ](images/console%20system%20design.png)


<u>**How to start the Console**</u>

The console has two modes:

**Interactive Mode** which is run as shown below;

> 
    $ ./console.py
    (hbnb) help

    Documented commands (type help <topic>):
    ========================================
    EOF  help  quit

    (hbnb) 
    (hbnb) 
    (hbnb) quit
    $
>

**Non-Interactive Mode** which is run as shown below;


>
      $ echo "help" | ./console.py
    (hbnb)

    Documented commands (type help <topic>):
    ========================================
    EOF  help  quit
    (hbnb) 
    $
    $ cat test_help
    help
    $
    $ cat test_help | ./console.py
    (hbnb)

    Documented commands (type help <topic>):
    ========================================
    EOF  help  quit
    (hbnb) 
    $
>
### Authors
---
- Erasto Wanjau [EWanjau](wamwanjau@gmail.com)
- Samuel Igwudu
 [Samuel-Igwudu]()
  