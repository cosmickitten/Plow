from celery import shared_task
from scrapper.services.start_parse import ParserCoordinator


@shared_task
def parse_all():
    parser = ParserCoordinator()
    res = parser.run()
    return res
