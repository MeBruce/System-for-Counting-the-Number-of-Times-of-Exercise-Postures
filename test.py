# def count_ba_sequence(s):
#     count = 0
#     found_b = False

#     for char in s:
#         if char == 'a':
#             found_b = False
#         elif char == 'b' and found_b:
#             count += 1
#         elif char == 'b':
#             found_b = True

#     return count

# # ตัวอย่างการใช้งาน
# s = "bbbababa"
# result = count_ba_sequence(s)
# print("จำนวนลำดับ 'b a' ที่พบ:", result)


def count_squat_sequences(lines):
    count = 0
    found_squat_up = False

    for line in lines:
        line = line.strip()
        if found_squat_up:
            if line == 'squat down':
                count += 1
                found_squat_up = False
        elif line == 'squat up':
            found_squat_up = True

    return count

s = """
squat down
squat down
squat down
squat down
squat down
squat up
squat up
squat up
squat down
squat down
squat down
squat down
squat down
squat down
squat down
squat down
squat down
squat down
squat up
squat up
squat up
squat up
squat up
squat up
squat up
squat down
squat up"""

lines = s.strip().split('\n')
result = count_squat_sequences(lines)
print("จำนวนลำดับ 'squat up, squat down, squat up' ที่พบ:", result)





# def count_squat_sequences(s):
#     count = 0
#     found_squat_down = False

#     for word in s.split(','):
#         if word.strip() == 'squat down':
#             found_squat_down = True
#         elif word.strip() == 'squat up' and found_squat_down:
#             count += 1
#             found_squat_down = False

#     return count

# # ตัวอย่างการใช้งาน
# s = "squat down,squat down,squat down,squat up,squat down,squat up,squat down"
# result = count_squat_sequences(s)
# print("จำนวนลำดับ 'squat down, squat up' ที่พบ:", result)
