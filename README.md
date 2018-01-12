# What is turkishsuffix?
A library for adding complex suffixes to Turkish words. While doing that, the code uses rule set and python's string manipulation to enhance quality. There are similar libraries in both GitHub and PyPi, but most of them are not functioning right, and other's algorithm are too straightforward and because of that their efficiency is less than turkishsuffix.

turkishsuffix uses math and ordered data to dynamically calculate possibilities instead of checking every possibility statically. It has a config, which can easily be edited.

For now, turkishsuffix has 2 main components:
* _\_\_init\_\_.py_
* _config.ini_
In future, I might modularize init file to make it more developer friendly. Right now, my main goal is functionality and effectivity.

### Which Features are Working Right Now?
* These Turkish suffixes are functioning right now:
  * çokluk hali
  * ilgi hali
  * eşitlik hali
  * yönelme hali
  * belirtme hali
  * bulunma hali
  * ayrılma hali

* There are exceptions for "su" and "ne" words in ilgi hali. So exception system is functioning right now.

* There is an option for apostrophe in special names (like human names, city names etc.), that is functioning right now.

### What are Missing?

Right now, a complicated suffix named  iyelik hali is missing. I am going to add that as a new method if I can find spare time. Also, making the code more modular is also on my list.

### How to Use?

Installing:
```python
pip install turkishsuffix
```

Importing:
```python
import turkishsuffix
```

Suffix construction:
```python
suffix = turkishsuffix.Suffix(word, suffix type) # suffix type is optional
```
Suffix methods:
```python
suffix.get_suffix()
suffix.get_word(special) # special = boolean
suffix.get_old_word()
suffix.set_suffix(suffix type)
```

# How Useful is turkishsuffix?

Programmers usually avoid using suffixes while coding in Turkish. The reason behind that is Turkish having a complex suffix system. For example, an easy one, plural form (çokluk hali) is done with lar or ler. If latest vowel of the word is soft, word's suffix must be ler, if not the suffix must be lar. If we delve deeper, it becomes more complicated. Sometimes some situations require extra letters, some require both hard/soft and  rounded/unrounded to be calculated. Because of this complexity, as I said at start, programmers avoid using suffixes. Instead of "Bora'nın", "Deniz'in", "Umut'un" and etc., they simply add another word into sentence and add suffix to that word. For example they add "bey" and those became "Bora Bey'in", "Deniz ,Bey'in" and "Umut Bey'in". While this can be used in Turkish, we should encourage people to use  formal ones more. If we can encourage people to use this, even Facebook may change how they approach into this issue.

(Bilkent Üniversitesi'**ne**)
![image.png](https://res.cloudinary.com/hpiynhbhq/image/upload/v1515773083/khh58xmznkvcpvmcxyud.png)
