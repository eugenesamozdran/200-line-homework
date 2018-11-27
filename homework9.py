def tag(name):
    def decor(func):
        def wrap(text):
            if name:
                name1 = name.lower()
                print("<{0}>{1}</{0}>".format(name1, func(text)))
            return func(text)
        return wrap
    return decor

@tag("SPAN")
def foo(text):
    try:
        return text.upper()
    except AttributeError:
        print("Please use strings as foo function arguments only")
        raise

foo([1])
