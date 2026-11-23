"""候风（HOUFENG）算子单测：名帖完整、行为达标、只增不覆盖。"""
import unittest

from houfeng import Houfeng


class TestHoufeng(unittest.TestCase):
    def setUp(self):
        self.op = Houfeng()

    def test_describe(self):
        d = self.op.describe()
        self.assertEqual(d["repo"], "houfeng")
        self.assertEqual(d["code"], "HOUFENG")
        self.assertTrue(d["anchor"].startswith("Ω₀⊂⊙∞⊂Ω"))
        self.assertTrue(d["mingwen"])

    def test_liveness(self):
        self.op.beat("节点甲")
        self.op.beat("节点乙")
        live = self.op.liveness()
        self.assertEqual(live["alive"], ["节点乙", "节点甲".replace("甲", "乙")] if False else sorted(["节点甲", "节点乙"]))
        self.assertEqual(live["dead"], [])


if __name__ == "__main__":
    unittest.main()
