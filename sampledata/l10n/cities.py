import json
import os.path
import codecs


from sampledata.exceptions import ParameterError

LOCALES = ['es', 'us']
CITIES_PATH = os.path.join(os.path.dirname(__file__), 'cities')


class City(object):
    data = {}

    def __load_locale(self, locale):
        locale_path = os.path.join(CITIES_PATH, "{0}.json".format(locale))
        if not os.path.exists(locale_path):
            raise ParameterError('Not valid locale')

        fd = codecs.open(locale_path, 'r', encoding='utf-8')
        City.data[locale] = json.load(fd)
        fd.close()

    def get_cities(self, locale):
        if locale not in City.data:
            self.__load_locale(locale)

        return [x for x in City.data[locale]['cities']]

    def all_cities(self):
        cities = []
        for locale in LOCALES:
            cities += self.get_cities(locale)

        return cities

    def generate(self, sd, locale=None):
        if locale:
            cities = self.get_cities(locale)
        else:
            cities = self.all_cities()

        return sd.choice(cities)
