


def main():
    n = int(input('请输入正整数'))
    for i in range(2, n):
        if n % i == 0:
            print('%d 不是一个素数.' % n)
            break
    else:
        print('%d 是一个素数' % n)

if __name__ == '__main__':
    main() 