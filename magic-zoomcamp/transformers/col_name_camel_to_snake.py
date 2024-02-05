if 'transformer' not in globals():
    from mage_ai.data_preparation.decorators import transformer
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test

import re

# Function to convert CamelCase to snake_case
def camel_to_snake(name):
    # First, insert underscores between CamelCase words and lowercase the entire string
    name_snake = re.sub('(.)([A-Z][a-z]+)', r'\1_\2', name)
    # Then, handle uppercase abbreviations and numbers in the middle of a word
    name_snake = re.sub('([a-z0-9])([A-Z])', r'\1_\2', name_snake).lower()
    return name_snake


@transformer
def transform(data, *args, **kwargs):

    print(f"Before column rename: {data.columns}")

    # Apply the function to each column name
    data.columns = [camel_to_snake(column) for column in data.columns]

    print(f"After column rename: {data.columns}")

    return data


@test
def test_output(output, *args) -> None:
    """
    Template code for testing the output of the block.
    """
    assert output is not None, 'The output is undefined'

@test
def test_vendor_id_exist(output, *args) -> None:
    assert 'vendor_id' in output.columns, 'Column `vendor_id` is not exist in the dataset'