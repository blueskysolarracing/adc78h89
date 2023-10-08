========
ADC78H89
========

ADC78H89 is a Python driver for Texas Instruments ADC78H89 7-Channel, 500 KSPS,
12-Bit A/D Converter.

Features
--------

- High-level hardware usage.
- Low-level hardware usage.

Installation
------------

.. code-block:: bash

   pip install adc78h89

Usage
-----

Below shows a sample usage of ADC78H89.

.. code-block:: python

   from adc78h89 import ADC78H89
   from periphery import SPI

   spi = SPI('/dev/spidev0.0', 3, 1e6)
   adc78h89 = ADC78H89(spi)
   voltages = adc78h89.sample_all()

   print(voltages[ADC78H89.InputChannel.AIN1])
   print(voltages[ADC78H89.InputChannel.GROUND])

Testing and Validation
----------------------

ADC78H89 has extensive test coverage, passes mypy static type checking with
strict parameter, and has been validated through extensive use in real-life
scenarios.

Contributing
------------

Contributions are welcome! Please read our Contributing Guide for more
information.

License
-------

ADC78H89 is distributed under the MIT license.
