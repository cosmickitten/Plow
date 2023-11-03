from .rut5_base_sum_gazeta import rut5_base_sum_gazeta
from scrapper.models import Article


class AICoordinator():

    def run(self):
        ai = rut5_base_sum_gazeta()
        unsummarized = Article.objects.filter(is_summarized = False)
        if len(unsummarized) > 0:
            article = unsummarized[0]
            article_text = str(article.title) +  str(article.intro)  +  str(article.content)
            article.summary  = ai.summarize(article_text=article_text)
            article.save()
            




