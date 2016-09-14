code=[]
sent=input("Enter a sentence")
num=input("enter a number")
#force all letters to lowercase
sent=sent.lower()
for i in range(len(sent)):
	#print(sent[i])
	#print (ord(sent[i]))
#getting rid of space
	if sent[i]!=" ":
		letternum=ord(sent[i])+int(num)
		if letternum>ord("z"):
#allow alphabet to loop back to a
			letternum=letternum-26
	#print (letternum)
		code.append(chr(letternum)) 
coderec="".join(code)
print (coderec)