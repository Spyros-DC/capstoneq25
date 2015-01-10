"""
Provided code for Question 25 on the Capstone Exam
"""

import urllib2
import q25a
import time        
##########################################################
# Code for loading graphs


def load_graph(graph_url):
    """
    Function that loads a graph given the URL
    for a text representation of the graph
    
    Returns a dictionary that models a graph
    """
    graph_file = urllib2.urlopen(graph_url)
    graph_text = graph_file.read()
    graph_lines = graph_text.split('\n')
    graph_lines = graph_lines[ : -1]
    
    print "Loaded graph with", len(graph_lines), "nodes"
    
    answer_graph = {}
    for line in graph_lines:
        neighbors = line.split(' ')
        node = int(neighbors[0])
        answer_graph[node] = set([])
        for neighbor in neighbors[1 : -1]:
            answer_graph[node].add(int(neighbor))

    return answer_graph



def run_example():
    """
    Generate example graphs
    """

    GRAPH1 = {1 : set([]), 2 : set([3, 7]), 3 : set([2, 4]), 4 : set([3, 5]),
              5 : set([4, 6]), 6 : set([5, 7]), 7 : set([2, 6])}
    GRAPH2 = {1 : set([2, 3, 4, 5, 6, 7]), 2 : set([1]), 3 : set([1]),
              4 : set([1]), 5 : set([1]), 6 : set([1]), 7 : set([1])}
    
    # Example graphs stored on Google (Storage)
    GRAPH3_URL = "http://storage.googleapis.com/codeskulptor-assets/foc_assets/graph3.txt"
    GRAPH4_URL = "http://storage.googleapis.com/codeskulptor-assets/foc_assets/graph4.txt"
    GRAPH5_URL = "http://storage.googleapis.com/codeskulptor-assets/foc_assets/graph5.txt"

    # Example graphs stored on Coursera (AWS) if Google Storage is inaccessible
    #GRAPH3_URL = "https://d396qusza40orc.cloudfront.net/foccapstone/exam_code/graph3.txt"
    #GRAPH4_URL = "https://d396qusza40orc.cloudfront.net/foccapstone/exam_code/graph4.txt"
    #GRAPH5_URL = "https://d396qusza40orc.cloudfront.net/foccapstone/exam_code/graph5.txt"
    
    GRAPH3 = load_graph(GRAPH3_URL)
    GRAPH4 = load_graph(GRAPH4_URL)
    GRAPH5 = load_graph(GRAPH5_URL)

    # The number of nodes in the sets returned by Mystery for GRAPH3 and GRAPH4
    # are respectively, 6 and 9.
    start_time = time.time()
    print(q25a.mystery(GRAPH3))
    print(q25a.mystery(GRAPH4))
    print(q25a.mystery(GRAPH5))
    elapsed_time = time.time() - start_time
    print(elapsed_time)
run_example()
            
    
    



    
    
    





