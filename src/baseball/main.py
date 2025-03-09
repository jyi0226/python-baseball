import random

def check_valid_input():
    arr_list=list(input("숫자를 입력하세요: "))

    if len(arr_list)!=3:
        raise ValueError("3 자리 숫자를 입력하세요")
    for i in range(3):
                         if not arr_list[i].isdigit():
                             raise ValueError("정수를 입력하세요")

    if len(arr_list) != len(set(arr_list)):
        raise ValueError("중복된 숫자를 입력하였습니다")

    return [int(x) for x in arr_list]

def regame():
    val = input("게임을 새로 시작하려면 1, 종료하려면 2를 입력하세요.: ")
    if val in ["1","2"]:
        return int(val)
    else:
        raise ValueError("1혹은 2를 입력해주세요.")

def make_num():
    return random.sample(range(1,10),3)

def input_num():
    return check_valid_input()

def check(com, arr):
    """
    숫자 야구 게임의 결과를 계산하는 함수
    - 같은 위치에 같은 숫자가 있으면 스트라이크
    - 다른 위치에 같은 숫자가 있으면 볼
    """
    strikes=0
    balls=0

    for i in range(3):
        if arr[i] == com[i]:
            strikes += 1
        else:
            if arr[i] in com:
                balls += 1

    return strikes, balls

def game():
    com=make_num()
    
    while(1):
        arr=input_num()
        strikes, balls = check(com,arr)

        if strikes==0 and balls==0:
            print("낫싱")
        elif strikes==3:
            print("3스트라이크")
            print("3개의 숫자를 모두 맞히셨습니다! 게임 종료")
            break
        else:
            print(f"{balls}볼 {strikes}스트라이크")
        
def main():

    print("숫자 야구 게임을 시작합니다.")

    while True:
        try:
            game()
            choice = regame()
            if choice == 1:
                continue
            elif choice == 2:
                break
        except ValueError as e:
            print(e)
            raise
    
if __name__ == "__main__":
    main()
