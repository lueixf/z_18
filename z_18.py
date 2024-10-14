input_data = open('input.txt' , 'r')
data = input_data.read()
data = data.split()


n = int(data[0])

factorial = 1

for i in range(2, n+1):
    factorial *= i

print(factorial)
output_data = open('output.txt','a')
output_data.write(str(factorial))
input_data.close()
output_data.close()
