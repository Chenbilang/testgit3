# -*- coding: utf-8 -*-
import sys
reload(sys)
sys.setdefaultencoding("utf-8")
s="附件是考虑"
str=['解放路口的','九分裤了',s]
ustr=[u'解放路口的',u'九分裤了']
print(s)

print(str)
print (ustr)
print(repr(str).decode('string-escape'))
print(repr(ustr).decode('unicode-escape'))
print (",".join(str))
print (",".join(ustr))