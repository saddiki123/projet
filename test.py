#from lib import init,hit,is_dead,gained_life_points,get_life_points
from lib import Person, Wizard, HealthPotion

def test_Person_name():

    value = Person('James')

    except_value = 'James'

    assert value.name == except_value

