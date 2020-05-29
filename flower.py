### -------------------------------------------------------------------------------------------------------------------
### i think this was for a puzzlehunt of some sort
### -------------------------------------------------------------------------------------------------------------------

import pprint


master = [[1,1,1,0,0,1,1],[1,1,1,0,1,0,0,1],[1,1,0,0,0,0],[1,0,1,1,1,1,0],[1,0,1,0,1,1,1],[1,0,1,1,0,1,0,1,0],[1,0]]
l = ['HE','DE','SU','LA','F','SH','K','A','GRA','BO','S','AQ','S','SE','C','S','E','TA','X','L','V','D','UR','E','E','AMI','C','Y','OB','UIT','U','C','L','H','P','R','L','DV','I','E','E','R','L','K','CR','L','A','E','A','A','E','A','R','S','A','I','ESM','LIS','S','AT','N','LE','AZ','U','IN','M','D','M','B','CT','I','IG','TZ','EN','E','H','IN','E','S','Y','E','E','E','A','UP','AN','S','ED','N','S']
n = 90

pluckornot = master[6]
plucked = [0]*n
print(plucked)

def allplucked(plucked):
  for x in plucked:
    if(x==0):
      return False
  return True

inc = True
i = 0
j = -1
k = -1
m = -1
o = 0
while(not allplucked(plucked)):
  if(plucked[i] == 0 and i != m):
    k = (k+1) % len(pluckornot)
    m = i
    o = 0
    if(pluckornot[k] == 1):
      print("plucked:" + str(i))
      j = i
      plucked[i] = 1

  if(i == n-1):
    inc = False
  if(i == 0):
    inc = True

  if(inc):
    i += 1
  else:
    i -= 1


  o += 1
  if(o>3*n):
    break

pprint.pprint(plucked)
for i in range(len(plucked)):
  if(plucked[i] == 0):
    print("the answer is " + str(i))
    print(l[i])
print("lol then answer is " + str(j))
print(l[j])

