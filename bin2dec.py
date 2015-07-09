
#10 digit binary to decimal conversion python code

b = "0010100110"

c = b[9]
d = b[8]
e = b[7]
f = b[6]
g = b[5]
h = b[4]
i = b[3]
j = b[2]
k = b[1]
l = b[0]

bin2dec = float(c)*(2**0)+float(d)*(2**1)+float(e)*(2**2)+float(f)*(2**3)+float(g)*(2**4)+float(h)*(2**5)+float(i)*(2**6)+float(j)*(2**7)+float(k)*(2**8)+float(l)*(2**9)

print bin2dec
    