import os
from mlflow import log_metric, log_param, log_artifact

def bar(p1) :
    # Log a parameter (key-value pair)
    log_param("param1", p1)

    # Log a metric; metrics can be updated throughout the run
    log_metric("foo", 1)
    log_metric("foo", 2)
    log_metric("foo", 3)

    # Log an artifact (output file)
    with open("output.txt", "w") as f:
        f.write("Hello world!")
    log_artifact("output.txt")
