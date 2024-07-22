import datetime as dt
import re

a = ['Raja','Raman','Belvina','Shyamantha','Meenashree']

starttime = dt.datetime.now()

new_list = [i[::-1].lower() for i in a]

endtime = dt.datetime.now()


print(endtime-starttime)

starttime = dt.datetime.now()

temp = []
for i in a:

    element = i[::-1].lower()
    temp.append(element)


endtime = dt.datetime.now()


print(endtime-starttime)

