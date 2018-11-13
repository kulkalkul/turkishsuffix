types = (
            "çokluk",
            "ilgi",
            "eşitlik",
            "yönelme",
            "belirtme",
            "bulunma",
            "ayrılma",
            "iyelik"
)

vowels = (
            "a", "ı",
            "e", "i",
            "o", "u",
            "ö", "ü"
)

softs = (
            "c", "d", "b", "ğ"
)

hards = (
            "ç", "t", "p", "k", "s", "ş", "f", "h"
)

rule_set = (
                "02lr",
                "24+n:;",
                "02c-",
                "02+-;",
                "24+-;",
                "02d-",
                "02dn",
                "24+-;,"
)

possessive_types = (
                    "1t", "2t", "3t",
                    "1ç", "2ç", "3ç"
)

possessive_rule_set = (
                "-m", "-n", "+-,",
                "mz:", "nz:", "--;"
)

suffix_vowels = (
                "a", "e",
                "ı", "i", "u", "ü"
)

uppercase_i = (
                "İ", "I"
)

lowercase_i = (
                "i", "ı"
)

turkish_i = (*uppercase_i, *lowercase_i)
