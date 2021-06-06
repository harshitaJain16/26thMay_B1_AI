#enter the string
string=input("Enter the string")
a={i:string.count(i) for i in string}
b=[i for i in a.values()]
l=len(b);m=min(b);s=sum(b)
print("my string" if l*m==s or (l*m)+1==s else "not my strig")
