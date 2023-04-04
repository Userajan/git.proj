###    main programme file written in module.py

#import module
#print(module.x)
#print(module.y)
#module.add(30,20)
#module.product(10,20)
             
             
             ######## module_Aliasing  :---

#import module as m 

# Here module_aliasing is origina module name and m is alias name
#we can access members by using alias name m

#m.add(10,20)
#m.product(10,20)
#print(m.x)
#print(m.y)


                    ######  from ....import :----

from module import x,add
print(x)
add(10,20)
add.product(10,20)
