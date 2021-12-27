from unittest import TestCase
from family.member import Member
from family.constants import Outputs
from family.family import FamilyTree

class TestFamilyTree(TestCase):

    def setUp(self):
        self.ftree = FamilyTree()

    def test_add_child(self):
        result = self.ftree.add_child("Father", "Male")
        self.assertEqual(result, Outputs.CHILD_ADDITION_SUCCEEDED.value)
        self.assertEqual(
            self.ftree.family.get("Father", None) is not None,
            True
        )

        self.assertEqual(
            self.ftree.add_child("Zim", "Male", "Mother"),
            Outputs.PERSON_NOT_FOUND.value
        )
        self.assertEqual(
            self.ftree.add_child("Zim", "Male", "Father"),
            Outputs.CHILD_ADDITION_FAILED.value
        )

        mother = Member(2, "Mother", "Female")
        mother.spouse = self.ftree.family["Father"]
        self.ftree.family["Father"].set_spouse(mother)
        self.ftree.family["Mother"] = mother

        self.assertEqual(
            self.ftree.add_child("Zim", "Male", "Mother"),
            Outputs.CHILD_ADDITION_SUCCEEDED.value
        )
        self.assertEqual(
            self.ftree.add_child("Zim", "Male", "Mother"),
            Outputs.CHILD_ADDITION_FAILED.value
        )
        self.assertEqual(
            self.ftree.family.get("Zim", None) is not None,
            True
        )

    def test_add_spouse(self):
        self.assertEqual(
            self.ftree.add_spouse("Wife", "Female", "Zim"),
            Outputs.SPOUSE_ADDITION_FAILED.value
        )
        dummy_member = Member(1, "DummyMember", "Male")
        self.ftree.family['DummyMember'] = dummy_member
        self.assertEqual(
            self.ftree.add_spouse("Wife", "Female", "Zim"),
            Outputs.PERSON_NOT_FOUND.value
        )
        spouse_a = Member(1, "FakeMember", "Female")
        spouse_b = Member(1, "AlreadyMarriedMember", "Male")
        spouse_b.set_spouse(spouse_a)
        spouse_c = Member(1, "Zim", "Male")
        self.ftree.family["FakeMember"] = spouse_a
        self.ftree.family["AlreadyMarriedMember"] = spouse_b
        self.ftree.family["Zim"] = spouse_c
        self.assertEqual(
            self.ftree.add_spouse("Wife", "Female", "FakeMember"),
            Outputs.SPOUSE_ADDITION_FAILED.value
        )
        self.assertEqual(
            self.ftree.add_spouse("Wife", "Female", "AlreadyMarriedMember"),
            Outputs.SPOUSE_ADDITION_FAILED.value
        )
        self.assertEqual(
            self.ftree.add_spouse("Wife", "Female", "Zim"),
            Outputs.SPOUSE_ADDITION_SUCCEEDED.value
        )
        self.assertEqual(
            self.ftree.add_spouse("Wife", "Female", "Zim"),
            Outputs.SPOUSE_ADDITION_FAILED.value
        )

    def test_get_relationship(self):
        self.assertEqual(
            self.ftree.get_relationship("Zim", "brother_in_law"),
            Outputs.PERSON_NOT_FOUND.value
        )
        member = Member(1, "Zim", "Male")
        son_a = Member(2, "SonA", "Male")
        son_b = Member(3, "SonB", "Male")
        member.add_child(son_b)
        member.add_child(son_a)
        son_a.set_father(member)
        son_b.set_father(member)
        self.ftree.family["Zim"] = member
        self.ftree.family["SonA"] = son_a
        self.ftree.family["SonB"] = son_b
        self.assertEqual(
            self.ftree.get_relationship("Zim", "daughter"),
            Outputs.NONE.value
        )
        self.assertEqual(
            self.ftree.get_relationship("Zim", "son"), "SonA SonB")
