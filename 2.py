name=input('Enter student\'s name')
mmarks=int(input('enter maximum marks'))
maths=float(input('enter maths marks'))
english=float(input('enter english marks'))
physics=float(input('enter physics marks'))
chemistry=float(input('enter chemistry marks'))
cs=float(input('enter maths marks'))
if maths>mmarks or english>mmarks or physics>mmarks or chemistry>mmarks:
    print('invalid marks inputed')
    print('reenter the name and marks')
else:
    totalmarks=maths+english+physics+chemistry+cs
    perc=(totalmarks/(5*mmarks))*100
    print(name,"got",perc,'%')
    
    if perc>=90 and perc<=100:
        print(name,'got A grade')
    elif perc>=80 and perc<90:
        print(name,'got B grade')
    elif perc>=40 and perc<80:
        print(name,'got C grade')
    elif perc>=33 and perc<40:
        print(name,'got D grade')
    else:
        print(name,'failed in the examination')
    