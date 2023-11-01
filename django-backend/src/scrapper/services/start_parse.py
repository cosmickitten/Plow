import logging

from.agroxxi import Agroxxi
from.agrinews import Agrinews
from.prime import Prime
from.agrovesti import Agrovesti
from.rg import RG
from.utils import timeit, Utils


logger = logging.getLogger("main")
utility = Utils()


class ParserCoordinator():
    help = "Подсказка"

    @timeit
    def run(self, *args, **kwargs):
        # self.stdout.write(f'[+] Запуск функции с args = {args} kwargs = {kwargs}')
        utility.set_null()
        a1 = Agrovesti()
        a2 = Agroxxi()
        a3 = Prime()
        a4 = Agrinews()
        a5 = RG()
        parsers = [a1, a2, a3, a4, a5]
        #parsers = [a5,]
        for parser in parsers:
            parser.start()
        logger.info("Успешно завершено!")
        logger.info( "%s",utility.count_of_queries())
        return utility.queries

        # return super().handle(*args, **kwargs)
