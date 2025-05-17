def main():
    print("Hello Worl")

    list = [1,2,3,4,(1,2), "A", 5]
    repeat(list)

  
def repeat(vals)->int:
    for i in vals:
        print(i)

main()  
