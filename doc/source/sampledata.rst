SampleData
==========

.. py:class:: SampleData(seed=None)

    SampleData easy the random data generation for a lot of common used
    data types.

Number methods
--------------

.. py:method:: SampleData.int(min_value=0, max_value=sys.maxsize)

    Return an integer between min_value and max_value

.. py:method:: SampleData.number(ndigits)

    Return a number of n digits as max

.. py:method:: SampleData.digits(ndigits)

    Return a number of exactly n digits

.. py:method:: SampleData.float(min, max)

    Return a float from min to max

.. py:method:: SampleData.number_string(ndigits)

    Return a string of n digits

Text methods
------------

.. py:method:: SampleData.char()

    Return a character between A-Z and a-z

.. py:method:: SampleData.chars(min_chars=1, max_chars=5)

    Return a string with n characters between A-Z and a-z being
    min_chars <= n <= max_chars

.. py:method:: SampleData.word()

    Returns a lorem ipsum word

.. py:method:: SampleData.words(min_words=1, max_words=5)

    Return a string with n lorem ipsum words being
    min_words <= n <= max_words

.. py:method:: SampleData.email()

    Return an email

.. py:method:: SampleData.url()

    Return an url

.. py:method:: SampleData.sentence()

    Return a lorem ipsum sentence (limited to 255 caracters)

.. py:method:: SampleData.short_sentence()

    Return a lorem ipsum sentence (limited to 100 caracters)

.. py:method:: SampleData.long_sentence()

    Return a lorem ipsum sentence (with 150 caracters or more)

.. py:method:: SampleData.paragraph()

    Return a lorem ipsum paragraph

.. py:method:: SampleData.paragraphs(min_paragraphs=1, max_paragraphs=5)

    Return a lorem ipsum text with n paragraphs being
    min_paragraphs <= n <= max_paragraphs

.. py:method:: SampleData.slug(min_words=5, max_words=5)

    Return a lorem ipsum slug between with n words being
    min_words <= n <= max_words

.. py:method:: SampleData.tags(min_tags=1, max_tags=5, tags_list=None)

    Return a string of n tags_list or lorem ipsum tags separated by commas
    being n max min_tags <= n <= max_tags

Time methods
------------

.. py:method:: SampleData.date(begin=-365, end=365)

    Return a date between now+begin and now+end in days

.. py:method:: SampleData.date_between(min_date, max_date)

    Return a date between the min_date and max_date date objects

.. py:method:: SampleData.future_date(min_distance=0, max_distance=365)

    Return a future date between now+min_distance and now+max_distance in days

.. py:method:: SampleData.past_date(min_distance=0, max_distance=365)

    Return a past date between now-max_distance and now-min_distance in days

.. py:method:: SampleData.datetime(begin=-1440, end=1440)

    Return a datetime between now+begin and now+end in minutes

.. py:method:: SampleData.datetime_between(min_datetime, max_datetime)

    Return a datetime between the min_datetime and max_datetime datetime objects

.. py:method:: SampleData.future_datetime(min_distance=0, max_distance=1440)

    Return a future datetime between now+min_distance and now+max_distance in minutes

.. py:method:: SampleData.past_datetime(min_distance=0, max_distance=1440)

    Return a past datetime between now-max_distance and now-min_distance in minutes

.. py:method:: SampleData.time()

    Return a time


Localized methods
-----------------

.. py:method:: SampleData.name(locale=None, number=1, as_list=False)

    Return a string or list of tipical names from locale using n names (compound names)

    Supported locales: cat, es, fr, us

.. py:method:: SampleData.surname(locale=None, number=1, as_list=False)

    Return a string or list of tipical surnames from locale using n surnames

    Supported locales: cat, es, fr, us

.. py:method:: SampleData.fullname(locale=None, as_list=False)

    Return a string or list of tipical names+surnames from locale

    Supported locales: cat, es, fr, us

.. py:method:: SampleData.phone(locale, country_code)

    Return a phone number from a country with or without country code

    Supported locales: es

.. py:method:: SampleData.zip_code(locale)

    Return a zip code for a country

    Supported locales: es

.. py:method:: SampleData.state_code(locale)

    Return a state code for the locale country.

    Supported locales: es, us

.. py:method:: SampleData.id_card(locale)

    Return a identification card code for a country

    Supported locales: es

Image methods
-------------

.. py:method:: SampleData.image_stream(width, height, typ="simple")

    Return an image of width x height size generated with the typ generator.

    Available typ generators: simple, plasma, mandelbrot, ifs, random

.. py:method:: SampleData.image_path_from_directory(directory_path, valid_extensions=['.jpg', '.bmp', '.png'])

    Return an image from a directory with a valid extension

Other methods
-------------

.. py:method:: SampleData.boolean()

    Return a boolean value

.. py:method:: SampleData.nullboolean()

    Return a boolean value or a None

.. py:method:: SampleData.ipv4()

    Return a ipv4 address

.. py:method:: SampleData.ipv6()

    Return a ipv6 address

.. py:method:: SampleData.mac_address()

    Return a mac address

.. py:method:: SampleData.hex_chars(min_chars=1, max_chars=5)

    Return a string with n characters between a-f and 0-9 being
    min_chars <= n <= max_chars

.. py:method:: SampleData.path(absolute=None, extension='', min_levels=1, max_levels=5)

    Return a absolute or relative path (based on `absolute` parameter) string
    finished in `extension`, and with n levels being min_levels <= n <= max_levels

.. py:method:: SampleData.choice(choices)

    Return a value from a list
