import random
import math
class Shuffle:
    @staticmethod
    def get_shuffled_matris(num_1:int,num_2:int,list_length:int):
        number_list = [num_1 if _ >= list_length//2 else num_2 for _ in range(list_length)]
        matris = list()

        num_of_start = 0
        num_of_end = list_length - 1
        for num in range(list_length):
            temp = number_list[num]
            random_num = random.randint(num_of_start,num_of_end)
            number_list[num] = number_list[random_num]
            number_list[random_num] = temp
            num_of_start += 1

        matris_range = int(math.sqrt(list_length))
        index = 0
        for i in range(matris_range):
            row = list()
            for j in range(matris_range):
                row.append(number_list[index])
                index += 1
            matris.append(row)
        return matris