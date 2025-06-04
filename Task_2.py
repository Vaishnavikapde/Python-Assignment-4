file1=open("output.txt","r")
reading= file1.read()
print(reading)
file1.close()


file1=open("output.txt","a")
writing= file1.write("\nThis is new line")
print(writing)
file1.close()

file1=open("output.txt","r")
reading= file1.read()
print(reading)
file1.close()