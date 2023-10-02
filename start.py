from datetime import datetime
c = datetime.now()
print(" i am from start")
current_time = c.strftime('%Y%m%d%H%M%S')
print(c)
print(current_time)
filename = "file_" + current_time +".txt"
f = open(filename, "a")
f.write("Now the file has more content!")
f.close()

