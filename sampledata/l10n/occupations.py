import json
import os.path
import codecs


from sampledata.exceptions import ParameterError

LOCALES = ['us']
OCCUPATIONS_PATH = os.path.join(os.path.dirname(__file__), 'occupations')


class Occupation(object):
    data = {}

    def __load_locale(self, locale):
        locale_path = os.path.join(OCCUPATIONS_PATH, "{0}.json".format(locale))
        if not os.path.exists(locale_path):
            raise ParameterError('Not valid locale')

        fd = codecs.open(locale_path, 'r', encoding='utf-8')
        Occupation.data[locale] = json.load(fd)
        fd.close()

    def get_occupations(self, locale):
        if locale not in Occupation.data:
            self.__load_locale(locale)

        return [x for x in Occupation.data[locale]['occupations']]

    def all_occupations(self):
        occupations = []
        for locale in LOCALES:
            occupations += self.get_occupations(locale)

        return occupations

    def generate(self, sd, locale=None):
        if locale:
            occupations = self.get_occupations(locale)
        else:
            occupations = self.all_occupations()

        return sd.choice(occupations)
