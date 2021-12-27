from family.member import Member
from family.constants import Outputs, Gender

class FamilyTree:

    def __init__(self):
        self.family = {}

    def add_child(self, name, gender, mother_name=None):
        _id = len(self.family.keys()) + 1
        member = Member(_id, name, gender)
        if not self.family:
            self.family[name] = member
            return Outputs.CHILD_ADDITION_SUCCEEDED.value

        if name in self.family:
            return Outputs.CHILD_ADDITION_FAILED.value

        mother = self.family.get(mother_name, None)
        if not mother:
            return Outputs.PERSON_NOT_FOUND.value
        if mother.gender != Gender.female:
            return Outputs.CHILD_ADDITION_FAILED.value

        father = mother.spouse
        if not father:
            return Outputs.CHILD_ADDITION_FAILED.value

        try:
            member.set_mother(mother)
            member.set_father(father)
            self.family[mother_name].add_child(member)
            self.family[father.name].add_child(member)
            self.family[name] = member
            return Outputs.CHILD_ADDITION_SUCCEEDED.value
        except ValueError:
            return Outputs.CHILD_ADDITION_FAILED.value

    def add_spouse(self, name, gender, spouse_name):
        _id = len(self.family.keys()) + 1
        member = Member(_id, name, gender)
        if not self.family:
            return Outputs.SPOUSE_ADDITION_FAILED.value

        if name in self.family:
            return Outputs.SPOUSE_ADDITION_FAILED.value

        spouse = self.family.get(spouse_name, None)
        if not spouse:
            return Outputs.PERSON_NOT_FOUND.value
        if spouse.gender == member.gender:
            return Outputs.SPOUSE_ADDITION_FAILED.value
        if spouse.spouse is not None:
            return Outputs.SPOUSE_ADDITION_FAILED.value

        try:
            member.set_spouse(self.family[spouse.name])
            self.family[spouse.name].set_spouse(member)
            self.family[name] = member
            return Outputs.SPOUSE_ADDITION_SUCCEEDED.value
        except ValueError:
            return Outputs.SPOUSE_ADDITION_FAILED.value

    def get_relationship(self, name, relationship_type):
        member = self.family.get(name, None)
        if not member:
            return Outputs.PERSON_NOT_FOUND.value
        result = member.get_relationship(relationship_type)
        if not result:
            return Outputs.NONE.value
        else:
            return ' '.join(
                list(
                    map(
                        lambda x: x.name,
                        sorted(result, key=lambda key: key.id)
                    )
                )
            )
