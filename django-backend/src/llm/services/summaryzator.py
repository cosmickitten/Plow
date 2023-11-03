import os
from django.conf import settings


class AI():
    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(AI, cls).__new__(cls)
        return cls.instance
    
    def __init__(self) -> None:
        self.model_name :str
        self.cache_dir = os.path.join(settings.BASE_DIR,'huggingface_cache')
        self.tokenizer :any
        self.model:any
    

    # def glue_text(self,title,intro,content):
    #     article_text = title + intro + content
    #     return article_text



    def summarize(self, article_text: str):
        input_ids = self.tokenizer(
            [article_text],
            max_length=600,
            add_special_tokens=True,
            padding="max_length",
            truncation=True,
            return_tensors="pt"
        )["input_ids"]

        output_ids = self.model.generate(
            input_ids=input_ids,
            no_repeat_ngram_size=4
        )[0]
        summary = self.tokenizer.decode(output_ids, skip_special_tokens=True)
        return summary
    
