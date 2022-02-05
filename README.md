
## What is a multi-clipboard?

We’ve all been there: you try to copy and paste a link or address, only to realize you’ve already overwritten your clipboard with something else (note that this issue has been resolved using the updated clipboard in Windows 10 tho). 

Now, a multi-clipboard is one in which you can add multiple items to the clipboard cache (i.e., you can copy multiple items to the clipboard without worring about the successive items overwriting the preceeding ones). Each item in the clipboard is associated with a key, using which you can access the item. Note, that by 'accessing the item' we mean that 'bringing the item to the top' in the clipboard cache - if item *I* is at the top, hitting CTRL+V will paste *I* on the editor/window. 

Here is an implementation of multi-clipboard in Python 3, and it is only a single minimalistic script. 

## Commands
If you're on Linux/Mac, use **python3** instead of **python**. 

### Adding to the clipboard cache
In this project's root directory, open the command line/terminal, enter:

    $ python clipb.py save

   Copy whatever you want from any window using  CTRL+V (say, I copied [this](https://en.wikipedia.org/wiki/Main_Page)). The terminal prompts you to enter a key for the item that you just copied: 

    key : 'wikipedia link'

### Visualizing the cache

    $ python clipb.py list
   Will result in 

    wikipedia link : https://en.wikipedia.org/wiki/Main_Page

If you have multiple items in it, 

    wikipedia link : https://en.wikipedia.org/wiki/Main_Page
    toi headlines : https://toi.org/headlines

### Pasting

    $ python clipb.py load
    key : 'toi headlines' 

CTRL + V gives you : `https://toi.org/headlines`

### Refreshing and Deleting
Refreshing: 

    $ python clipb.py refresh 

Deleting

    $ python clib.py del 
    key : 'movie link' 


