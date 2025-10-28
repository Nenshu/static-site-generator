import unittest

from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)

    def test_italic(self):
        node = TextNode("This is an italic text node", TextType.ITALIC)
        node2 = TextNode("This is an italic text node", TextType.ITALIC)
        self.assertEqual(node, node2)

    def test_code(self):
        node = TextNode("This is code", TextType.CODE)
        node2 = TextNode("This is code", TextType.CODE)
        self.assertEqual(node, node2)

    def test_link(self):
        node = TextNode("this is a link", TextType.LINK)
        node2 = TextNode("this is a link", TextType.LINK)
        self.assertEqual(node, node2)

    def test_url(self):
        node = TextNode("this is an image", TextType.IMAGE)
        node2 = TextNode("this is an image", TextType.IMAGE)
        self.assertEqual(node, node2)

if __name__ == "__main__":
    unittest.main()
