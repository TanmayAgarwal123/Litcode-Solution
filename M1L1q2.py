def find_max_length(nums):
    max_length = 0
    count = 0
    count_dict = {0: -1}

    for i in range(len(nums)):
        if nums[i] == 0:
            count -= 1
        else:
            count += 1

        if count in count_dict:
            max_length = max(max_length, i - count_dict[count])
        else:
            count_dict[count] = i

    return max_length

if __name__ == "__main__":
    nums = []
    continue_input = 'y'

    while continue_input != 'n':
        num = int(input())
        nums.append(num)
        continue_input = input()

    result = find_max_length(nums)
    print(result)
