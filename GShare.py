import time
from TwoLevelGlobalPredictor import ReturnValues, convert_string_to_int, convert_int_to_string, push_on_ght


def predict_GShare(branch_list, start_state):
    start_time = time.time()
    correctPredicts = 0
    falsePredicts = 0
    list_length = len(branch_list)
    branch_count = 0
    ght = []
    ght_index = 0
    for x in range(16):
        ght.append(start_state)
    for x in range(list_length):
        actualBranch = branch_list[branch_count][0:8]
        actualPrediction = branch_list[branch_count][9:10]
        ght_index_string = convert_int_to_string(ght_index)
        ght_index_string = push_on_ght(ght_index_string, actualPrediction)
        ght_index = convert_string_to_int(ght_index_string)
        ght_index = xor_operation(ght_index, actualBranch)
        state_string = ght[ght_index]
        if state_string == '00':
            if actualPrediction == '0':
                correctPredicts += 1
            else:
                falsePredicts += 1
                ght[ght_index] = "01"
        elif state_string == '01':
            if actualPrediction == '0':
                correctPredicts += 1
                ght[ght_index] = "00"
            else:
                falsePredicts += 1
                ght[ght_index] = "10"
        elif state_string == '10':
            if actualPrediction == '1':
                correctPredicts += 1
                ght[ght_index] = "11"
            else:
                falsePredicts += 1
                ght[ght_index] = "01"
        elif state_string == '11':
            if actualPrediction == '1':
                correctPredicts += 1
            else:
                falsePredicts += 1
                ght[ght_index] = "10"
        branch_count += 1
    end_time = time.time()
    time_elapsed = (end_time - start_time)
    rt_GShare = ReturnValues(correctPredicts, falsePredicts, time_elapsed)
    return rt_GShare


def hex_to_binary(hex_number: str, num_digits: int = 4) -> str:
    return str(bin(int(hex_number, 16)))[2:].zfill(num_digits)


def xor_operation(ght_index, address_string):
    letter_to_convert = address_string[-1]
    letter_binary = hex_to_binary(letter_to_convert, 4)
    letter_int = int(letter_binary, 2)
    ght_binary_number = ght_index ^ letter_int
    return ght_binary_number
