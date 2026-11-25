/*
 * Project: Hello World
 * Architecture: x86-64
 * Operating System: Windows 64-bit
 * Assembler: GNU Assembler (GAS)
 * Toolchain: GCC / MinGW-w64
 * Syntax: Intel
 * Calling Convention: Microsoft x64 ABI
 */


#### .rdata area


#interpretation of assembly Syntax
.intel_syntax noprefix 

# .intel_syntax - assembly using intel syntax
# noprefix -  Register names do not require a preceding percentage character (%).

.section .rdata,"dr"

# .section - Switch to or create a specific section.
# .rdata - name of section
# "dr" - Initialized, read-only data (d = data, r = read-only) in Windows target format.

#message: - Label: startposition of the message

message:
    .asciz "Hello World!"



.text
.global main #stand for global. This will make the main available for other object files.


#### 


main:

    push rbp    # Save the previous base pointer
    mov rbp, rsp # Set the new base pointer
    sub rsp, 32 #Reserve 32 byte on the stack, Shadow Space | reservation down

    lea	rcx, message[rip] #calculate and save startadress of message in rcx
    #lea -   Load Effective Address
    # rcx - 64 bit: rcx --> complete register
    #rip = Instruction Pointer, 64-bit processor register that refers to the next machine instruction when running an instruction.


    call "printf"

    mov	eax, 0      #Sets the return value to 0
    add rsp, 32     # Release the shadow space
    pop rbp         # Restore the previous base pointer

    ret             #Jumps back to the place from which main was called
