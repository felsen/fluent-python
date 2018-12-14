"""
Basic decorator function for registration.
"""


registry = []


def register(func):
    print('running register {}'.format(func))
    registry.append(func)
    return func


@register
def f1():
    print('running function 1')


@register
def f2():
    print('running function 2')


def f3():
    print('running function 3')


def main():
    print('running main function')
    print('registry-- {}'.format(registry))
    f1()
    f2()
    f3()
    print('registry-- {}'.format(registry))


if __name__ == '__main__':
    main()

