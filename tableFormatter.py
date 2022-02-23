class BestsFormatter:
    '''From https://github.com/mohammed-amr/latexTableFormatter'''
    def __init__(self, metrics_list, comp_order):
        # metrics list: names of metrics. 
        # comp_order: boolean list for metric sorting. True: higher is better. False: lower is better
        self.bests = {}
        self.second_bests = {}
        self.comp_order_dict = {}

        for index, metric_name in enumerate(metrics_list):
            self.bests[metric_name] = {}
            self.bests[metric_name]["value"] = None
            self.bests[metric_name]["method_name"] = ""

            self.second_bests[metric_name] = {}
            self.second_bests[metric_name]["value"] = None
            self.second_bests[metric_name]["method_name"] = ""

            self.comp_order_dict[metric_name] = comp_order[index]

    def update_ordering(self, metric_name, value, method_name):
        
        if self.comp_order_dict[metric_name]:
            # ascending
            if self.bests[metric_name]["value"] is None or value > self.bests[metric_name]["value"]:
                # new first place. demote old first place and put in second place. store new best place
                self.second_bests[metric_name]["value"] = self.bests[metric_name]["value"]
                self.second_bests[metric_name]["method_name"] = self.bests[metric_name]["method_name"]
                self.bests[metric_name]["value"] = value
                self.bests[metric_name]["method_name"] = method_name
            else:
                # not better than first place.
                if self.second_bests[metric_name]["value"] is None or value > self.second_bests[metric_name]["value"]:
                    # new second place. store new second place
                    self.second_bests[metric_name]["value"] = value
                    self.second_bests[metric_name]["method_name"] = method_name

        else:
            #other way around. descending
            if self.bests[metric_name]["value"] is None or value < self.bests[metric_name]["value"]:
                # new first place. demote old first place and put in second place. store new best place
                self.second_bests[metric_name]["value"] = self.bests[metric_name]["value"]
                self.second_bests[metric_name]["method_name"] = self.bests[metric_name]["method_name"]
                self.bests[metric_name]["value"] = value
                self.bests[metric_name]["method_name"] = method_name
            else:
                # not better than first place.
                if self.second_bests[metric_name]["value"] is None or value < self.second_bests[metric_name]["value"]:
                    # new second place. store new second place
                    self.second_bests[metric_name]["value"] = value
                    self.second_bests[metric_name]["method_name"] = method_name
    
    def get_string(self, value_string, metric_name, method_name):
        if self.bests[metric_name]["method_name"] == method_name:
            return "\\textbf{" + value_string + "}"
        elif self.second_bests[metric_name]["method_name"] == method_name:
            return "\\underline{" + value_string + "}"
        else:
            return value_string
