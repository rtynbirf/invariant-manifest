#!/usr/bin/env python3
"""Мутационные тесты: валидатор обязан ловить каждый дефект.
Запуск: python3 test_mutations.py"""
import copy, json, unittest, sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent / "scripts"))
import fork3_corpus as fc
import fork3_judge_v023 as judge

CORPUS = fc.CORPUS
TRANSFORMS = json.loads((Path(__file__).parent / "data" / "FORK3_TRANSFORMS.json").read_text("utf-8"))["трансформации"]

def check(cid, transform_key, text):
    """Run check_transform directly for a specific corpus item + transform."""
    c = next(x for x in CORPUS if x["id"] == cid)
    return judge.check_transform(c, text)["verdict"]

class Mutations(unittest.TestCase):
    def test_base_ok(self):
        """Base transforms should run without error."""
        r = judge.run()
        self.assertEqual(len(r["результаты"]), 10)

    def test_number_removed_break(self):
        """Removing a number should produce BREAK."""
        t = next(x for x in TRANSFORMS if x["id"] == "C01")["T2a"]
        t = t.replace("1,618", "XXX").replace("1.618", "XXX")
        self.assertEqual(check("C01", "T2a", t), "BREAK")

    def test_negation_removed_break(self):
        """Removing negation should produce BREAK."""
        self.assertEqual(check("C03", "T2a", "Носитель умирает; смысл слова вечен."), "BREAK")

    def test_rare_term_removed_break(self):
        """Removing a rare term should produce BREAK."""
        t = next(x for x in TRANSFORMS if x["id"] == "C09")["T2a"]
        t = t.replace("Дяхан", "язык").replace("дяхан", "язык")
        self.assertEqual(check("C09", "T2a", t), "BREAK")

    def test_condition_drift_or_worse(self):
        """Removing condition marker should produce DRIFT or BREAK."""
        t = "Проекция — вера; проекция — знание."
        v = check("C05", "T2a", t)
        self.assertIn(v, ("DRIFT", "BREAK"))

    def test_empty_transform_break(self):
        """Empty text should produce BREAK."""
        self.assertEqual(check("C01", "T2a", ""), "BREAK")

    def test_extra_numbers_not_break(self):
        """Extra numbers should NOT produce BREAK."""
        t = next(x for x in TRANSFORMS if x["id"] == "C01")["T2a"] + " Дополнительно: 42."
        self.assertNotEqual(check("C01", "T2a", t), "BREAK")

    def test_c08_fixed_soft(self):
        """C08 T2b (fixed: negation restored) should be SOFT."""
        t = next(x for x in TRANSFORMS if x["id"] == "C08")["T2b"]
        self.assertEqual(check("C08", "T2b", t), "SOFT")

if __name__ == "__main__":
    unittest.main(verbosity=1)
