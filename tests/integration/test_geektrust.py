from unittest import TestCase
from geektrust import Geektrust


class TestGeektrust(TestCase):

    def setUp(self):
        self.geektrust_app = Geektrust()

    def test_translate(self):
        result = self.geektrust_app.translate('setup.sampleInput.txt')
        self.assertEqual(
            result,
            [
                'self.family.add_child("Shan", "Male")',
                'self.family.add_spouse("Anga", "Female", "Shan")',
                'self.family.add_child("Chit", "Male", "Anga")',
                'self.family.add_child("Ish", "Male", "Anga")',
                'self.family.add_child("Vich", "Male", "Anga")',
                'self.family.add_child("Aras", "Male", "Anga")',
                'self.family.add_child("Satya", "Female", "Anga")',
                'self.family.add_spouse("Amba", "Female", "Chit")',
                'self.family.add_spouse("Lika", "Female", "Vich")',
                'self.family.add_spouse("Chitra", "Female", "Aras")',
                'self.family.add_spouse("Vyan", "Male", "Satya")',
                'self.family.add_child("Dritha", "Female", "Amba")',
                'self.family.add_child("Tritha", "Female", "Amba")',
                'self.family.add_child("Vritha", "Male", "Amba")',
                'self.family.add_child("Vila", "Female", "Lika")',
                'self.family.add_child("Chika", "Female", "Lika")',
                'self.family.add_child("Jnki", "Female", "Chitra")',
                'self.family.add_child("Ahit", "Male", "Chitra")',
                'self.family.add_child("Asva", "Male", "Satya")',
                'self.family.add_child("Vyas", "Male", "Satya")',
                'self.family.add_child("Atya", "Female", "Satya")',
                'self.family.add_spouse("Jaya", "Male", "Dritha")',
                'self.family.add_spouse("Arit", "Male", "Jnki")',
                'self.family.add_spouse("Satvy", "Female", "Asva")',
                'self.family.add_spouse("Krpi", "Female", "Vyas")',
                'self.family.add_child("Yodhan", "Male", "Dritha")',
                'self.family.add_child("Laki", "Male", "Jnki")',
                'self.family.add_child("Lavnya", "Female", "Jnki")',
                'self.family.add_child("Vasa", "Male", "Satvy")',
                'self.family.add_child("Kriya", "Male", "Krpi")',
                'self.family.add_child("Krithi", "Female", "Krpi")'
            ]
        )

    def test_execute(self):
        result = self.geektrust_app.execute(
            [
                'self.family.add_child("Shan", "Male")',
                'self.family.add_spouse("Anga", "Female", "Shan")',
                'self.family.add_child("Chit", "Male", "Anga")',
                'self.family.add_child("Ish", "Male", "Anga")',
                'self.family.add_child("Vich", "Male", "Anga")',
                'self.family.add_child("Aras", "Male", "Anga")',
                'self.family.add_child("Satya", "Female", "Anga")',
                'self.family.add_spouse("Amba", "Female", "Chit")',
                'self.family.add_spouse("Lika", "Female", "Vich")',
                'self.family.add_spouse("Chitra", "Female", "Aras")',
                'self.family.add_spouse("Vyan", "Male", "Satya")',
                'self.family.add_child("Dritha", "Female", "Amba")',
                'self.family.add_child("Tritha", "Female", "Amba")',
                'self.family.add_child("Vritha", "Male", "Amba")',
                'self.family.add_child("Vila", "Female", "Lika")',
                'self.family.add_child("Chika", "Female", "Lika")',
                'self.family.add_child("Jnki", "Female", "Chitra")',
                'self.family.add_child("Ahit", "Male", "Chitra")',
                'self.family.add_child("Asva", "Male", "Satya")',
                'self.family.add_child("Vyas", "Male", "Satya")',
                'self.family.add_child("Atya", "Female", "Satya")',
                'self.family.add_spouse("Jaya", "Male", "Dritha")',
                'self.family.add_spouse("Arit", "Male", "Jnki")',
                'self.family.add_spouse("Satvy", "Female", "Asva")',
                'self.family.add_spouse("Krpi", "Female", "Vyas")',
                'self.family.add_child("Yodhan", "Male", "Dritha")',
                'self.family.add_child("Laki", "Male", "Jnki")',
                'self.family.add_child("Lavnya", "Female", "Jnki")',
                'self.family.add_child("Vasa", "Male", "Satvy")',
                'self.family.add_child("Kriya", "Male", "Krpi")',
                'self.family.add_child("Krithi", "Female", "Krpi")'
            ]
        )
        self.assertEqual(
            result,
            [
                'CHILD_ADDITION_SUCCEEDED',
                'SPOUSE_ADDITION_SUCCEEDED',
                'CHILD_ADDITION_SUCCEEDED',
                'CHILD_ADDITION_SUCCEEDED',
                'CHILD_ADDITION_SUCCEEDED',
                'CHILD_ADDITION_SUCCEEDED',
                'CHILD_ADDITION_SUCCEEDED',
                'SPOUSE_ADDITION_SUCCEEDED',
                'SPOUSE_ADDITION_SUCCEEDED',
                'SPOUSE_ADDITION_SUCCEEDED',
                'SPOUSE_ADDITION_SUCCEEDED',
                'CHILD_ADDITION_SUCCEEDED',
                'CHILD_ADDITION_SUCCEEDED',
                'CHILD_ADDITION_SUCCEEDED',
                'CHILD_ADDITION_SUCCEEDED',
                'CHILD_ADDITION_SUCCEEDED',
                'CHILD_ADDITION_SUCCEEDED',
                'CHILD_ADDITION_SUCCEEDED',
                'CHILD_ADDITION_SUCCEEDED',
                'CHILD_ADDITION_SUCCEEDED',
                'CHILD_ADDITION_SUCCEEDED',
                'SPOUSE_ADDITION_SUCCEEDED',
                'SPOUSE_ADDITION_SUCCEEDED',
                'SPOUSE_ADDITION_SUCCEEDED',
                'SPOUSE_ADDITION_SUCCEEDED',
                'CHILD_ADDITION_SUCCEEDED',
                'CHILD_ADDITION_SUCCEEDED',
                'CHILD_ADDITION_SUCCEEDED',
                'CHILD_ADDITION_SUCCEEDED',
                'CHILD_ADDITION_SUCCEEDED',
                'CHILD_ADDITION_SUCCEEDED'
            ]
        )
