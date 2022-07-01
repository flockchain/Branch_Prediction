from TwoBitLocalPredictor import *
from TwoLevelGlobalPredictor import *
from GShare import *
from Tournament import *

with open("trace.txt") as file_in:
    branches_txt = []
    for line in file_in:
        branches_txt.append(line)
with open("trace_gcc.txt") as file_in:
    branches_gcc = []
    for line in file_in:
        branches_gcc.append(line)
with open("trace_jpeg.txt") as file_in:
    branches_jpeg = []
    for line in file_in:
        branches_jpeg.append(line)
with open("trace_perl.txt") as file_in:
    branches_perl = []
    for line in file_in:
        branches_perl.append(line)


rv_global_txt = predict_global(branches_txt, "00")
prediction_accuracy = rv_global_txt.correct_predicts / (len(branches_txt)/100)
print("\n\n\nThe Two Level Global Predictor needs ", rv_global_txt.time, " seconds for the trace.txt file")
print("The Prediction accuracy of the Two Level Global Predictor for the trace.txt is ", prediction_accuracy, "%")

rv_global_gcc = predict_global(branches_gcc, "00")
prediction_accuracy = rv_global_gcc.correct_predicts / (len(branches_gcc)/100)
print("\nThe Two Level Global Predictor needs ", rv_global_gcc.time, " seconds for the trace_gcc.txt file")
print("The Prediction accuracy of the Two Level Global Predictor for the trace_gcc.txt is ", prediction_accuracy, "%")

rv_global_jpeg = predict_global(branches_jpeg, "00")
prediction_accuracy = rv_global_jpeg.correct_predicts / (len(branches_jpeg)/100)
print("\nThe Two Level Global Predictor needs ", rv_global_jpeg.time, " seconds for the trace_jpeg.txt file")
print("The Prediction accuracy of the Two Level Global Predictor for the trace_jpeg.txt is ", prediction_accuracy, "%")

rv_global_perl = predict_global(branches_perl, "00")
prediction_accuracy = rv_global_perl.correct_predicts / (len(branches_perl)/100)
print("\nThe Two Level Global Predictor needs ", rv_global_perl.time, " seconds for the trace_perl.txt file")
print("The Prediction accuracy of the Two Level Global Predictor for the trace_perl.txt is ", prediction_accuracy, "%")


rv_GShare_txt = predict_GShare(branches_txt, "00")
prediction_accuracy = rv_GShare_txt.correct_predicts / (len(branches_txt)/100)
print("\n\n\nThe GShare Predictor needs ", rv_GShare_txt.time, " seconds for the trace.txt file")
print("The Prediction accuracy of the GShare Predictor for the trace.txt is ", prediction_accuracy, "%")

rv_GShare_gcc = predict_GShare(branches_gcc, "00")
prediction_accuracy = rv_GShare_gcc.correct_predicts / (len(branches_gcc)/100)
print("\nThe GShare Predictor needs ", rv_GShare_gcc.time, " seconds for the trace_gcc.txt file")
print("The Prediction accuracy of the GShare Predictor for the trace_gcc.txt is ", prediction_accuracy, "%")

rv_GShare_jpeg = predict_GShare(branches_jpeg, "00")
prediction_accuracy = rv_GShare_jpeg.correct_predicts / (len(branches_jpeg)/100)
print("\nThe GShare Predictor needs ", rv_GShare_jpeg.time, " seconds for the trace_jpeg.txt file")
print("The Prediction accuracy of the GShare Predictor for the trace_jpeg.txt is ", prediction_accuracy, "%")

rv_GShare_perl = predict_GShare(branches_perl, "00")
prediction_accuracy = rv_GShare_perl.correct_predicts / (len(branches_perl)/100)
print("\nThe GShare Predictor needs ", rv_GShare_perl.time, " seconds for the trace_perl.txt file")
print("The Prediction accuracy of the Two GShare Predictor for the trace_perl.txt is ", prediction_accuracy, "%")


#rv_tournament_txt = predict_tournament(branches_txt, "00")
#prediction_accuracy = rv_tournament_txt.correct_predicts / (len(branches_txt)/100)
#print("\n\n\nThe Tournament Predictor needs ", rv_tournament_txt.time, " seconds for the trace.txt file")
#print("The Prediction accuracy of the Tournament Predictor for the trace.txt is ", prediction_accuracy, "%")

rv_tournament_gcc = predict_tournament(branches_gcc, "00")
prediction_accuracy = rv_tournament_gcc.correct_predicts / (len(branches_gcc)/100)
print("\nThe Tournament Predictor needs ", rv_tournament_gcc.time, " seconds for the trace_gcc.txt file")
print("The Prediction accuracy of the Tournament Predictor for the trace_gcc.txt is ", prediction_accuracy, "%")

