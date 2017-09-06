words = "It's thanksgiving day. It's my birthday, too!"
print words.find("day")
new_words = words.replace("day", "month",1)
print new_words


x = [2,54,-2,7,12,98]
print "Min =", min(x), " Max =", max(x)


x = ["hello",2,54,-2,7,12,98,"world"]
print x[0], x[len(x)-1]
new_list = [x[0], x[len(x)-1]]
print new_list


x = [19,2,54,-2,7,12,98,32,10,-3,6]
x.sort()
print x
print len(x)
y = x[:len(x)/2]
z = x[len(x)/2 -1:]
z[0] = y
print z