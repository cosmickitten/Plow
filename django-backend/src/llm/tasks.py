from celery import shared_task
from llm.services.AICoordinator import AICoordinator


@shared_task
def task_summury():
    sum = AICoordinator()
    sum.run()
    
