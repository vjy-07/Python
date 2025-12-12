with open("Part 5/sample3.txt", 'w+') as f:
    f.write("new file created")
    
import os
os.remove("Part 5/sample3.txt")