import time
import sys

toolbar_width = 100

# setup toolbar

persent = 0
b = 0
sys.stdout.write("[%s] %s%% " % (" " * toolbar_width,str(persent)))
sys.stdout.flush()
sys.stdout.write("\b" * (toolbar_width+5))

for i in xrange(toolbar_width):
    persent = i
    time.sleep(0.1) # do real work here
    if i < 9:
        back = 5 + 1
    elif i >= 9 :
        back = 5 + 2
    # update the bar
    sys.stdout.write("-") 
    if i == toolbar_width-1 :
        sys.stdout.write("%s] %s%% " % (" " * int(toolbar_width-i-1),str(persent+1)))
    else:
        sys.stdout.write("%s] %s%% " % (" " * int(toolbar_width-i),str(persent+1)))
    sys.stdout.write("\b" * (toolbar_width+back-i-1))
    sys.stdout.flush()

sys.stdout.write("\n")
