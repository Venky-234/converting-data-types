# PYTHON IS DRUUUNNNKKKKK !!!! LOOLLLL
num_str = "1234567890"
dig_num = [1,2,3,4,5,6,7,8,9,0]
#num = 0
#str1 = ''
def str_to_int(str):
    num = 0
    for i in str:
        num *= 10 
        num += dig_num[num_str.find(i)]
           
    #print(num+1)
    #print(type(num))
    return num

def int_to_str(num1):
    #last_digit = 0
    str1 = ''
    while num1 > 0:
         #print(dig_num.index(num1 % 10))
         str1 = num_str[dig_num.index(num1 % 10)] + str1
         num1 = num1 // 10
    
    #print(str1)
    #print(type(str1))
    return str1

a = str_to_int('564')
print(type(a))
print(a)
print("----------------")
b = int_to_str(123)
print(type(b))
print(b)
