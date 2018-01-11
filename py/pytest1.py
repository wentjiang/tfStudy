print('out of function')


def say_hello(word,*persons):
    for person in persons:
        print(word, person)

def say_something(word,**somebody):
    for k,v in somebody.items():
        print(word,k,v)


if __name__ == '__main__':
    print('in name function')
