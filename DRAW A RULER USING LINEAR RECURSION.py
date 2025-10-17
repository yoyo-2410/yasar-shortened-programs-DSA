# TO DRAW A RULER USING LINEAR RECURSION

def line(len, label=''):
    print('-'*len, label)

def interval(len):
    if len > 0:
        interval(len-1)
        line(len)
        interval(len-1)

def ruler(inch, major):
    line(major, '0')
    for i in range(1, inch+1):
        interval(major-1)
        line(major, str(i))

ruler(5, 4)
