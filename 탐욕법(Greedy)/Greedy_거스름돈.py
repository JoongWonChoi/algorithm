##Greedy 거스름돈 문제###

def min_coin_count(value, coin_list):
    # 코드를 작성하세요.
    answer = 0
    left = value
    coin_list.sort(reverse=True)
    for coin in coin_list:
        answer += left // coin

        left = left % coin

    return answer
# 테스트
default_coin_list = [100, 500, 10, 50]
print(min_coin_count(1440, default_coin_list))
print(min_coin_count(1700, default_coin_list))
print(min_coin_count(23520, default_coin_list))
print(min_coin_count(32590, default_coin_list))