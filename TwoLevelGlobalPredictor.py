import time


class ReturnValues:
    correct_predicts = 0
    false_predicts = 0
    time = 0

    def __init__(self, correct_predictions, false_predictions, the_time):
        self.correct_predicts = correct_predictions
        self.false_predicts = false_predictions
        self.time = the_time


def predict_global(branch_list, start_state):
    start_time = time.time()
    correctPredicts = 0
    falsePredicts = 0
    list_length = len(branch_list)
    prediction_count = 0
    ght = []
    ght_index = 0
    for x in range(16):
        ght.append(start_state)
    for x in range(list_length):
        actualPrediction = branch_list[prediction_count][9:10]
        ght_index_string = convert_int_to_string(ght_index)
        ght_index_string = push_on_ght(ght_index_string, actualPrediction)
        ght_index = convert_string_to_int(ght_index_string)
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
        prediction_count += 1
    end_time = time.time()
    time_elapsed = (end_time - start_time)
    rt_global = ReturnValues(correctPredicts, falsePredicts, time_elapsed)
    return rt_global


def convert_int_to_string(ght_index):
    match ght_index:
        case 0:
            return "0000"
        case 1:
            return "0001"
        case 2:
            return "0010"
        case 3:
            return "0011"
        case 4:
            return "0100"
        case 5:
            return "0101"
        case 6:
            return "0110"
        case 7:
            return "0111"
        case 8:
            return "1000"
        case 9:
            return "1001"
        case 10:
            return "1010"
        case 11:
            return "1011"
        case 12:
            return "1100"
        case 13:
            return "1101"
        case 14:
            return "1110"
        case 15:
            return "1111"


def push_on_ght(ght_string, new_prediction):
    ght_string = ght_string[0: 3:] + ght_string[3 + 1::]
    ght_string = ght_string[:0] + new_prediction + ght_string[0:]
    return ght_string


def convert_string_to_int(ght_index):
    ght_index_int = 0
    multiplication_count = 1
    for element in ght_index:
        if element == '1':
            match multiplication_count:
                case 1:
                    ght_index_int += 8
                case 2:
                    ght_index_int += 4
                case 3:
                    ght_index_int += 2
                case 4:
                    ght_index_int += 1
        multiplication_count += 1
    return ght_index_int


class GlobalPredictor:

    def __init__(self):
        self.ght = []
        self.ght_index = 0
        for x in range(16):
            self.ght.append("00")

    def predict_global_once(self, prediction):
        actualPrediction = prediction
        ght_index_string = convert_int_to_string(self.ght_index)
        ght_index_string = push_on_ght(ght_index_string, actualPrediction)
        self.ght_index = convert_string_to_int(ght_index_string)
        state_string = self.ght[self.ght_index]
        if state_string == '00':
            if actualPrediction == '0':
                return "1"
            else:
                self.ght[self.ght_index] = "01"
                return "0"
        elif state_string == '01':
            if actualPrediction == '0':
                self.ght[self.ght_index] = "00"
                return "1"
            else:
                self.ght[self.ght_index] = "10"
                return "0"
        elif state_string == '10':
            if actualPrediction == '1':
                self.ght[self.ght_index] = "11"
                return "1"
            else:
                self.ght[self.ght_index] = "01"
                return "0"
        elif state_string == '11':
            if actualPrediction == '1':
                return "1"
            else:
                self.ght[self.ght_index] = "10"
                return "0"
