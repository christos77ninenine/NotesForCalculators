import ti_system as ts
K=["NTLD","N2LD","N3LD","N4LD","N5LD"]
W=21
D="-"*W
def sv(N,a):
 s=str(a)
 for n in N:
  s+="\n\n"+n[0]
  for l in n[1]:s+="\n"+l
 e=[ord(c) for c in s]
 for p in range(5):ts.store_list(K[p],e[p*999:p*999+999] or [0])
def ld():
 e=[]
 for k in K:
  try:
   c=ts.recall_list(k)
   if c!=[0]:e+=c
  except:pass
 if not e:return [],0
 try:
  s=""
  for v in e:
   if v!=int(v) or v<32 and v!=10:return
   s+=chr(int(v))
  e=0;b=s.split("\n\n");N=[]
  for t in b[1:]:
   l=t.split("\n");N.append([l[0],l[1:]])
  a=int(b[0])
  if 0<=a<max(1,len(N)):return N,a
 except:pass
def cl():print("\n"*11+"="*W)
def gi(p,n):
 x=input(p)
 if x and x in "123456789" and int(x)<=n:return int(x)-1
 return -1
def wr(p,s):
 m=W-len(p);o=[];c=""
 for w in s.split(" "):
  while len(w)>m:
   if c:o.append(c);c=""
   o.append(w[:m]);w=w[m:]
  if not c:c=w
  elif len(c)+1+len(w)<=m:c+=" "+w
  else:o.append(c);c=w
 o.append(c)
 for j in range(len(o)):
  print((p if j==0 else " "*len(p))+o[j])
r=ld()
if not r:
 cl();print(" DATA CORRUPTION\n DETECTED!\n"+D+"\n Format lists?\n (wipes all notes)")
 if input("y/n:").lower()=="y":
  for k in K:ts.store_list(k,[0])
  r=[],0
N,a=r or (None,0)
md=0
try:
 while N!=None:
  cl()
  if md==0:
   print(" "+(str(len(N))+" notes" if N else "Notes (empty)")+"\n"+D)
   if not N:print(" (none)")
   for i in range(len(N)):
    t=N[i][0]
    if len(t)>W-4:t=t[:W-6]+".."
    print(str(i+1)+". "+t)
   print(D+"\n1-9:sel +:new D:del\nR:ren Q:quit")
  else:
   n=N[a];L=n[1]
   h="("+str(a+1)+"/"+str(len(N))+")";t=n[0];m=W-len(h)-2
   if len(t)>m:t=t[:m-2]+".."
   print(" "+t+" "+h+"\n "+str(len(L))+" lines\n"+D)
   if not L:print(" (empty)")
   for i in range(len(L)):wr(str(i+1)+". ",L[i])
   print(D+"\n+:add D:del E:edt\nC:clr N:nts Q:quit")
  c=input("> ").lower()
  if c=="q":sv(N,a);print("Saved!");break
  elif md==0:
   if c=="+":
    t=input("Title:")
    if t:N.append([t,[]]);a=len(N)-1;sv(N,a)
   elif c=="d" and N:
    x=gi("Note#:",len(N))
    if x>=0:
     N.pop(x);a=min(a,max(0,len(N)-1));sv(N,a)
   elif c=="r" and N:
    t=input("Name:")
    if t:N[a][0]=t;sv(N,a)
   elif c and c in "123456789" and N and int(c)<=len(N):a=int(c)-1;md=1
  else:
   if c=="+":
    l=input("(empty=done):")
    while l:L.append(l);l=input(":")
    sv(N,a)
   elif c=="d" and L:
    x=gi("Line#:",len(L))
    if x>=0:L.pop(x);sv(N,a)
   elif c=="e" and L:
    x=gi("Line#:",len(L))
    if x>=0:
     t=input("New:")
     if t:L[x]=t;sv(N,a)
   elif c=="c":
    if input("Clr?y/n:").lower()=="y":L.clear();sv(N,a)
   elif c in "nl" and c:md=0
except KeyboardInterrupt:
 sv(N,a);print("Saved!")
