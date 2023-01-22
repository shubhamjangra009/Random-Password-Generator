import random
alphabets=['a','b','c','d','e','f','g','h','i','j','k','m','n','o','p','q','r','s','t','u','v','w','x','y','z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
numbers=[1,2,3,4,5,6,7,8,9,0]
specials=['!','@','#','$','^','&','*','(',')']
#totallength=int(input('enter total length of password less than 10: '))
alphalen=int(input('enter number of alphabets you want: '))
numlen=int(input('enter number of numbers you want: '))
spcllen=int(input('enter number of special characters you want: '))
a=[]
for n in range(1,alphalen+1):
    if n<=alphalen:
        r=random.choice(alphabets)
        a.append(r)
#print(a)
b=[]
for n in range(1,numlen+1):
    if n<=numlen:
        r=random.choice(numbers)
        b.append(r)
c=[]
for n in range(1,spcllen+1):
    if n<=spcllen:
        r=random.choice(specials)
        c.append(r)
f=a+b+c
#print(f)
random.shuffle(f)
fstr=' '.join(map(str, f))
#print(fstr)
final=''.join(fstr.split())
print(f'Your password can be: {final}')

#empty list or append fir conversion ki bajay string concatination se ho jega easily