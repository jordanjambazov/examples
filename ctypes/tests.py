import unittest
import persons


class PersonTestCases(unittest.TestCase):
    def test_c_structure_is_unpacked_properly(self):
        person_proxy = persons.PersonProxy()
        person = person_proxy.get_person("Jordan", 21)
        self.assertEquals("Jordan", person.name,
                          "Person name is wrong.")
        self.assertEquals(21, person.age,
                          "Person age is wrong.")



if __name__ == '__main__':
    unittest.main()
