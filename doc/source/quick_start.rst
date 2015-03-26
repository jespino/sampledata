Quick start
===========

You can build any kind of object using the :code:`SampleData` class.

.. code:: python

  def generate_random_users(instances):
      sd = SampleData(seed=123)

      users = []
      for x in range(instances):
          data = {
              "slug": sd.slug(2, 3),
              "name": sd.name(2, 3),
              "claim": sd.sentence(),
              "description": sd.paragraph(),
              "email": sd.email(),
              "photo": sd.image_stream(64, 64),
              "is_active": sd.boolean(),
              "birth_date": sd.past_date(),
              "expected_death_date": sd.future_date(),
          }
          users.append(instance)
      return users
