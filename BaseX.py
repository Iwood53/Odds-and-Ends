import sys


def is_number(s):
    try:
        int(s)
        return True
    except ValueError:
        return False


def convert(base_10_int, conv_to_base):
    num_to_alpha = {10: 'A', 11: 'B', 12: 'C', 13: 'D', 14: 'E', 15: 'F', 16: 'G', 17: 'H', 18: 'I', 19: 'J'}
    num_to_alpha.update({20: 'K', 21: 'L', 22: 'M', 23: 'N', 24: 'O', 25: 'P', 26: 'Q', 27: 'R', 28: 'S', 29: 'T'})
    num_to_alpha.update({30: 'U', 31: 'V', 32: 'W', 33: 'X', 34: 'Y', 35: 'Z'})
    place_holder = [1]
    running_max = conv_to_base - 1

    while base_10_int > running_max:
        place_holder.append(place_holder[-1] * conv_to_base)
        running_max += place_holder[-1] * (conv_to_base - 1)

    place_holder.reverse()

    final_num = []
    running_count = 0
    max_places = conv_to_base - 1
    for place in place_holder:
        current_place = max_places
        will_continue = True
        while will_continue:
            if (place * current_place) + running_count <= base_10_int:
                final_num.append(current_place)
                running_count += place * current_place
                will_continue = False
            else:
                current_place -= 1
            if current_place == 0:
                final_num.append(0)
                will_continue = False

    for index, num in enumerate(final_num):
        if num > 9:
            print 'above 9'
            final_num[index] = num_to_alpha[num]
    final_num_string = "".join(str(x) for x in final_num)
    return final_num_string

if __name__ == "__main__":
    if len(sys.argv) == 3 and is_number(sys.argv[1]) and is_number(sys.argv[2]):
        print(convert(int(sys.argv[1]), int(sys.argv[2])))
    else:
        print("Usage: BaseX.py <convert from base 10 num> <to base x>")







