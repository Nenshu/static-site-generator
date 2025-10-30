import unittest
from htmlnode import HTMLNode

class TestHTMLNode(unittest.TestCase):
    def test_props_to_html_multiple(self):
        node = HTMLNode(tag="a", props={"href":"https://www.google.com", "target":"_blank"})
        
        self.assertEqual(node.props_to_html(), ' href="https://www.google.com" target="_blank"')

    def test_props_to_html_empty(self):
        self.assertEqual(HTMLNode(props=None).props_to_html(), "")
        self.assertEqual(HTMLNode(props={}).props_to_html(), "")

    def test_repr_contains_fields(self):
        r = repr(HTMLNode(tag="p", value="Hello", children=None, props={"class":"lead"}))
        self.assertIn("tag='p'", r)
        self.assertIn("value='Hello'", r)
        self.assertIn("{'class': 'lead'}", r)

    def test_to_html_raises(self):
        with self.assertRaises(NotImplementedError):
            HTMLNode(tag="p", value="x").to_html()

if __name__ == "__main__":
    unittest.main()

