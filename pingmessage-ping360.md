# Ping360 messages

## set

#### 2000 device_id
Change the device id

| Type | Name             | Description                                                      | Units |
|------|------------------|------------------------------------------------------------------|-------|
| u8 | id | Device ID (1-254). 0 and 255 are reserved. |  |
| u8 | reserved | reserved |  |

## get

#### 2300 device_data
This message is used to communicate the current sonar state. If the data field is populated, the other fields indicate the sonar state when the data was captured. The time taken before the response to the command is sent depends on the difference between the last angle scanned and the new angle in the parameters as well as the number of samples and sample interval (range). To allow for the worst case reponse time the command timeout should be set to 4000 msec.

| Type | Name             | Description                                                      | Units |
|------|------------------|------------------------------------------------------------------|-------|
| u8 | mode | Operating mode (1 for Ping360) |  |
| u8 | gain_setting | Analog gain setting (0 = low, 1 = normal, 2 = high) |  |
| u16 | angle | Head angle | gradian |
| u16 | transmit_duration | Acoustic transmission duration (1~1000 microseconds) | microsecond |
| u16 | sample_period | Time interval between individual signal intensity samples in 25nsec increments (80 to 40000 == 2 microseconds to 1000 microseconds) |  |
| u16 | transmit_frequency | Acoustic operating frequency. Frequency range is 500kHz to 1000kHz, however it is only practical to use say 650kHz to 850kHz due to the narrow bandwidth of the acoustic receiver. | kHz |
| u16 | number_of_samples | Number of samples per reflected signal |  |
| u16 | data_length | The length of the proceeding vector field | |
| u8[] | data | 8 bit binary data array representing sonar echo strength |  |

#### 2301 auto_device_data
Extended version of *device_data* with *auto_transmit* information. The sensor emits this message when in *auto_transmit* mode.

| Type | Name             | Description                                                      | Units |
|------|------------------|------------------------------------------------------------------|-------|
| u8 | mode | Operating mode (1 for Ping360) |  |
| u8 | gain_setting | Analog gain setting (0 = low, 1 = normal, 2 = high) |  |
| u16 | angle | Head angle | gradian |
| u16 | transmit_duration | Acoustic transmission duration (1~1000 microseconds) | microsecond |
| u16 | sample_period | Time interval between individual signal intensity samples in 25nsec increments (80 to 40000 == 2 microseconds to 1000 microseconds) |  |
| u16 | transmit_frequency | Acoustic operating frequency. Frequency range is 500kHz to 1000kHz, however it is only practical to use say 650kHz to 850kHz due to the narrow bandwidth of the acoustic receiver. | kHz |
| u16 | start_angle | Head angle to begin scan sector for autoscan in gradians (0~399 = 0~360 degrees). | gradian |
| u16 | stop_angle | Head angle to end scan sector for autoscan in gradians (0~399 = 0~360 degrees). | gradian |
| u8 | num_steps | Number of 0.9 degree motor steps between pings for auto scan (1~10 = 0.9~9.0 degrees) | gradian |
| u8 | delay | An additional delay between successive transmit pulses (0~100 ms). This may be necessary for some programs to avoid collisions on the RS485 USRT. | millisecond |
| u16 | number_of_samples | Number of samples per reflected signal |  |
| u16 | data_length | The length of the proceeding vector field | |
| u8[] | data | 8 bit binary data array representing sonar echo strength |  |

## control

#### 2600 reset
Reset the sonar. The bootloader may run depending on the selection according to the `bootloader` payload field. When the bootloader runs, the external LED flashes at 5Hz. If the bootloader is not contacted within 5 seconds, it will run the current program. If there is no program, then the bootloader will wait forever for a connection. Note that if you issue a reset then you will have to close all your open comm ports and go back to issuing either a discovery message for UDP or go through the break sequence for serial comms before you can talk to the sonar again.

| Type | Name             | Description                                                      | Units |
|------|------------------|------------------------------------------------------------------|-------|
| u8 | bootloader | 0 = skip bootloader; 1 = run bootloader |  |
| u8 | reserved | reserved |  |

#### 2601 transducer
The transducer will apply the commanded settings. The sonar will reply with a `ping360_data` message. If the `transmit` field is 0, the sonar will not transmit after locating the transducer, and the `data` field in the `ping360_data` message reply will be empty. If the `transmit` field is 1, the sonar will make an acoustic transmission after locating the transducer, and the resulting data will be uploaded in the `data` field of the `ping360_data` message reply. To allow for the worst case reponse time the command timeout should be set to 4000 msec.

| Type | Name             | Description                                                      | Units |
|------|------------------|------------------------------------------------------------------|-------|
| u8 | mode | Operating mode (1 for Ping360) |  |
| u8 | gain_setting | Analog gain setting (0 = low, 1 = normal, 2 = high) |  |
| u16 | angle | Head angle | gradian |
| u16 | transmit_duration | Acoustic transmission duration (1~1000 microseconds) | microsecond |
| u16 | sample_period | Time interval between individual signal intensity samples in 25nsec increments (80 to 40000 == 2 microseconds to 1000 microseconds) |  |
| u16 | transmit_frequency | Acoustic operating frequency. Frequency range is 500kHz to 1000kHz, however it is only practical to use say 650kHz to 850kHz due to the narrow bandwidth of the acoustic receiver. | kHz |
| u16 | number_of_samples | Number of samples per reflected signal |  |
| u8 | transmit | 0 = do not transmit; 1 = transmit after the transducer has reached the specified angle |  |
| u8 | reserved | reserved |  |

#### 2602 auto_transmit
Extended *transducer* message with auto-scan function. The sonar will automatically scan the region between start_angle and end_angle and send auto_device_data messages as soon as new data is available. Send a line break to stop scanning (and also begin the autobaudrate procedure). Alternatively, a motor_off message may be sent (but retrys might be necessary on the half-duplex RS485 interface).

| Type | Name             | Description                                                      | Units |
|------|------------------|------------------------------------------------------------------|-------|
| u8 | mode | Operating mode (1 for Ping360) |  |
| u8 | gain_setting | Analog gain setting (0 = low, 1 = normal, 2 = high) |  |
| u16 | transmit_duration | Acoustic transmission duration (1~1000 microseconds) | microsecond |
| u16 | sample_period | Time interval between individual signal intensity samples in 25nsec increments (80 to 40000 == 2 microseconds to 1000 microseconds) |  |
| u16 | transmit_frequency | Acoustic operating frequency. Frequency range is 500kHz to 1000kHz, however it is only practical to use say 650kHz to 850kHz due to the narrow bandwidth of the acoustic receiver. | kHz |
| u16 | number_of_samples | Number of samples per reflected signal |  |
| u16 | start_angle | Head angle to begin scan sector for autoscan in gradians (0~399 = 0~360 degrees). | gradian |
| u16 | stop_angle | Head angle to end scan sector for autoscan in gradians (0~399 = 0~360 degrees). | gradian |
| u8 | num_steps | Number of 0.9 degree motor steps between pings for auto scan (1~10 = 0.9~9.0 degrees) | gradian |
| u8 | delay | An additional delay between successive transmit pulses (0~100 ms). This may be necessary for some programs to avoid collisions on the RS485 USRT. | millisecond |

#### 2903 motor_off
The sonar switches the current through the stepper motor windings off to save power. The sonar will send an ack message in response. The command timeout should be set to 50 msec. If the sonar is idle (not scanning) for more than 30 seconds then the motor current will automatically turn off. When the user sends any command that involves moving the transducer then the motor current is automatically re-enabled.

No payload.

