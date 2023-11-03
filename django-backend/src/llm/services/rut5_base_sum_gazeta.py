import logging
import os
from django.conf import settings
from transformers import AutoTokenizer, T5ForConditionalGeneration
from .summaryzator import AI

logger = logging.getLogger('main')


class rut5_base_sum_gazeta(AI):
    def __init__(self) -> None:
        logger.info('Иницилизация языковой модели rut5_base_sum_gazeta')
        self.model_name = "IlyaGusev/rut5_base_sum_gazeta"
        self.tokenizer = AutoTokenizer.from_pretrained(
            self.model_name, cache_dir = os.path.join(settings.BASE_DIR,'huggingface_cache'))
        self.model = T5ForConditionalGeneration.from_pretrained(
            self.model_name, cache_dir = os.path.join(settings.BASE_DIR,'huggingface_cache'))
