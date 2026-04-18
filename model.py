from config import HF_TOKEN
from huggingface_hub import InferenceClient
from google import genai
import logging
import time


logger = logging.getLogger(__name__)



class ModelClient:
    def api_call(self, prompt: str) -> str:
        raise NotImplementedError("generate() must be implemented")
    
class HFClient(ModelClient):
    def __init__(self, model_name):
        self.client = InferenceClient(api_key=HF_TOKEN)
        self.model_name=model_name

    def api_call(self, prompt: str) -> str:

        logger.debug(f"Prompt preview: {prompt[:200]}")
        call_start_time = time.time()
        logger.info(f"Call to {self.model_name} model started.")

        try:
            completion = self.client.chat.completions.create(
                    model=self.model_name,
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
                logger.error(f"Call failed for {self.model_name}: {e}")
                raise

        response_end_time = time.time()
        duration = response_end_time - call_start_time
        logger.info(f"{self.model_name} response finished in {duration:.2f}s")

        return raw
    
class GEMINIClient(ModelClient):

    def __init__(self,model_name):
        self.client = genai.Client()
        self.model_name=model_name

    def api_call(self, prompt: str) -> str:

        logger.debug(f"Prompt preview: {prompt[:200]}")
        call_start_time = time.time()
        logger.info(f"Call to {self.model_name} model started.")

        try:
            response = self.client.models.generate_content(
                model=self.model_name, contents=prompt
                )
            raw=response.text
            logger.debug(f"Raw response preview: {raw[:200]}")


        except Exception as e:
                logger.error(f"Call failed for {self.model_name}: {e}")
                raise

        response_end_time = time.time()
        duration = response_end_time - call_start_time
        logger.info(f"{self.model_name} response finished in {duration:.2f}s")

        return raw



         

