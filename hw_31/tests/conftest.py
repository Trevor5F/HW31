from pytest_factoryboy import register

from factories import *

pytest_plugins = "fixtures"

register(AdFactory)
register(CategoryFactory)
register(UserFactory)