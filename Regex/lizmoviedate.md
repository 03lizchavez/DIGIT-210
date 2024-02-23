# Liz Movie Data Markup

This will be the results from my markup
* Find: ` (.+?$) `
** Replace: ` <movie> \0 </movie> ` 
* Find: ` (<movie>)(.+?$)\t `
** Replace: ` \1 <title> \2 </title> `
* Find: `(</title>)(\d\d*)` 
** Replace: ` \1 <year> \2 </year> `
* Find: ` (</year>)(\W\w*)\t `
** Replace: ` \1 <country>\2</country> `
* Find: `(</year>)(\W\w*)(".*")`
* * Replace: `\1<country>\2\3</country>`
* Find: `(\d\d*) ([a-z]+) `
** Replace: ` <runTime> \1 \2 </runTime> `
