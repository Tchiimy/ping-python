
from brping import definitions
from brping import Ping1D
from brping import pingmessage

class PingS500(Ping1D):
    ##
    # @brief Get a altitude message from the device\n
    # Message description:\n
    # The result of the most recent distance calculation.
    #
    # @return None if there is no reply from the device, otherwise a dictionary with the following keys:\n
    # altitude_mm: Units: mm; Most recent calculated distance from the device to the target.\n
    # quality: Units: %; Confidence in the distance measurement.\n
    def get_altitude(self):
        if self.legacyRequest(definitions.PINGS500_ALTITUDE) is None:
            return None
        data = ({
            "altitude_mm": self._altitude_mm,  # Units: mm; Most recent calculated distance from the device to the target.
            "quality": self._quality,  # Units: %; Confidence in the distance measurement.
        })
        return data

    ##
    # @brief Get a distance2 message from the device\n
    # Message description:\n
    # A simple distance measurement.
    #
    # @return None if there is no reply from the device, otherwise a dictionary with the following keys:\n
    # this_ping_distance_mm: Most recent ping distance measurement in mm.\n
    # averaged_distance_mm: Averaged distance over the last 20 pings in mm.\n
    # reserved: Reserved field.\n
    # this_ping_confidence: Confidence in this ping measurement (0-100).\n
    # confidence_of_averaged_distance: Confidence in the averaged distance measurement (0-100).\n
    # timestamp: Timestamp in milliseconds.\n
    def get_distance2(self):
        if self.legacyRequest(definitions.PINGS500_DISTANCE2) is None:
            return None
        data = ({
            "this_ping_distance_mm": self._this_ping_distance_mm,  # Most recent ping distance measurement in mm.
            "averaged_distance_mm": self._averaged_distance_mm,  # Averaged distance over the last 20 pings in mm.
            "reserved": self._reserved,  # Reserved field.
            "this_ping_confidence": self._this_ping_confidence,  # Confidence in this ping measurement (0-100).
            "confidence_of_averaged_distance": self._confidence_of_averaged_distance,  # Confidence in the averaged distance measurement (0-100).
            "timestamp": self._timestamp,  # Timestamp in milliseconds.
        })
        return data

    ##
    # @brief Get a fw_version message from the device\n
    # Message description:\n
    # Device information
    #
    # @return None if there is no reply from the device, otherwise a dictionary with the following keys:\n
    # device_type: Device type\n
    # device_model: Device model\n
    # version_major: Firmware version major number.\n
    # version_minor: Firmware version minor number.\n
    def get_fw_version(self):
        if self.legacyRequest(definitions.PINGS500_FW_VERSION) is None:
            return None
        data = ({
            "device_type": self._device_type,  # Device type
            "device_model": self._device_model,  # Device model
            "version_major": self._version_major,  # Firmware version major number.
            "version_minor": self._version_minor,  # Firmware version minor number.
        })
        return data

    ##
    # @brief Get a gain_index message from the device\n
    # Message description:\n
    # The current gain setting.
    #
    # @return None if there is no reply from the device, otherwise a dictionary with the following keys:\n
    # gain_index: The current gain index setting.\n
    def get_gain_index(self):
        if self.legacyRequest(definitions.PINGS500_GAIN_INDEX) is None:
            return None
        data = ({
            "gain_index": self._gain_index,  # The current gain index setting.
        })
        return data

    ##
    # @brief Get a ping_rate_msec message from the device\n
    # Message description:\n
    # The interval between acoustic measurements.
    #
    # @return None if there is no reply from the device, otherwise a dictionary with the following keys:\n
    # msec_per_ping: Units: ms; Minimum time between successive pings. Can be longer depending on range.\n
    def get_ping_rate_msec(self):
        if self.legacyRequest(definitions.PINGS500_PING_RATE_MSEC) is None:
            return None
        data = ({
            "msec_per_ping": self._msec_per_ping,  # Units: ms; Minimum time between successive pings. Can be longer depending on range.
        })
        return data

    ##
    # @brief Get a processor_degC message from the device\n
    # Message description:\n
    # Temperature of the device CPU.
    #
    # @return None if there is no reply from the device, otherwise a dictionary with the following keys:\n
    # centi_degC: Units: cC; The temperature in centi-degrees Centigrade (100 * degrees C).\n
    def get_processor_degC(self):
        if self.legacyRequest(definitions.PINGS500_PROCESSOR_DEGC) is None:
            return None
        data = ({
            "centi_degC": self._centi_degC,  # Units: cC; The temperature in centi-degrees Centigrade (100 * degrees C).
        })
        return data

    ##
    # @brief Get a profile6_t message from the device\n
    # Message description:\n
    # A detailed measurement of signal strength at all depths within the ping range.
    #
    # @return None if there is no reply from the device, otherwise a dictionary with the following keys:\n
    # ping_number: Sequentially assigned ping number from 0 at power up.\n
    # start_mm: Start of the measurement range in mm.\n
    # length_mm: Length of the measurement range in mm.\n
    # start_ping_hz: Starting frequency of the ping in Hz.\n
    # end_ping_hz: Ending frequency of the ping in Hz.\n
    # adc_sample_hz: Sampling frequency of the ADC in Hz.\n
    # timestamp_msec: Timestamp in milliseconds.\n
    # spare2: Reserved field.\n
    # pulse_duration_sec: Duration of the acoustic pulse in seconds.\n
    # analog_gain: Analog gain applied during measurement.\n
    # max_pwr_db: Maximum power in dB.\n
    # min_pwr_db: Minimum power in dB.\n
    # this_ping_depth_m: Depth in meters as calculated from the most recent ping.\n
    # smooth_depth_m: Smoothed calculated depth in meters.\n
    # fspare2: Reserved field, set to 0.\n
    # this_ping_depth_confidence: Confidence in the depth measurement based on the most recent ping (0-100).\n
    # gain_index: Gain index used during the measurement.\n
    # decimation: Decimation setting affecting range resolution.\n
    # smooth_depth_confidence: Confidence in the smoothed depth measurement (0-100).\n
    # num_results: lenght of the pwr_results array.\n
    # pwr_results: Power results scaled from min_pwr to max_pwr. Number of entries equals num_results.\n
    def get_profile6_t(self):
        if self.legacyRequest(definitions.PINGS500_PROFILE6_T) is None:
            return None
        data = ({
            "ping_number": self._ping_number,  # Sequentially assigned ping number from 0 at power up.
            "start_mm": self._start_mm,  # Start of the measurement range in mm.
            "length_mm": self._length_mm,  # Length of the measurement range in mm.
            "start_ping_hz": self._start_ping_hz,  # Starting frequency of the ping in Hz.
            "end_ping_hz": self._end_ping_hz,  # Ending frequency of the ping in Hz.
            "adc_sample_hz": self._adc_sample_hz,  # Sampling frequency of the ADC in Hz.
            "timestamp_msec": self._timestamp_msec,  # Timestamp in milliseconds.
            "spare2": self._spare2,  # Reserved field.
            "pulse_duration_sec": self._pulse_duration_sec,  # Duration of the acoustic pulse in seconds.
            "analog_gain": self._analog_gain,  # Analog gain applied during measurement.
            "max_pwr_db": self._max_pwr_db,  # Maximum power in dB.
            "min_pwr_db": self._min_pwr_db,  # Minimum power in dB.
            "this_ping_depth_m": self._this_ping_depth_m,  # Depth in meters as calculated from the most recent ping.
            "smooth_depth_m": self._smooth_depth_m,  # Smoothed calculated depth in meters.
            "fspare2": self._fspare2,  # Reserved field, set to 0.
            "this_ping_depth_confidence": self._this_ping_depth_confidence,  # Confidence in the depth measurement based on the most recent ping (0-100).
            "gain_index": self._gain_index,  # Gain index used during the measurement.
            "decimation": self._decimation,  # Decimation setting affecting range resolution.
            "smooth_depth_confidence": self._smooth_depth_confidence,  # Confidence in the smoothed depth measurement (0-100).
            "num_results": self._num_results,  # lenght of the pwr_results array.
            "pwr_results": self._pwr_results,  # Power results scaled from min_pwr to max_pwr. Number of entries equals num_results.
        })
        return data

    ##
    # @brief Get a range message from the device\n
    # Message description:\n
    # The scan range for acoustic measurements.
    #
    # @return None if there is no reply from the device, otherwise a dictionary with the following keys:\n
    # start_mm: Units: mm; The beginning of the scan range in mm from the transducer.\n
    # length_mm: Units: mm; Length of the scan range. Measurements will be within start_mm and start_mm + length_mm.\n
    def get_range(self):
        if self.legacyRequest(definitions.PINGS500_RANGE) is None:
            return None
        data = ({
            "start_mm": self._start_mm,  # Units: mm; The beginning of the scan range in mm from the transducer.
            "length_mm": self._length_mm,  # Units: mm; Length of the scan range. Measurements will be within start_mm and start_mm + length_mm.
        })
        return data

    ##
    # @brief Get a speed_of_sound message from the device\n
    # Message description:\n
    # The speed of sound used for distance calculations.
    #
    # @return None if there is no reply from the device, otherwise a dictionary with the following keys:\n
    # sos_mm_per_sec: Units: mm/s; Current speed of sound setting in mm/sec. Default is 1500000 mm/sec.\n
    def get_speed_of_sound(self):
        if self.legacyRequest(definitions.PINGS500_SPEED_OF_SOUND) is None:
            return None
        data = ({
            "sos_mm_per_sec": self._sos_mm_per_sec,  # Units: mm/s; Current speed of sound setting in mm/sec. Default is 1500000 mm/sec.
        })
        return data

    ##
    # @brief Send a set_device_id message to the device\n
    # Message description:\n
    # Set the device ID.\n
    # Send the message to write the device parameters, then read the values back from the device\n
    #
    # @param device_id - Device ID (0-254). 255 is reserved for broadcast messages.
    #
    # @return If verify is False, True on successful communication with the device. If verify is False, True if the new device parameters are verified to have been written correctly. False otherwise (failure to read values back or on verification failure)
    def set_device_id(self, device_id, verify=True):
        m = pingmessage.PingMessage(definitions.PINGS500_SET_DEVICE_ID)
        m.device_id = device_id
        m.pack_msg_data()
        self.write(m.msg_data)
        if self.legacyRequest(definitions.PINGS500_DEVICE_ID) is None:
            return False
        # Read back the data and check that changes have been applied
        if (verify
                and (self._device_id != device_id)):
            return False
        return True  # success

    ##
    # @brief Send a set_ping_params message to the device\n
    # Message description:\n
    # Configure ping parameters.\n
    # Send the message to write the device parameters, then read the values back from the device\n
    #
    # @param start_mm - Units: mm; Start of ping range, normally 0.
    # @param length_mm - Units: mm; Length of the returned profile. End of range = start_mm + length_mm. Set to 0 for auto range.
    # @param gain_index - Set to -1 for auto gain, otherwise 0-13 sets gain for manual gain.
    # @param msec_per_ping - Units: ms; Set to -1 to start a single ping. Otherwise, sets minimum ping interval.
    # @param pulse_len_usec - Units: µs; Set to 0 for auto mode. Currently ignored and auto duration is always used.
    # @param report_id - The ID of the packet type you want in response. Options: distance2 (1223), profile6 (1308), or zero. Zero disables pinging.
    # @param reserved - Set to 0.
    # @param chirp - Set to 1 for chirp, 0 for monotone ping.
    # @param decimation - Set to 0 for auto range resolution in chirp mode.
    #
    # @return If verify is False, True on successful communication with the device. If verify is False, True if the new device parameters are verified to have been written correctly. False otherwise (failure to read values back or on verification failure)
    def set_ping_params(self, start_mm, length_mm, gain_index, msec_per_ping, pulse_len_usec, report_id, reserved, chirp, decimation, verify=True):
        m = pingmessage.PingMessage(definitions.PINGS500_SET_PING_PARAMS)
        m.start_mm = start_mm
        m.length_mm = length_mm
        m.gain_index = gain_index
        m.msec_per_ping = msec_per_ping
        m.pulse_len_usec = pulse_len_usec
        m.report_id = report_id
        m.reserved = reserved
        m.chirp = chirp
        m.decimation = decimation
        m.pack_msg_data()
        self.write(m.msg_data)
        if self.legacyRequest(definitions.PINGS500_PING_PARAMS) is None:
            return False
        # Read back the data and check that changes have been applied
        if (verify
                and (self._start_mm != start_mm or self._length_mm != length_mm or self._gain_index != gain_index or self._msec_per_ping != msec_per_ping or self._pulse_len_usec != pulse_len_usec or self._report_id != report_id or self._reserved != reserved or self._chirp != chirp or self._decimation != decimation)):
            return False
        return True  # success

    ##
    # @brief Send a set_speed_of_sound message to the device\n
    # Message description:\n
    # Set the speed of sound used for distance calculations.\n
    # Send the message to write the device parameters, then read the values back from the device\n
    #
    # @param sos_mm_per_sec - The speed of sound in mm/sec. Default is 15000000 mm/sec (1500 m/sec).
    #
    # @return If verify is False, True on successful communication with the device. If verify is False, True if the new device parameters are verified to have been written correctly. False otherwise (failure to read values back or on verification failure)
    def set_speed_of_sound(self, sos_mm_per_sec, verify=True):
        m = pingmessage.PingMessage(definitions.PINGS500_SET_SPEED_OF_SOUND)
        m.sos_mm_per_sec = sos_mm_per_sec
        m.pack_msg_data()
        self.write(m.msg_data)
        if self.legacyRequest(definitions.PINGS500_SPEED_OF_SOUND) is None:
            return False
        # Read back the data and check that changes have been applied
        if (verify
                and (self._sos_mm_per_sec != sos_mm_per_sec)):
            return False
        return True  # success



