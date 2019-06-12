arq = open('notakto-gt.txt', 'a')
arq.write("text arq")
arq.close()

arq = open('notakto-gt.txt', 'r')
print(arq.read())