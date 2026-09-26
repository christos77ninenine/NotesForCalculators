import ti_system as ts
K=["NTLD","N2LD","N3LD","N4LD","N5LD"]
def sv(N,a):
 s=str(a)
 for n in N:
  s+="\n\n"+n[0]
  for l in n[1]:s+="\n"+l
 e=[]
 for c in s:e.append(ord(c))
 for p in range(5):
  c=e[p*999:p*999+999]
  if c:ts.store_list(K[p],c)
  else:ts.store_list(K[p],[0])
def ld():
 e=[]
 for p in range(5):
  try:
   c=ts.recall_list(K[p])
   if c and c!=[0]:e.extend(c)
  except:pass
 if not e:return [],0
 s=""
 for v in e:s+=chr(int(v))
 b=s.split("\n\n")
 a=int(b[0]);N=[]
 for i in range(1,len(b)):
  l=b[i].split("\n")
  N.append([l[0],l[1:]])
 return N,a
N,a=ld()
try:
 while 1:
  print("\n"*11)
  print("=== NOTES ===")
  if not N:print(" (none)")
  else:
   for i in range(len(N)):
    m=">" if i==a else " "
    print(m+str(i+1)+"."+N[i][0])
  print("N/V/E/D/R/Q/</>")
  c=input(">").lower()
  if c=="q":
   sv(N,a);print("Saved!");break
  elif c=="n":
   t=input("Title:")
   if t:
    N.append([t,[]])
    a=len(N)-1;sv(N,a)
  elif c=="v" and N:
   print("\n"*11)
   n=N[a]
   print("=="+n[0]+"==")
   if not n[1]:print("(empty)")
   else:
    for l in n[1]:print(l)
   input("[Enter]back")
  elif c=="e" and N:
   print("Empty=done")
   while 1:
    l=input(":")
    if l=="":break
    N[a][1].append(l)
   sv(N,a)
  elif c=="d" and N:
   if input("Del?y/n:").lower()=="y":
    N.pop(a)
    if a>=len(N):
     a=max(0,len(N)-1)
    sv(N,a)
  elif c=="r" and N:
   t=input("Name:")
   if t:N[a][0]=t;sv(N,a)
  elif c=="<" and N:
   a=(a-1)%len(N)
  elif c==">" and N:
   a=(a+1)%len(N)
except KeyboardInterrupt:
 sv(N,a);print("Saved!")
