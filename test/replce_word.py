
import re
def multiple_replace(text, adict):
     rx = re.compile('|'.join(map(re.escape, adict)))
     def one_xlat(match):
           return adict[match.group(0)]
     return rx.sub(one_xlat, text)
multiple_replace('123456,ss,a,v,f',)