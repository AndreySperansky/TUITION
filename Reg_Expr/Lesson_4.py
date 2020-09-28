'''
https://www.youtube.com/watch?v=xYm6o-TrFeg&list=PLA0M1Bcd0w8w8gtWzf9YkfAxFCgDb09pA&index=4
'''

'''
Флаги и проверки
'''
import re

text = "подоходный налог"
match = re.findall(r"прибыль|обретение|доход", text)
print(match)
# ['доход']

text = "подоходный налог, прибыль"
match = re.findall(r"\bприбыль\b|налог|\bдоход\b", text)
print(match)
# ['налог', 'прибыль']


text = "подоходный налог, прибыль"
match = re.findall(r"\b(прибыль|налог|доход)\b", text)
print(match)
# ['налог', 'прибыль']

text = "подоходный налог, прибыль"
match = re.findall(r"\b(?:прибыль|налог|доход)\b", text)
print(match)




text = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width">
    <link rel="stylesheet" href="content3.css">
    <title></title>
</head>

<body>
<p align=center>Hello World!</p>
<script type="text/javascript">
   let o = document.getElementById('id_div');
   consile.log(obj);
</script>
</body>
</html>"""

# опережающая проверка (script не влкючается в шаблон)
match = re.findall(r"^<script.*?>([\w\W\s]+)(?=</script>)", text, re.MULTILINE)
print(match)
# ["\n   let o = document.getElementById('id_div');\n   consile.log(obj);\n"]

# ретроспективная проверка (script тоже включается в шаблон)
match = re.findall(r"^<script.*?>([\w\W\s]+)(?<=</script>)", text, re.MULTILINE)
print(match)
# ["\n   let o = document.getElementById('id_div');\n   consile.log(obj);\n</script>"]


match = re.findall(r"([-\w]+)[ \t]*=[ \t]*(?P<name>[\"'])?(?(name)([^\"']+(?<![ \t]))|([^ \t>]+))", text, re.M)
print(match)
# [('lang', '"', 'en', ''), ('charset', '"', 'utf-8', ''), ('name', '"', 'viewport', ''),
#  ('content', '"', 'width=device-width', ''), ('rel', '"', 'stylesheet', ''), ('href', '"', 'content3.css', ''),
# ('align', '', '', 'center'), ('type', '"', 'text/javascript', ''), ('o', '', '', "document.getElementById('id_div');
# \n")]


match = re.findall(r"""([-\w]+)         # выделяем атрибут
                    [ \t]*=[ \t]*       # Далее, должно идти равно и кавычки
                    (?P<name>[\"'])?    # Проверяем наличие кавычки
                    (?(name)([^\"']+(?<![ \t]))|([^ \t>]+))     # выделяем значение атрибута
                    """,
                    text, re.MULTILINE|re.VERBOSE)
print(match)

# Использование флагов
text = "Python, python, PYTHON"
match = re.findall(r"(?im)python", text)
print(match)
# ['Python', 'python', 'PYTHON']