#=============================================================================#
#                             Homework 4: yoursql                             #
#         SI 100B: Introduction to Information Science and Technology         #
#                     Spring 2020, ShanghaiTech University                    #
#                     Author: Diao Zihao <hi@ericdiao.com>                    #
#                         Last motified: 05/01/2020                           #
#=============================================================================#
# test.py - test your implementation.
# PLEASE NOTE: Teatcases here are different from those in the auto-grader. Only
# results of the testcases in the auto-grader will be considered valid and will
# count for your final score.

import unittest
import yoursql

# Feel Free to motify the testcases below to create your own testcases.




class TestBonus(unittest.TestCase):

    def setUp(self):
        self.q = {
            'select': ['testcases/student_gpa.gpa', 'testcases/student_gpa.id'],
            'from': ['testcases/student_name.csv', 'testcases/student_gpa.csv'],
            'where': [('testcases/student_gpa.id', 4, '>=')]
        }

    def testInit(self):
        table = yoursql.JoinQuery(self.q).as_table()
        print()
        table.export()

if __name__ == '__main__':
    unittest.main()
