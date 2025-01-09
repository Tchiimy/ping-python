
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
    # @brief Get a fw_version message from the device\n
    # Message description:\n
    # Device information
    #
    # @return None if there is no reply from the device, otherwise a dictionary with the following keys:\n
    # device_type: Device type. 0: Unknown; 1: Echosounder\n
    # device_model: Device model. 0: Unknown; 1: Ping1D\n
    # version_major: Firmware version major number.\n
    # version_minor: Firmware version minor number.\n
    def get_fw_version(self):
        if self.legacyRequest(definitions.PINGS500_FW_VERSION) is None:
            return None
        data = ({
            "device_type": self._device_type,  # Device type. 0: Unknown; 1: Echosounder
            "device_model": self._device_model,  # Device model. 0: Unknown; 1: Ping1D
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
    def get_processor_deg(self):
        if self.legacyRequest(definitions.PINGS500_PROCESSOR_DEG) is None:
            return None
        data = ({
            "centi_degc": self._centi_degc,  # Units: cC; The temperature in centi-degrees Centigrade (100 * degrees C).
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
    
    def get_distance_2(self):
        if self.legacyRequest(definitions.PINGS500_DISTANCE2) is None:
            return None
        data = ({
            "ping_distance_mm": self._ping_distance_mm,  # Units: mm/s; Current speed of sound setting in mm/sec. Default is 1500000 mm/sec.
            "averaged_distance_mm": self._averaged_distance_mm,
            "reserved": self._reserved,
            "confidence_this_ping": self._confidence_this_ping,
            "confidence_averaged_distance": self._confidence_averaged_distance,
            "timestamp_msec": self._timestamp_msec,
        })
        return data


    def get_profile6_t(self):
        if self.legacyRequest(definitions.PINGS500_PROFILE6_T) is None:
            return None
        


        data = {
            "ping_number": self._ping_number,  # sequentially assigned from 0 at power up
            "start_mm": self._start_mm,  # start of ping (mm)
            "length_mm": self._length_mm,  # length of ping (mm)
            "start_ping_hz": self._start_ping_hz,  # start frequency of ping (Hz)
            "end_ping_hz": self._end_ping_hz,  # end frequency of ping (Hz)
            "adc_sample_hz": self._adc_sample_hz,  # ADC sampling rate (Hz)
            "timestamp_msec": self._timestamp_msec,  # timestamp in milliseconds
            "spare2": self._spare2,  # spare value (unused)
            "pulse_duration_sec": self._pulse_duration_sec,  # pulse duration (seconds)
            "analog_gain": self._analog_gain,  # analog gain
            "max_pwr_db": self._max_pwr_db,  # max power in dB
            "min_pwr_db": self._min_pwr_db,  # min power in dB
            "this_ping_depth_m": self._this_ping_depth_m,  # this ping depth in meters
            "smooth_depth_m": self._smooth_depth_m,  # smoothed depth in meters
            "fspare2": self._fspare2,  # spare value (unused)
            "depth_measurement_confidence": self._depth_measurement_confidence,  # depth measurement confidence (0-100)
            "gain_index": self._gain_index,  # gain index
            "decimation": self._decimation,  # decimation index
            "smoothed_depth_measurement_confidence": self._smoothed_depth_measurement_confidence,  # smoothed depth confidence (0-100)
            "pwr_results": self._pwr_results,  # power results array
        }
        return data
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
    import time
    import struct
    import math


    device = PingS500()
    print(device)

    # Connect to the device
    device.connect_udp("192.168.3.51", 51200)

    # Test get_fw_version
    fw_version = device.get_fw_version()
    #print("Firmware Version:", fw_version)

    # Test get_speed_of_sound
    speed_of_sound = device.get_speed_of_sound()
    #print("Speed of Sound (mm/s):", speed_of_sound)

    # Test set_speed_of_sound
    #print("Setting speed of sound to 1485000 mm/s...")
    if device.set_speed_of_sound(15000000):
        print("Speed of sound set successfully.")
    else:
        print("Failed to set speed of sound.")

    # Test set_ping_params
    print("Setting ping parameters...")
    device.set_ping_params(
        start_mm=0,
        length_mm=0,
        gain_index=-1,
        msec_per_ping=-1,
        pulse_len_usec=0,
        report_id=1223,
        reserved=0,
        chirp=1,
        decimation=0
    )

    for i in range(1):
        distance = device.get_distance_2()
        print("Distance:", distance)
        time.sleep(0.1)

    device.set_ping_params(
        start_mm=0,
        length_mm=0,
        gain_index=-1,
        msec_per_ping=-1,
        pulse_len_usec=0,
        report_id=1308,
        reserved=0,
        chirp=0,
        decimation=0
    )

    for i in range(1):
        distance = device.get_profile6_t()
        print("Distance:", distance)

        converted_data = [struct.unpack('H', distance["pwr_results"][i:i+2])[0] for i in range(0, len(distance["pwr_results"]), 2)]
        print(converted_data)
        print("Length of Converted Data:", len(converted_data))


        # Convert integers to dB, handle zero values safely
        converted_data_db = [
            10 * math.log10(x/1e-12) if x > 0 else float('-inf') 
            for x in converted_data
        ]
        print("Length of Converted Data in dB:", len(converted_data_db))
        print(converted_data_db)

        time.sleep(0.1)

    # Test get_altitude
    altitude = device.get_altitude()
    #print("Altitude:", altitude)

    # Test get_gain_index
    gain_index = device.get_gain_index()
    #print("Gain Index:", gain_index)

    # Test get_ping_rate_msec
    ping_rate = device.get_ping_rate_msec()
    #print("Ping Rate (ms):", ping_rate)

    # Test get_processor_degC
    processor_temp = device.get_processor_deg()
    #print("Processor Temperature (centi-degrees C):", processor_temp)
    #print("Processor Temperature (degrees C):", processor_temp["centi_degc"] / 100)

    # Test get_range
    scan_range = device.get_range()
    #print("Scan Range:", scan_range)


    del device