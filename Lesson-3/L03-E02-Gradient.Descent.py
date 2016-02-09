import numpy
import pandas
import pandasql

def normalize_data (array):
    """
    This function is the key.!!! Otherwise the gradient descent would diverge !!
    """
    array_normalized = (array - array.mean())/array.std()
    return array_normalized

def compute_cost(features, values, theta):
    """
    Compute the cost of a list of parameters, theta, given a list of features 
    (input data points) and values (output data points).
    """
    m = len(values)
    sum_of_square_errors = numpy.square(numpy.dot(features, theta) - values).sum()
    cost = sum_of_square_errors / (2*m)

    return cost

def gradient_descent(features, values, theta, alpha, num_iterations):
    """
    Perform gradient descent given a data set with an arbitrary number of features.
    """

    # Write code here that performs num_iterations updates to the elements of theta.
    # times. Every time you compute the cost for a given list of thetas, append it 
    # to cost_history.
    # See the Instructor notes for hints. 
    
    cost_history = []
    m = float(len(values))
    n = float(len(features))
    for i in range(num_iterations):
        theta = theta + (alpha/m)*numpy.dot((values - numpy.dot(features,theta)),features)
        cost_history.append(compute_cost(features, values, theta))
    
    return theta, pandas.Series(cost_history) # leave this line for the grader

if __name__ == "__main__":
    df = pandas.read_csv("baseball_stats.csv")
    q_features = """ SELECT height, weight , avg
                     FROM df
                     WHERE height != ' ' and weight != ' '
                     LIMIT 10000;
    """
    q_values = """ SELECT HR
                   FROM df
                   WHERE height != ' ' and weight != ' '
                   LIMIT 10000;
    """  
    features = normalize_data(numpy.array(pandasql.sqldf(q_features,locals()),dtype = float))
    values = normalize_data(numpy.squeeze(numpy.array(pandasql.sqldf(q_values,locals()))))
    theta = [0.0]*features.shape[1]
    print gradient_descent(features, values, theta, 0.01, 1000)