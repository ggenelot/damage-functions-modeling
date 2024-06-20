Usage
=====

.. _installation:

Installation
------------

To use Lumache, first install it using pip:

.. code-block:: console

   (.venv) $ pip install lumache

Creating recipes
----------------

To retrieve a list of random ingredients,
you can use the ``lumache.get_random_ingredients()`` function:

.. autofunction:: lumache.get_random_ingredients

The ``kind`` parameter should be either ``"meat"``, ``"fish"``,
or ``"veggies"``. Otherwise, :py:func:`lumache.get_random_ingredients`
will raise an exception.

.. autofunction:: fund.fund_a2_agricultural_impact_of_the_rate_of_climate_change

.. autoexception:: lumache.InvalidKindError

.. autofunction:: fund.fund_a2_agricultural_impact_of_the_rate_of_climate_change