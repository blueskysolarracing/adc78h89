Usage
=====

Both high and low level interactions are supported by this library.

High-level Usage
----------------

The examples of high-level usages are shown below.

.. code-block:: pycon

   >>> from adc78h89 import ADC78H89
   >>> from periphery import SPI
   >>> spi = SPI('/dev/spidev0.0', 3, 1e6)
   >>> adc78h89 = ADC78H89(spi)
   >>> voltages = adc78h89.sample_all()
   >>> voltages
   {<InputChannel.AIN1: 0>: 1.4142135623730951, <InputChannel.AIN2: 1>: 1.25...}
   >>> voltages[ADC78H89.InputChannel.AIN1]
   1.4142135623730951
   >>> voltages[ADC78H89.InputChannel.GROUND]
   0.0

Low-level Usage
---------------

The examples of low-level usages are shown below. Note that the returned voltage
corresponds to the previous input channel. The voltage at the passed input
channel will be returned on the next call.

.. code-block:: pycon

   >>> from adc78h89 import ADC78H89
   >>> from periphery import SPI
   >>> spi = SPI('/dev/spidev0.0', 3, 1e6)
   >>> adc78h89 = ADC78H89(spi)
   >>> adc78h89.sample(InputChannel.GROUND)
   [0.47140452079103173]
   >>> adc78h89.sample(InputChannel.AIN1)
   [0]
   >>> adc78h89.sample(InputChannel.AIN1, GROUND, InputChannel.AIN1)
   [1.4142135623730951, 1.4142135623730951, 0]
