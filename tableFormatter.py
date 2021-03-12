import json
import os
import sys


class BestsFormatter:
    def __init__(self, metricsList, compOrder):
        # metrics list: names of metrics. 
        # compOrder: boolean list for metric sorting. True: higher is better. False: lower is better
        self.bests = {}
        self.secondBests = {}
        self.compOrderDict = {}

        for index, metricName in enumerate(metricsList):
            self.bests[metricName] = {}
            self.bests[metricName]["value"] = None
            self.bests[metricName]["methodName"] = ""

            self.secondBests[metricName] = {}
            self.secondBests[metricName]["value"] = None
            self.secondBests[metricName]["methodName"] = ""

            self.compOrderDict[metricName] = compOrder[index]

    def updateBests(self, metricName, value, methodName):
        
        if self.compOrderDict[metricName]:
            # ascending
            if self.bests[metricName]["value"] is None or value > self.bests[metricName]["value"]:
                # new first place. demote old first place and put in second place. store new best place
                self.secondBests[metricName]["value"] = self.bests[metricName]["value"]
                self.secondBests[metricName]["methodName"] = self.bests[metricName]["methodName"]
                self.bests[metricName]["value"] = value
                self.bests[metricName]["methodName"] = methodName
            else:
                # not better than first place.
                if self.secondBests[metricName]["value"] is None or value > self.secondBests[metricName]["value"]:
                    # new second place. store new second place
                    self.secondBests[metricName]["value"] = value
                    self.secondBests[metricName]["methodName"] = methodName

        else:
            #other way around. descending
            if self.bests[metricName]["value"] is None or value < self.bests[metricName]["value"]:
                # new first place. demote old first place and put in second place. store new best place
                self.secondBests[metricName]["value"] = self.bests[metricName]["value"]
                self.secondBests[metricName]["methodName"] = self.bests[metricName]["methodName"]
                self.bests[metricName]["value"] = value
                self.bests[metricName]["methodName"] = methodName
            else:
                # not better than first place.
                if self.secondBests[metricName]["value"] is None or value < self.secondBests[metricName]["value"]:
                    # new second place. store new second place
                    self.secondBests[metricName]["value"] = value
                    self.secondBests[metricName]["methodName"] = methodName
    
    def getString(self, valueString, metricName, methodName):
        if self.bests[metricName]["methodName"] == methodName:
            return "\\textbf{" + valueString + "}"
        elif self.secondBests[metricName]["methodName"] == methodName:
            return "\\underline{" + valueString + "}"
        else:
            return valueString
