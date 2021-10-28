list =["Realize","that","excellent","marks","qualify","everybody","for","jumps","in","wages"]
a=input ("Enter the string - ") #taking input
p = 0
l = len (a) #taking lenth of input
while (p < l - 2):
    i = int (a[p])           #typecasting char into int
    if (a[p + 1] != '-'):    #taking 1 0 as 10
        i = 10
    if (i == 10):
        p += 1               #incrementing value of p when i=10
    j = int (a[p + 2])       #typecasting char into int
    print ((list [i - 1])[j - 1], end = "")   
    if(p + 3 < l and a[p + 3] == '@'):  #checking the delimiter for spacing
        print (" ", end = "")
    p += 4                    #incrementing p by 4 so that it can skip "number" "-" and "," 

