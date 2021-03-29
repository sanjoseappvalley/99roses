import unittest
from ninetynineroses import verse, sing
from textwrap import dedent


class RosesTest(unittest.TestCase):

    maxDiff = None

    def test_the_first_verse(self):
        expected = (
            '99 roses in me, '
            '99 roses.\n'
            'I take one rose and give it to you, '
            "98 roses left.\n"
        )
        self.assertEqual(verse(99), expected)

    def test_another_verse(self):
        expected = (
            '56 roses in me, '
            '56 roses.\n'
            'I take one rose and give it to you, '
            '55 roses left.\n'
        )
        self.assertEqual(verse(56), expected)

    def test_verse_2(self):
        expected = (
            '2 roses in me, '
            '2 roses.\n'
            'I take one rose and give it to you, '
            '1 rose left.\n'
        )
        self.assertEqual(verse(2), expected)

    def test_verse_1(self):
        expected = (
            '1 rose in me, '
            '1 rose.\n'
            'I take one rose and give it to you, '
            'no more rose left.\n'
        )
        self.assertEqual(verse(1), expected)

    def test_verse_0(self):
        expected = (
            'No more rose in me, '
            'no more rose.\n'
            'Go to the store and buy more roses, '
            '99 roses left.\n'
        )
        self.assertEqual(verse(0), expected)

    def test_sing_9_verse(self):
        expected = dedent(
            """
            99 roses in me, 99 roses.
            I take one rose and give it to you, 98 roses left.

            98 roses in me, 98 roses.
            I take one rose and give it to you, 97 roses left.

            97 roses in me, 97 roses.
            I take one rose and give it to you, 96 roses left.

            96 roses in me, 96 roses.
            I take one rose and give it to you, 95 roses left.

            95 roses in me, 95 roses.
            I take one rose and give it to you, 94 roses left.

            94 roses in me, 94 roses.
            I take one rose and give it to you, 93 roses left.

            93 roses in me, 93 roses.
            I take one rose and give it to you, 92 roses left.

            92 roses in me, 92 roses.
            I take one rose and give it to you, 91 roses left.

            91 roses in me, 91 roses.
            I take one rose and give it to you, 90 roses left.
            """
        ).lstrip()
        self.assertEqual(sing(9), expected)


if __name__ == "__main__":
    unittest.main()
