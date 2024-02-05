if 'transformer' not in globals():
    from mage_ai.data_preparation.decorators import transformer
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test


@transformer
def transform(data, *args, **kwargs):
    """
    Template code for a transformer block.

    Add more parameters to this function if this block has multiple parent blocks.
    There should be one parameter for each output variable from each parent block.

    Args:
        data: The output from the upstream parent block
        args: The output from any additional upstream blocks (if applicable)

    Returns:
        Anything (e.g. data frame, dictionary, array, int, str, etc.)
    """

    # Create a new column lpep_pickup_date by converting lpep_pickup_datetime to a date.
    data['lpep_pickup_date'] = data['lpep_pickup_datetime'].dt.date

    print(f"Preprocessing: rows with zero passengers: {data['passenger_count'].isin([0]).sum()}")
    data = data[data['passenger_count'] > 0]

    print(f"Preprocessing: rows with zero trip distanct: {data['trip_distance'].isin([0]).sum()}")
    data = data[data['trip_distance'] > 0]

    return data

@test
def test_passenger_count(output, *args) -> None:
    assert output['passenger_count'].isin([0]).sum() == 0, 'There are rides with 0 passenger'

@test
def test_trip_distance(output, *args) -> None:
    assert output['trip_distance'].isin([0]).sum() == 0, 'There are rides with 0 trip distance'
