def func(a, b):
    
    if len(a) and len(b) == 10:
        x = 0
        for i in range(10):
            if a[i] == b[i]:
                x+=10
        print(x)
    else:
        print('Длина строк не 10')

func('asdfghjklo', 'qseftgjukl')
func('helloworld', 'helloworld')