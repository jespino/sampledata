Sample Data
===========

.. image:: https://travis-ci.org/jespino/sampledata.png?branch=master
    :target: https://travis-ci.org/jespino/sampledata

.. image:: https://coveralls.io/repos/jespino/sampledata/badge.png?branch=master
    :target: https://coveralls.io/r/jespino/sampledata?branch=master

.. image:: https://pypip.in/v/sampledata/badge.png
    :target: https://crate.io/packages/sampledata

.. image:: https://pypip.in/d/sampledata/badge.png
    :target: https://crate.io/packages/sampledata

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
