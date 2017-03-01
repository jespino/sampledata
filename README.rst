Sample Data
===========

.. image:: https://img.shields.io/travis/jespino/sampledata/master.svg
    :target: https://travis-ci.org/jespino/sampledata

.. image:: https://img.shields.io/coveralls/jespino/sampledata.svg
    :target: https://coveralls.io/r/jespino/sampledata?branch=master

.. image:: https://img.shields.io/pypi/v/sampledata.svg
    :target: https://pypi.python.org/pypi/sampledata


App to automatically populate django database.

Install
=======

Install using pip, including any pillow if you want image genetion...:

.. code:: bash

  pip install sampledata
  pip install pillow  # For image generation


Quick start
===========

You can build any kind of object using the :code:`SampleData` class.

.. code:: python

  from sampledata.helper import SampleData

  def generate_random_users(instances):
      sd = SampleData(seed=123)

      users = []
      for x in range(instances):
          data = {
              "slug": sd.slug(2, 3),
              "name": sd.name('us'),
              "claim": sd.sentence(),
              "description": sd.paragraph(),
              "email": sd.email(),
              "photo": sd.image_stream(64, 64),
              "is_active": sd.boolean(),
              "birth_date": sd.past_date(),
              "expected_death_date": sd.future_date(),
          }
          users.append(data)
      return users


Documentation
-------------

Read the Docs: https://sampledata.readthedocs.org/en/latest/
