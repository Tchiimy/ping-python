#!/usr/bin/python -u

# Ping1D.py
# A device API for the Blue Robotics Ping1D echosounder

#~!~!~!~!~!~!~!~!~!~!~!~!~!~!~!~!~!~!~!~!~!~!~!~!~!~!~!~!~!
# THIS IS AN AUTOGENERATED FILE
# DO NOT EDIT
#~!~!~!~!~!~!~!~!~!~!~!~!~!~!~!~!~!~!~!~!~!~!~!~!~!~!~!~!~!

from Ping import PingMessage
import serial
import time

class Ping1D(object):
    def __init__(self, deviceName, baudrate = 115200):
        if deviceName is None:
            print("Device name is required")
            return

        try:
            print("Opening %s at %d bps" % (deviceName, baudrate))

            ## Serial object for device communication
            self.iodev = serial.Serial(deviceName, baudrate)
            self.iodev.timeout = 1

        except Exception as e:
            print("Failed to open the given serial port")
            print("\t", e)
            exit(1)

        ## A helper class to take care of decoding the input stream
        self.parser = PingMessage.PingParser()

        ## device id of this Ping1D object, used for dst_device_id in outgoing messages
        self.my_id = 255

    ##
    # @brief Consume rx buffer data until a new message is successfully decoded
    #
    # @return A new PingMessage: as soon as a message is parsed (there may be data remaining in the buffer to be parsed, thus requiring subsequent calls to read())
    # @return None: if the buffer is empty and no message has been parsed
    def read(self):
        while(self.iodev.in_waiting):
            b = self.iodev.read()

            if self.parser.parseByte(ord(b)) == PingMessage.PingParser.NEW_MESSAGE:
                self.handleMessage(self.parser.rxMsg)
                return self.parser.rxMsg
        return None

    ##
    # @brief Write data to device
    #
    # @param data: bytearray to write to device
    #
    # @return Number of bytes written
    def write(self, data):
        return self.iodev.write(data)

    ##
    # @brief Make sure there is a device on and read some initial data
    #
    # @return True if the device replies with expected data, False otherwise
    def initialize(self):
        if self.request(PingMessage.PING1D_VOLTAGE_5) is None:
            return False
        return True

    ##
    # @brief Request the given message ID
    #
    # @param m_id: The message ID to request from the device
    # @param timeout: The time in seconds to wait for the device to send
    # the requested message before timing out and returning
    #
    # @return PingMessage: the device reply if it is received within timeout period, None otherwise
    #
    # @todo handle nack to exit without blocking
    def request(self, m_id, timeout = 0.5):
        msg = PingMessage.PingMessage()
        msg.request_id = m_id
        msg.packMsgData()
        self.write(msg.msgData)
        return self.waitMessage(m_id, timeout)

    ##
    # @brief Wait until we receive a message from the device with the desired message_id for timeout seconds
    #
    # @param message_id: The message id to wait to receive from the device
    # @param timeout: The timeout period in seconds to wait
    #
    # @return PingMessage: the message from the device if it is received within timeout period, None otherwise
    def waitMessage(self, message_id, timeout = 0.5):
        tstart = time.time()
        while(time.time() < tstart + timeout):
            msg = self.read()
            if msg is not None:
                if msg.message_id == message_id:
                    return msg
        return None

    ##
    # @brief Handle an incoming messge from the device.
    # Extract message fields into self attributes.
    #
    # @param msg: the PingMessage to handle.
    def handleMessage(self, msg):
        if msg.message_id in PingMessage.payloadDict:
            for attr in PingMessage.payloadDict[msg.message_id]["field_names"]:
                setattr(self, attr, getattr(msg, attr))
        else:
            print("Unrecognized message: %d", msg)

    ##
    # @brief Dump object into string representation.
    #
    # @return string: a string representation of the object
    def __repr__(self):
        representation = "---------------------------------------------------------\n~Ping1D Object~"

        attrs = vars(self)
        for attr in sorted(attrs):
            try:
                if attr != 'iodev':
                    representation += "\n  - " + attr + "(hex): " + str([hex(ord(item)) for item in getattr(self, attr)])
                if attr != 'data':
                    representation += "\n  - " + attr + "(string): " + str(getattr(self, attr))
            except:
                representation += "\n  - " + attr + ": " + str(getattr(self, attr))
        return representation

    ##
    # @brief Get a firmware_version message from the device\n
    # Message description:\n
    # Device information
    #
    # @return None if there is no reply from the device, otherwise a dictionary with the following keys:\n
    # device_type: Device type. 0: 1D Echosounder\n
    # device_model: Device model. 0: Ping1D\n
    # firmware_version_major: Firmware version major number.\n
    # firmware_version_minor: Firmware version minor number.\n
    def get_firmware_version(self):
        if self.request(PingMessage.PING1D_FIRMWARE_VERSION) is None:
            return None
        data = ({
            "device_type": self.device_type, # Device type. 0: 1D Echosounder
            "device_model": self.device_model, # Device model. 0: Ping1D
            "firmware_version_major": self.firmware_version_major, # Firmware version major number.
            "firmware_version_minor": self.firmware_version_minor, # Firmware version minor number.
        })
        return data

    ##
    # @brief Get a device_id message from the device\n
    # Message description:\n
    # The device ID.
    #
    # @return None if there is no reply from the device, otherwise a dictionary with the following keys:\n
    # device_id: The device ID (0-254). 255 is reserved for broadcast messages.\n
    def get_device_id(self):
        if self.request(PingMessage.PING1D_DEVICE_ID) is None:
            return None
        data = ({
            "device_id": self.device_id, # The device ID (0-254). 255 is reserved for broadcast messages.
        })
        return data

    ##
    # @brief Get a voltage_5 message from the device\n
    # Message description:\n
    # The 5V rail voltage.
    #
    # @return None if there is no reply from the device, otherwise a dictionary with the following keys:\n
    # voltage_5: Units: mV; The 5V rail voltage.\n
    def get_voltage_5(self):
        if self.request(PingMessage.PING1D_VOLTAGE_5) is None:
            return None
        data = ({
            "voltage_5": self.voltage_5, # Units: mV; The 5V rail voltage.
        })
        return data

    ##
    # @brief Get a speed_of_sound message from the device\n
    # Message description:\n
    # The speed of sound used for distance calculations.
    #
    # @return None if there is no reply from the device, otherwise a dictionary with the following keys:\n
    # speed_of_sound: Units: mm/s; The speed of sound in the measurement medium. ~1,500,000 mm/s for water.\n
    def get_speed_of_sound(self):
        if self.request(PingMessage.PING1D_SPEED_OF_SOUND) is None:
            return None
        data = ({
            "speed_of_sound": self.speed_of_sound, # Units: mm/s; The speed of sound in the measurement medium. ~1,500,000 mm/s for water.
        })
        return data

    ##
    # @brief Get a range message from the device\n
    # Message description:\n
    # The scan range for acoustic measurements. Measurements returned by the device will lie in the range (scan_start, scan_start + scan_length).
    #
    # @return None if there is no reply from the device, otherwise a dictionary with the following keys:\n
    # scan_start: Units: mm; The beginning of the scan range in mm from the transducer.\n
    # scan_length: Units: mm; The length of the scan range.\n
    def get_range(self):
        if self.request(PingMessage.PING1D_RANGE) is None:
            return None
        data = ({
            "scan_start": self.scan_start, # Units: mm; The beginning of the scan range in mm from the transducer.
            "scan_length": self.scan_length, # Units: mm; The length of the scan range.
        })
        return data

    ##
    # @brief Get a mode_auto message from the device\n
    # Message description:\n
    # The current operating mode of the device. Manual mode allows for manual selection of the gain and scan range.
    #
    # @return None if there is no reply from the device, otherwise a dictionary with the following keys:\n
    # mode_auto: 0: manual mode, 1: auto mode\n
    def get_mode_auto(self):
        if self.request(PingMessage.PING1D_MODE_AUTO) is None:
            return None
        data = ({
            "mode_auto": self.mode_auto, # 0: manual mode, 1: auto mode
        })
        return data

    ##
    # @brief Get a ping_interval message from the device\n
    # Message description:\n
    # The interval between acoustic measurements.
    #
    # @return None if there is no reply from the device, otherwise a dictionary with the following keys:\n
    # ping_interval: Units: ms; The interval between acoustic measurements.\n
    def get_ping_interval(self):
        if self.request(PingMessage.PING1D_PING_INTERVAL) is None:
            return None
        data = ({
            "ping_interval": self.ping_interval, # Units: ms; The interval between acoustic measurements.
        })
        return data

    ##
    # @brief Get a gain_index message from the device\n
    # Message description:\n
    # The current gain setting.
    #
    # @return None if there is no reply from the device, otherwise a dictionary with the following keys:\n
    # gain_index: 0: 0.6dB, 1: 1.8dB, 2: 5.5dB, 3: 12.9dB, 4: 30.2dB, 5: 66.1dB, 6: 144dB\n
    def get_gain_index(self):
        if self.request(PingMessage.PING1D_GAIN_INDEX) is None:
            return None
        data = ({
            "gain_index": self.gain_index, # 0: 0.6dB, 1: 1.8dB, 2: 5.5dB, 3: 12.9dB, 4: 30.2dB, 5: 66.1dB, 6: 144dB
        })
        return data

    ##
    # @brief Get a pulse_duration message from the device\n
    # Message description:\n
    # The duration of the acoustic activation/transmission.
    #
    # @return None if there is no reply from the device, otherwise a dictionary with the following keys:\n
    # pulse_duration: Units: microseconds; Acoustic pulse duration.\n
    def get_pulse_duration(self):
        if self.request(PingMessage.PING1D_PULSE_DURATION) is None:
            return None
        data = ({
            "pulse_duration": self.pulse_duration, # Units: microseconds; Acoustic pulse duration.
        })
        return data

    ##
    # @brief Get a general_info message from the device\n
    # Message description:\n
    # General information.
    #
    # @return None if there is no reply from the device, otherwise a dictionary with the following keys:\n
    # firmware_version_major: Firmware major version.\n
    # firmware_version_minor: Firmware minor version.\n
    # voltage_5: Units: mV; Device supply voltage.\n
    # ping_interval: Units: ms; The interval between acoustic measurements.\n
    # gain_index: The current gain setting. 0: 0.6dB, 1: 1.8dB, 2: 5.5dB, 3: 12.9dB, 4: 30.2dB, 5: 66.1dB, 6: 144dB\n
    # mode_auto: The current operating mode of the device. 0: manual mode, 1: auto mode\n
    def get_general_info(self):
        if self.request(PingMessage.PING1D_GENERAL_INFO) is None:
            return None
        data = ({
            "firmware_version_major": self.firmware_version_major, # Firmware major version.
            "firmware_version_minor": self.firmware_version_minor, # Firmware minor version.
            "voltage_5": self.voltage_5, # Units: mV; Device supply voltage.
            "ping_interval": self.ping_interval, # Units: ms; The interval between acoustic measurements.
            "gain_index": self.gain_index, # The current gain setting. 0: 0.6dB, 1: 1.8dB, 2: 5.5dB, 3: 12.9dB, 4: 30.2dB, 5: 66.1dB, 6: 144dB
            "mode_auto": self.mode_auto, # The current operating mode of the device. 0: manual mode, 1: auto mode
        })
        return data

    ##
    # @brief Get a distance_simple message from the device\n
    # Message description:\n
    # The distance to target with confidence estimate.
    #
    # @return None if there is no reply from the device, otherwise a dictionary with the following keys:\n
    # distance: Units: mm; Distance to the target.\n
    # confidence: Units: %; Confidence in the distance measurement.\n
    def get_distance_simple(self):
        if self.request(PingMessage.PING1D_DISTANCE_SIMPLE) is None:
            return None
        data = ({
            "distance": self.distance, # Units: mm; Distance to the target.
            "confidence": self.confidence, # Units: %; Confidence in the distance measurement.
        })
        return data

    ##
    # @brief Get a distance message from the device\n
    # Message description:\n
    # The distance to target with confidence estimate. Relevant device parameters during the measurement are also provided.
    #
    # @return None if there is no reply from the device, otherwise a dictionary with the following keys:\n
    # distance: Units: mm; The current return distance determined for the most recent acoustic measurement.\n
    # confidence: Units: %; Confidence in the most recent range measurement.\n
    # pulse_duration: Units: us; The acoustic pulse length during acoustic transmission/activation.\n
    # ping_number: The pulse/measurement count since boot.\n
    # scan_start: Units: mm; The beginning of the scan region in mm from the transducer.\n
    # scan_length: Units: mm; The length of the scan region.\n
    # gain_index: The current gain setting. 0: 0.6dB, 1: 1.8dB, 2: 5.5dB, 3: 12.9dB, 4: 30.2dB, 5: 66.1dB, 6: 144dB\n
    def get_distance(self):
        if self.request(PingMessage.PING1D_DISTANCE) is None:
            return None
        data = ({
            "distance": self.distance, # Units: mm; The current return distance determined for the most recent acoustic measurement.
            "confidence": self.confidence, # Units: %; Confidence in the most recent range measurement.
            "pulse_duration": self.pulse_duration, # Units: us; The acoustic pulse length during acoustic transmission/activation.
            "ping_number": self.ping_number, # The pulse/measurement count since boot.
            "scan_start": self.scan_start, # Units: mm; The beginning of the scan region in mm from the transducer.
            "scan_length": self.scan_length, # Units: mm; The length of the scan region.
            "gain_index": self.gain_index, # The current gain setting. 0: 0.6dB, 1: 1.8dB, 2: 5.5dB, 3: 12.9dB, 4: 30.2dB, 5: 66.1dB, 6: 144dB
        })
        return data

    ##
    # @brief Get a processor_temperature message from the device\n
    # Message description:\n
    # Temperature of the device cpu.
    #
    # @return None if there is no reply from the device, otherwise a dictionary with the following keys:\n
    # processor_temperature: Units: cC; The temperature in centi-degrees Centigrade (100 * degrees C).\n
    def get_processor_temperature(self):
        if self.request(PingMessage.PING1D_PROCESSOR_TEMPERATURE) is None:
            return None
        data = ({
            "processor_temperature": self.processor_temperature, # Units: cC; The temperature in centi-degrees Centigrade (100 * degrees C).
        })
        return data

    ##
    # @brief Get a pcb_temperature message from the device\n
    # Message description:\n
    # Temperature of the on-board thermistor.
    #
    # @return None if there is no reply from the device, otherwise a dictionary with the following keys:\n
    # pcb_temperature: Units: cC; The temperature in centi-degrees Centigrade (100 * degrees C).\n
    def get_pcb_temperature(self):
        if self.request(PingMessage.PING1D_PCB_TEMPERATURE) is None:
            return None
        data = ({
            "pcb_temperature": self.pcb_temperature, # Units: cC; The temperature in centi-degrees Centigrade (100 * degrees C).
        })
        return data

    ##
    # @brief Get a ping_enable message from the device\n
    # Message description:\n
    # Acoustic output enabled state.
    #
    # @return None if there is no reply from the device, otherwise a dictionary with the following keys:\n
    # ping_enabled: The state of the acoustic output. 0: disabled, 1:enabled\n
    def get_ping_enable(self):
        if self.request(PingMessage.PING1D_PING_ENABLE) is None:
            return None
        data = ({
            "ping_enabled": self.ping_enabled, # The state of the acoustic output. 0: disabled, 1:enabled
        })
        return data

    ##
    # @brief Get a profile message from the device\n
    # Message description:\n
    # A profile produced from a single acoustic measurement. The data returned is an array of response strength at even intervals across the scan region. The scan region is defined as the region between <scan_start> and <scan_start + scan_length> millimeters away from the transducer. A distance measurement to the target is also provided.
    #
    # @return None if there is no reply from the device, otherwise a dictionary with the following keys:\n
    # distance: Units: mm; The current return distance determined for the most recent acoustic measurement.\n
    # confidence: Units: %; Confidence in the most recent range measurement.\n
    # pulse_duration: Units: us; The acoustic pulse length during acoustic transmission/activation.\n
    # ping_number: The pulse/measurement count since boot.\n
    # scan_start: Units: mm; The beginning of the scan region in mm from the transducer.\n
    # scan_length: Units: mm; The length of the scan region.\n
    # gain_index: The current gain setting. 0: 0.6dB, 1: 1.8dB, 2: 5.5dB, 3: 12.9dB, 4: 30.2dB, 5: 66.1dB, 6: 144dB\n
    # profile_data: An array of return strength measurements taken at regular intervals across the scan region.\n
    def get_profile(self):
        if self.request(PingMessage.PING1D_PROFILE) is None:
            return None
        data = ({
            "distance": self.distance, # Units: mm; The current return distance determined for the most recent acoustic measurement.
            "confidence": self.confidence, # Units: %; Confidence in the most recent range measurement.
            "pulse_duration": self.pulse_duration, # Units: us; The acoustic pulse length during acoustic transmission/activation.
            "ping_number": self.ping_number, # The pulse/measurement count since boot.
            "scan_start": self.scan_start, # Units: mm; The beginning of the scan region in mm from the transducer.
            "scan_length": self.scan_length, # Units: mm; The length of the scan region.
            "gain_index": self.gain_index, # The current gain setting. 0: 0.6dB, 1: 1.8dB, 2: 5.5dB, 3: 12.9dB, 4: 30.2dB, 5: 66.1dB, 6: 144dB
            "profile_data": self.profile_data, # An array of return strength measurements taken at regular intervals across the scan region.
        })
        return data

    ##
    # @brief Get a protocol_version message from the device\n
    # Message description:\n
    # The protocol version
    #
    # @return None if there is no reply from the device, otherwise a dictionary with the following keys:\n
    # protocol_version: The protocol version\n
    def get_protocol_version(self):
        if self.request(PingMessage.PING1D_PROTOCOL_VERSION) is None:
            return None
        data = ({
            "protocol_version": self.protocol_version, # The protocol version
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
        m = PingMessage.PingMessage(PingMessage.PING1D_SET_DEVICE_ID)
        m.device_id = device_id
        m.packMsgData()
        self.write(m.msgData)
        if self.request(PingMessage.PING1D_DEVICE_ID) is None:
            return False
        # Read back the data and check that changes have been applied
        if (verify
              and (self.device_id != device_id)):
            return False
        return True # success

    ##
    # @brief Send a set_range message to the device\n
    # Message description:\n
    # Set the scan range for acoustic measurements.\n
    # Send the message to write the device parameters, then read the values back from the device\n
    #
    # @param scan_start - Units: mm; 
    # @param scan_length - Units: mm; The length of the scan range.
    #
    # @return If verify is False, True on successful communication with the device. If verify is False, True if the new device parameters are verified to have been written correctly. False otherwise (failure to read values back or on verification failure)
    def set_range(self, scan_start, scan_length, verify=True):
        m = PingMessage.PingMessage(PingMessage.PING1D_SET_RANGE)
        m.scan_start = scan_start
        m.scan_length = scan_length
        m.packMsgData()
        self.write(m.msgData)
        if self.request(PingMessage.PING1D_RANGE) is None:
            return False
        # Read back the data and check that changes have been applied
        if (verify
              and (self.scan_start != scan_start or self.scan_length != scan_length)):
            return False
        return True # success

    ##
    # @brief Send a set_speed_of_sound message to the device\n
    # Message description:\n
    # Set the speed of sound used for distance calculations.\n
    # Send the message to write the device parameters, then read the values back from the device\n
    #
    # @param speed_of_sound - Units: mm/s; The speed of sound in the measurement medium. ~1,500,000 mm/s for water.
    #
    # @return If verify is False, True on successful communication with the device. If verify is False, True if the new device parameters are verified to have been written correctly. False otherwise (failure to read values back or on verification failure)
    def set_speed_of_sound(self, speed_of_sound, verify=True):
        m = PingMessage.PingMessage(PingMessage.PING1D_SET_SPEED_OF_SOUND)
        m.speed_of_sound = speed_of_sound
        m.packMsgData()
        self.write(m.msgData)
        if self.request(PingMessage.PING1D_SPEED_OF_SOUND) is None:
            return False
        # Read back the data and check that changes have been applied
        if (verify
              and (self.speed_of_sound != speed_of_sound)):
            return False
        return True # success

    ##
    # @brief Send a set_mode_auto message to the device\n
    # Message description:\n
    # Set automatic or manual mode. Manual mode allows for manual selection of the gain and scan range.\n
    # Send the message to write the device parameters, then read the values back from the device\n
    #
    # @param mode_auto - 0: manual mode. 1: auto mode.
    #
    # @return If verify is False, True on successful communication with the device. If verify is False, True if the new device parameters are verified to have been written correctly. False otherwise (failure to read values back or on verification failure)
    def set_mode_auto(self, mode_auto, verify=True):
        m = PingMessage.PingMessage(PingMessage.PING1D_SET_MODE_AUTO)
        m.mode_auto = mode_auto
        m.packMsgData()
        self.write(m.msgData)
        if self.request(PingMessage.PING1D_MODE_AUTO) is None:
            return False
        # Read back the data and check that changes have been applied
        if (verify
              and (self.mode_auto != mode_auto)):
            return False
        return True # success

    ##
    # @brief Send a set_ping_interval message to the device\n
    # Message description:\n
    # The interval between acoustic measurements.\n
    # Send the message to write the device parameters, then read the values back from the device\n
    #
    # @param ping_interval - Units: ms; The interval between acoustic measurements.
    #
    # @return If verify is False, True on successful communication with the device. If verify is False, True if the new device parameters are verified to have been written correctly. False otherwise (failure to read values back or on verification failure)
    def set_ping_interval(self, ping_interval, verify=True):
        m = PingMessage.PingMessage(PingMessage.PING1D_SET_PING_INTERVAL)
        m.ping_interval = ping_interval
        m.packMsgData()
        self.write(m.msgData)
        if self.request(PingMessage.PING1D_PING_INTERVAL) is None:
            return False
        # Read back the data and check that changes have been applied
        if (verify
              and (self.ping_interval != ping_interval)):
            return False
        return True # success

    ##
    # @brief Send a set_gain_index message to the device\n
    # Message description:\n
    # Set the current gain selection.\n
    # Send the message to write the device parameters, then read the values back from the device\n
    #
    # @param gain_index - 0: 0.6dB, 1: 1.8dB, 2: 5.5dB, 3: 12.9dB, 4: 30.2dB, 5: 66.1dB, 6: 144dB
    #
    # @return If verify is False, True on successful communication with the device. If verify is False, True if the new device parameters are verified to have been written correctly. False otherwise (failure to read values back or on verification failure)
    def set_gain_index(self, gain_index, verify=True):
        m = PingMessage.PingMessage(PingMessage.PING1D_SET_GAIN_INDEX)
        m.gain_index = gain_index
        m.packMsgData()
        self.write(m.msgData)
        if self.request(PingMessage.PING1D_GAIN_INDEX) is None:
            return False
        # Read back the data and check that changes have been applied
        if (verify
              and (self.gain_index != gain_index)):
            return False
        return True # success

    ##
    # @brief Send a set_ping_enable message to the device\n
    # Message description:\n
    # Enable or disable acoustic measurements.\n
    # Send the message to write the device parameters, then read the values back from the device\n
    #
    # @param ping_enabled - 0: Disable, 1: Enable.
    #
    # @return If verify is False, True on successful communication with the device. If verify is False, True if the new device parameters are verified to have been written correctly. False otherwise (failure to read values back or on verification failure)
    def set_ping_enable(self, ping_enabled, verify=True):
        m = PingMessage.PingMessage(PingMessage.PING1D_SET_PING_ENABLE)
        m.ping_enabled = ping_enabled
        m.packMsgData()
        self.write(m.msgData)
        if self.request(PingMessage.PING1D_PING_ENABLE) is None:
            return False
        # Read back the data and check that changes have been applied
        if (verify
              and (self.ping_enabled != ping_enabled)):
            return False
        return True # success


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="Ping python library example.")
    parser.add_argument('--device', action="store", required=True, type=str, help="Ping device port.")
    parser.add_argument('--baudrate', action="store", type=int, default=115200, help="Ping device baudrate.")
    args = parser.parse_args()

    p = Ping1D(args.device, args.baudrate)

    print("Initialized: %s" % p.initialize())

    print("\ntesting get_firmware_version")
    result = p.get_firmware_version()
    print("  " + str(result))
    print("  > > pass: %s < <" % (result != None))

    print("\ntesting get_device_id")
    result = p.get_device_id()
    print("  " + str(result))
    print("  > > pass: %s < <" % (result != None))

    print("\ntesting get_voltage_5")
    result = p.get_voltage_5()
    print("  " + str(result))
    print("  > > pass: %s < <" % (result != None))

    print("\ntesting get_speed_of_sound")
    result = p.get_speed_of_sound()
    print("  " + str(result))
    print("  > > pass: %s < <" % (result != None))

    print("\ntesting get_range")
    result = p.get_range()
    print("  " + str(result))
    print("  > > pass: %s < <" % (result != None))

    print("\ntesting get_mode_auto")
    result = p.get_mode_auto()
    print("  " + str(result))
    print("  > > pass: %s < <" % (result != None))

    print("\ntesting get_ping_interval")
    result = p.get_ping_interval()
    print("  " + str(result))
    print("  > > pass: %s < <" % (result != None))

    print("\ntesting get_gain_index")
    result = p.get_gain_index()
    print("  " + str(result))
    print("  > > pass: %s < <" % (result != None))

    print("\ntesting get_pulse_duration")
    result = p.get_pulse_duration()
    print("  " + str(result))
    print("  > > pass: %s < <" % (result != None))

    print("\ntesting get_general_info")
    result = p.get_general_info()
    print("  " + str(result))
    print("  > > pass: %s < <" % (result != None))

    print("\ntesting get_distance_simple")
    result = p.get_distance_simple()
    print("  " + str(result))
    print("  > > pass: %s < <" % (result != None))

    print("\ntesting get_distance")
    result = p.get_distance()
    print("  " + str(result))
    print("  > > pass: %s < <" % (result != None))

    print("\ntesting get_processor_temperature")
    result = p.get_processor_temperature()
    print("  " + str(result))
    print("  > > pass: %s < <" % (result != None))

    print("\ntesting get_pcb_temperature")
    result = p.get_pcb_temperature()
    print("  " + str(result))
    print("  > > pass: %s < <" % (result != None))

    print("\ntesting get_ping_enable")
    result = p.get_ping_enable()
    print("  " + str(result))
    print("  > > pass: %s < <" % (result != None))

    print("\ntesting get_profile")
    result = p.get_profile()
    print("  " + str(result))
    print("  > > pass: %s < <" % (result != None))

    print("\ntesting get_protocol_version")
    result = p.get_protocol_version()
    print("  " + str(result))
    print("  > > pass: %s < <" % (result != None))

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
    print("\ntesting set_gain_index")
    print("  > > pass: %s < <" % p.set_gain_index(3))
    print("\ntesting set_ping_enable")
    print("  > > pass: %s < <" % p.set_ping_enable(False))

    print(p)