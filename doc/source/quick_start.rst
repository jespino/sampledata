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
