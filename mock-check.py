#Rehearse mock scenarios and asserts
from unittest.mock import Mock, patch, call
from unittest.mock import MagicMock
import sys
mock = Mock(side_effect=KeyError('foo'))
#mock()

values = {'a': 1, 'b': 2, 'c': 3}
def side_effect(arg):
    return values[arg]

mock.side_effect = side_effect
mock('a'), mock('b'), mock('c')

mock.side_effect = [5, 4, 3, 2, 1]
mock(), mock(), mock()
mocked_print = 'foo'

@patch('builtins.print')
def test_print(mocked_print):
    print('foo')
    print()

    assert mocked_print.mock_calls == [call('foo'), call()]

test_print()
print(mock.side_effect.__hash__)
print("Mock Side effect ")
print(sys.stdout)

#Mock calls
mock = MagicMock()
mock.method()
mock.attribute.method(10, x=53)
mock.mock_calls

expected = [call.method(), call.attribute.method(10, x=53)]
if mock.mock_calls == expected :
    print("Mock call vs expected")
    print(mock.mock_calls + expected)

#Using return
mock.return_value = 3
mock.method.return_value = 3
mock()

#mock attribute value
mock.x = 3
print("Mock value of x mocked vaiable ")
print(mock.x)
