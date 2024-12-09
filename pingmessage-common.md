# Common messages

## general

#### 1 ack
Acknowledged.

| Type | Name             | Description                                                      | Units |
|------|------------------|------------------------------------------------------------------|-------|
| u16 | acked_id | The message ID that is ACKnowledged. |  |

#### 2 nack
Not acknowledged.

| Type | Name             | Description                                                      | Units |
|------|------------------|------------------------------------------------------------------|-------|
| u16 | nacked_id | The message ID that is Not ACKnowledged. |  |
| char[] | nack_message | ASCII text message indicating NACK condition. (not necessarily NULL terminated) Length is derived from payload_length in the header. |  |

#### 3 ascii_text
A message for transmitting text data.

| Type | Name             | Description                                                      | Units |
|------|------------------|------------------------------------------------------------------|-------|
| char[] | ascii_message | ASCII text message. (not necessarily NULL terminated) Length is derived from payload_length in the header. |  |

#### 6 general_request
Requests a specific message to be sent from the sonar to the host. Command timeout should be set to 50 msec.

| Type | Name             | Description                                                      | Units |
|------|------------------|------------------------------------------------------------------|-------|
| u16 | requested_id | Message ID to be requested. |  |

## get

#### 4 device_information
Device information

| Type | Name             | Description                                                      | Units |
|------|------------------|------------------------------------------------------------------|-------|
| u8 | device_type | Device type. 0: Unknown; 1: Ping Echosounder; 2: Ping360 |  |
| u8 | device_revision | device-specific hardware revision |  |
| u8 | firmware_version_major | Firmware version major number. |  |
| u8 | firmware_version_minor | Firmware version minor number. |  |
| u8 | firmware_version_patch | Firmware version patch number. |  |
| u8 | reserved | reserved |  |

#### 5 protocol_version
The protocol version

| Type | Name             | Description                                                      | Units |
|------|------------------|------------------------------------------------------------------|-------|
| u8 | version_major | Protocol version major number. |  |
| u8 | version_minor | Protocol version minor number. |  |
| u8 | version_patch | Protocol version patch number. |  |
| u8 | reserved | reserved |  |

## set

#### 100 set_device_id
Set the device ID.

| Type | Name             | Description                                                      | Units |
|------|------------------|------------------------------------------------------------------|-------|
| u8 | device_id | Device ID (1-254). 0 is unknown and 255 is reserved for broadcast messages. |  |

