import time
from TwoLevelGlobalPredictor import ReturnValues, GlobalPredictor
from TwoBitLocalPredictor import LocalPredictor


def predict_tournament(branch_list, start_state):
    start_time = time.time()
    decision_state = start_state
    correct_predicts = 0
    false_predicts = 0
    branch_count = 0
    lp = LocalPredictor()
    gp = GlobalPredictor()
    list_length = len(branch_list)
    for x in range(list_length):
        actualBranch = branch_list[branch_count][0:8]
        actualPrediction = branch_list[branch_count][9:10]
        local_prediction = lp.predict_local_once(actualBranch, actualPrediction)
        global_prediction = gp.predict_global_once(actualPrediction)
        if decision_state == '0':
            if local_prediction == actualPrediction:
                correct_predicts += 1
            elif global_prediction == actualPrediction:
                false_predicts += 1
                decision_state = "1"
            else:
                false_predicts += 1
        else:
            if global_prediction == actualPrediction:
                correct_predicts += 1
            elif local_prediction == actualPrediction:
                false_predicts += 1
                decision_state = "0"
            else:
                false_predicts += 1
        branch_count += 1
    end_time = time.time()
    time_elapsed = (end_time - start_time)
    rt_tournament = ReturnValues(correct_predicts, false_predicts, time_elapsed)
    return rt_tournament
