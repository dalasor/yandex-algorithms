"""
Вам даны три списка чисел. Найдите все числа, которые встречаются хотя бы в двух из трёх списков.

|-----------------------|
|--- time limit: 1 s ---|
|- memory limit: 64 Mb -|
|-----------------------|

"""


def req_nums_list(list1, list2, list3) -> list:
    set1, set2, set3 = set(list1), set(list2), set(list3)
    return list((set1 & set2) | (set1 & set3) | (set2 & set3))


n1 = int(input())
nums1 = list(map(int, input().split()))
n2 = int(input())
nums2 = list(map(int, input().split()))
n3 = int(input())
nums3 = list(map(int, input().split()))

# ans = nums1 & nums2
# merged12 = nums1.union(nums2)
# ans = ans.union(merged12 & nums3)

print(*sorted(req_nums_list(nums1, nums2, nums3)))


# Ниже решение без использования множеств, только списки, по эффективности почти одинаково

# ns, nums = [], []
# req_nums = []
# for _ in range(3):
#     _ = int(input())
#     s = list(set(map(int, input().split())))
#     ns.append(len(s))
#     nums.append(s)
#
# for i in range(ns[0]):
#     if nums[0][i] in nums[1]:
#         if nums[0][i] not in req_nums:
#             req_nums.append(nums[0][i])
#     elif nums[0][i] in nums[2]:
#         if nums[0][i] not in req_nums:
#             req_nums.append(nums[0][i])
#
# for i in range(ns[1]):
#     if nums[1][i] in nums[2]:
#         if nums[1][i] not in req_nums:
#             req_nums.append(nums[1][i])
#
# print(*sorted(req_nums))



