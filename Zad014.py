s1="uniwersytet"
s2="terminologia"
s3="mikrometr"
a=list(set(s1)&set(s2)&set(s3))
print("The common letters are:")
for i in a:
    print(i)