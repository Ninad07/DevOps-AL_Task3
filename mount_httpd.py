import os

p = os.popen("ls /kubernetes/code/ | grep .html")
q = p.read()
n = q.split("\n")
N = n[:-1]
print(N[0])


a=os.popen("kubectl get pods | grep httpd-dep")
b = a.read()
x=b.split("\n")
X = x[:-1]
print(X)
for y in X:
    z = y.split()
    print(z[0])
    os.system("kubectl cp /kubernetes/code/%s  %s:/usr/local/apache2/htdocs/" %(N[0],z[0]))

