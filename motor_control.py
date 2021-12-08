c=int(input("Choose number of checks:"))
for i in range(c):
    print("Hello Electrician, let's start the machines")
    n=int(input("Give number of motors:"))
    for i in range(n):
        V=float(input("Give nominal voltage:"))
        f=float(input("Give nominal frequency:"))
        print(V,"V","/",f,"Hz")
        power=int(input("Give state of motor:"))
        y="-1"
        if  bool(power)==True:
            print("ONLINE")
            mf=V/f
            print(mf)
            for i in range(2):
                if mf<4:
                    print("ERROR")
                else:
                    print("OK")
            curr=input("Give reference current:")
            curr=curr+"t"
            if curr>="uvwt":
                print("END OF CONTROL")
                y="0"
            else:
                print("START OF CONTROL")
                y="1"
        else:
            print("OFFLINE")
        print("Hello Programmer, let's begin the function")
        for i in [0,2,4,6,8,10,12,14,16]:
            print("State of motor:(",i*2-16,")",end="\n",sep="")
        x=input("Choose state of motor:")
        if x>"0" or x<"0":
            print("ON_"+x)
            if y=="1":
                print("RUN CONTROL")
            elif y=="0":
                print ("STOP CONTROL")
            elif y=="-1":
                print("ERROR")
        else:
            print("OFF")
print("Bye Bye Electrician")
