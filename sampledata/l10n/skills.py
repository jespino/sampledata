import json
import os.path
import codecs
import six
import random


from sampledata.exceptions import ParameterError

LOCALES = ['us', 'es']
SKILLS_PATH = os.path.join(os.path.dirname(__file__), 'skills')


class Skill(object):
    data = {}

    def __load_locale(self, locale):
        locale_path = os.path.join(SKILLS_PATH, "{0}.json".format(locale))
        if not os.path.exists(locale_path):
            raise ParameterError('Not valid locale')

        fd = codecs.open(locale_path, 'r', encoding='utf-8')
        Skill.data[locale] = json.load(fd)
        fd.close()

    def get_skills(self, locale):
        if locale not in Skill.data:
            self.__load_locale(locale)

    def all_skills(self):
        skills = []
        for locale in LOCALES:
            self.get_skills(locale)
            for subtype in Skill.data[locale]['skills']:
                skills.extend(Skill.data[locale]['skills'][subtype])

        return skills

    def generate(self, sd, locale=None, subtype=None):
        skills = self.generate_skills(sd, locale=locale, subtype=subtype)
        return sd.choice(skills)

    def generate_skills(self, sd, locale=None, subtype=None, total=None):
        if locale and subtype:
            self.get_skills(locale)
            if subtype not in Skill.data[locale]['skills']:
                raise ParameterError('Not valid subtype')
            skills = Skill.data[locale]['skills'][subtype]

        elif locale and not subtype:
            skills = []
            self.get_skills(locale)
            for subtype in Skill.data[locale]['skills']:
                skills.extend(Skill.data[locale]['skills'][subtype])

        elif subtype and not locale:
            skills = []
            for locale in LOCALES:
                self.get_skills(locale)
                if subtype not in Skill.data[locale]['skills']:
                    raise ParameterError('Not valid subtype')
                skills.extend(Skill.data[locale]['skills'][subtype])

        else:
            skills = self.all_skills()

        random.shuffle(skills)

        if total:
            if not isinstance(total, int):
                raise ParameterError('Not valid total')
            return skills[0:total]

        return skills

