# Nav-Bar-Handler
Please read the documentation completely before you use the script.

## Safety first
I'm an inexperienced programmer and I'm still in Training. With this Programm I change files and dont want u to destroy your Homepage.

Its not dangerous at all but can overwrite a part of your file.

So the first thing u have to do before u try this script is **make a Backup** and test it first. If it works use it!

I use the script for my own page and i tested it a lot in Linux Ubuntu without any mistakes.

**Thats why i created a testing area for you. In this folder you have some templates and can test my script without a risk**

If you find an issue pls let me know.

## Let's go in testarea
The test area is configured right and you just have to go into *main.py*.

At the bottom `if __name__ == "__main__"` you have to remove `pass` and the *#* in front of `main`. 

Now you hit the **run-Button** and find the output in */testordner*

## Let's go for your personal config 
You have to change a few paths. The easiest way is that u right click it an select *relative paths* then u can paste it. Dont forget the **/** after the paste

Dont worry. If something is wrong the prog wont work and exit() u can taste this aswell in the testing area for sure.

- go to */script/NavHandler.py*
```python
class TemplateFile():         
    TEMPLATE_PATH = "YOURPATH HERE"         #<-- CHANGE ME!
    HEADER_NAV = "<!-- NAVBAR START -->"    #<-- YOUR MARKER HERE
    FOOTER_NAV = "<!-- NAVBAR END -->"      #<-- YOUR MARKER HERE
```
- go to */script/main.py* 
```python
# Use Relative PATHS
# CHANGE TEMPLATE PATH IN script/NavHandler.py

INPUT_FOLDER="YOUR PATH HERE"           #<- add your path here
OUTPUT_FOLDER="output/"                 #<- add your path here "/"!!!!


## IMPORTANT u have to add "/" 
## if u copy relative path you get only "testordner"
```
- file structure
```python
<website>
    first.html
    second.html
    <script>
        main.py
        NavHandler.py
    <template>
        mytemplate.html
```
you can change it for sure but i didnt test it
- template.html / first.html

**template.html** -> 

**IMPORTANT** ENTER(\n) before and after the `<!-- NAV -->`

I donno why yet but without it wont work. 
```html

<!-- NAVBAR START -->
<nav>
    Your Navbar here
</nav>
<!-- NAVBAR END -->

```

**first.html**
```html
<html>
    <head>
        Content
    </head>
    <body>

        <!-- NAVBAR START -->
            empty or old content
        <!-- NAVBAR END -->

        <!-- CONTENT START -->
            You dont hv to use content start/end is just prefere it
        <!-- CONTENT END -->

        <footer>
            content
        </footer>
    </body>
</html>
```

## Thanks
I hope i dont forget anything and thanks for reading.
