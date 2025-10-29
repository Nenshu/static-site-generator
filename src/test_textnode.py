import unittest 
from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
    def test_eq_same_text_type_default_url(self):
        node = TextNode("same", TextType.BOLD)
        node2 = TextNode("same", TextType.BOLD)
        self.assertEqual(node, node2)

    def test_not_eq_different_text(self):
        node = TextNode("A", TextType.BOLD) 
        node2 = TextNode("B", TextType.BOLD) 
        self.assertNotEqual(node, node2) 

    def test_not_eq_different_type(self):
        node = TextNode("same", TextType.BOLD)
        node2 = TextNode("same", TextType.ITALIC)
        self.assertEqual(node, node2)

    def test_eq_explicit_none_url(self):
        node = TextNode("same", TextType.CODE, None)
        node2 = TextNode("same", TextType.CODE)
        self.assertEqual(node,node2)

    def test_link_equality_includes_url(self):
        node = TextNode("click", TextType.LINK, "https://a.com")
        node2 = TextNode("click", TextType.LINK, "https://a.com")
        self.assertEqual(node, node2)

    def test_link_not_equal_if_url_differs(self):
        node = TextNode("click", TextType.LINK, "https://a.com")
        node2 = TextNode("click", TextType.LINK, "https://b.com")
        self.assertNotEqual(node, node2)

    def test_image_not_equal_if_url_missing(self):
        node = TextNode("alt", TextType.IMAGE, "https://img.png")
        node2 = TextNode("alt", TextType.IMAGE)
        self.assertNotEqual(node, node2)


if __name__ == "__main__":
    unittest.main()
