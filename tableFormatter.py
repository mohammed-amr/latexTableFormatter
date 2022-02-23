import json
import os
import sys

class ResultsStore():
    def __init__(self, exp_name, metrics_name):
        self.exp_name = exp_name
        self.metrics_name = metrics_name


        
        self.elem_metrics_list = []
        self.running_metrics = None
        self.running_count = 0

        self.final_computed_average = None

    def update_results(self, elem_metrics):
        """Updates running_metrics with incomming metrics while handling a running averaging."""

        self.elem_metrics_list.append(elem_metrics.copy())

        if self.running_metrics is None:
            self.running_metrics = elem_metrics.copy()
        else:
            for key in list(elem_metrics.keys()):
                self.running_metrics[key] = (self.running_metrics[key] * self.running_count + elem_metrics[key]) / (self.running_count + 1)

        self.running_count += 1

    def print_sheets_friendly(self, print_exp_name=True, include_metrics_names=False, running_metrics=True):
        """Pretty print for sheets copy/paste.
        
        include_names: print a row for metric names 
        """

        if print_exp_name:
            print(f"{self.exp_name}, {self.metrics_name}")

        if running_metrics:
            metrics_to_print = self.running_metrics
        else:
            metrics_to_print = self.final_metrics 

        metric_names_row = ""
        metrics_row = ""
        for k, v in metrics_to_print.items():
            metric_names_row += f"{k:8} "
            metric_string = f"{v:.4f},"
            metrics_row += f"{metric_string:8} "
        
        if include_metrics_names:
            print(metric_names_row)
        print(metrics_row)

    def pretty_print_results(self, print_exp_name=True, running_metrics=True):

        if running_metrics:
            metrics_to_print = self.running_metrics
        else:
            metrics_to_print = self.final_metrics 

        if print_exp_name:
            print(f"{self.exp_name}, {self.metrics_name}")
        for k, v in metrics_to_print.items():
            print(f"{k:8}: {v:.4f}")

    def compute_final_average(self):
        """Computes final a final average on the metrics element list using numpy.
        
        This should be more accurate than running metrics as it's a single average vs multiple 
        multiplications and divisions."""

        self.final_metrics = {}

        for key in list(self.running_metrics.keys()):
            values = []
            for element in self.elem_metrics_list:
                if torch.is_tensor(element[key]):
                    values.append(element[key].cpu().numpy())
                else:
                    values.append(element[key])

            mean_value = np.array(values).mean()
            self.final_metrics[key] = mean_value
