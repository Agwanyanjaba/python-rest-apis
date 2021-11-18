tokens = ['<greeting>', 'Hello World!', '</greeting>']
count = 0

# write your for loop here
string_list = []
count = 0
for token in tokens:
    if token[0] == '<' and token[-1] == '>':
        count += 1


#working solution
# write your code here
items = ['first string', 'second string']
html_str = "<ul>\n"
for item in items:
    html_str = html_str + "<li>" + str(item) + "</li>" "\n"
html_str = html_str + "</ul>"
print(html_str) 



for token in tokens:
    if token[0] == '<' and token[-1] == '>':
        count = count + 1
    
print(count)

items = ['first string', 'second string']
html_str = "<ul>\n"  # "\ n" is the character that marks the end of the line, it does
                     # the characters that are after it in html_str are on the next line

# write your code here
for item in items:
    html_str = html_str + "<li>" + str(item) + "</li>" "\n"
html_str = html_str + "</ul>"
print(html_str)



colors = ['Red', 'Blue', 'Green', 'Purple']
lower_colors = [ ]

for color in colors:
    lower_colors.append(color.lower())

print(lower_colors)