if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="Ping python library example.")
    parser.add_argument('--device', action="store", required=False, type=str, help="Ping device port. E.g: /dev/ttyUSB0")
    parser.add_argument('--baudrate', action="store", type=int, default=115200, help="Ping device baudrate. E.g: 115200")
    parser.add_argument('--udp', action="store", required=False, type=str, help="Ping UDP server. E.g: 192.168.2.2:9090")
    args = parser.parse_args()
    if args.device is None and args.udp is None:
        parser.print_help()
        exit(1)

    p = PingS500()
    if args.device is not None:
        p.connect_serial(args.device, args.baudrate)
    elif args.udp is not None:
        (host, port) = args.udp.split(':')
        p.connect_udp(host, int(port))

    print("Initialized: %s" % p.initialize())

    print("\ntesting get_altitude")
    result = p.get_altitude()
    print("  " + str(result))
    print("  > > pass: %s < <" % (result is not None))

    print("\ntesting get_distance2")
    result = p.get_distance2()
    print("  " + str(result))
    print("  > > pass: %s < <" % (result is not None))

    print("\ntesting get_fw_version")
    result = p.get_fw_version()
    print("  " + str(result))
    print("  > > pass: %s < <" % (result is not None))

    print("\ntesting get_gain_index")
    result = p.get_gain_index()
    print("  " + str(result))
    print("  > > pass: %s < <" % (result is not None))

    print("\ntesting get_ping_rate_msec")
    result = p.get_ping_rate_msec()
    print("  " + str(result))
    print("  > > pass: %s < <" % (result is not None))

    print("\ntesting get_processor_degC")
    result = p.get_processor_degC()
    print("  " + str(result))
    print("  > > pass: %s < <" % (result is not None))

    print("\ntesting get_profile6_t")
    result = p.get_profile6_t()
    print("  " + str(result))
    print("  > > pass: %s < <" % (result is not None))

    print("\ntesting get_range")
    result = p.get_range()
    print("  " + str(result))
    print("  > > pass: %s < <" % (result is not None))

    print("\ntesting get_speed_of_sound")
    result = p.get_speed_of_sound()
    print("  " + str(result))
    print("  > > pass: %s < <" % (result is not None))

    print("\ntesting set_device_id")
    print("  > > pass: %s < <" % p.set_device_id(43))
    print("\ntesting set_mode_auto")
    print("  > > pass: %s < <" % p.set_mode_auto(False))
    print("\ntesting set_range")
    print("  > > pass: %s < <" % p.set_range(1000, 2000))
    print("\ntesting set_speed_of_sound")
    print("  > > pass: %s < <" % p.set_speed_of_sound(1444000))
    print("\ntesting set_ping_interval")
    print("  > > pass: %s < <" % p.set_ping_interval(36))
    print("\ntesting set_gain_setting")
    print("  > > pass: %s < <" % p.set_gain_setting(3))
    print("\ntesting set_ping_enable")
    print("  > > pass: %s < <" % p.set_ping_enable(True))

    print(p)