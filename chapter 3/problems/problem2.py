# Write a program to fill in a letter template given below with name and date.

letter = ''' Dear <|Name|> ,
You Are seleced!
<|Date|>'''

print(letter.replace("<|Name|>","Shreyang").replace("<|Date|>","28 May 2050"))
