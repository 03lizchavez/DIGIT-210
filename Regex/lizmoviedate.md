# Liz Movie Data Markup

This will be the results from my markup
* Find: ` (.+?$) `
** Replace: ` <movie> \0 </movie> ` 
* Find: ` (<movie>)(.+?$)\t `
** Replace: ` \1 <title> \2 </title> `
* Find: ` \d\d\d\d ` 
** Replace: ` <year> \1 </year> `
* Find: ` (</year>)(.+$?)\t `
** Replace: ` \1 <country>\2</country> `
* Find: `(\d\d*) ([a-z]+) `
** Replace: ` <runTime> \1 \2 </runTime> `
