#!/usr/bin/env python

header = """
<!DOCTYPE html>
<html>
<head>
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Haiku </title>
<link rel="stylesheet" type="text/css" href="./haiku.css">
<style>
td {
  margin: 1em;
  border: 1px solid gray;
  border-radius: 4px;
  padding: 1em;
}
</style>
</head>

<body bgcolor="#ffffff"
link="#993333" vlink="#888888" alink="#cc3333">

<p>These are haiku/senryu I&rsquo;ve published on Threads, and then Bluesky. Each is preceded by the
day&rsquo;s single-word prompt by <code>@haikufeels</code> / <code>@annemorrigan</code>.

"""

footer = """
<p><hr>
&larr; <a href="../index.html"><i>Back</i> </a>

</body>
</html>
"""

import re

num_per_row = 3

print(header)

with open('items.txt') as f:
    body = f.read()

body = body.strip()
paragraphs = re.split(r"\n\n+", body)

print("<table>")
i = 0
npara = len(paragraphs)
for paragraph in paragraphs:
    lines = paragraph.split("\n")
    title = lines[0]
    lines = lines[1:]

    if (i % num_per_row) == 0:
        print("  <tr>")
    print("    <td>")
    print(f"      <span class=boldmaroon>{title}</span>")

    for line in lines:
        line = re.sub("^  *", "", line)
        line = re.sub("--", "&mdash;", line)
        line = re.sub("'", "&rsquo;", line)

        print(f"      <br>{line}")

    print("    </td>")
    if ((i % num_per_row) == (num_per_row - 1)) or (i == npara - 1):
        print("  </tr>")
    print()

    i += 1

print("</table>")
print(footer)
