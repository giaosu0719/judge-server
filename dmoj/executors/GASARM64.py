from dmoj.executors.asm_executor import GASExecutor, PlatformARM64Mixin


class Executor(PlatformARM64Mixin, GASExecutor):
    as_name = 'as_arm64'
    test_program = r"""
.global _start

_start:
    mov x8, #64          // syscall: write (64)
    mov x0, #1           // fd = 1 (stdout)
    ldr x1, =string      // buffer
    mov x2, #20          // length
    svc #0

    mov x8, #93          // syscall: exit (93)
    mov x0, #0
    svc #0

.data
string:
    .ascii "echo: Hello, World!\n"
"""
