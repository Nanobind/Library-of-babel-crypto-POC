randoom = "42421236122384521393832324861446431638"

f = open("filewithsecret.txt", "r")

secret = (f.read()).replace(str(randoom), " ") #replaces every instance of randoom with a space 

secret_vault = []

Secret = secret.split(" ") # splits in each individual number 
 
for i in range(0,3):
    
    secret2 = [int(x) for x in Secret]

    for x in secret2: #increments over every value of x
                    
        secret_vaulted = str(chr(x)) #turns integer to ascii letter equiv
        secret_vault.append(secret_vaulted) #appends to the array 
        completedmessage = "".join(secret_vault) #joins all in one string 
        Secret = completedmessage.split(" ") #splits apart into list
        print(Secret)
        Secret.pop()        
        
    if i != 2:
        secret_vault.clear()
    else:
        print(completedmessage)
 