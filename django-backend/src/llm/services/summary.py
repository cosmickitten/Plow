import logging
import os
from transformers import MBartTokenizer, MBartForConditionalGeneration
from django.conf import settings




logger = logging.getLogger('main')


class AI():
    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(AI, cls).__new__(cls)
        return cls.instance

    def __init__(self,model_name) -> None:
        logger.info('Иницилизация языковой модели mbart_ru_sum_gazeta')
        self.model_name = "IlyaGusev/mbart_ru_sum_gazeta"
        
        self.tokenizer = MBartTokenizer.from_pretrained(
            self.model_name, cache_dir = os.path.join(settings.BASE_DIR,'huggingface_cache'))
        self.model = MBartForConditionalGeneration.from_pretrained(
            self.model_name, cache_dir = os.path.join(settings.BASE_DIR,'huggingface_cache'))

    def glue_text(self,title,intro,content):
        article_text= title + intro + content
        return article_text

    def summarize(self, article_text: str):
        input_ids = self.tokenizer(
            [article_text],
            max_length=600,
            padding="max_length",
            truncation=True,
            return_tensors="pt",
        )["input_ids"]

        output_ids = self.model.generate(
            input_ids=input_ids,
            no_repeat_ngram_size=4
        )[0]
        summary = self.tokenizer.decode(output_ids, skip_special_tokens=True)
        return summary


    
