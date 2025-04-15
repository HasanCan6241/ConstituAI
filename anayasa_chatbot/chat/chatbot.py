# chat/chatbot.py

import requests
import json
import logging

logger = logging.getLogger(__name__)


class AnayasaChatBot:
    API_URL = "API-URL"

    @classmethod
    def get_response(cls, prompt):
        try:
            payload = json.dumps({"prompt": prompt})
            headers = {'Content-Type': 'application/json'}

            response = requests.post(cls.API_URL, headers=headers, data=payload, timeout=30)
            response.raise_for_status()  # HTTP hataları için kontrol

            result = response.json()
            return result.get("response", "Üzgünüm, bir cevap alamadım. Lütfen tekrar deneyin.")

        except requests.exceptions.Timeout:
            logger.error("API isteği zaman aşımına uğradı")
            return "Üzgünüm, yanıt alırken zaman aşımı oluştu. Lütfen daha sonra tekrar deneyin."

        except requests.exceptions.RequestException as e:
            logger.error(f"API isteği başarısız: {str(e)}")
            return "Üzgünüm, şu anda hizmet veremiyorum. Lütfen daha sonra tekrar deneyin."

        except json.JSONDecodeError:
            logger.error("API yanıtı geçerli bir JSON formatında değil")
            return "Üzgünüm, yanıtı işlerken bir hata oluştu. Lütfen daha sonra tekrar deneyin."

        except Exception as e:
            logger.error(f"Beklenmeyen hata: {str(e)}")
            return "Beklenmeyen bir hata oluştu. Lütfen daha sonra tekrar deneyin."