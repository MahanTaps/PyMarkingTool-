import re
def starts_with_a(string):
    pattern=r'^\(a\)'
    return bool(re.search(pattern,string))
def has_no_stem(string):
    regex=r'QUESTION\s+\d+\s\n\s\n\(a\)\s'
    return bool(re.fullmatch(regex,string))

str1='(a) \nDetermine the coordinates for the y-intercept of the graph of f. \n \n \n \n \n(1)'
str2="(b) \nDetermine ( )\n'\n.\nf\nx\n \n \n \n \n \n \n \n \n \n \n \n \n \n(3)"
str3='QUESTION 1 \n \n(a) '
str4='QUESTION 2 \n \nIf ( )\n(\n)(\n)(\n)\n2\n4\n4\nf x\nx\nx\nx\n=\n+\n−\n−\n then: \n \n(a) '
str5='QUESTION 3 \n \nThe graphs of f and g have been sketched on the set of axes below. \n \n• \n( )\n(\n)\nlog\n2\nm\nf x\nx\n=\n+\n \n• \n( )\n4\ng x\nx\n= −+\n \n• B and C are the x- and y-intercept of the graph of f respectively. \n• \n(\n)\nA 3 ;1  lies on both f and g. \n• The dotted line through D with equation \n2\nx = − is the asymptote for f. \n \n \n \n(a) '
str6='QUESTION 4 \n \n(a) '
print(starts_with_a(str1))
print(starts_with_a(str2))
print(has_no_stem(str4))
print(has_no_stem(str6))

