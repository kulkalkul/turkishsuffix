# What is turkishsuffix?

turkishsuffix is a library to add complex suffixes to Turkish words.
There are similar libraries on both GitHub and PyPi, but turkishsuffix
achieves it dynamically using single harmony detection algorithm instead of
static checks. It does that with the help of simple math and ordered data. It
also includes a config which is easy to edit.

turkishsuffix has 2 components:
* _suffix.py_ - Main class for turkishsuffix.
* _loader.py_ - Config loader for turkishsuffix.

### Which Features are Working Right Now?
* These Turkish suffixes are functioning right now:
  * çokluk hali (plural form)
  * ilgi hali (genitive form)
  * eşitlik hali (likeliness? form)
  * yönelme hali (dative form)
  * belirtme hali (accusative form)
  * bulunma hali (locative form)
  * ayrılma hali (ablative form)
  * iyelik hali (possessive form)

* Exception system for "ne" and "su" is working right now. Normally, buffer letter 
for the genitive form is "n", but those two words are exceptions and use "y" as the buffer
letter. The reason is these two words originally spelled with a "y" e.g. "suy" and "ney". But
over time, that became archaic. The same thing also applies for possessive form but in a much
more complex manner.

* Exception system for non-Turkish words is working. Turkish has a vowel harmony
based on the last vowel of the word. But some non-Turkish does not follow this rule.
For example, the plural form of "hayal" -an Arabic word meaning "dream"- looks like should be
"lar", but actually its "ler". The reason behind is an archaic feature of the language.
The last "a" of "hayal" is pronounced softly than the other. Normally, it is described
with a caret (^) like "hayâl". But as it is archaic in most words, it fools the
computer. I fixed this with an exception list.

* There is an option for an apostrophe in proper names (like human names, city names etc.).

### What are Missing?

I reached all my goals which I defined from the start of the project. Still, I would
like to add other, basic suffix types. Also, I'm thinking of a wrapper class which
is more suitable for usage than the real class.

### How to Install?

Installing:
```python
pip install turkishsuffix
```

### How to Use?

Importing:
```python
from turkishsuffix import turkishSuffix
```

TurkishSuffix construction:
```python
turkishSuffix.suffix(word, suffix_type, apostrophe(optional), possessive(optional))
```

Several Examples:
```python
turkishSuffix.suffix("okul", "ayrılma") # -> okuldan
turkishSuffix.suffix("Bora", "ilgi", True) # -> Bora'nın
turkishSuffix.suffix("kedi", "iyelik", possessive="1ç") # -> kedimiz
```

# How Useful is turkishsuffix?

Programmers usually avoid using suffixes while coding in Turkish. The reason behind
that is Turkish having a complex suffix system. Instead of "Bora'nın", "Deniz'in",
"Umut'un", they simply add a static word into sentence suffix that word e.g.
"Bora Bey'in", "Deniz Bey'in", "Umut Bey'in" While this isn't against Turkish, we
should encourage people to use normal ones. If we can encourage people to use this,
even Facebook may change how they approach into this issue.

You can check out examples at /example.

(Bilkent Üniversitesi'**ne**) - not "ye".

![image.png](https://res.cloudinary.com/hpiynhbhq/image/upload/v1515773083/khh58xmznkvcpvmcxyud.png)
