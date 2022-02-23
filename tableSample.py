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
    
    method_names = {"our_method_the_best": "Our Method", "the_method_we_hate": "Second Best Method", "scape_goat": "All we have is Hope", "the_OG": "CNN v1.0", "here_for_show":"Old SOTA"}

    bests_formatter = BestsFormatter(["TP", "FP", "TS", "MT", "averageDistance"], comp_order = [True, False, False, False, False])
    
    # loop once through method results to get best indices.
    for method_name in list(method_names.keys()):

        method_results = stored_results[method_name]

        bests_formatter.update_ordering("TP", method_results["TP"], method_name)
        bests_formatter.update_ordering("FP", method_results["FP"], method_name)
        bests_formatter.update_ordering("TS", method_results["TS"], method_name)
        bests_formatter.update_ordering("MT", method_results["MT"], method_name)
        bests_formatter.update_ordering("averageDistance", method_results["averageDistance"], method_name)


    # loop to build table string. 
    overall_string = ""
    for method_name in list(method_names.keys()):
        line_string = method_names[method_name]

        actorIndex = 0
        results = stored_results[method_name]

        TP_string = bests_formatter.get_string("%.3f" % results["TP"], "TP", method_name)
        FP_string = bests_formatter.get_string("%.3f" % results["FP"], "FP", method_name)
        MT_string = bests_formatter.get_string("%.3f" % results["MT"], "MT", method_name)
        TS_string = bests_formatter.get_string("%.3f" % results["TS"], "TS", method_name)
        avg_distance_string = bests_formatter.get_string("%.1f" % (results["averageDistance"]), "averageDistance", method_name)


        line_string += " & " + TP_string + " & " + MT_string + " & " + FP_string+ " & " + TS_string + " & " + avg_distance_string

        overall_string += line_string + " \\\\" + "\n" + "\\hline" + "\n" 

    print(overall_string)
