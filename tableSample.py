import json
import os
import sys
import tableFormatter as tF

####### Dummy data ########
storedResults = {}
storedResults["our_method_the_best"] = {}
storedResults["our_method_the_best"]["TP"] = 1337
storedResults["our_method_the_best"]["FP"] = 42
storedResults["our_method_the_best"]["TS"] = 13
storedResults["our_method_the_best"]["MT"] = 400
storedResults["our_method_the_best"]["averageDistance"] = 32.5


storedResults["the_method_we_hate"] = {}
storedResults["the_method_we_hate"]["TP"] = 1336
storedResults["the_method_we_hate"]["FP"] = 43
storedResults["the_method_we_hate"]["TS"] = 12
storedResults["the_method_we_hate"]["MT"] = 800
storedResults["the_method_we_hate"]["averageDistance"] = 77


storedResults["scape_goat"] = {}
storedResults["scape_goat"]["TP"] = 300
storedResults["scape_goat"]["FP"] = 3000
storedResults["scape_goat"]["TS"] = 34
storedResults["scape_goat"]["MT"] = 5500
storedResults["scape_goat"]["averageDistance"] = 1000

storedResults["the_OG"] = {}
storedResults["the_OG"]["TP"] = 1000
storedResults["the_OG"]["FP"] = 60
storedResults["the_OG"]["TS"] = 50
storedResults["the_OG"]["MT"] = 1000
storedResults["the_OG"]["averageDistance"] = 100

storedResults["the_OG"] = {}
storedResults["the_OG"]["TP"] = 1005
storedResults["the_OG"]["FP"] = 70
storedResults["the_OG"]["TS"] = 36
storedResults["the_OG"]["MT"] = 1200
storedResults["the_OG"]["averageDistance"] = 70

storedResults["here_for_show"] = {}
storedResults["here_for_show"]["TP"] = 1010
storedResults["here_for_show"]["FP"] = 250
storedResults["here_for_show"]["TS"] = 300
storedResults["here_for_show"]["MT"] = 1500
storedResults["here_for_show"]["averageDistance"] = 60
####### Dummy data ########


if __name__ == '__main__':
    

    methodNames = ["our_method_the_best", "the_method_we_hate", "scape_goat", "the_OG", "here_for_show"]
    methodPrettyNames = ["Our Method", "Second Best Method", "All we have is Hope", "CNN v1.0", "Old SOTA"]

    bestsFormatter = tF.BestsFormatter(["TP", "FP", "TS", "MT", "averageDistance"], compOrder = [True, False, False, False, False])
    
    # loop once through method results to get best indices.
    for methodNameIndex, methodName in enumerate(methodNames):

        methodResults = storedResults[methodName]

        bestsFormatter.updateBests("TP", methodResults["TP"], methodName)
        bestsFormatter.updateBests("FP", methodResults["FP"], methodName)
        bestsFormatter.updateBests("TS", methodResults["TS"], methodName)
        bestsFormatter.updateBests("MT", methodResults["MT"], methodName)
        bestsFormatter.updateBests("averageDistance", methodResults["averageDistance"], methodName)


    # loop to build table string. 
    overallString = ""
    for methodNameIndex, methodName in enumerate(methodNames):
        lineString = methodPrettyNames[methodNameIndex]

        actorIndex = 0
        results = storedResults[methodName]

        TPString = bestsFormatter.getString("%.3f" % results["TP"], "TP", methodName)
        FPString = bestsFormatter.getString("%.3f" % results["FP"], "FP", methodName)
        MTString = bestsFormatter.getString("%.3f" % results["MT"], "MT", methodName)
        TSString = bestsFormatter.getString("%.3f" % results["TS"], "TS", methodName)
        averageDistanceString = bestsFormatter.getString("%.1f" % (results["averageDistance"]), "averageDistance", methodName)


        lineString += " & " + TPString + " & " + MTString + " & " + FPString+ " & " + TSString + " & " + averageDistanceString

        overallString += lineString + " \\\\" + "\n" + "\\hline" + "\n" 

    print(overallString)
