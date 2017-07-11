import os
from unittest import TestCase
import turbinelearn as tblearn

class TestLearning(TestCase):

    def setUp(self):
        self.fname = 'data/turbin_data.csv'
        self.data = tblearn.load_data(self.fname)

    def preprocess(self):
        self.data = tblearn.preprocess_data(self.data)

    def test_outlier(self):
        self.assertNotIn('OUTLIER', self.data)
        self.preprocess()
        tblearn.detect_outliers(self.data)
        self.assertIn('OUTLIER', self.data)

    def test_pca(self):
        X_1, X_2, y = tblearn.pca(self.fname, limits=tblearn.LIMITS)
        self.assertEqual(1489, len(X_1))
        self.assertEqual(len(X_1), len(X_2))
        self.assertEqual(len(X_1), len(y))

    def test_simple(self):
        train = tblearn.train_and_evaluate_single_file
        data, training_data, test_data, reg_mod = train(self.fname, degree=3)
        poly = tblearn.generate_polynomial(reg_mod, 3)
        self.assertTrue(poly)