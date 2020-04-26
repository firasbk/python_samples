def say_hello(person):
    print("Hello " + person + " how you do")

name = input("enter your name: ")
say_hello(name)

def fahrtocels(fahr):
    cels = ( 5 * ( fahr - 32) ) / 9
    return cels

print(" 100 fahr in cels are: ", fahrtocels(100) )
print(" 100 fahr in Kalvin are: ", round ( fahrtocels(100) + 273.5 , 2) )
