from unittest import TestCase
from unittest.mock import patch, Mock

from family.family import FamilyTree
from family.member import Member
from family.constants import Outputs, Gender
from tests.unit import create_fake_member

class TestFamilyTree(TestCase):

    def setUp(self):
        self.ftree = FamilyTree()

    def test_initialization(self):
        self.assertEqual(self.ftree.family, {})

    @patch('family.family.Member', return_value=create_fake_member(
        id=1, name="Zim", gender=Gender.male))
    def test_add_child(self, mock_member):
        # if tree is empty
        result = self.ftree.add_child("Zim", "Male", "Mother")
        mock_member.assert_called_with(1, "Zim", "Male")

        self.assertEqual(
            isinstance(self.ftree.family.get("Zim", None), Mock),
            True
        )
        self.assertEqual(result, Outputs.CHILD_ADDITION_SUCCEEDED.value)

        # if either mother/ father do not exist
        mother = create_fake_member(id=2, name="Mother", gender=Gender.female)
        fakemother = create_fake_member(
            id=4, name="Fakemother", gender=Gender.male)
        father = create_fake_member(id=3, name="Father", gender=Gender.male)

        self.assertEqual(
            self.ftree.add_child("Zim2", "Male", "Mother"),
            Outputs.PERSON_NOT_FOUND.value
        )
        self.ftree.family['Fakemother'] = fakemother
        self.assertEqual(
            self.ftree.add_child("Zim2", "Male", "Fakemother"),
            Outputs.CHILD_ADDITION_FAILED.value
        )
        self.ftree.family['Mother'] = mother
        self.assertEqual(
            self.ftree.add_child("Zim2", "Male", "Mother"),
            Outputs.CHILD_ADDITION_FAILED.value
        )
        self.ftree.family['Father'] = father
        self.ftree.family['Mother'].spouse = father
        self.ftree.family['Father'].spouse = mother

        self.assertEqual(
            self.ftree.add_child("Zim2", "Male", "Mother"),
            Outputs.CHILD_ADDITION_SUCCEEDED.value
        )
        self.assertEqual(
            self.ftree.add_child("Zim2", "Male", "Mother"),
            Outputs.CHILD_ADDITION_FAILED.value
        )
        self.assertEqual(
            isinstance(
                self.ftree.family.get("Zim2", None),
                Mock
            ),
            True
        )

    @patch('family.family.Member', return_value=create_fake_member(
        id=1, name="Wife", gender=Gender.female))
    def test_add_spouse(self, mock_member):
        # if tree is empty
        result = self.ftree.add_spouse("Wife", "Female", "Zim")
        mock_member.assert_called_with(1, "Wife", "Female")

        self.assertEqual(
            self.ftree.family.get("Zim", None),
            None
        )
        self.assertEqual(result, Outputs.SPOUSE_ADDITION_FAILED.value)

        # if spouse does not exist
        dummy_member = create_fake_member(
            id=0, name="DummyMember", gender=Gender.male)
        self.ftree.family["DummyMember"] = dummy_member
        spouse_a = create_fake_member(id=2, name="Zim", gender=Gender.male)
        spouse_b = create_fake_member(
            id=3, name="FakeMember", gender=Gender.female)
        spouse_c = create_fake_member(
            id=3, name="MarriedMember", gender=Gender.male, spouse=spouse_b)

        self.assertEqual(
            self.ftree.add_spouse("Wife", Gender.female, "Zim"),
            Outputs.PERSON_NOT_FOUND.value
        )
        self.ftree.family["Zim"] = spouse_a
        self.ftree.family["FakeMember"] = spouse_b
        self.ftree.family["MarriedMember"] = spouse_c

        self.assertEqual(
            self.ftree.add_spouse("Wife", Gender.female, "FakeMember"),
            Outputs.SPOUSE_ADDITION_FAILED.value
        )
        self.assertEqual(
            self.ftree.add_spouse("Wife", Gender.female, "MarriedMember"),
            Outputs.SPOUSE_ADDITION_FAILED.value
        )
        self.assertEqual(
            self.ftree.add_spouse("Wife", Gender.female, "Zim"),
            Outputs.SPOUSE_ADDITION_SUCCEEDED.value
        )
        self.assertEqual(
            self.ftree.add_spouse("Wife", Gender.female, "Zim"),
            Outputs.SPOUSE_ADDITION_FAILED.value
        )

    @patch('family.family.Member.get_relationship', side_effect=[
        [],
        [
            create_fake_member(id=1, name="Zim"),
            create_fake_member(id=2, name="Wife")
        ]
    ])
    def test_get_relationship(self, mock_get_relationship):
        self.assertEqual(
            self.ftree.get_relationship("Zim", "brother_in_law"),
            Outputs.PERSON_NOT_FOUND.value
        )
        self.ftree.family["Zim"] = Member(1, "Zim", "Male")
        self.assertEqual(
            self.ftree.get_relationship("Zim", "brother_in_law"),
            Outputs.NONE.value
        )
        self.assertEqual(
            self.ftree.get_relationship("Zim", "brother_in_law"),
            "Zim Wife"
        )
