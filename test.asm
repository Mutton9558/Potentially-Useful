@ Make code visible to Assembler
global _start
_start:

@ std::cout << "Hello World\n" equivalent
    mov r7, #4
    mov r0, #1
    ldr r1, =msg
    mov r2, #12
    svc 0

@ return 0 equivalent
    mov r7, #1
    mov r0, #0
    svc 0

msg:
    .ascii "Hello World\n"