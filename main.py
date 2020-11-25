a = "9"*999
b = int(a)

fn_1 = 1
fn = 1
n =2

while fn < b:
   fn_1, fn = fn, fn + fn_1
   n +=1
   
print(fn/fn_1)