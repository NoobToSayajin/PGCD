def PGCD(pN0, pN1):
    A,B = pN0, pN1
    R = 1
    OldR = 0

    if A == 0 or B == 0:
        print("Nomre entier non nul uniquement!")
    
    if A < B:
        A,B = B,A

    while(R!=0):
        OldR=R
        R = A%B
        A = B
        B = R

    if OldR == 1:
        print("les nombres: "+str(pN0)+";"+str(pN1)+" sont premiers entre eux.")

    result = print("PGCD("+str(pN0)+";"+str(pN1)+") = "+ str(OldR))

    return result