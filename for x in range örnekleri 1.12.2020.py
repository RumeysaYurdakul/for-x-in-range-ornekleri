#for döngü örnekleri
#1.12.2020

#[..n)
print("[0..10) arası sayılar")
for x in range(10):
     print(x,end=' - ')

#[a,b)

print("\n(5..12) arası sayılar") #\n --> alt sayıra geçiş
for x in range (5,12):   #5,6,7,8,9,10,11
     print(x,end=' - ')

#[a,b,k) "k" kadar artarak
print("\n[10..110) arası sayılar 5 'er artımlı")
for x in range(10,110,5):   #10,15,20,25,...100,105)
     print(x,end=' - ')
#[a,b,-k)
print("\n [20..0) arası sayılar, 2 azalarak")
for x in range(20,0,-2): 
     print(x,end=' - ')

for x in range (5,5): #5'ten başla 5 'e kadar 5 hariç(hiç çalışmaz)
     print(x,end='-')

print("\n [0..20) arası sayılar, 2 azalarak")
for x in range(0,20,-2): #çalışmaz 
     print(x,end=' - ')
