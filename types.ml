(* Enumerated type to represent different system calls *)
type system_call =
  | CreateProcess
  | TerminateProcess
  | SendMessage
  | ReceiveMessage
  | AllocateMemory
  | FreeMemory

(* Enumerated type to represent different states of a process *)
type process_state =
  | Ready
  | Running
  | Waiting
  | Terminated

(* Record type to represent a process in the system *)
type process = {
  pid: int;
  state: process_state;
  memory: int; (* Amount of memory allocated to the process *)
  message_queue: string list; (* Queue of messages for IPC *)
}

(* Record type to represent the microkernel *)
type microkernel = {
  processes: process list;
  system_calls: (system_call * process) list;
}
