# http://simeonfranklin.com/blog/2012/jul/1/python-decorators-in-12-steps/

# example of something I've never encountered before...

def outer():
    x = 1
    y = 2.1
    def inner():
        print(x)
        print(x+y)
    inner()
    return inner

foo = outer()
print(foo.__closure__)

print(globals())
print(locals())

