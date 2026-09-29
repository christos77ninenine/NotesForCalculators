import ti_system as ts
K=["NTLD","N2LD","N3LD","N4LD","N5LD"]
W=21
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
def hd(t,x,n):
 print("\n"*11)
 print("="*W)
 h="("+str(x+1)+"/"+str(n)+")"
 mx=W-len(h)-2
 if len(t)>mx:t=t[:mx-2]+".."
 print(" "+t+" "+h)
N,a=ld()
md=0
try:
 while 1:
  if md==0:
   print("\n"*11)
   print("="*W)
   if N:print(" "+str(len(N))+" notes")
   else:print(" Notes (empty)")
   print("-"*W)
   if not N:print(" (none)")
   else:
    for i in range(len(N)):
     t=N[i][0]
     if len(t)>W-4:
      t=t[:W-6]+".."
     print(str(i+1)+". "+t)
   print("-"*W)
   print("1-9:sel +:new D:del")
   print("R:ren Q:quit")
  else:
   n=N[a]
   hd(n[0],a,len(N))
   print(" "+str(len(n[1]))+" lines")
   print("-"*W)
   if not n[1]:print(" (empty)")
   else:
    for i in range(len(n[1])):
     print(str(i+1)+". "+n[1][i])
   print("-"*W)
   print("+:add D:del E:edt")
   print("C:clr N:nts Q:quit")
  c=input("> ").lower()
  if c=="q":
   sv(N,a)
   print("Saved!");break
  elif md==0:
   if c=="+":
    t=input("Title:")
    if t:
     N.append([t,[]])
     a=len(N)-1;sv(N,a)
   elif c=="d" and N:
    if input("Del?y/n:").lower()=="y":
     N.pop(a)
     if a>=len(N):
      a=max(0,len(N)-1)
     sv(N,a)
   elif c=="r" and N:
    t=input("Name:")
    if t:N[a][0]=t;sv(N,a)
   elif c and c in "123456789" and N:
    x=int(c)-1
    if x<len(N):a=x;md=1
  else:
   if c=="+":
    l=input("(empty=done):")
    while l!="":
     N[a][1].append(l)
     l=input(":")
    sv(N,a)
   elif c=="d" and N[a][1]:
    x=input("Line#:")
    if x and x in "123456789":
     x=int(x)-1
     if x<len(N[a][1]):
      N[a][1].pop(x)
      sv(N,a)
   elif c=="e" and N[a][1]:
    x=input("Line#:")
    if x and x in "123456789":
     x=int(x)-1
     if x<len(N[a][1]):
      t=input("New:")
      if t:
       N[a][1][x]=t
       sv(N,a)
   elif c=="c":
    if input("Clr?y/n:").lower()=="y":
     N[a][1]=[];sv(N,a)
   elif c in ("n","l"):md=0
except KeyboardInterrupt:
 sv(N,a);print("Saved!")
