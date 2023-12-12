	.section	__TEXT,__text,regular,pure_instructions
	.build_version macos, 14, 0	sdk_version 14, 0
	.globl	_init_str                       ; -- Begin function init_str
	.p2align	2
_init_str:                              ; @init_str
	.cfi_startproc
; %bb.0:
	sub	sp, sp, #32
	.cfi_def_cfa_offset 32
	stp	x29, x30, [sp, #16]             ; 16-byte Folded Spill
	add	x29, sp, #16
	.cfi_def_cfa w29, 16
	.cfi_offset w30, -8
	.cfi_offset w29, -16
	str	x0, [sp, #8]
	ldr	x0, [sp, #8]
	adrp	x1, l_.str@PAGE
	add	x1, x1, l_.str@PAGEOFF
	mov	x2, #-1
	bl	___strcpy_chk
	mov	w0, #0
	ldp	x29, x30, [sp, #16]             ; 16-byte Folded Reload
	add	sp, sp, #32
	ret
	.cfi_endproc
                                        ; -- End function
	.globl	_main                           ; -- Begin function main
	.p2align	2
_main:                                  ; @main
	.cfi_startproc
; %bb.0:
	sub	sp, sp, #96
	.cfi_def_cfa_offset 96
	stp	x29, x30, [sp, #80]             ; 16-byte Folded Spill
	add	x29, sp, #80
	.cfi_def_cfa w29, 16
	.cfi_offset w30, -8
	.cfi_offset w29, -16
	stur	wzr, [x29, #-4]
	stur	w0, [x29, #-8]
	stur	x1, [x29, #-16]
	sub	x0, x29, #21
	str	x0, [sp, #40]                   ; 8-byte Folded Spill
	bl	_init_str
	ldr	x8, [sp, #40]                   ; 8-byte Folded Reload
	mov	x9, sp
	str	x8, [x9]
	adrp	x0, l_.str.1@PAGE
	add	x0, x0, l_.str.1@PAGEOFF
	bl	_printf
	sub	x0, x29, #26
	str	x0, [sp, #32]                   ; 8-byte Folded Spill
	bl	_gets
	ldr	x1, [sp, #32]                   ; 8-byte Folded Reload
	ldr	x0, [sp, #40]                   ; 8-byte Folded Reload
	stur	wzr, [x29, #-32]
	mov	x2, #5
	bl	_strncmp
	subs	w8, w0, #0
	cset	w8, ne
	tbnz	w8, #0, LBB1_2
	b	LBB1_1
LBB1_1:
	mov	w8, #1
	stur	w8, [x29, #-32]
	b	LBB1_2
LBB1_2:
	ldur	w9, [x29, #-32]
                                        ; implicit-def: $x8
	mov	x8, x9
	mov	x9, sp
	sub	x10, x29, #21
	str	x10, [x9]
	sub	x10, x29, #26
	str	x10, [x9, #8]
	str	x8, [x9, #16]
	adrp	x0, l_.str.2@PAGE
	add	x0, x0, l_.str.2@PAGEOFF
	bl	_printf
	mov	w0, #0
	ldp	x29, x30, [sp, #80]             ; 16-byte Folded Reload
	add	sp, sp, #96
	ret
	.cfi_endproc
                                        ; -- End function
	.section	__TEXT,__cstring,cstring_literals
l_.str:                                 ; @.str
	.asciz	"ciao"

l_.str.1:                               ; @.str.1
	.asciz	"%s\n"

l_.str.2:                               ; @.str.2
	.asciz	"buffer1: str1(%s), str2(%s), valid(%d)\n"

.subsections_via_symbols
