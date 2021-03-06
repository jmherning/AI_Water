"""
Tests to see if the output of the models architecture is correct.
"""
from src.model.architecture.masked import create_model_masked
from src.config import NETWORK_DEMS as dems


def model_final_layer(model):
    return model.layers[-1].output_shape


def test_architecture():
    model = create_model_masked("masked_test")
    assert model_final_layer(model) == (None, dems, dems, 1)
