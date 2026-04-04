from config import HF_TOKEN,MODEL_NAME
from huggingface_hub import InferenceClient
import logging
import time

logger = logging.getLogger(__name__)


class ModelClient:
    def api_call(self, prompt: str) -> str:
        raise NotImplementedError("generate() must be implemented")
    
class HFClient(ModelClient):
    def __init__(self):
        self.client = InferenceClient(api_key=HF_TOKEN)

    def api_call(self, prompt: str) -> str:

        logger.debug(f"Prompt preview: {prompt[:200]}")
        call_start_time = time.time()
        logger.info(f"Call to {MODEL_NAME} model started.")

        try:
            completion = self.client.chat.completions.create(
                    model=MODEL_NAME,
                    messages=[
                        {
                            "role": "user",
                            "content": prompt
                        }
                    ],
                )

            raw = completion.choices[0].message.content.strip()
            logger.debug(f"Raw response preview: {raw[:200]}")

        except Exception as e:
                logger.error(f"Model call failed for {MODEL_NAME}: {e}")
                raise

        response_end_time = time.time()
        duration = response_end_time - call_start_time
        logger.info(f"Model {MODEL_NAME} response finished in {duration:.2f}s")

        return raw

