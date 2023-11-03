import logging
import os
from transformers import MBartTokenizer, MBartForConditionalGeneration
from django.conf import settings
from .summaryzator import AI



logger = logging.getLogger('main')


class mbart_ru_sum_gazeta(AI):

    def __init__(self) -> None:
        logger.info('Иницилизация языковой модели mbart_ru_sum_gazeta')
        self.model_name = "IlyaGusev/mbart_ru_sum_gazeta"
        
        self.tokenizer = MBartTokenizer.from_pretrained(
            self.model_name, cache_dir = os.path.join(settings.BASE_DIR,'huggingface_cache'))
        self.model = MBartForConditionalGeneration.from_pretrained(
            self.model_name, cache_dir = os.path.join(settings.BASE_DIR,'huggingface_cache'))

