import secrets 

secretGenerator = secrets.SystemRandom()

random_seperation = [] #table of the random seperation code 

random_seperator_range = secretGenerator.randint(8,30) #length of the random seperation between values

for i in range(random_seperator_range):
    random_seperator = secretGenerator.randint(0,50)
    random_seperation.append(random_seperator)
    
randoom = [str(item) for item in random_seperation] #random string to differentiate between each letter 


User_input = input("Input the secret message: ")

secret2 = [ord(x) for x in User_input] #turns the input into ascii values 
    
for i in range(0,2): 
        
    secretised = ' '.join([str(item) for item in secret2]) #takes the ascii values joins together 
    secret3 = [str(x) for x in secretised] 
    secret2 = [ord(x) for x in secret3] #converts further via ascii 
    secret2.append(32)
    
passwordtranslated = str(secret2).translate({ord(i): None for i in '[],'}) #removes the unnessecary characters to be translated back to a message 
randoomy = str(randoom).translate({ord(i): None for i in "[],' "})

print(secret2) # each letter in ascii encoded 3 times

furtherENCODE = str(passwordtranslated).replace(" ",str(randoomy))

print(passwordtranslated) #final encoded message with string inbetween 



with open("filewithsecret.txt", "w")as file: 

    file.writelines(furtherENCODE) #write the encoded message to filewithsecret 
    
with open("LOB-stage2.py", "r")as file: #reads the first line to be replaced 
    
    data = file.readlines()
    
data[0] = f'randoom = "{randoomy}"\n' #writes the first line of stage 2 with the random section that needs to be removed 

with open("LOB-stage2.py", "w")as file:
    file.writelines(data)