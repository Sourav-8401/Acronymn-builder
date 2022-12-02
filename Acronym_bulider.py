'''s:randoom assses memory
p:staff selection commision
r:computer science engineering
t:union public service commision'''



print("\n_______THIS PROGRAM WILL GENERATE ACRONYM FOR YOUR SENTENCE_______ \n\n")
        #TAKING NUMBER OF SENTENCE TO FIND
n = int(input("Enter the number of sentence to convert into acroynm: "))
list1 = []
i = 1
            #STORING IN LIST
while i<=n:
    element = input("Enter the {} element: ".format(i))
    list1.append(element)
    i += 1
       #MAKING ACROYNM FUNCTION
def acroynm(sentence):
    l1 = sentence.split(" ")
    c = ""
    for i in l1:
        c = c + i[0]
    return c.upper()
     #PRINTING THE RESULT
m = 0
while m < n:
    print("Acroymn of ({}) is: {}".format(list1[m], acroynm(list1[m])))
    m += 1
         #END
