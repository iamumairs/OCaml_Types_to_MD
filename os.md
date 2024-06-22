| Type Name | Type Category |
|-----------|----------------|
| system_call | Enumerated |
| process_state | Enumerated |
| process | Record |
| microkernel | Record |

# OCaml Types

## Enumerated Types
### system_call
- CreateProcess
- TerminateProcess
- SendMessage
- ReceiveMessage
- AllocateMemory
- FreeMemory

### process_state
- Ready
- Running
- Waiting
- Terminated

## Record Types
### process

| Field | Type |
|-|-|
| pid | int |
| state | process_state |
| memory | int |
| message_queue | string list |

### microkernel

| Field | Type |
|-|-|
| processes | process list |
| system_calls | (system_call * process) list |

