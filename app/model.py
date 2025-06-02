from transformers import T5ForConditionalGeneration
from transformers import T5TokenizerFast as T5Tokenizer
from transformers.tokenization_utils import PreTrainedTokenizer

MODEL_NAME = "t5-small"
MAX_INPUT_LENGTH = 512
MAX_TARGET_LENGTH = 128


def get_model_tokenizer() -> PreTrainedTokenizer:
    """Return a Pre-trained instance of the T5 Model Tokenizer

    Returns:
        PreTrainedTokenizer: The tokenizer instance.
    """
    return T5Tokenizer.from_pretrained(MODEL_NAME)


def get_peft_adapted_model(device: str) -> T5ForConditionalGeneration:
    """Return the LoRA adapted model moved to the mentioned device.

    Args:
        device (str): The device to move the model to ("cpu" or "cuda")

    Returns:
        T5ForConditionalGeneration: The model instance to run inference on.
    """
    # Since the saved weights already have the LoRA adapter config
    # there's no need to pass it separately.
    base_model = T5ForConditionalGeneration.from_pretrained(
        "model/t5-small-base")
    return base_model
