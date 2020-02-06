import unittest
from maths import max_c,min_c,sum_c,mean_c,variance_c,standard_deviation 
#from statistics import stdev,variance


#test cases check kartoy yetehey

class Util_math_test:
    def __init__(self,collection):
        self.collection = collection

    def test_max_c(self):
        self.assertEqual(max_c(self.collection),max(collection))
    
    def test_min_c(self):
        self.assertEqual(min_c(self.collection),min(collection))
    
    def test_sum_c(self):
        self.assertEqual(sum_c(self.collection),float(sum(collection)))
    
    def test_mean_c(self):
        self.assertEqual(mean_c(self.collection),float(mean(collection)))
    
    '''def test_variance_c(self):
        self.assertEqual(variance_c(self.collection),variance(collection))
    
    def test_standard_deviation(self):
        self.assertEqual(standard_deviation(self.collection),stdev(collection))
    '''

if __name__=='__main__':
    unittest.main()



