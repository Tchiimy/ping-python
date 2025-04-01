
from brping import definitions
from brping import Ping1D
from brping import pingmessage

class Omniscan450(Ping1D):
    ##
    # @brief Get a os_mono_profile message from the device\n
    # Message description:\n
    # A detailed measurement of signal strength at all depths within the ping range.
    #
    # @return None if there is no reply from the device, otherwise a dictionary with the following keys:\n
    # ping_number: Sequentially assigned ping number from 0 at power up.\n
    # start_mm: Units: mm; Start of the measurement range in mm.\n
    # length_mm: Units: mm; Length of the measurement range in mm.\n
    # timestamp_ms: Milliseconds since power up at time of ping.\n
    # ping_hz: Ping frequency in Hz. Default is 450000 Hz.\n
    # gain_index: Gain index used during the measurement (0-7).\n
    # num_results: Length of pwr_results array.\n
    # sos_dmps: Speed of sound in decimeters per second.\n
    # channel_number: Channel number (0).\n
    # reserved: Set to 0.\n
    # pulse_duration_sec: Duration of the acoustic pulse in seconds.\n
    # analog_gain: Analog gain applied during measurement.\n
    # max_pwr_db: Maximum power in dB.\n
    # min_pwr_db: Minimum power in dB.\n
    # transducer_heading_deg: Heading of the transducer in degrees.\n
    # vehicle_heading_deg: Heading of the vehicle in degrees.\n
    # pwr_results: Power results scaled from min_pwr_db to max_pwr_db. Number of entries equals num_results.\n
    def get_os_mono_profile(self):
        if self.legacyRequest(definitions.OMNISCAN450_OS_MONO_PROFILE) is None:
            return None
        data = ({
            "ping_number": self._ping_number,  # Sequentially assigned ping number from 0 at power up.
            "start_mm": self._start_mm,  # Units: mm; Start of the measurement range in mm.
            "length_mm": self._length_mm,  # Units: mm; Length of the measurement range in mm.
            "timestamp_ms": self._timestamp_ms,  # Milliseconds since power up at time of ping.
            "ping_hz": self._ping_hz,  # Ping frequency in Hz. Default is 450000 Hz.
            "gain_index": self._gain_index,  # Gain index used during the measurement (0-7).
            "num_results": self._num_results,  # Length of pwr_results array.
            "sos_dmps": self._sos_dmps,  # Speed of sound in decimeters per second.
            "channel_number": self._channel_number,  # Channel number (0).
            "reserved": self._reserved,  # Set to 0.
            "pulse_duration_sec": self._pulse_duration_sec,  # Duration of the acoustic pulse in seconds.
            "analog_gain": self._analog_gain,  # Analog gain applied during measurement.
            "max_pwr_db": self._max_pwr_db,  # Maximum power in dB.
            "min_pwr_db": self._min_pwr_db,  # Minimum power in dB.
            "transducer_heading_deg": self._transducer_heading_deg,  # Heading of the transducer in degrees.
            "vehicle_heading_deg": self._vehicle_heading_deg,  # Heading of the vehicle in degrees.
            "pwr_results": self._pwr_results,  # Power results scaled from min_pwr_db to max_pwr_db. Number of entries equals num_results.
        })
        return data

    ##
    # @brief Send a os_ping_params message to the device\n
    # Message description:\n
    # Configure ping parameters.\n
    # Send the message to write the device parameters, then read the values back from the device\n
    #
    # @param start_mm - Units: mm; Start of ping range, set to 0.
    # @param length_mm - Units: mm; Length of the returned profile. End of range = start_mm + length_mm.
    # @param msec_per_ping - Units: ms; Normally set to 0 for best ping rate. Set value to limit ping rate.
    # @param reserved - Set to 0.
    # @param reserved - Set to 0.
    # @param pulse_len_percent - % of total ping time for current range. 0.002 typical.
    # @param filter_duration_percent - 0.0015 typical.
    # @param gain_index - Set to -1 for auto gain, otherwise 0-7 sets gain.
    # @param number_of_signal_data_points - Number of signal data points in resulting profile. 200-1200, 600 typical.
    # @param enable - 1 or 0 to enable or disable pinging.
    # @param reserved - Set to 0.
    #
    # @return If verify is False, True on successful communication with the device. If verify is False, True if the new device parameters are verified to have been written correctly. False otherwise (failure to read values back or on verification failure)
    def os_ping_params(self, start_mm, length_mm, msec_per_ping, pulse_len_percent, 
                    filter_duration_percent, gain_index, number_of_signal_data_points, 
                    enable, verify=True):
        """Set OS ping parameters with input validation.
        
        Args:
            start_mm (u32): Start of ping range (0 or positive)
            length_mm (u32): Length of the returned profile
            msec_per_ping (u32): Normally 0 for best ping rate
            pulse_len_percent (float): % of total ping time (0.002 typical)
            filter_duration_percent (float): (0.0015 typical)
            gain_index (i16): -1 for auto gain, otherwise 0-7
            number_of_signal_data_points (u16): 200-1200 (600 typical)
            enable (u8): 1 or 0 to enable/disable pinging
            verify (bool): Whether to validate inputs (default True)
        """
        if verify:
            # Validate types and ranges
            if not isinstance(start_mm, int) or start_mm < 0:
                raise ValueError("start_mm must be a positive integer (u32)")
            if not isinstance(length_mm, int) or length_mm <= 0:
                raise ValueError("length_mm must be a positive integer (u32)")
            if not isinstance(msec_per_ping, int) or msec_per_ping < 0:
                raise ValueError("msec_per_ping must be a non-negative integer (u32)")
            if not isinstance(pulse_len_percent, (int, float)) or pulse_len_percent <= 0:
                raise ValueError("pulse_len_percent must be a positive float")
            if not isinstance(filter_duration_percent, (int, float)) or filter_duration_percent <= 0:
                raise ValueError("filter_duration_percent must be a positive float")
            if not isinstance(gain_index, int) or gain_index < -1 or gain_index > 7:
                raise ValueError("gain_index must be -1 (auto) or 0-7")
            if not isinstance(number_of_signal_data_points, int) or \
            number_of_signal_data_points < 200 or number_of_signal_data_points > 1200:
                raise ValueError("number_of_signal_data_points must be between 200-1200")
            if not isinstance(enable, int) or enable not in (0, 1):
                raise ValueError("enable must be 0 or 1")

        m = pingmessage.PingMessage(definitions.OMNISCAN450_OS_PING_PARAMS)
        m.start_mm = start_mm
        m.length_mm = length_mm
        m.msec_per_ping = msec_per_ping
        m.reserved1 = 0.0  # float
        m.reserved2 = 0.0  # float
        m.pulse_len_percent = pulse_len_percent
        m.filter_duration_percent = filter_duration_percent
        m.gain_index = gain_index
        m.number_of_signal_data_points = number_of_signal_data_points
        m.enable = enable
        m.reserved3 = 0
        m.pack_msg_data()
        self.write(m.msg_data)
    ##
    # @brief Send a set_speed_of_sound message to the device\n
    # Message description:\n
    # Set the speed of sound used for distance calculations.\n
    # Send the message to write the device parameters, then read the values back from the device\n
    #
    # @param sos_mm_per_sec - The speed of sound in mm/sec. Default value is 15000000 mm/sec (1500 meters/sec).
    #
    # @return If verify is False, True on successful communication with the device. If verify is False, True if the new device parameters are verified to have been written correctly. False otherwise (failure to read values back or on verification failure)
    def set_speed_of_sound(self, sos_mm_per_sec, verify=True):
        m = pingmessage.PingMessage(definitions.OMNISCAN450_SET_SPEED_OF_SOUND)
        m.sos_mm_per_sec = sos_mm_per_sec
        m.pack_msg_data()
        self.write(m.msg_data)
        if self.legacyRequest(definitions.OMNISCAN450_SPEED_OF_SOUND) is None:
            return False
        # Read back the data and check that changes have been applied
        if (verify
                and (self._sos_mm_per_sec != sos_mm_per_sec)):
            return False
        return True  # success
    

if __name__ == "__main__":
    import time
    import sys 
    import numpy as np
    import os 


    device = Omniscan450()

    
    device.connect_udp("192.168.2.92",51200)

    print(dir(device))

    test = device.my_id
    print(test)

    device.os_ping_params(start_mm=0,
                            length_mm=1000,
                            msec_per_ping=1000,
                            pulse_len_percent=0.002,
                            filter_duration_percent=0.0015,
                            gain_index=1,
                            number_of_signal_data_points=250,
                            enable=1,
                            verify=True)
    
    time.sleep(1)

    # get the os_mono_profile from the device 
    data = device.get_os_mono_profile()

    device.os_ping_params(start_mm=0,
                            length_mm=1000,
                            msec_per_ping=1000,
                            pulse_len_percent=0.002,
                            filter_duration_percent=0.0015,
                            gain_index=1,
                            number_of_signal_data_points=200,
                            enable=0,
                            verify=True)

    print(data)
    # Assuming 'data' is your dictionary containing the ping data
    binary_data = data["pwr_results"]
    print(len(binary_data))

    # Convert the binary data to a numpy array of uint16
    power_results = np.frombuffer(binary_data, dtype=np.uint16)

    print(len(power_results))  # This should now work correctly
    print(power_results)