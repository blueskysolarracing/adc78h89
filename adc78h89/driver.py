from collections import deque
from dataclasses import dataclass
from enum import IntEnum
from typing import ClassVar
from warnings import warn

from periphery import SPI


@dataclass
class ADC78H89:
    """The class for Texas Instruments ADC78H89 7-Channel, 500 KSPS,
    12-Bit A/D Converter.
    """

    class InputChannel(IntEnum):
        """The enum class for input channels."""

        AIN1: int = 0
        """The first (default) input channel."""
        AIN2: int = 1
        """The second input channel."""
        AIN3: int = 2
        """The third input channel."""
        AIN4: int = 3
        """The fourth input channel."""
        AIN5: int = 4
        """The fifth input channel."""
        AIN6: int = 5
        """The fifth input channel."""
        AIN7: int = 6
        """The seventh input channel."""
        GROUND: int = 7
        """The ground input channel."""

    SPI_MODE: ClassVar[int] = 3
    """The supported spi mode."""
    MIN_SPI_MAX_SPEED: ClassVar[float] = 5e5
    """The supported minimum spi maximum speed."""
    MAX_SPI_MAX_SPEED: ClassVar[float] = 8e6
    """The supported maximum spi maximum speed."""
    SPI_BIT_ORDER: ClassVar[str] = 'msb'
    """The supported spi bit order."""
    SPI_WORD_BIT_COUNT: ClassVar[int] = 8
    """The supported spi number of bits per word."""
    OFFSET: ClassVar[int] = 3
    """The input channel bit offset for control register bits."""
    REFERENCE_VOLTAGE: ClassVar[float] = 3.3
    """The reference voltage value (in volts)."""
    DIVISOR: ClassVar[float] = 4096
    """The lsb width for ADC78H89."""
    DEFAULT_INPUT_CHANNEL: ClassVar[InputChannel] = InputChannel(0)
    """The default input channel."""
    spi: SPI
    """The SPI for the ADC device."""
    previous_input_channel: InputChannel = DEFAULT_INPUT_CHANNEL
    """The previous input channel."""

    def __post_init__(self) -> None:
        if self.spi.mode != self.SPI_MODE:
            raise ValueError('unsupported spi mode')
        elif not (
                self.MIN_SPI_MAX_SPEED
                <= self.spi.max_speed
                <= self.MAX_SPI_MAX_SPEED
        ):
            raise ValueError('unsupported spi maximum speed')
        elif self.spi.bit_order != self.SPI_BIT_ORDER:
            raise ValueError('unsupported spi bit order')
        elif self.spi.bits_per_word != self.SPI_WORD_BIT_COUNT:
            raise ValueError('unsupported spi number of bits per word')

        if self.spi.extra_flags:
            warn(f'unknown spi extra flags {self.spi.extra_flags}')

    def get_voltage(self, next_input_channel: InputChannel) -> float:
        """Return the voltage of the previous input channel.

        :param next_input_channel: The next input channel.
        :return: The voltage of the previous input channel.
        """
        self.previous_input_channel = next_input_channel
        transmitted_data = [(next_input_channel << self.OFFSET), 0]
        received_data = self.spi.transfer(transmitted_data)

        assert len(received_data) == 2

        raw_data = (
            received_data[0] << self.SPI_WORD_BIT_COUNT | received_data[1]
        )

        return self.REFERENCE_VOLTAGE * raw_data / self.DIVISOR

    def get_voltages(self) -> dict[InputChannel, float]:
        """Return the voltages of all input channels.

        :return: The voltages of all input channels.
        """
        input_channels = deque(self.InputChannel)

        assert input_channels

        self.get_voltage(input_channels[0])
        input_channels.rotate(-1)

        voltages = {}

        for input_channel in input_channels:
            previous_input_channel = self.previous_input_channel
            voltages[previous_input_channel] = self.get_voltage(input_channel)

        return voltages
