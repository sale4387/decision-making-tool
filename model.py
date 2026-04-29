from config import HF_TOKEN, MODEL_TIMEOUT, MAX_TOKENS, TEMPERATURE, MAX_RETRIES
from huggingface_hub import InferenceClient, InferenceTimeoutError
from google import genai
from google.genai import types, errors
import logging
import time

logger = logging.getLogger(__name__)

class ModelClient:
    def api_call(self, prompt: str) -> str:
        raise NotImplementedError("generate() must be implemented")
    
class HFClient(ModelClient):
    def __init__(self, model_name):
        self.client = InferenceClient(api_key=HF_TOKEN, timeout=MODEL_TIMEOUT)
        self.model_name=model_name

    def api_call(self, prompt: str) -> str:

        logger.debug(f"Prompt preview: {prompt[:200]}")
        call_start_time = time.time()
        logger.info(f"Call to {self.model_name} model started.")

        retries=0
        raw=None
        while retries < MAX_RETRIES:
            try:
                completion = self.client.chat.completions.create(
                        model=self.model_name,
                        messages=[
                            {
                                "role": "user",
                                "content": prompt
                            }
                        ],
                        max_tokens=MAX_TOKENS,
                        temperature=TEMPERATURE

                    )

                raw = completion.choices[0].message.content.strip()
                if raw:
                    logger.debug(f"Raw response preview: {raw[:200]}")
                    break
                else:
                    logger.error("Raw response undefined")
                    retries=retries+1
                        
            except InferenceTimeoutError:
                logger.error(f"Request for {self.model_name} timed out.")
                retries=retries+1
                
            except Exception as e:
                logger.error(f"Call failed for {self.model_name}: {e}")
                retries=retries+1
        if raw is None:
            logger.error(f"Maximum number of retries reached for {self.model_name}")
            raise Exception("Maximum numbers of retries reached.")

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

        raw=None
        retries=0
        while retries < MAX_RETRIES:
            try:
                response = self.client.models.generate_content(
                    model=self.model_name, 
                    contents=prompt,
                    config=types.GenerateContentConfig(
                            http_options=types.HttpOptions(
                                timeout=MODEL_TIMEOUT  
                            ),
                    max_output_tokens=MAX_TOKENS,
                    temperature= TEMPERATURE
                        )
                    )
                raw=response.text
                if raw:
                    logger.debug(f"Raw response preview: {raw[:200]}")
                    break
                else:
                    logger.error("Raw response undefined")
                    retries=retries+1
                    continue

            except errors.APIError as e:
                if e.code == 504:
                    logger.error(f"Request for {self.model_name} timed out.")
                    retries=retries+1
                    continue
                    
                else:
                    logger.error(f"Call failed for {self.model_name}: {e}")
                    retries=retries+1
                    continue
        if raw is None:
            logger.error(f"Maximum number of retries reached for {self.model_name}")
            raise Exception("Maximum numbers of retries reached.")
        response_end_time = time.time()
        duration = response_end_time - call_start_time
        logger.info(f"{self.model_name} response finished in {duration:.2f}s")
        return raw


         

