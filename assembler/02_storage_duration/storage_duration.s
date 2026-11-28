
# gcc translated code of storage_duration.c in assembly


##Assembler Directives
	.file	"storage_duration.c"						#name of original file

	.intel_syntax noprefix								#syntax definition

	.text												#switch to .text section

	.globl	"a"											# declaration a as global symbol | visible for linker

	.data												# switch to .data section

	.align 4											# storage alignment | address mod 4 = 0 ? ; if not: (adress + padding 1) mod 4 = 0 ? .... 
"a":
	.long	10											# x86 system: .long = 4 Bytes and the value is 10
	.globl	"b"											
	.bss												#switch to .bss-section
	.align 4
"b":
	.space 4											 # Reserve 4 bytes in .bss, zero-initialized before program execution
	.text
	.globl	"main"										# main visible for linker
	.def	"main";	.scl	2;	.type	32;	.endef
	.seh_proc	"main"									# start of function metadata for Windows exception handling & stack unwinding
"main":
	push	rbp											#Save the previous base pointer
	.seh_pushreg	rbp									# tells Windows SEH that rbp was pushed (for stack unwinding)

	mov	rbp, rsp										# set new base pointer (rbp) to current stack pointer (rsp)
	.seh_setframe	rbp, 0								

	sub	rsp, 48											# reserve 48 bytes on the stack
	.seh_stackalloc	48
	.seh_endprologue
	call	"__main"
	mov	DWORD PTR -4[rbp], 20							# store 20 (4-byte int) into local variable on stack at [rbp - 4] | variable 'c'
	mov	eax, 0											#Sets the return value to 0
	add	rsp, 48											# release the 48bytes on the stack
	pop	rbp												#restore the previous base Pointer
	ret													# pops return address from stack and jumps back to caller
	.seh_endproc
.lcomm "e.1",4,4										# allocates 4 zero-initialized bytes in .bss for local static 'e'
	.data
	.align 4
"d.0":
	.long	30
	.def	"__main";	.scl	2;	.type	32;	.endef
	.ident	"GCC: (MinGW-W64 x86_64-ucrt-posix-seh, built by Brecht Sanders, r2) 16.2.0"
