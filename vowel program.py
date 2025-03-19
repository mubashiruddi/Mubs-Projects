s6=s3=s4=""
s5=" "
a=e=i=o=u=length=vowel=notvowel=0
while s6 in ""or s6 in"Y"or s6 in "y" :
    s2=input("Do you like Typing Yes/No: ")
    s2=s2.lower()
    if s2 in"yes" or s2 in "y":

        while s3 in"Y" or s3 in "y"or s3 in "" :
            
            s1=(input("Write any line or alphebat: "))
            l=len(s1)
            if s1!="":
                x=0
                space=z=w=v=t=s=q=y=0
                while x < len(s1):
                    s1=s1.lower()
                    if s1[x] in "aeiou ":
                        if s1[x]=='a':
                            z=z+len(s1[x])  
                            
                        elif s1[x]=='e':
                            w=w+len(s1[x])
                            
                        elif s1[x]=='i':
                            v=v+len(s1[x])
                            
                        elif s1[x]=='o':
                            t=t+len(s1[x])
                            
                        elif s1[x]=='u':
                            s=s+len(s1[x])
                            
                        elif s1[x]==' ':
                            space=space+len(s1[x])
                        y=z+w+v+t+s    

                    else:
                        q=q+len(s1[x])
                    
                    x=x+1

                l=l-space    
            s3=input("Do You want more Typing yes/no: ")
            s3=s3.lower()
            if s3 in "n" or s3 in "no":
                s3="n"
                s6="n"
            s4=s4+s5+s1
            a=a+z
            e=e+w
            i=i+v
            o=o+t
            u=u+s
            vowel=a+e+i+o+u
            notvowel=notvowel+q
            length=length+l   
        else:
            print("Invalid Input")
    else:
        print("Invalid Input")
        print("Do you want to Continue")
        s6=input("press yes/no ")
        s6=s6.lower()



print("Your Cridential is giving bellow")  
print(f"maximum aplabet of (a) is {a}") 
print(f"maximum aplabet of (e) is {e}")        
print(f"maximum aplabet of (i) is {i}")
print(f"maximum aplabet of (o) is {o}")
print(f"maximum aplabet of (u) is {u}")
print(f"Your total vowel in ({s4}) ")
print(f"is equal to {vowel}")
print(f"maximum alphabet not vowel {notvowel}",end=" ")
print(f"your total alphebat is {length} ")
print("Thank you")   