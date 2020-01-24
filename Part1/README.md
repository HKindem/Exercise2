# Mutex and Channel basics

### What is an atomic operation?
> Atomic ooperation are operations that run independently of other processes.  these will avoid  racing conditions and conflicting concurrency by serializing the processes at the lower leverls, making sure shared resourced at the same time by paralell processes.

### What is a semaphore?
> A semaphore is a variable that indicates whether a resource is being used by a process. This variable can be read by other resources, blocking them from using the shared resource until it is free.

### What is a mutex?
> A mutex behaves in the same way as a semaphore, but can only be toggled on or off. a semaphoore can exist as a variable and can therefore handle cases with limited but not singular resources or other more complex cases of shared resources. 

### What is the difference between a mutex and a binary semaphore?
> They behave similarly, but control is different. a process grabbing a mutex is the only one who can release the mutex, toggle it back to open. Control of a semaphore is shared, meaning any process can release it regardless of which process grabbed it. 

### What is a critical section?
> Any section using shared resources is a critical section, which must use atomic action to ensure correct execution of the running program

### What is the difference between race conditions and data races?
 > Race conditions describe timing issues between threads, but which can happen without programs accessing resources at the same time, just in undetermined sequence. A data race regards processes accessing resources at the same time,  making the received value uncertain. race conditions can happen without data race conditions being present.

### List some advantages of using message passing over lock-based synchronization primitives.
> message passing scales better, since messages can be sent asyncronously, reducing data demands. additionally, message passing can be easier to conceptualize over shared resources, which can be hard to follow as the number of processes increases. 

### List some advantages of using lock-based synchronization primitives over message passing.
Allows more efficient proocesses. is  in general better suited for limited applications over message passing. 
