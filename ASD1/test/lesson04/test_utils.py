from unittest import TestCase

from ASD1.test.lesson04.utils import is_brackets_balanced, is_brackets_balanced_extended, calc_postfix_expression
from ASD1.test.lesson04.stack import Stack

class Test(TestCase):
    def test_is_brackets_balanced(self):
        self.assertTrue(is_brackets_balanced('((()))()'))
        self.assertFalse(is_brackets_balanced('()((())))'))
        self.assertTrue(is_brackets_balanced('((())())'))
        self.assertTrue(is_brackets_balanced("()"))
        self.assertTrue(is_brackets_balanced("(((())))"))
        self.assertTrue(is_brackets_balanced("()()()()()"))
        self.assertFalse(is_brackets_balanced(")()()("))
        self.assertFalse(is_brackets_balanced("())("))
        self.assertFalse(is_brackets_balanced("))(("))
        self.assertFalse(is_brackets_balanced("((())"))

    def test_is_brackets_balanced_extended(self):
        self.assertTrue(is_brackets_balanced_extended('((()))()'))
        self.assertFalse(is_brackets_balanced_extended('()((())))'))
        self.assertTrue(is_brackets_balanced_extended('((())())'))
        self.assertTrue(is_brackets_balanced_extended("()"))
        self.assertTrue(is_brackets_balanced_extended("(((())))"))
        self.assertTrue(is_brackets_balanced_extended("()()()()()"))
        self.assertFalse(is_brackets_balanced_extended(")()()("))
        self.assertFalse(is_brackets_balanced_extended("())("))
        self.assertFalse(is_brackets_balanced_extended("))(("))
        self.assertFalse(is_brackets_balanced_extended("((())"))

        self.assertTrue(is_brackets_balanced_extended("({[]})"))
        self.assertTrue(is_brackets_balanced_extended("(){}[][]{}()"))
        self.assertFalse(is_brackets_balanced_extended("({)}"))
        self.assertFalse(is_brackets_balanced_extended("}{"))
        self.assertFalse(is_brackets_balanced_extended("((}}"))
        self.assertFalse(is_brackets_balanced_extended("{}[]]"))
        self.assertFalse(is_brackets_balanced_extended("[[{}(}]]"))

        # assertEquals(9, utils.postfixExpressionCalculate("1 2 + 3 *"));
        #         int res = utils.postfixExpressionCalculate("8 2 + 5 * 9 + =");
        #         assertEquals(59, res);
        #         assertEquals(2, utils.postfixExpressionCalculate("3 8 - 6 + 2 * 44 / ="));

    def test_calc_postfix_expression(self):
        self.assertEqual(9, calc_postfix_expression('1 2 + 3 *'))
        self.assertEqual(59, calc_postfix_expression('8 2 + 5 * 9 + ='))
        self.assertEqual(2, calc_postfix_expression('3 8 - 6 + 2 * 44 / ='))