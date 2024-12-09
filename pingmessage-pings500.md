# Pings500 messages

## set

#### 1000 set_device_id
Set the device ID.

| Type | Name             | Description                                                      | Units |
|------|------------------|------------------------------------------------------------------|-------|
| u8 | device_id | Device ID (0-254). 255 is reserved for broadcast messages. |  |

#### 1002 set_speed_of_sound
Set the speed of sound used for distance calculations.

| Type | Name             | Description                                                      | Units |
|------|------------------|------------------------------------------------------------------|-------|
| u32 | sos_mm_per_sec | The speed of sound in mm/sec. Default is 15000000 mm/sec (1500 m/sec). |  |

#### 1015 set_ping_params
Configure ping parameters.

| Type | Name             | Description                                                      | Units |
|------|------------------|------------------------------------------------------------------|-------|
| u32 | start_mm | Start of ping range, normally 0. | mm |
| u32 | length_mm | Length of the returned profile. End of range = start_mm + length_mm. Set to 0 for auto range. | mm |
| i16 | gain_index | Set to -1 for auto gain, otherwise 0-13 sets gain for manual gain. |  |
| i16 | msec_per_ping | Set to -1 to start a single ping. Otherwise, sets minimum ping interval. | ms |
| u16 | pulse_len_usec | Set to 0 for auto mode. Currently ignored and auto duration is always used. | µs |
| u16 | report_id | The ID of the packet type you want in response. Options: distance2 (1223), profile6 (1308), or zero. Zero disables pinging. |  |
| u16 | reserved | Set to 0. |  |
| u8 | chirp | Set to 1 for chirp, 0 for monotone ping. |  |
| u8 | decimation | Set to 0 for auto range resolution in chirp mode. |  |

## get

#### 1200 fw_version
Device information

| Type | Name             | Description                                                      | Units |
|------|------------------|------------------------------------------------------------------|-------|
| u8 | device_type | Device type. 0: Unknown; 1: Echosounder |  |
| u8 | device_model | Device model. 0: Unknown; 1: Ping1D |  |
| u16 | version_major | Firmware version major number. |  |
| u16 | version_minor | Firmware version minor number. |  |

#### 1203 speed_of_sound
The speed of sound used for distance calculations.

| Type | Name             | Description                                                      | Units |
|------|------------------|------------------------------------------------------------------|-------|
| u32 | sos_mm_per_sec | Current speed of sound setting in mm/sec. Default is 1500000 mm/sec. | mm/s |

#### 1204 range
The scan range for acoustic measurements.

| Type | Name             | Description                                                      | Units |
|------|------------------|------------------------------------------------------------------|-------|
| u32 | start_mm | The beginning of the scan range in mm from the transducer. | mm |
| u32 | length_mm | Length of the scan range. Measurements will be within start_mm and start_mm + length_mm. | mm |

#### 1206 ping_rate_msec
The interval between acoustic measurements.

| Type | Name             | Description                                                      | Units |
|------|------------------|------------------------------------------------------------------|-------|
| u16 | msec_per_ping | Minimum time between successive pings. Can be longer depending on range. | ms |

#### 1207 gain_index
The current gain setting.

| Type | Name             | Description                                                      | Units |
|------|------------------|------------------------------------------------------------------|-------|
| u32 | gain_index | The current gain index setting. |  |

#### 1211 altitude
The result of the most recent distance calculation.

| Type | Name             | Description                                                      | Units |
|------|------------------|------------------------------------------------------------------|-------|
| u32 | altitude_mm | Most recent calculated distance from the device to the target. | mm |
| u8 | quality | Confidence in the distance measurement. | % |

#### 1213 processor_degC
Temperature of the device CPU.

| Type | Name             | Description                                                      | Units |
|------|------------------|------------------------------------------------------------------|-------|
| u32 | centi_degC | The temperature in centi-degrees Centigrade (100 * degrees C). | cC |

