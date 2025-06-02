import litserve as ls
import torch

from app.model import get_model_tokenizer, get_peft_adapted_model
from app.utils.constants import Constants
from app.utils.parser import create_arg_parser, create_config


class SummarisationInference(ls.LitAPI):
    def setup(self, device: str):
        """Initialisation hook provided by the LitServe API to initialise our model.

        Args:
            device (str): Which device to load the model to, provided by the API.
        """
        self.model = get_peft_adapted_model(device)
        self.tokenizer = get_model_tokenizer()

    def predict(self, request) -> dict[str, str]:
        """Handle the actual request, extracting the request body and generating summary.

        Args:
            request (_type_): _description_

        Returns:
            dict[str, str]: Return a dictionary containing the output summary.
        """
        # Extract the body of text.
        text = request["input"]
        print(f"Received body: {text}")
        body = "summarize: " + text

        # Generate summary
        inputs = self.tokenizer(body,
                                return_tensors="pt", truncation=True, padding=True)
        inputs = {k: v.to(self.model.device) for k, v in inputs.items()}
        with torch.no_grad():
            outputs = self.model.generate(
                **inputs, max_length=128, num_beams=4)

        summary = self.tokenizer.decode(outputs[0], skip_special_tokens=True)

        print(f"Generated summary: {summary}")

        return {"output": summary}


if __name__ == "__main__":
    parser = create_arg_parser()
    args = parser.parse_args()
    config = create_config(args)

    server = ls.LitServer(SummarisationInference(
        max_batch_size=config[Constants.BATCH]))
    server.run(port=config[Constants.PORT])
