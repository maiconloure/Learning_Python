def outer():
    x = 'local'

    def inner():
        nonlocal x
        x = 'nonlocal'
        print("inner: ", x)

    print('outer before inner: ', x)
    inner()
    print('outer after inner: ', x)


outer()

