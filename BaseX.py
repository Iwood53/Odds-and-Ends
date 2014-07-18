import sys


def is_number(s):
    try:
        int(s)
        return True
    except ValueError:
        return False


def convert(base_10_int, conv_to_base):
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

    final_num_string = "".join(str(x) for x in final_num)
    return final_num_string


if len(sys.argv) == 3 and is_number(sys.argv[1]) and is_number(sys.argv[2]):
    print(convert(int(sys.argv[1]), int(sys.argv[2])))
else:
    print("Usage: BaseX.py <convert from base 10 num> <to base x>")






