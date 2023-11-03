from .rut5_base_sum_gazeta import rut5_base_sum_gazeta
from scrapper.models import Article


class AICoordinator():

    def run():
        ai = rut5_base_sum_gazeta
        unsummarized = Article.objects.get(is_summarized = False)
        article_text = ai.glue_text(str(unsummarized.title) + str(unsummarized.intro) + str(unsummarized.content))
        unsummarized.summary  = ai.summarize(article_text)
        unsummarized.save()
        




