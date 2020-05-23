#non local variable

def outer():
 x = 'local' #local to outer function
 def inner():
  nonlocal x #isnt the new variable just using the upper x (jumping and using another scope of its parent)
  #as long as ita not global the parent will givee it
  x = 'nonLocal'
  print("inner : ", x)

 inner() # inner function is called
 print("outer", x) # as the inner local change value of outer local x it aslo print the same

outer()
