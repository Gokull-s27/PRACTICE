#data types , input

#task 1
name=input("enter ur name: ")

age=int(input("enter ur age: "))
weight=int(input("enter ur weight: "))

height=float(input("enter ur height: "))
bmi=weight/(height)**2

if(bmi<16):
    cat=("too less")
elif(bmi<18.5):
    cat=("less")
elif(bmi<25):
    cat=("normal")
elif(bmi<30):
    cat=("high")
else:
    cat=("obese")

print("BOY:My name is ",name,"i'm ",age,"yrs old ...hmm my height around",height,"feet and i weight around",weight, "kgs ...byee byee good night" )
print("so ur bmi is ",bmi,"then category is",cat)