#rv_tournament_jpeg = predict_tournament(branches_jpeg, "00")
#prediction_accuracy = rv_tournament_jpeg.correct_predicts / (len(branches_jpeg)/100)
#print("\nThe Tournament Predictor needs ", rv_tournament_jpeg.time, " seconds for the trace_jpeg.txt file")
#print("The Prediction accuracy of the Tournament Predictor for the trace_jpeg.txt is ", prediction_accuracy, "%")

#rv_tournament_perl = predict_tournament(branches_perl, "00")
#prediction_accuracy = rv_tournament_perl.correct_predicts / (len(branches_perl)/100)
#print("\nThe Tournament Predictor needs ", rv_tournament_perl.time, " seconds for the trace_perl.txt file")
#print("The Prediction accuracy of the Tournament Predictor for the trace_perl.txt is ", prediction_accuracy, "%")


#rv_local_txt = predict_local(branches_txt, "00")
#prediction_accuracy = rv_local_txt.correct_predicts / (len(branches_txt)/100)
#print("\n\n\nThe Two Bit Local Predictor needs ", rv_local_txt.time, " seconds for the trace.txt file")
#print("The Prediction accuracy of the Two Bit Local Predictor for the trace.txt is ", prediction_accuracy, "%")

#rv_local_gcc = predict_local(branches_gcc, "00")
#prediction_accuracy = rv_local_gcc.correct_predicts / (len(branches_gcc)/100)
#print("\nThe Two Bit Local Predictor needs ", rv_local_gcc.time, " seconds for the trace_gcc.txt file")
#print("The Prediction accuracy of the Two Bit Local Predictor for the trace_gcc.txt is ", prediction_accuracy, "%")

#rv_local_jpeg = predict_local(branches_jpeg, "00")
#prediction_accuracy = rv_local_jpeg.correct_predicts / (len(branches_jpeg)/100)
#print("\nThe Two Bit Local Predictor needs ", rv_local_jpeg.time, " seconds for the trace_jpeg.txt file")
#print("The Prediction accuracy of the Two Bit Local Predictor for the trace_jpeg.txt is ", prediction_accuracy, "%")

#rv_local_perl = predict_local(branches_perl, "00")
#prediction_accuracy = rv_local_perl.correct_predicts / (len(branches_perl)/100)
#print("\nThe Two Bit Local Predictor needs ", rv_local_perl.time, " seconds for the trace_perl.txt file")
#print("The Prediction accuracy of the Two Bit Local Predictor for the trace_perl.txt is ", prediction_accuracy, "%")


#rv_local_ten_bits_txt = predict_local_ten_bits(branches_txt, "00")
#prediction_accuracy = rv_local_ten_bits_txt.correct_predicts / (len(branches_txt)/100)
#print("\n\n\nThe Two Bit Local Predictor with ten bit addresses needs ", rv_local_ten_bits_txt.time, " seconds for the trace.txt file")
#print("The Prediction accuracy of the Two Bit Local Predictor with ten bit addresses for the trace.txt is ", prediction_accuracy, "%")

#rv_local_ten_bits_gcc = predict_local_ten_bits(branches_gcc, "00")
#prediction_accuracy = rv_local_ten_bits_gcc.correct_predicts / (len(branches_gcc)/100)
#print("\nThe Two Bit Local Predictor with ten bit addresses needs ", rv_local_ten_bits_gcc.time, " seconds for the trace_gcc.txt file")
#print("The Prediction accuracy of the Two Bit Local Predictor with ten bit addresses for the trace_gcc.txt is ", prediction_accuracy, "%")

#rv_local_ten_bits_jpeg = predict_local(branches_jpeg, "00")
#prediction_accuracy = rv_local_ten_bits_jpeg.correct_predicts / (len(branches_jpeg)/100)
#print("\nThe Two Bit Local Predictor with ten bit addresses needs ", rv_local_ten_bits_jpeg.time, " seconds for the trace_jpeg.txt file")
#print("The Prediction accuracy of the Two Bit Local Predictor with ten bit addresses for the trace_jpeg.txt is ", prediction_accuracy, "%")

#rv_local_ten_bits_perl = predict_local(branches_perl, "00")
#prediction_accuracy = rv_local_ten_bits_perl.correct_predicts / (len(branches_perl)/100)
#print("\nThe Two Bit Local Predictor with ten bit addresses needs ", rv_local_ten_bits_perl.time, " seconds for the trace_perl.txt file")
#print("The Prediction accuracy of the Two Bit Local Predictor with ten bit addresses for the trace_perl.txt is ", prediction_accuracy, "%")
