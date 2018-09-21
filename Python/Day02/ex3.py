from random import randint

def main():
    result = randint(1, 6)
    count = 0
    while count < 3:
        guess = int(input('请输入数字:'))
        if guess < result:
            print('再大点.')
        elif guess > result:
            print('再小点.')
        else:
            print('恭喜你,猜对了.')
            break
        count += 1
    else:
        print('抱歉,你没有猜对.')
    

if __name__ == '__main__':
    main() 