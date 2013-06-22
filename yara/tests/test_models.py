from yara.tests import TestCase
from yara.models import State, Phone, Address


class ModelTestCase(TestCase):
    def test_state(self):
        state = State(code='FL', name='Florida')
        self.assertEquals(repr(state), 'Florida')

        phone = Phone(area_code='111', exchange='222', number='3333')
        self.assertEquals(repr(phone), '(111) 222-3333')

        address = Address(
            street1 = '100 Main St.',
            city='Lithia',
            state=state,
            postal_code='33547'
        )

        self.assertEquals(repr(address), '100 Main St. Lithia, FL 33547')