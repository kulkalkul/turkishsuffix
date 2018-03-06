# What is turkishsuffix?
A library for adding complex suffixes to Turkish words. While doing that, the code uses rule set and python's string manipulation to enhance quality. There are similar libraries in both GitHub and PyPi, but most of them are not functioning right, and other's algorithm are too straightforward and because of that their efficiency is less than turkishsuffix.

turkishsuffix uses math and ordered data to dynamically calculate possibilities instead of checking every possibility statically. It has a config, which can easily be edited.

turkishsuffix has 3 main components:
* _suffix.py_ - Main class for turkishsuffix.
* _loader.py_ - Config loader for turkishsuffix.
* _config.ini_ - Config for turkishsuffix.

### Which Features are Working Right Now?
* These Turkish suffixes are functioning right now:
  * çokluk hali
  * ilgi hali
  * eşitlik hali
  * yönelme hali
  * belirtme hali
  * bulunma hali
  * ayrılma hali
  * iyelik hali

* There are exceptions for "su" and "ne" words in ilgi hali. So exception system is functioning right now.

* There is an option for apostrophe in proper names (like human names, city names etc.), that is functioning right now.

### What are Missing?

All complex suffixes are added to the project. Some basic suffix types are missing at the moment.
Also, there are exceptions caused by some non-Turkish words. For example Arabic word for "dream/illusion"
is "hayâl". It has a carret, but as this feature is archaic, we don't write the carret (which 
indicates it should sound soft or long) but pronounce like there is a carret. As suffixes in Turkish
depends on harmony, this causes system to be fooled. This can be fixed with proper exception dictionary.
I'll try to implement that in future (maybe a month later). If you can help, don't be shy. I would be happy.
### How to Use?

Installing:
```python
pip install turkishsuffix
```

Importing:
```python
from turkishsuffix import TurkishSuffix
```

TurkishSuffix construction:
```python
suffix = TurkishSuffix(word, suffix type, possessive state)  # suffix type and posessive state is optional
```
TurkishSuffix methods:
```python
suffix.get_word(type: string, proper: boolean, possessive: string) #  Main method for the most of
#  the situations. As this can return word with suffix, it can also create words with suffixes.
#  For possessive, use "1", "2", "3" as person and "t" or "ç" for plurality. As an example, "1t".
suffix.get_old_word()  # Public method that returns the unchanged word.
suffix.get_suffix()  # Public method that returns only the suffix.
suffix.get_type()  # Public method that returns the suffix type.
suffix.get_possessive()  # Public method that returns possessive state of the suffix.
```

Simple Example:
```python
word = TurkishSuffix("Test")
print(word.get_word("çokluk", True))
word2 = TurkishSuffix("Test", "iyelik", "2t")
print(word2)
```

# How Useful is turkishsuffix?

Programmers usually avoid using suffixes while coding in Turkish. The reason behind that is Turkish having a complex suffix system. For example, an easy one, plural form (çokluk hali) is done with lar or ler. If latest vowel of the word is soft, word's suffix must be ler, if not the suffix must be lar. If we delve deeper, it becomes more complicated. Sometimes some situations require extra letters, some require both hard/soft and  rounded/unrounded to be calculated. Because of this complexity, as I said at start, programmers avoid using suffixes. Instead of "Bora'nın", "Deniz'in", "Umut'un" and etc., they simply add another word into sentence and add suffix to that word. For example they add "bey" and those became "Bora Bey'in", "Deniz ,Bey'in" and "Umut Bey'in". While this can be used in Turkish, we should encourage people to use  formal ones more. If we can encourage people to use this, even Facebook may change how they approach into this issue.

You can check out the more examples at /example.

(Bilkent Üniversitesi'**ne**)

![image.png](https://res.cloudinary.com/hpiynhbhq/image/upload/v1515773083/khh58xmznkvcpvmcxyud.png)
