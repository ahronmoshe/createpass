import random
def createpass():
     rand=random.randint(1,4)
     if rand==1:
          p=random.choice('qazwsxedcrfvtgbyhnujmikolp');
     elif rand==2:
          p=random.choice('QAZWSXEDCRFVTGBYHNUJMIKOLP');
     elif rand==3:
          p=random.choice('1234567890');
     else:
          p=random.choice('`~!@#$%^&*()_+=-][{}|\\\'\"?.><,*')
     return p

c=''
for i in range(0,8):
     c+=createpass();     
print c;

