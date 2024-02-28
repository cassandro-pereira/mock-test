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

