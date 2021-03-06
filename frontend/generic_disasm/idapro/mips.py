# 
# Copyright (c) 2017 Sebastian Muniz
# 
# This code is part of point source decompiler
#

import idaapi


class InstructionSet(object):
    MIPS_add = idaapi.MIPS_add         # Add
    MIPS_addu = idaapi.MIPS_addu        # Add Unsigned
    MIPS_and = idaapi.MIPS_and         # AND
    MIPS_dadd = idaapi.MIPS_dadd        # Doubleword Add
    MIPS_daddu = idaapi.MIPS_daddu       # Doubleword Add Unsigned
    MIPS_dsub = idaapi.MIPS_dsub        # Doubleword Subtract
    MIPS_dsubu = idaapi.MIPS_dsubu       # Doubleword Subtract Unsigned
    MIPS_nor = idaapi.MIPS_nor         # NOR
    MIPS_or = idaapi.MIPS_or          # OR
    MIPS_slt = idaapi.MIPS_slt         # Set on Less Than
    MIPS_sltu = idaapi.MIPS_sltu        # Set on Less Than Unsigned
    MIPS_sub = idaapi.MIPS_sub         # Subtract
    MIPS_subu = idaapi.MIPS_subu        # Subtract Unsigned
    MIPS_xor = idaapi.MIPS_xor         # Exclusive OR
    MIPS_dsll = idaapi.MIPS_dsll        # Doubleword Shift Left Logical
    MIPS_dsll32 = idaapi.MIPS_dsll32      # Doubleword Shift Left Logical + 32
    MIPS_dsra = idaapi.MIPS_dsra        # Doubleword Shift Right Arithmetic
    MIPS_dsra32 = idaapi.MIPS_dsra32      # Doubleword Shift Right Arithmetic + 32
    MIPS_dsrl = idaapi.MIPS_dsrl        # Doubleword Shift Right Logical
    MIPS_dsrl32 = idaapi.MIPS_dsrl32      # Doubleword Shift Right Logical + 32
    MIPS_sll = idaapi.MIPS_sll         # Shift Left Logical
    MIPS_sra = idaapi.MIPS_sra         # Shift Right Arithmetic
    MIPS_srl = idaapi.MIPS_srl         # Shift Right Logical
    MIPS_dsllv = idaapi.MIPS_dsllv       # Doubleword Shift Left Logical Variable
    MIPS_dsrav = idaapi.MIPS_dsrav       # Doubleword Shift Right Arithmetic Variable
    MIPS_dsrlv = idaapi.MIPS_dsrlv       # Doubleword Shift Right Logical Variable
    MIPS_sllv = idaapi.MIPS_sllv        # Shift Left Logical Variable
    MIPS_srav = idaapi.MIPS_srav        # Shift Right Arithmetic Variable
    MIPS_srlv = idaapi.MIPS_srlv        # Shift Right Logical Variable
    MIPS_addi = idaapi.MIPS_addi        # Add Immediate
    MIPS_addiu = idaapi.MIPS_addiu       # Add Immediate Unsigned
    MIPS_daddi = idaapi.MIPS_daddi       # Doubleword Add Immediate
    MIPS_daddiu = idaapi.MIPS_daddiu      # Doubleword Add Immediate Unsigned
    MIPS_slti = idaapi.MIPS_slti        # Set on Less Than Immediate
    MIPS_sltiu = idaapi.MIPS_sltiu       # Set on Less Than Immediate Unsigned
    MIPS_andi = idaapi.MIPS_andi        # AND Immediate
    MIPS_ori = idaapi.MIPS_ori         # OR Immediate
    MIPS_xori = idaapi.MIPS_xori        # Exclusive OR Immediate
    MIPS_teq = idaapi.MIPS_teq         # Trap if Equal
    MIPS_tge = idaapi.MIPS_tge         # Trap if Greater Than or Equal
    MIPS_tgeu = idaapi.MIPS_tgeu        # Trap if Greater Than or Equal Unsigned
    MIPS_tlt = idaapi.MIPS_tlt         # Trap if Less Than
    MIPS_tltu = idaapi.MIPS_tltu        # Trap if Less Than Unsigned
    MIPS_tne = idaapi.MIPS_tne         # Trap if Not Equal
    MIPS_cfc1 = idaapi.MIPS_cfc1        # Move Control From FPU
    MIPS_cfc2 = idaapi.MIPS_cfc2        # Move Control From Coprocessor 2
    MIPS_ctc1 = idaapi.MIPS_ctc1        # Move Control to FPU
    MIPS_ctc2 = idaapi.MIPS_ctc2        # Move Control to Coprocessor 2
    MIPS_dmfc0 = idaapi.MIPS_dmfc0       # Doubleword Move From CP0
    MIPS_qmfc2 = idaapi.MIPS_qmfc2       # Quadword Move From CP2
    MIPS_dmtc0 = idaapi.MIPS_dmtc0       # Doubleword Move To CP0
    MIPS_qmtc2 = idaapi.MIPS_qmtc2       # Quadword Move To CP2
    MIPS_mfc0 = idaapi.MIPS_mfc0        # Move from CP0
    MIPS_mfc1 = idaapi.MIPS_mfc1        # Move from FPU
    MIPS_mfc2 = idaapi.MIPS_mfc2        # Move from CP2
    MIPS_mtc0 = idaapi.MIPS_mtc0        # Move to CP0
    MIPS_mtc1 = idaapi.MIPS_mtc1        # Move to FPU
    MIPS_mtc2 = idaapi.MIPS_mtc2        # Move to CP2
    MIPS_teqi = idaapi.MIPS_teqi        # Trap if Equal Immediate
    MIPS_tgei = idaapi.MIPS_tgei        # Trap if Greater Than or Equal Immediate
    MIPS_tgeiu = idaapi.MIPS_tgeiu       # Trap if Greater Than or Equal Immediate Unsigned
    MIPS_tlti = idaapi.MIPS_tlti        # Trap if Less Than Immediate
    MIPS_tltiu = idaapi.MIPS_tltiu       # Trap if Less Than Immediate Unsigned
    MIPS_tnei = idaapi.MIPS_tnei        # Trap if Not Equal Immediate
    MIPS_ddiv = idaapi.MIPS_ddiv        # Doubleword Divide
    MIPS_ddivu = idaapi.MIPS_ddivu       # Doubleword Divide Unsigned
    MIPS_div = idaapi.MIPS_div         # Divide
    MIPS_divu = idaapi.MIPS_divu        # Divide Unsigned
    MIPS_dmult = idaapi.MIPS_dmult       # Doubleword Multiply
    MIPS_dmultu = idaapi.MIPS_dmultu      # Doubleword Multiply Unsigned
    MIPS_mult = idaapi.MIPS_mult        # Multiply
    MIPS_multu = idaapi.MIPS_multu       # Multiply Unsigned
    MIPS_mthi = idaapi.MIPS_mthi        # Move To HI
    MIPS_mtlo = idaapi.MIPS_mtlo        # Move To LO
    MIPS_mfhi = idaapi.MIPS_mfhi        # Move From HI
    MIPS_mflo = idaapi.MIPS_mflo        # Move From LO
    MIPS_cop0 = idaapi.MIPS_cop0        # Coprocessor 0 Operation
    MIPS_cop1 = idaapi.MIPS_cop1        # FPU Operation
    MIPS_cop2 = idaapi.MIPS_cop2        # Coprocessor 2 Operation
    MIPS_break = idaapi.MIPS_break       # Break
    MIPS_syscall = idaapi.MIPS_syscall     # System Call
    MIPS_bc0f = idaapi.MIPS_bc0f        # Branch on Coprocessor 0 False
    MIPS_bc1f = idaapi.MIPS_bc1f        # Branch on FPU False
    MIPS_bc2f = idaapi.MIPS_bc2f        # Branch on Coprocessor 2 False
    MIPS_bc3f = idaapi.MIPS_bc3f        # Branch on Coprocessor 3 False
    MIPS_bc0fl = idaapi.MIPS_bc0fl       # Branch on Coprocessor 0 False Likely
    MIPS_bc1fl = idaapi.MIPS_bc1fl       # Branch on FPU False Likely
    MIPS_bc2fl = idaapi.MIPS_bc2fl       # Branch on Coprocessor 2 False Likely
    MIPS_bc3fl = idaapi.MIPS_bc3fl       # Branch on Coprocessor 3 False Likely
    MIPS_bc0t = idaapi.MIPS_bc0t        # Branch on Coprocessor 0 True
    MIPS_bc1t = idaapi.MIPS_bc1t        # Branch on FPU True
    MIPS_bc2t = idaapi.MIPS_bc2t        # Branch on Coprocessor 2 True
    MIPS_bc3t = idaapi.MIPS_bc3t        # Branch on Coprocessor 3 True
    MIPS_bc0tl = idaapi.MIPS_bc0tl       # Branch on Coprocessor 0 True Likely
    MIPS_bc1tl = idaapi.MIPS_bc1tl       # Branch on FPU True Likely
    MIPS_bc2tl = idaapi.MIPS_bc2tl       # Branch on Coprocessor 2 True Likely
    MIPS_bc3tl = idaapi.MIPS_bc3tl       # Branch on Coprocessor 3 True Likely
    MIPS_bgez = idaapi.MIPS_bgez        # Branch on Greater Than or Equal to Zero
    MIPS_bgezal = idaapi.MIPS_bgezal      # Branch on Greater Than or Equal to Zero And Link
    MIPS_bgezall = idaapi.MIPS_bgezall     # Branch on Greater Than or Equal to Zero And Link Likely
    MIPS_bgezl = idaapi.MIPS_bgezl       # Branch on Greater Than or Equal to Zero Likely
    MIPS_bgtz = idaapi.MIPS_bgtz        # Branch on Greater Than Zero
    MIPS_bgtzl = idaapi.MIPS_bgtzl       # Branch on Greater Than Zero Likely
    MIPS_blez = idaapi.MIPS_blez        # Branch on Less Than or Equal to Zero
    MIPS_blezl = idaapi.MIPS_blezl       # Branch on Less Than or Equal to Zero Likely
    MIPS_bltz = idaapi.MIPS_bltz        # Branch on Less Than Zero
    MIPS_bltzal = idaapi.MIPS_bltzal      # Branch on Less Than Zero And Link
    MIPS_bltzall = idaapi.MIPS_bltzall     # Branch on Less Than Zero And Link Likely
    MIPS_bltzl = idaapi.MIPS_bltzl       # Branch on Less Than Zero Likely
    MIPS_beq = idaapi.MIPS_beq         # Branch on Equal
    MIPS_beql = idaapi.MIPS_beql        # Branch on Equal Likely
    MIPS_bne = idaapi.MIPS_bne         # Branch on Not Equal
    MIPS_bnel = idaapi.MIPS_bnel        # Branch on Not Equal Likely
    MIPS_jalr = idaapi.MIPS_jalr        # Jump And Link Register
    MIPS_j = idaapi.MIPS_j           # Jump
    MIPS_jr = idaapi.MIPS_jr          # Jump Register
    MIPS_jal = idaapi.MIPS_jal         # Jump And Link
    MIPS_jalx = idaapi.MIPS_jalx        # Jump And Link And Exchange
    MIPS_cache = idaapi.MIPS_cache       # Cache Operation
    MIPS_lb = idaapi.MIPS_lb          # Load Byte
    MIPS_lbu = idaapi.MIPS_lbu         # Load Byte Unsigned
    MIPS_ldl = idaapi.MIPS_ldl         # Load Doubleword Left
    MIPS_ldr = idaapi.MIPS_ldr         # Load Doubleword Right
    MIPS_lwl = idaapi.MIPS_lwl         # Load Word Left
    MIPS_lwr = idaapi.MIPS_lwr         # Load Word Right
    MIPS_ld = idaapi.MIPS_ld          # Load Doubleword
    MIPS_lld = idaapi.MIPS_lld         # Load Linked Doubleword
    MIPS_ldc1 = idaapi.MIPS_ldc1        # Load Double FPU
    MIPS_ldc2 = idaapi.MIPS_ldc2        # Load Double Coprocessor 2
    MIPS_ll = idaapi.MIPS_ll          # Load Linked
    MIPS_lw = idaapi.MIPS_lw          # Load Word
    MIPS_lwu = idaapi.MIPS_lwu         # Load Word Unsigned
    MIPS_lh = idaapi.MIPS_lh          # Load Halfword
    MIPS_lhu = idaapi.MIPS_lhu         # Load Halfword Unsigned
    MIPS_lui = idaapi.MIPS_lui         # Load Upper Immediate
    MIPS_lwc1 = idaapi.MIPS_lwc1        # Load Word to FPU
    MIPS_lwc2 = idaapi.MIPS_lwc2        # Load Word to Coprocessor 2
    MIPS_sb = idaapi.MIPS_sb          # Store Byte
    MIPS_sdl = idaapi.MIPS_sdl         # Store Doubleword Left
    MIPS_sdr = idaapi.MIPS_sdr         # Store Doubleword Right
    MIPS_swl = idaapi.MIPS_swl         # Store Word Left
    MIPS_swr = idaapi.MIPS_swr         # Store Word Right
    MIPS_scd = idaapi.MIPS_scd         # Store Conditional Doubleword
    MIPS_sd = idaapi.MIPS_sd          # Store Doubleword
    MIPS_sdc1 = idaapi.MIPS_sdc1        # Store Double FPU
    MIPS_sdc2 = idaapi.MIPS_sdc2        # Store Double Coprocessor 2
    MIPS_sc = idaapi.MIPS_sc          # Store Conditional
    MIPS_sw = idaapi.MIPS_sw          # Store Word
    MIPS_sh = idaapi.MIPS_sh          # Store Halfword
    MIPS_swc1 = idaapi.MIPS_swc1        # Store Word from FPU
    MIPS_swc2 = idaapi.MIPS_swc2        # Store Word from Coprocessor 2
    MIPS_sync = idaapi.MIPS_sync        # Sync

    # Coprocessor 0 instructions

    MIPS_eret = idaapi.MIPS_eret        # Exception Return
    MIPS_tlbp = idaapi.MIPS_tlbp        # Probe TLB for Matching Entry
    MIPS_tlbr = idaapi.MIPS_tlbr        # Read Indexed TLB Entry
    MIPS_tlbwi = idaapi.MIPS_tlbwi       # Write Indexed TLB Entry
    MIPS_tlbwr = idaapi.MIPS_tlbwr       # Write Random TLB Entry


    # Coprocessor 1 (FPU) instructions

    MIPS_fadd = idaapi.MIPS_fadd        # Floating-point Add
    MIPS_fsub = idaapi.MIPS_fsub        # Floating-point Subtract
    MIPS_fmul = idaapi.MIPS_fmul        # Floating-point Multiply
    MIPS_fdiv = idaapi.MIPS_fdiv        # Floating-point Divide
    MIPS_fabs = idaapi.MIPS_fabs        # Floating-point Absolute Value
    MIPS_fcvt_s = idaapi.MIPS_fcvt_s      # Floating-point Convert to Single Fixed-Point Format
    MIPS_fcvt_d = idaapi.MIPS_fcvt_d      # Floating-point Convert to Double Floating-Point Format
    MIPS_fcvt_w = idaapi.MIPS_fcvt_w      # Floating-point Convert to Fixed-Point Format
    MIPS_fcvt_l = idaapi.MIPS_fcvt_l      # Floating-point Convert to Long Fixed-Point Format
    MIPS_fround_l = idaapi.MIPS_fround_l    # Floating-point Round to Long Fixed-Point Format
    MIPS_ftrunc_l = idaapi.MIPS_ftrunc_l    # Floating-point Truncate to Long Fixed-Point Format
    MIPS_fceil_l = idaapi.MIPS_fceil_l     # Floating-point Ceiling to Long Fixed-Point Format
    MIPS_ffloor_l = idaapi.MIPS_ffloor_l    # Floating-point Floor to Long Fixed-Point Format
    MIPS_fround_w = idaapi.MIPS_fround_w    # Floating-point Round to Single Fixed-Point Format
    MIPS_ftrunc_w = idaapi.MIPS_ftrunc_w    # Floating-point Truncate to Single Fixed-Point Format
    MIPS_fceil_w = idaapi.MIPS_fceil_w     # Floating-point Ceiling to Single Fixed-Point Format
    MIPS_ffloor_w = idaapi.MIPS_ffloor_w    # Floating-point Floor to Single Fixed-Point Format
    MIPS_fmov = idaapi.MIPS_fmov        # Floating-point Move
    MIPS_fneg = idaapi.MIPS_fneg        # Floating-point Negate
    MIPS_fsqrt = idaapi.MIPS_fsqrt       # Floating-point Square Root
    MIPS_fc_f = idaapi.MIPS_fc_f        # Floating-point Compare
    MIPS_fc_un = idaapi.MIPS_fc_un       # Floating-point Compare
    MIPS_fc_eq = idaapi.MIPS_fc_eq       # Floating-point Compare
    MIPS_fc_ueq = idaapi.MIPS_fc_ueq      # Floating-point Compare
    MIPS_fc_olt = idaapi.MIPS_fc_olt      # Floating-point Compare
    MIPS_fc_ult = idaapi.MIPS_fc_ult      # Floating-point Compare
    MIPS_fc_ole = idaapi.MIPS_fc_ole      # Floating-point Compare
    MIPS_fc_ule = idaapi.MIPS_fc_ule      # Floating-point Compare
    MIPS_fc_sf = idaapi.MIPS_fc_sf       # Floating-point Compare
    MIPS_fc_ngle = idaapi.MIPS_fc_ngle     # Floating-point Compare
    MIPS_fc_seq = idaapi.MIPS_fc_seq      # Floating-point Compare
    MIPS_fc_ngl = idaapi.MIPS_fc_ngl      # Floating-point Compare
    MIPS_fc_lt = idaapi.MIPS_fc_lt       # Floating-point Compare
    MIPS_fc_nge = idaapi.MIPS_fc_nge      # Floating-point Compare
    MIPS_fc_le = idaapi.MIPS_fc_le       # Floating-point Compare
    MIPS_fc_ngt = idaapi.MIPS_fc_ngt      # Floating-point Compare

    # Pseudo instructions

    MIPS_nop = idaapi.MIPS_nop         # No operation
    MIPS_mov = idaapi.MIPS_mov         # Move register
    MIPS_neg = idaapi.MIPS_neg         # Negate
    MIPS_negu = idaapi.MIPS_negu        # Negate Unsigned
    MIPS_bnez = idaapi.MIPS_bnez        # Branch on Not Zero
    MIPS_bnezl = idaapi.MIPS_bnezl       # Branch on Not Zero Likely
    MIPS_beqz = idaapi.MIPS_beqz        # Branch on Zero
    MIPS_beqzl = idaapi.MIPS_beqzl       # Branch on Zero Likely
    MIPS_b = idaapi.MIPS_b           # Branch Always
    MIPS_bal = idaapi.MIPS_bal         # Branch Always and Link
    MIPS_li = idaapi.MIPS_li          # Load Immediate
    MIPS_la = idaapi.MIPS_la          # Load Address

    # MIPS IV instructions

    MIPS_pref = idaapi.MIPS_pref        # Prefetch
    MIPS_ldxc1 = idaapi.MIPS_ldxc1       # Load Doubleword Indexed to Floating Point
    MIPS_lwxc1 = idaapi.MIPS_lwxc1       # Load Word Indexed to Floating Point
    MIPS_sdxc1 = idaapi.MIPS_sdxc1       # Store Doubleword Indexed from Floating Point
    MIPS_swxc1 = idaapi.MIPS_swxc1       # Store Word Indexed from Floating Point
    MIPS_madd_s = idaapi.MIPS_madd_s      # Floating-Point Multiply Add
    MIPS_madd_d = idaapi.MIPS_madd_d      # Floating-Point Multiply Add
    MIPS_msub_s = idaapi.MIPS_msub_s      # Floating-Point Multiply Subtract
    MIPS_msub_d = idaapi.MIPS_msub_d      # Floating-Point Multiply Subtract
    MIPS_movf = idaapi.MIPS_movf        # Move Conditional on FP False
    MIPS_movt = idaapi.MIPS_movt        # Move Conditional on FP True
    MIPS_movn = idaapi.MIPS_movn        # Move Conditional on Not Zero
    MIPS_movz = idaapi.MIPS_movz        # Move Conditional on Zero
    MIPS_fmovf = idaapi.MIPS_fmovf       # Floating-Point Move Conditional on FP False
    MIPS_fmovt = idaapi.MIPS_fmovt       # Floating-Point Move Conditional on FP True
    MIPS_fmovn = idaapi.MIPS_fmovn       # Floating-Point Move Conditional on Not Zero
    MIPS_fmovz = idaapi.MIPS_fmovz       # Floating-Point Move Conditional on Zero
    MIPS_nmadd_s = idaapi.MIPS_nmadd_s     # Floating-Pont Negative Multiply Add
    MIPS_nmadd_d = idaapi.MIPS_nmadd_d     # Floating-Pont Negative Multiply Add
    MIPS_nmsub_s = idaapi.MIPS_nmsub_s     # Floating-Pont Negative Multiply Subtract
    MIPS_nmsub_d = idaapi.MIPS_nmsub_d     # Floating-Pont Negative Multiply Subtract
    MIPS_prefx = idaapi.MIPS_prefx       # Prefetch Indexed
    MIPS_frecip = idaapi.MIPS_frecip      # Reciprocal Approximation
    MIPS_frsqrt = idaapi.MIPS_frsqrt      # Reciprocal Suare Root Approximation

    # RSP instructions

    MIPS_lbv = idaapi.MIPS_lbv         # Load Byte into Vector
    MIPS_lsv = idaapi.MIPS_lsv         # Load Short into Vector
    MIPS_llv = idaapi.MIPS_llv         # Load Word into Vector
    MIPS_ldv = idaapi.MIPS_ldv         # Load Doubleword into Vector
    MIPS_lqv = idaapi.MIPS_lqv         # Load Quadword into Vector
    MIPS_lrv = idaapi.MIPS_lrv         # Load Rest Vector
    MIPS_lpv = idaapi.MIPS_lpv         # Load Packed Vector
    MIPS_luv = idaapi.MIPS_luv         # Load Unpack Vector
    MIPS_lhv = idaapi.MIPS_lhv         # Load Half Vector
    MIPS_lfv = idaapi.MIPS_lfv         # Load Fourth Vector
    MIPS_lwv = idaapi.MIPS_lwv         # Load Wrap Vector
    MIPS_ltv = idaapi.MIPS_ltv         # Load Transpose Vector
    MIPS_sbv = idaapi.MIPS_sbv         # Store Byte from Vector
    MIPS_ssv = idaapi.MIPS_ssv         # Store Short from Vector
    MIPS_slv = idaapi.MIPS_slv         # Store Word from Vector
    MIPS_sdv = idaapi.MIPS_sdv         # Store Doubleword from Vector
    MIPS_sqv = idaapi.MIPS_sqv         # Store Quadword from Vector
    MIPS_srv = idaapi.MIPS_srv         # Store Rest Vector
    MIPS_spv = idaapi.MIPS_spv         # Store Packed Vector
    MIPS_suv = idaapi.MIPS_suv         # Store Unpack Vector
    MIPS_shv = idaapi.MIPS_shv         # Store Half Vector
    MIPS_sfv = idaapi.MIPS_sfv         # Store Fourth Vector
    MIPS_swv = idaapi.MIPS_swv         # Store Wrap Vector
    MIPS_stv = idaapi.MIPS_stv         # Store Transpose Vector
    MIPS_vmulf = idaapi.MIPS_vmulf       # Vector (Frac) Multiply
    MIPS_vmacf = idaapi.MIPS_vmacf       # Vector (Frac) Multiply Accumulate
    MIPS_vmulu = idaapi.MIPS_vmulu       # Vector (Unsigned Frac) Multiply
    MIPS_vmacu = idaapi.MIPS_vmacu       # Vector (Unsigned Frac) Multiply Accumulate
    MIPS_vrndp = idaapi.MIPS_vrndp       # Vector DCT Round (+)
    MIPS_vrndn = idaapi.MIPS_vrndn       # Vector DCT Round (-)
    MIPS_vmulq = idaapi.MIPS_vmulq       # Vector (Integer) Multiply
    MIPS_vmacq = idaapi.MIPS_vmacq       # Vector (Integer) Multiply Accumulate
    MIPS_vmudh = idaapi.MIPS_vmudh       # Vector (High) Multiply
    MIPS_vmadh = idaapi.MIPS_vmadh       # Vector (High) Multiply Accumulate
    MIPS_vmudm = idaapi.MIPS_vmudm       # Vector (Mid-M) Multiply
    MIPS_vmadm = idaapi.MIPS_vmadm       # Vector (Mid-M) Multiply Accumulate
    MIPS_vmudn = idaapi.MIPS_vmudn       # Vector (Mid-N) Multiply
    MIPS_vmadn = idaapi.MIPS_vmadn       # Vector (Mid-N) Multiply Accumulate
    MIPS_vmudl = idaapi.MIPS_vmudl       # Vector (Low) Multiply
    MIPS_vmadl = idaapi.MIPS_vmadl       # Vector (Low) Multiply Accumulate
    MIPS_vadd = idaapi.MIPS_vadd        # Vector Add
    MIPS_vsub = idaapi.MIPS_vsub        # Vector Subtract
    MIPS_vsut = idaapi.MIPS_vsut        # Vector SUT (vt - vs)
    MIPS_vabs = idaapi.MIPS_vabs        # Vector Absolute Value
    MIPS_vaddc = idaapi.MIPS_vaddc       # Vector ADDC
    MIPS_vsubc = idaapi.MIPS_vsubc       # Vector SUBC
    MIPS_vaddb = idaapi.MIPS_vaddb       # Vector Add Byte
    MIPS_vsubb = idaapi.MIPS_vsubb       # Vector Subtract Byte
    MIPS_vaccb = idaapi.MIPS_vaccb       # Vector Add Byte/Add Accumulator
    MIPS_vsucb = idaapi.MIPS_vsucb       # Vector Subtract Byte/Add Accumulator
    MIPS_vsad = idaapi.MIPS_vsad        # Vector SAD
    MIPS_vsac = idaapi.MIPS_vsac        # Vector SAC
    MIPS_vsum = idaapi.MIPS_vsum        # Vector SUM
    MIPS_vsaw = idaapi.MIPS_vsaw        # Vector SAW
    MIPS_vlt = idaapi.MIPS_vlt         # Vector Less Than
    MIPS_veq = idaapi.MIPS_veq         # Vector Equal To
    MIPS_vne = idaapi.MIPS_vne         # Vector Not Equal To
    MIPS_vge = idaapi.MIPS_vge         # Vector Greater Than or Equal To
    MIPS_vcl = idaapi.MIPS_vcl         # Vector Clip Low
    MIPS_vch = idaapi.MIPS_vch         # Vector Clip High
    MIPS_vcr = idaapi.MIPS_vcr         # Vector 1's Complement Clip
    MIPS_vmrg = idaapi.MIPS_vmrg        # Vector Merge
    MIPS_vand = idaapi.MIPS_vand        # Vector Logical AND
    MIPS_vnand = idaapi.MIPS_vnand       # Vector Logical NAND
    MIPS_vor = idaapi.MIPS_vor         # Vector Logical OR
    MIPS_vnor = idaapi.MIPS_vnor        # Vector Logical NOR
    MIPS_vxor = idaapi.MIPS_vxor        # Vector Logical Exclusive OR
    MIPS_vnxor = idaapi.MIPS_vnxor       # Vector Logical NOT Exclusive OR
    MIPS_vnoop = idaapi.MIPS_vnoop       # Vector No-Operation
    MIPS_vmov = idaapi.MIPS_vmov        # Vector Scalar-Element Move
    MIPS_vrcp = idaapi.MIPS_vrcp        # Single Precision, Lookup Source, Write Result
    MIPS_vrsq = idaapi.MIPS_vrsq        # Single Precision, Lookup Source, Write Result
    MIPS_vrcph = idaapi.MIPS_vrcph       # Set Source, Write Previous Result
    MIPS_vrsqh = idaapi.MIPS_vrsqh       # Set Source, Write Previous Result
    MIPS_vrcpl = idaapi.MIPS_vrcpl       # Lookup Source and Previous, Write Result
    MIPS_vrsql = idaapi.MIPS_vrsql       # Lookup Source and Previous, Write Result
    MIPS_vinst = idaapi.MIPS_vinst       # Vector Insert Triple (5/5/5/1)
    MIPS_vextt = idaapi.MIPS_vextt       # Vector Extract Triple (5/5/5/1)
    MIPS_vinsq = idaapi.MIPS_vinsq       # Vector Insert Quad (4/4/4/4)
    MIPS_vextq = idaapi.MIPS_vextq       # Vector Extract Quad (4/4/4/4)
    MIPS_vinsn = idaapi.MIPS_vinsn       # Vector Insert Nibble (4/4/4/4) Sign-Extended
    MIPS_vextn = idaapi.MIPS_vextn       # Vector Insert Nibble (4/4/4/4) Sign-Extended
    MIPS_cfc0 = idaapi.MIPS_cfc0        # Move Control From Coprocessor 0
    MIPS_ctc0 = idaapi.MIPS_ctc0        # Move Control to Coprocessor 0

    # R5900 (PSX2 or PlayStation2) processor additional commands

    MIPS_mtsa = idaapi.MIPS_mtsa              # Move To Shift Amount Register
    MIPS_R5900_first = MIPS_mtsa,
    MIPS_mfsa = idaapi.MIPS_mfsa              # Move From Shift Amount Register
    MIPS_mtsab = idaapi.MIPS_mtsab             # Move Byte Count To Shift Amount Register
    MIPS_mtsah = idaapi.MIPS_mtsah             # Move Halfword Count To Shift Amount Register
    MIPS_fadda = idaapi.MIPS_fadda             # Floating-point add to accumulator
    MIPS_fsuba = idaapi.MIPS_fsuba             # Floating-point subtract to accumulator
    MIPS_fmula = idaapi.MIPS_fmula             # Floating-point multiply to accumulator
    MIPS_fmadda = idaapi.MIPS_fmadda            # Floating-point multiply and add to accumulator
    MIPS_fmsuba = idaapi.MIPS_fmsuba            # Floating-point multiply and subtract from accumulator
    MIPS_fmadd = idaapi.MIPS_fmadd             # Floating-point multiply and add
    MIPS_fmsub = idaapi.MIPS_fmsub             # Floating-point multiply and subtract
    MIPS_fmax = idaapi.MIPS_fmax              # Floating-point maximum
    MIPS_fmin = idaapi.MIPS_fmin              # Floating-point minimum
    MIPS_plzcw = idaapi.MIPS_plzcw             # Parallel Leading Zero or One Count Word
    MIPS_mthi1 = idaapi.MIPS_mthi1             # Move To HI1 Register
    MIPS_mtlo1 = idaapi.MIPS_mtlo1             # Move To LO1 Register
    MIPS_pmthl_lw = idaapi.MIPS_pmthl_lw          # Parallel Move From HI/LO Register
    MIPS_pmthi = idaapi.MIPS_pmthi             # Parallel Move To HI Register
    MIPS_pmtlo = idaapi.MIPS_pmtlo             # Parallel Move To LO Register
    MIPS_div1 = idaapi.MIPS_div1              # Divide Pipeline 1
    MIPS_divu1 = idaapi.MIPS_divu1             # Divide Unsigned Pipeline 1
    MIPS_pdivw = idaapi.MIPS_pdivw             # Parallel Divide Word
    MIPS_pdivuw = idaapi.MIPS_pdivuw            # Parallel Divide Unsigned Word
    MIPS_pdivbw = idaapi.MIPS_pdivbw            # Parallel Divide Broadcast Word
    MIPS_paddw = idaapi.MIPS_paddw             # Parallel Add Word
    MIPS_pmaddw = idaapi.MIPS_pmaddw            # Parallel Multiply-Add Word
    MIPS_mult1 = idaapi.MIPS_mult1             # Multiply Pipeline 1
    MIPS_multu1 = idaapi.MIPS_multu1            # Multiply Unsigned Pipeline 1
    MIPS_madd1 = idaapi.MIPS_madd1             # Multiply-Add Pipeline 1
    MIPS_maddu1 = idaapi.MIPS_maddu1            # Multiply-Add Unsigned Pipeline 1
    MIPS_pmadduw = idaapi.MIPS_pmadduw           # Parallel Multiply-Add Unsigned Word
    MIPS_psubw = idaapi.MIPS_psubw             # Parallel Subtract HalfWord
    MIPS_pcgtw = idaapi.MIPS_pcgtw             # Parallel Compare for Greater Than Word
    MIPS_psllvw = idaapi.MIPS_psllvw            # Parallel Shift Left Logical Variable Word
    MIPS_pceqw = idaapi.MIPS_pceqw             # Parallel Compare for Equal Word
    MIPS_pmaxw = idaapi.MIPS_pmaxw             # Parallel Maximize Word
    MIPS_psrlvw = idaapi.MIPS_psrlvw            # Parallel Shift Right Logical Variable Word
    MIPS_pminw = idaapi.MIPS_pminw             # Parallel Minimize Word
    MIPS_psravw = idaapi.MIPS_psravw            # Parallel Shift Right Arithmetic Variable Word
    MIPS_paddh = idaapi.MIPS_paddh             # Parallel Add Halfword
    MIPS_pmsubw = idaapi.MIPS_pmsubw            # Parallel Multiply-Subtract Word
    MIPS_padsbh = idaapi.MIPS_padsbh            # Parallel Add/Subtract Halfword
    MIPS_psubh = idaapi.MIPS_psubh             # Parallel Subtract Halfword
    MIPS_pcgth = idaapi.MIPS_pcgth             # Parallel Compare for Greater Than Halfword
    MIPS_pceqh = idaapi.MIPS_pceqh             # Parallel Compare for Equal Halfword
    MIPS_pmaxh = idaapi.MIPS_pmaxh             # Parallel Maximize Halfword
    MIPS_pminh = idaapi.MIPS_pminh             # Parallel Minimize Halfword
    MIPS_paddb = idaapi.MIPS_paddb             # Parallel Add Byte
    MIPS_psubb = idaapi.MIPS_psubb             # Parallel Subtract Byte
    MIPS_pcgtb = idaapi.MIPS_pcgtb             # Parallel Compare for Greater Than Byte
    MIPS_pinth = idaapi.MIPS_pinth             # Parallel Interleave Halfword
    MIPS_pceqb = idaapi.MIPS_pceqb             # Parallel Compare for Equal Byte
    MIPS_pintoh = idaapi.MIPS_pintoh            # Parallel Interleave Odd Halfword
    MIPS_pmultw = idaapi.MIPS_pmultw            # Parallel Multiply Word
    MIPS_pmultuw = idaapi.MIPS_pmultuw           # Parallel Multiply Unsigned Word
    MIPS_pcpyld = idaapi.MIPS_pcpyld            # Parallel Copy Lower Doubleword
    MIPS_pcpyud = idaapi.MIPS_pcpyud            # Parallel Copy Upper Doubleword
    MIPS_paddsw = idaapi.MIPS_paddsw            # Parallel Add with Signed Saturation Word
    MIPS_pmaddh = idaapi.MIPS_pmaddh            # Parallel Multiply-Add Halfword
    MIPS_padduw = idaapi.MIPS_padduw            # Parallel Add with Unsigned Saturation Word
    MIPS_psubsw = idaapi.MIPS_psubsw            # Parallel Subtract with Signed Saturation Word
    MIPS_phmadh = idaapi.MIPS_phmadh            # Parallel Horizontal Multiply-Add Halfword
    MIPS_psubuw = idaapi.MIPS_psubuw            # Parallel Subtract with Unsigned Saturation Word
    MIPS_pextlw = idaapi.MIPS_pextlw            # Parallel Extend Lower from Word
    MIPS_pand = idaapi.MIPS_pand              # Parallel AND
    MIPS_pextuw = idaapi.MIPS_pextuw            # Parallel Extend Upper from Word
    MIPS_por = idaapi.MIPS_por               # Parallel OR
    MIPS_ppacw = idaapi.MIPS_ppacw             # Paralle Pack to Word
    MIPS_pxor = idaapi.MIPS_pxor              # Parallel XOR
    MIPS_pnor = idaapi.MIPS_pnor              # Parallel NOR
    MIPS_paddsh = idaapi.MIPS_paddsh            # Parallel Add with Signed Saturation Halfword
    MIPS_pmsubh = idaapi.MIPS_pmsubh            # Parallel Multiply-Subtract Halfword
    MIPS_padduh = idaapi.MIPS_padduh            # Parallel Add with Unsigned Saturation Halfword
    MIPS_psubsh = idaapi.MIPS_psubsh            # Parallel Subtract with Signed Saturation Halfword
    MIPS_phmsbh = idaapi.MIPS_phmsbh            # Parallel Horizontal Multiply-Subtract Halfword
    MIPS_psubuh = idaapi.MIPS_psubuh            # Parallel Subtract with Unsigned Saturation Halfword
    MIPS_pextlh = idaapi.MIPS_pextlh            # Parallel Extend Lower from Halfword
    MIPS_pextuh = idaapi.MIPS_pextuh            # Parallel Extend Upper from Halfword
    MIPS_ppach = idaapi.MIPS_ppach             # Paralle Pack to Halfword
    MIPS_paddsb = idaapi.MIPS_paddsb            # Parallel Add with Signed Saturation Byte
    MIPS_paddub = idaapi.MIPS_paddub            # Parallel Add with Unsigned Saturation Byte
    MIPS_psubsb = idaapi.MIPS_psubsb            # Parallel Subtract with Signed Saturation Byte
    MIPS_psubub = idaapi.MIPS_psubub            # Parallel Subtract with Unsigned Saturation Byte
    MIPS_pextlb = idaapi.MIPS_pextlb            # Parallel Extend Lower from Byte
    MIPS_pextub = idaapi.MIPS_pextub            # Parallel Extend Upper from Byte
    MIPS_ppacb = idaapi.MIPS_ppacb             # Paralle Pack to Byte
    MIPS_qfsrv = idaapi.MIPS_qfsrv             # Quadword Funnel Shift Right Variable
    MIPS_pmulth = idaapi.MIPS_pmulth            # Parallel Multiply Halfword
    MIPS_pabsw = idaapi.MIPS_pabsw             # Parallel Absolute Word
    MIPS_pabsh = idaapi.MIPS_pabsh             # Parallel Absolute Halfword
    MIPS_pexoh = idaapi.MIPS_pexoh             # Parallel Exchange Odd Halfword
    MIPS_pexch = idaapi.MIPS_pexch             # Parallel Exchange Center Halfword
    MIPS_prevh = idaapi.MIPS_prevh             # Parallel Reverse Halfword
    MIPS_pcpyh = idaapi.MIPS_pcpyh             # Parallel Copy Halfword
    MIPS_pext5 = idaapi.MIPS_pext5             # Parallel Extend Upper from 5 bits
    MIPS_pexow = idaapi.MIPS_pexow             # Parallel Exchange Odd Word
    MIPS_pexcw = idaapi.MIPS_pexcw             # Parallel Exchange Center Word
    MIPS_ppac5 = idaapi.MIPS_ppac5             # Parallel Pack to 5 bits
    MIPS_prot3w = idaapi.MIPS_prot3w            # Parallel Rotate 3 Words
    MIPS_psllh = idaapi.MIPS_psllh             # Parallel Shift Left Logical Halfword
    MIPS_psrlh = idaapi.MIPS_psrlh             # Parallel Shift Right Logical Halfword
    MIPS_psrah = idaapi.MIPS_psrah             # Parallel Shift Right Arithmetic Halfword
    MIPS_psllw = idaapi.MIPS_psllw             # Parallel Shift Left Logical Word
    MIPS_psrlw = idaapi.MIPS_psrlw             # Parallel Shift Right Logical Word
    MIPS_psraw = idaapi.MIPS_psraw             # Parallel Shift Right Arithmetic Word
    MIPS_mfhi1 = idaapi.MIPS_mfhi1             # Move From HI1 Register
    MIPS_mflo1 = idaapi.MIPS_mflo1             # Move From LO1 Register
    MIPS_pmfhi = idaapi.MIPS_pmfhi             # Parallel Move From HI Register
    MIPS_pmflo = idaapi.MIPS_pmflo             # Parallel Move From LO Register
    MIPS_pmfhl = idaapi.MIPS_pmfhl             # Parallel Move From HI/LO Register
    MIPS_lq = idaapi.MIPS_lq                # Load Quadword
    MIPS_sq = idaapi.MIPS_sq                # Store Quadword
    MIPS_lqc2 = idaapi.MIPS_lqc2              # Load Quadword Coprocessor 2
    MIPS_sqc2 = idaapi.MIPS_sqc2              # Store Quadword Coprocessor 2
    MIPS_madd_r5900 = idaapi.MIPS_madd_r5900        # Multiply/Add
    MIPS_maddu_r5900 = idaapi.MIPS_maddu_r5900       # Multiply/Add Unsigned
    MIPS_R5900_last = MIPS_maddu_r5900,
    MIPS_mult3 = idaapi.MIPS_mult3             # Multiply (3-operand)
    MIPS_multu3 = idaapi.MIPS_multu3            # Multiply Unsigned (3-operand)

    # 16-bit instructions
    # NOTE: in previous version of IDA, all mips16 instructions
    #  had separate numbers, even for the instructions with the
    #  same mnemonics. Now same mnemonics have the same numbers,
    #  regardless of the encoding.

    MIPS_bteqz = idaapi.MIPS_bteqz           # Branch on T Equal to Zero
    MIPS_btnez = idaapi.MIPS_btnez               # Branch on T Not Equal to Zero
    MIPS_cmp = idaapi.MIPS_cmp                 # Compare
    MIPS_cmpi = idaapi.MIPS_cmpi                # Compare Immediate
    MIPS_extend = idaapi.MIPS_extend          # Extend
    MIPS_move = idaapi.MIPS_mov            # Move
    MIPS_not = idaapi.MIPS_not             # Not
    MIPS_dla = idaapi.MIPS_dla             # Load 64-bit address

    # Instructions which belong to MIPS32 but which were not decoded by IDA

    MIPS_clo = idaapi.MIPS_clo           # Count Leading Ones in Word
    MIPS_clz = idaapi.MIPS_clz               # Count Leading Zeros in Word
    MIPS_madd = idaapi.MIPS_madd              # Multiply/Add
    MIPS_maddu = idaapi.MIPS_maddu             # Multiply/Add Unsigned
    MIPS_msub = idaapi.MIPS_msub              # Multiply and Subtract Word to Hi,Lo
    MIPS_msubu = idaapi.MIPS_msubu             # Multiply and Subtract Word to Hi,Lo
    MIPS_mul = idaapi.MIPS_mul               # Multiply Word to GPR
    MIPS_sdbbp = idaapi.MIPS_sdbbp             # Software Debug Breakpoint
    MIPS_wait = idaapi.MIPS_wait              # Enter Standby Mode

    # New instructions for MIPS32 Release 2.0

    MIPS_alnv_ps = idaapi.MIPS_alnv_ps           # Floating Point Align Variable
    MIPS_deret = idaapi.MIPS_deret             # Debug Exception Return
    MIPS_di = idaapi.MIPS_di                # Disable interrupts
    MIPS_ehb = idaapi.MIPS_ehb               # Execution Hazard Barrier
    MIPS_ei = idaapi.MIPS_ei                # Enable interrupts
    MIPS_ext = idaapi.MIPS_ext               # Extract Bit Field
    MIPS_fcvt_ps = idaapi.MIPS_fcvt_ps           # Floating Point Convert Pair to Paired Single
    MIPS_fcvt_s_pl = idaapi.MIPS_fcvt_s_pl         # Floating Point Convert Pair Lower to Single Floating Point
    MIPS_fcvt_s_pu = idaapi.MIPS_fcvt_s_pu         # Floating Point Convert Pair Upper to Single Floating Point
    MIPS_ins = idaapi.MIPS_ins               # Insert Bit Field
    MIPS_jalr_hb = idaapi.MIPS_jalr_hb           # Jump and Link Register with Hazard Barrier
    MIPS_jr_hb = idaapi.MIPS_jr_hb             # Jump Register with Hazard Barrier
    MIPS_luxc1 = idaapi.MIPS_luxc1             # Load Doubleword Indexed Unaligned to Floating Point
    MIPS_madd_ps = idaapi.MIPS_madd_ps           # Floating Point Multiply Add
    MIPS_mfhc1 = idaapi.MIPS_mfhc1             # Move Word from High Half of Floating Point Register
    MIPS_mfhc2 = idaapi.MIPS_mfhc2             # Move Word from High Half of Coprocessor 2 Register
    MIPS_msub_ps = idaapi.MIPS_msub_ps           # Floating Point Multiply Subtract
    MIPS_mthc1 = idaapi.MIPS_mthc1             # Move Word to High Half of Floating Point Register
    MIPS_mthc2 = idaapi.MIPS_mthc2             # Move Word to High Half of Coprocessor 2 Register
    MIPS_nmadd_ps = idaapi.MIPS_nmadd_ps          # Floating Point Negative Multiply Add
    MIPS_nmsub_ps = idaapi.MIPS_nmsub_ps          # Floating Point Negative Multiply Subtract
    MIPS_pll = idaapi.MIPS_pll               # Pair Lower Lower
    MIPS_plu = idaapi.MIPS_plu               # Pair Lower Upper
    MIPS_pul = idaapi.MIPS_pul               # Pair Upper Lower
    MIPS_puu = idaapi.MIPS_puu               # Pair Upper Upper
    MIPS_rdhwr = idaapi.MIPS_rdhwr             # Read Hardware Register
    MIPS_rdpgpr = idaapi.MIPS_rdpgpr            # Read GPR from Previous Shadow Set
    MIPS_rotr = idaapi.MIPS_rotr              # Rotate Word Right
    MIPS_rotrv = idaapi.MIPS_rotrv             # Rotate Word Right Variable
    MIPS_seb = idaapi.MIPS_seb               # Sign-Extend Byte
    MIPS_seh = idaapi.MIPS_seh               # Sign-Extend Halfword
    MIPS_suxc1 = idaapi.MIPS_suxc1             # Store Doubleword Indexed Unaligned from Floating Point
    MIPS_synci = idaapi.MIPS_synci             # Synchronize Caches to Make Instruction Writes Effective
    MIPS_wrpgpr = idaapi.MIPS_wrpgpr            # Write GPR to Previous Shadow Set
    MIPS_wsbh = idaapi.MIPS_wsbh              # Word Swap Bytes Within Halfwords

    # Missing instructions - for some reason they were not supported before

    MIPS_dmfc1 = idaapi.MIPS_dmfc1             # Doubleword Move From CP1
    MIPS_dmtc1 = idaapi.MIPS_dmtc1             # Doubleword Move To CP1

    # additional MIPS16e instructions

    MIPS_save = idaapi.MIPS_save              # Save Registers and Set Up Stack Frame
    MIPS_restore = idaapi.MIPS_restore           # Restore Registers and Deallocate Stack Frame
    MIPS_jalrc = idaapi.MIPS_jalrc             # Jump and Link Register, Compact
    MIPS_jrc = idaapi.MIPS_jrc               # Jump Register, Compact
    MIPS_sew = idaapi.MIPS_sew               # Sign-Extend Word
    MIPS_zeb = idaapi.MIPS_zeb               # Zero-Extend Byte
    MIPS_zeh = idaapi.MIPS_zeh               # Zero-Extend Halfword
    MIPS_zew = idaapi.MIPS_zew               # Zero-Extend Word

    # extra pseudoinstructions
    MIPS_ssnop = idaapi.MIPS_ssnop             # Superscalar No operation
    MIPS_li_s = idaapi.MIPS_li_s              # Load floating-point immediate
    MIPS_li_d = idaapi.MIPS_li_d              # Load floating-point immediate
    MIPS_dneg = idaapi.MIPS_dneg              # Negate
    MIPS_dnegu = idaapi.MIPS_dnegu             # Negate Unsigned
    MIPS_pause = idaapi.MIPS_pause             # Wait for the LLBit to clear

    # Missing instructions from MIPS64 Release 2

    MIPS_dclo = idaapi.MIPS_dclo              # Count Leading Ones in Doubleword
    MIPS_dclz = idaapi.MIPS_dclz              # Count Leading Zeros in Doubleword
    MIPS_dext = idaapi.MIPS_dext              # Doubleword Extract Bit Field
    MIPS_dextm = idaapi.MIPS_dextm             # Doubleword Extract Bit Field Middle
    MIPS_dextu = idaapi.MIPS_dextu             # Doubleword Extract Bit Field Upper
    MIPS_dins = idaapi.MIPS_dins              # Doubleword Insert Bit Field
    MIPS_dinsm = idaapi.MIPS_dinsm             # Doubleword Insert Bit Field Middle
    MIPS_dinsu = idaapi.MIPS_dinsu             # Doubleword Insert Bit Field Upper
    MIPS_dmfc2 = idaapi.MIPS_dmfc2             # Doubleword Move From CP2
    MIPS_dmtc2 = idaapi.MIPS_dmtc2             # Doubleword Move To CP2
    MIPS_drotr = idaapi.MIPS_drotr             # Doubleword Rotate Right
    MIPS_drotr32 = idaapi.MIPS_drotr32           # Doubleword Rotate Right Plus 32
    MIPS_drotrv = idaapi.MIPS_drotrv            # Doubleword Rotate Right Variable
    MIPS_dsbh = idaapi.MIPS_dsbh              # Doubleword Swap Bytes Within Halfwords
    MIPS_dshd = idaapi.MIPS_dshd              # Doubleword Swap Halfwords Within Doublewords

    # cnMIPS (Cavium Networks Octeon) instructions

    MIPS_baddu = idaapi.MIPS_baddu             # Unsigned Byte Add
    MIPS_bbit0 = idaapi.MIPS_bbit0             # Branch on Bit Clear
    MIPS_bbit032 = idaapi.MIPS_bbit032           # Branch on Bit Clear Plus 32
    MIPS_bbit1 = idaapi.MIPS_bbit1             # Branch on Bit Set
    MIPS_bbit132 = idaapi.MIPS_bbit132           # Branch on Bit Set Plus 32
    MIPS_cins = idaapi.MIPS_cins              # Clear and Insert a Bit Field
    MIPS_cins32 = idaapi.MIPS_cins32            # Clear and Insert a Bit Field Plus 32
    MIPS_dmul = idaapi.MIPS_dmul              # Multiply Doubleword to GPR
    MIPS_dpop = idaapi.MIPS_dpop              # Count Ones in a Doubleword
    MIPS_exts = idaapi.MIPS_exts              # Extract a Signed Bit Field
    MIPS_exts32 = idaapi.MIPS_exts32            # Extract a Signed Bit Field Plus 32
    MIPS_mtm0 = idaapi.MIPS_mtm0              # Load Multiplier Register MPL0
    MIPS_mtm1 = idaapi.MIPS_mtm1              # Load Multiplier Register MPL1
    MIPS_mtm2 = idaapi.MIPS_mtm2              # Load Multiplier Register MPL2
    MIPS_mtp0 = idaapi.MIPS_mtp0              # Load Multiplier Register P0
    MIPS_mtp1 = idaapi.MIPS_mtp1              # Load Multiplier Register P1
    MIPS_mtp2 = idaapi.MIPS_mtp2              # Load Multiplier Register P2
    MIPS_pop = idaapi.MIPS_pop               # Count Ones in a Word
    MIPS_saa = idaapi.MIPS_saa               # Store Atomic Add Word
    MIPS_saad = idaapi.MIPS_saad              # Store Atomic Add Double Word
    MIPS_seq = idaapi.MIPS_seq               # Set on Equal
    MIPS_seqi = idaapi.MIPS_seqi              # Set on Equal Immediate
    MIPS_sne = idaapi.MIPS_sne               # Set on Not Equal
    MIPS_snei = idaapi.MIPS_snei              # Set on Not Equal Immediate
    MIPS_synciobdma = idaapi.MIPS_synciobdma        # Synchronize IOBDMAs
    MIPS_syncs = idaapi.MIPS_syncs             # Synchronize Special
    MIPS_syncw = idaapi.MIPS_syncw             # Synchronize Stores
    MIPS_syncws = idaapi.MIPS_syncws            # Synchronize Stores Special
    MIPS_uld = idaapi.MIPS_uld               # Unaligned Load Doubleword
    MIPS_ulw = idaapi.MIPS_ulw               # Unaligned Load Word
    MIPS_usd = idaapi.MIPS_usd               # Unaligned Store Doubleword
    MIPS_usw = idaapi.MIPS_usw               # Unaligned Store Word
    MIPS_v3mulu = idaapi.MIPS_v3mulu            # 192-bit x 64-bit Unsigned Multiply and Add
    MIPS_vmm0 = idaapi.MIPS_vmm0              # 64-bit Unsigned Multiply and Add Move
    MIPS_vmulu_cn = idaapi.MIPS_vmulu_cn          # 64-bit Unsigned Multiply and Add

    # NEC VR5432 and PSP instructions

    MIPS_dbreak = idaapi.MIPS_dbreak            # Debug Break
    MIPS_dret = idaapi.MIPS_dret              # Debug Return
    MIPS_mfdr = idaapi.MIPS_mfdr              # Move from Debug Register
    MIPS_mtdr = idaapi.MIPS_mtdr              # Move to Debug Register

    # Allegrex (Sony PSP) instructions

    PSP_bitrev = idaapi.PSP_bitrev            # Bit reverse
    PSP_max = idaapi.PSP_max               # Maximum
    PSP_min = idaapi.PSP_min               # Minimum
    PSP_mfic = idaapi.PSP_mfic              # Move from interrupt controller
    PSP_mtic = idaapi.PSP_mtic              # Move to interrupt controller
    PSP_wsbw = idaapi.PSP_wsbw              # Word Swap Bytes Within Word
    PSP_sleep = idaapi.PSP_sleep             # Sleep

    # Allegrex VFPU instructions

    PSP_lv = idaapi.PSP_lv                # Load Vector
    PSP_lvl = idaapi.PSP_lvl               # Load Vector Left
    PSP_lvr = idaapi.PSP_lvr               # Load Vector Right
    PSP_sv = idaapi.PSP_sv                # Store Vector
    PSP_svl = idaapi.PSP_svl               # Store Vector Left
    PSP_svr = idaapi.PSP_svr               # Store Vector Right
    PSP_mfv = idaapi.PSP_mfv               # Move from VFPU
    PSP_mtv = idaapi.PSP_mtv               # Move to VFPU
    PSP_mfvc = idaapi.PSP_mfvc              # Move Control from VFPU
    PSP_mtvc = idaapi.PSP_mtvc              # Move Control to VFPU
    PSP_bvf = idaapi.PSP_bvf               # Branch on VFPU False
    PSP_bvt = idaapi.PSP_bvt               # Branch on VFPU True
    PSP_bvfl = idaapi.PSP_bvfl              # Branch on VFPU False Likely
    PSP_bvtl = idaapi.PSP_bvtl              # Branch on VFPU True Likely
    PSP_vnop = idaapi.PSP_vnop              # VFPU no-op
    PSP_vflush = idaapi.PSP_vflush            # VFPU flush
    PSP_vsync = idaapi.PSP_vsync             # VFPU sync
    PSP_vabs = idaapi.PSP_vabs              # Vector absolute value
    PSP_vadd = idaapi.PSP_vadd              # Vector add
    PSP_vasin = idaapi.PSP_vasin             # Vector arcsine
    PSP_vavg = idaapi.PSP_vavg              # Vector average
    PSP_vbfy1 = idaapi.PSP_vbfy1             # IDCT butterfly 1
    PSP_vbfy2 = idaapi.PSP_vbfy2             # IDCT butterfly 2
    PSP_vc2i = idaapi.PSP_vc2i              # Vector convert signed char to integer
    PSP_vcmovf = idaapi.PSP_vcmovf            # Vector move if condition field is true
    PSP_vcmovt = idaapi.PSP_vcmovt            # Vector move if condition field is false
    PSP_vcmp = idaapi.PSP_vcmp              # Vector compare and set condition fields
    PSP_vcos = idaapi.PSP_vcos              # Vector cosine
    PSP_vcrs = idaapi.PSP_vcrs              # Vector cross multiplication: vd = [y1*z2, z1*x2, x1*y2]
    PSP_vcrsp = idaapi.PSP_vcrsp             # Vector cross product
    PSP_vcst = idaapi.PSP_vcst              # Set constant
    PSP_vdet = idaapi.PSP_vdet              # Determinant
    PSP_vdiv = idaapi.PSP_vdiv              # Vector divide
    PSP_vdot = idaapi.PSP_vdot              # Vector dot product
    PSP_vexp2 = idaapi.PSP_vexp2             # Vector exponent of 2 (2^x)
    PSP_vf2h = idaapi.PSP_vf2h              # Vector convert float single to half precision
    PSP_vf2id = idaapi.PSP_vf2id             # Vector convert float to integer, round down
    PSP_vf2in = idaapi.PSP_vf2in             # Vector convert float to integer, round to nearest
    PSP_vf2iu = idaapi.PSP_vf2iu             # Vector convert float to integer, round up
    PSP_vf2iz = idaapi.PSP_vf2iz             # Vector convert float to integer, round toward zero
    PSP_vfad = idaapi.PSP_vfad              # Vector funnel add (sum components)
    PSP_vfim = idaapi.PSP_vfim              # Set floating-point immediate
    PSP_vh2f = idaapi.PSP_vh2f              # Vector convert float half to single precision
    PSP_vhdp = idaapi.PSP_vhdp              # Vector homogenous dot product
    PSP_vhtfm2 = idaapi.PSP_vhtfm2            # Homogenous transform vector by matrix
    PSP_vhtfm3 = idaapi.PSP_vhtfm3            # Homogenous transform vector by matrix
    PSP_vhtfm4 = idaapi.PSP_vhtfm4            # Homogenous transform vector by matrix
    PSP_vi2c = idaapi.PSP_vi2c              # Vector convert integer to signed char
    PSP_vi2f = idaapi.PSP_vi2f              # Vector convert integer to float
    PSP_vi2s = idaapi.PSP_vi2s              # Vector convert integer to signed short
    PSP_vi2uc = idaapi.PSP_vi2uc             # Vector convert integer to unsigned char
    PSP_vi2us = idaapi.PSP_vi2us             # Vector convert integer to unsigned short
    PSP_vidt = idaapi.PSP_vidt              # Set vector to identity
    PSP_viim = idaapi.PSP_viim              # Set integer immediate
    PSP_vlgb = idaapi.PSP_vlgb              # 
    PSP_vlog2 = idaapi.PSP_vlog2             # Vector logarithm base 2
    PSP_vmax = idaapi.PSP_vmax              # Vector maximum values
    PSP_vmfvc = idaapi.PSP_vmfvc             # Vector move from control register
    PSP_vmidt = idaapi.PSP_vmidt             # Set matrix to identity
    PSP_vmin = idaapi.PSP_vmin              # Vector minimum values
    PSP_vmmov = idaapi.PSP_vmmov             # Move matrix
    PSP_vmmul = idaapi.PSP_vmmul             # Matrix multiply
    PSP_vmone = idaapi.PSP_vmone             # Set matrix to ones
    PSP_vmov = idaapi.PSP_vmov              # Move vector
    PSP_vmscl = idaapi.PSP_vmscl             # Scale matrix by
    PSP_vmtvc = idaapi.PSP_vmtvc             # Vector move to control register
    PSP_vmul = idaapi.PSP_vmul              # Vector multiply
    PSP_vmzero = idaapi.PSP_vmzero            # Set matrix to zeroes
    PSP_vneg = idaapi.PSP_vneg              # Vector negate
    PSP_vnrcp = idaapi.PSP_vnrcp             # Vector negative reciprocal (-1/x)
    PSP_vnsin = idaapi.PSP_vnsin             # Vector negative sine
    PSP_vocp = idaapi.PSP_vocp              # Vector one complement (1-x)
    PSP_vone = idaapi.PSP_vone              # Set vector to ones
    PSP_vpfxd = idaapi.PSP_vpfxd             # Set prefix operation for vd
    PSP_vpfxs = idaapi.PSP_vpfxs             # Set prefix operation for vs
    PSP_vpfxt = idaapi.PSP_vpfxt             # Set prefix operation for vt
    PSP_vqmul = idaapi.PSP_vqmul             # Quaternion multiply
    PSP_vrcp = idaapi.PSP_vrcp              # Vector reciprocal (1/x)
    PSP_vrexp2 = idaapi.PSP_vrexp2            # Vector reciprocal exponent of 2 (1/(2^x))
    PSP_vrndf1 = idaapi.PSP_vrndf1            # Vector generate pseudorandom float (1.0 ~ 2.0)
    PSP_vrndf2 = idaapi.PSP_vrndf2            # Vector generate pseudorandom float (2.0 ~ 4.0)
    PSP_vrndi = idaapi.PSP_vrndi             # Vector generate pseudorandom integer
    PSP_vrnds = idaapi.PSP_vrnds             # Vector set pseudorandom seed
    PSP_vrot = idaapi.PSP_vrot              # Rotate vector
    PSP_vrsq = idaapi.PSP_vrsq              # Vector reciprocal square root (1/sqrt(x))
    PSP_vs2i = idaapi.PSP_vs2i              # Vector convert signed short to integer
    PSP_vsat0 = idaapi.PSP_vsat0             # Vector saturate to range 0..1
    PSP_vsat1 = idaapi.PSP_vsat1             # Vector saturate to range -1..1
    PSP_vsbn = idaapi.PSP_vsbn              # Vector scale by 2^x, round to nearest
    PSP_vsbz = idaapi.PSP_vsbz              # Vector scale by 2^x, round towards zero
    PSP_vscl = idaapi.PSP_vscl              # Vector scale by
    PSP_vscmp = idaapi.PSP_vscmp             # Vector set signed compare
    PSP_vsge = idaapi.PSP_vsge              # Vector set results for greater than or equal
    PSP_vsgn = idaapi.PSP_vsgn              # Vector get sign
    PSP_vsin = idaapi.PSP_vsin              # Vector sine
    PSP_vslt = idaapi.PSP_vslt              # Vector set results for less
    PSP_vsocp = idaapi.PSP_vsocp             # Vector split and one complement
    PSP_vsqrt = idaapi.PSP_vsqrt             # Vector square root
    PSP_vsrt1 = idaapi.PSP_vsrt1             # Vector sort 1: vd = min(x,y), max(x,y), min(z,w), max(z,w)
    PSP_vsrt2 = idaapi.PSP_vsrt2             # Vector sort 2: vd = min(x,w), max(y,z), min(y,z), max(x,w)
    PSP_vsrt3 = idaapi.PSP_vsrt3             # Vector sort 3: vd = max(x,y), min(x,y), max(z,w), min(z,w)
    PSP_vsrt4 = idaapi.PSP_vsrt4             # Vector sort 4: vd = max(x,w), max(y,z), min(y,z), max(x,w)
    PSP_vsub = idaapi.PSP_vsub              # Vector subtract
    PSP_vt4444 = idaapi.PSP_vt4444            # Transform color RGBA8888 to RGBA4444
    PSP_vt5551 = idaapi.PSP_vt5551            # Transform color RGBA8888 to RGBA5551
    PSP_vt5650 = idaapi.PSP_vt5650            # Transform color RGB888 to RGB565
    PSP_vtfm2 = idaapi.PSP_vtfm2             # Transform vector by matrix
    PSP_vtfm3 = idaapi.PSP_vtfm3             # Transform vector by matrix
    PSP_vtfm4 = idaapi.PSP_vtfm4             # Transform vector by matrix
    PSP_vuc2i = idaapi.PSP_vuc2i             # Vector convert unsigned char to integer
    PSP_vus2i = idaapi.PSP_vus2i             # Vector convert unsigned short to integer
    PSP_vwbn = idaapi.PSP_vwbn              # 
    PSP_vzero = idaapi.PSP_vzero             # VFPU set vector to zeroes

    # PSP Media Engine instructions
    PSP_mfvme = idaapi.PSP_mfvme  # move from VME
    PSP_mtvme = idaapi.PSP_mtvme  # move to VME

    # Toshiba TX19a instructions
    MIPS_ac0iu = idaapi.MIPS_ac0iu            # Add Coprocessor 0 Immediate Unsigned
    MIPS_bs1f = idaapi.MIPS_bs1f             # Bit Search One Forward
    MIPS_bfins = idaapi.MIPS_bfins            # Bit field insert
    MIPS_addmiu = idaapi.MIPS_addmiu           # Add Immediate to Memory Word
    MIPS_sadd = idaapi.MIPS_sadd             # Saturated Add
    MIPS_ssub = idaapi.MIPS_ssub             # Saturated Subtract
    MIPS_btst = idaapi.MIPS_btst             # Bit Test
    MIPS_bclr = idaapi.MIPS_bclr             # Bit Clear
    MIPS_bset = idaapi.MIPS_bset             # Bit Set
    MIPS_bins = idaapi.MIPS_bins             # Bit Insert
    MIPS_bext = idaapi.MIPS_bext             # Bit Extract
    MIPS_dive = idaapi.MIPS_dive             # Divide, with Overflow Exception
    MIPS_diveu = idaapi.MIPS_diveu            # Divide unsigned, with Overflow Exception
    MIPS_min = idaapi.MIPS_min              # Minimum signed
    MIPS_max = idaapi.MIPS_max              # Maximum signed

    MIPS_madd3 = idaapi.MIPS_madd3            # Multiply/Add (3-operand)
    MIPS_maddu3 = idaapi.MIPS_maddu3           # Multiply/Add Unsigned (3-operand)
    MIPS_msub3 = idaapi.MIPS_msub3            # Multiply and Subtract Word to Hi,Lo (3-operand)
    MIPS_msubu3 = idaapi.MIPS_msubu3           # Multiply and Subtract Word to Hi,Lo (3-operand)

    # MIPS-MT
    MIPS_dvpe = idaapi.MIPS_dvpe             # Disable Virtual Processor Execution
    MIPS_evpe = idaapi.MIPS_evpe             # Enable Virtual Processor Execution
    MIPS_dmt = idaapi.MIPS_dmt              # Disable Multi-Threaded Execution
    MIPS_emt = idaapi.MIPS_emt              # Enable Multi-Threaded Execution
    MIPS_fork = idaapi.MIPS_fork             # Allocate and Schedule a New Thread
    MIPS_yield = idaapi.MIPS_yield            # Conditionally Deschedule or Deallocate the Current Thread
    MIPS_mftr = idaapi.MIPS_mftr             # Move From Thread Context
    MIPS_mftc0 = idaapi.MIPS_mftc0
    MIPS_mftlo = idaapi.MIPS_mftlo
    MIPS_mfthi = idaapi.MIPS_mfthi
    MIPS_mftacx = idaapi.MIPS_mftacx
    MIPS_mftdsp = idaapi.MIPS_mftdsp
    MIPS_mfthc1 = idaapi.MIPS_mfthc1
    MIPS_mftc1 = idaapi.MIPS_mftc1
    MIPS_cftc1 = idaapi.MIPS_cftc1
    MIPS_mfthc2 = idaapi.MIPS_mfthc2
    MIPS_mftc2 = idaapi.MIPS_mftc2
    MIPS_cftc2 = idaapi.MIPS_cftc2
    MIPS_mftgpr = idaapi.MIPS_mftgpr
    MIPS_mttr = idaapi.MIPS_mttr             # Move To Thread Context
    MIPS_mttc0 = idaapi.MIPS_mttc0
    MIPS_mttlo = idaapi.MIPS_mttlo
    MIPS_mtthi = idaapi.MIPS_mtthi
    MIPS_mttacx = idaapi.MIPS_mttacx
    MIPS_mttdsp = idaapi.MIPS_mttdsp
    MIPS_mtthc1 = idaapi.MIPS_mtthc1
    MIPS_mttc1 = idaapi.MIPS_mttc1
    MIPS_cttc1 = idaapi.MIPS_cttc1
    MIPS_mtthc2 = idaapi.MIPS_mtthc2
    MIPS_mttc2 = idaapi.MIPS_mttc2
    MIPS_cttc2 = idaapi.MIPS_cttc2
    MIPS_mttgpr = idaapi.MIPS_mttgpr

    # MIPS-3D
    MIPS_faddr = idaapi.MIPS_faddr          # Floating-point Reduction Addition
    MIPS_bc1any2f = idaapi.MIPS_bc1any2f       # Branch on Any of Two Floating Point Condition Codes False
    MIPS_bc1any2t = idaapi.MIPS_bc1any2t       # Branch on Any of Two Floating Point Condition Codes True
    MIPS_bc1any4f = idaapi.MIPS_bc1any4f       # Branch on Any of Four Floating Point Condition Codes False
    MIPS_bc1any4t = idaapi.MIPS_bc1any4t       # Branch on Any of Four Floating Point Condition Codes True
    MIPS_fcabs_f = idaapi.MIPS_fcabs_f        # Floating-point Absolute Compare
    MIPS_fcabs_un = idaapi.MIPS_fcabs_un       # Floating-point Absolute Compare
    MIPS_fcabs_eq = idaapi.MIPS_fcabs_eq       # Floating-point Absolute Compare
    MIPS_fcabs_ueq = idaapi.MIPS_fcabs_ueq      # Floating-point Absolute Compare
    MIPS_fcabs_olt = idaapi.MIPS_fcabs_olt      # Floating-point Absolute Compare
    MIPS_fcabs_ult = idaapi.MIPS_fcabs_ult      # Floating-point Absolute Compare
    MIPS_fcabs_ole = idaapi.MIPS_fcabs_ole      # Floating-point Absolute Compare
    MIPS_fcabs_ule = idaapi.MIPS_fcabs_ule      # Floating-point Absolute Compare
    MIPS_fcabs_sf = idaapi.MIPS_fcabs_sf       # Floating-point Absolute Compare
    MIPS_fcabs_ngle = idaapi.MIPS_fcabs_ngle     # Floating-point Absolute Compare
    MIPS_fcabs_seq = idaapi.MIPS_fcabs_seq      # Floating-point Absolute Compare
    MIPS_fcabs_ngl = idaapi.MIPS_fcabs_ngl      # Floating-point Absolute Compare
    MIPS_fcabs_lt = idaapi.MIPS_fcabs_lt       # Floating-point Absolute Compare
    MIPS_fcabs_nge = idaapi.MIPS_fcabs_nge      # Floating-point Absolute Compare
    MIPS_fcabs_le = idaapi.MIPS_fcabs_le       # Floating-point Absolute Compare
    MIPS_fcabs_ngt = idaapi.MIPS_fcabs_ngt      # Floating-point Absolute Compare
    MIPS_fcvt_pw_ps = idaapi.MIPS_fcvt_pw_ps     # Floating-point Convert Paired Single to Paired Word
    MIPS_fcvt_ps_pw = idaapi.MIPS_fcvt_ps_pw     # Floating-point Convert Paired Word to Paired Single
    MIPS_fmulr = idaapi.MIPS_fmulr          # Floating-point Reduction Multiply
    MIPS_frecip1 = idaapi.MIPS_frecip1        # Floating-point Reduced Precision Reciprocal (Step 1)
    MIPS_frecip2 = idaapi.MIPS_frecip2        # Floating-point Reduced Precision Reciprocal (Step 2)
    MIPS_frsqrt1 = idaapi.MIPS_frsqrt1        # Floating-point Reduced Precision Reciprocal Square Root (Step 1)
    MIPS_frsqrt2 = idaapi.MIPS_frsqrt2        # Floating-point Reduced Precision Reciprocal Square Root (Step 2)

    # smartMIPS
    MIPS_lwxs = idaapi.MIPS_lwxs
    MIPS_maddp = idaapi.MIPS_maddp
    MIPS_mflhxu = idaapi.MIPS_mflhxu
    MIPS_mtlhx = idaapi.MIPS_mtlhx
    MIPS_multp = idaapi.MIPS_multp
    MIPS_pperm = idaapi.MIPS_pperm

    # microMIPS
    MIPS_jals = idaapi.MIPS_jals      # Jump and Link, Short Delay Slot
    MIPS_lwp = idaapi.MIPS_lwp       # Load Word Pair
    MIPS_ldp = idaapi.MIPS_ldp       # Load Doubleword Pair
    MIPS_lwm = idaapi.MIPS_lwm       # Load Word Multiple
    MIPS_ldm = idaapi.MIPS_ldm       # Load Doubleword Multiple
    MIPS_swp = idaapi.MIPS_swp       # Store Word Pair
    MIPS_sdp = idaapi.MIPS_sdp       # Store Doubleword Pair
    MIPS_swm = idaapi.MIPS_swm       # Store Word Multiple
    MIPS_sdm = idaapi.MIPS_sdm       # Store Doubleword Multiple
    MIPS_bnezc = idaapi.MIPS_bnezc     # Branch on Not Equal to Zero, Compact
    MIPS_bltzals = idaapi.MIPS_bltzals   # Branch on Less Than Zero and Link, Short Delay-Slot
    MIPS_beqzc = idaapi.MIPS_beqzc     # Branch on Equal to Zero, Compact
    MIPS_bgezals = idaapi.MIPS_bgezals   # Branch on Greater Than or Equal to Zero and Link, Short Delay-Slot
    MIPS_jraddiusp = idaapi.MIPS_jraddiusp, # Jump Register, Adjust Stack Pointer
    MIPS_jalrs = idaapi.MIPS_jalrs     # Jump and Link Register, Short Delay Slot
    MIPS_jalrs_hb = idaapi.MIPS_jalrs_hb  # Jump and Link Register with Hazard Barrier, Short Delay-Slot
    MIPS_movep = idaapi.MIPS_movep     # Move a Pair of Registers

    # had been missed; 64-bit MIPS pseudoinstruction
    MIPS_dli = idaapi.MIPS_dli       # Doubleword Load Immediate

    # DSP ASE instructions
    MIPS_insv = idaapi.MIPS_insv             # Insert Bit Field Variable
    MIPS_dinsv = idaapi.MIPS_dinsv            # Doubleword Insert Variable Bit Field
    MIPS_bposge32 = idaapi.MIPS_bposge32         # Branch on Greater Than or Equal To Value 32 in DSPControl Pos Field
    MIPS_bposge64 = idaapi.MIPS_bposge64         # Branch on Greater Than or Equal To Value 64 in DSPControl Pos Field
    MIPS_addu_qb = idaapi.MIPS_addu_qb          # Unsigned Add Quad Byte Vectors
    MIPS_addu_ph = idaapi.MIPS_addu_ph          # Unsigned Add Integer Halfwords
    MIPS_addsc = idaapi.MIPS_addsc            # Add Signed Word and Set Carry Bit
    MIPS_subu_qb = idaapi.MIPS_subu_qb          # Subtract Unsigned Quad Byte Vector
    MIPS_subu_ph = idaapi.MIPS_subu_ph          # Subtract Unsigned Integer Halfwords
    MIPS_addwc = idaapi.MIPS_addwc            # Add Word with Carry Bit
    MIPS_addq_ph = idaapi.MIPS_addq_ph          # Add Fractional Halfword Vectors
    MIPS_modsub = idaapi.MIPS_modsub           # Modular Subtraction on an Index Value
    MIPS_subq_ph = idaapi.MIPS_subq_ph          # Subtract Fractional Halfword Vector
    MIPS_addu_s_qb = idaapi.MIPS_addu_s_qb        # Unsigned Add Quad Byte Vectors
    MIPS_addu_s_ph = idaapi.MIPS_addu_s_ph        # Unsigned Add Integer Halfwords
    MIPS_raddu_w_qb = idaapi.MIPS_raddu_w_qb       # Unsigned Reduction Add Vector Quad Bytes
    MIPS_muleq_s_w_phl = idaapi.MIPS_muleq_s_w_phl    # Multiply Vector Fractional Left Halfwords to Expanded Width Products
    MIPS_subu_s_qb = idaapi.MIPS_subu_s_qb        # Subtract Unsigned Quad Byte Vector
    MIPS_subu_s_ph = idaapi.MIPS_subu_s_ph        # Subtract Unsigned Integer Halfwords
    MIPS_muleq_s_w_phr = idaapi.MIPS_muleq_s_w_phr    # Multiply Vector Fractional Right Halfwords to Expanded Width Products
    MIPS_muleu_s_ph_qbl = idaapi.MIPS_muleu_s_ph_qbl   # Multiply Unsigned Vector Left Bytes by Halfwords to Halfword Products
    MIPS_addq_s_ph = idaapi.MIPS_addq_s_ph        # Add Fractional Halfword Vectors
    MIPS_addq_s_w = idaapi.MIPS_addq_s_w         # Add Fractional Words
    MIPS_mulq_s_ph = idaapi.MIPS_mulq_s_ph        # Multiply Vector Fractional Half-Words to Same Size Products
    MIPS_muleu_s_ph_qbr = idaapi.MIPS_muleu_s_ph_qbr   # Multiply Unsigned Vector Right Bytes with halfwords to Half Word Products
    MIPS_subq_s_ph = idaapi.MIPS_subq_s_ph        # Subtract Fractional Halfword Vector
    MIPS_subq_s_w = idaapi.MIPS_subq_s_w         # Subtract Fractional Word
    MIPS_mulq_rs_ph = idaapi.MIPS_mulq_rs_ph       # Multiply Vector Fractional Halfwords to Fractional Halfword Products
    MIPS_addu_ob = idaapi.MIPS_addu_ob          # Unsigned Add Octal Byte Vectors
    MIPS_subu_ob = idaapi.MIPS_subu_ob          # Subtract Unsigned Octal Byte Vector
    MIPS_addq_qh = idaapi.MIPS_addq_qh          # Add Fractional Halfword Vectors
    MIPS_addq_pw = idaapi.MIPS_addq_pw          # Add Fractional Word Vectors
    MIPS_subq_qh = idaapi.MIPS_subq_qh          # Subtract Fractional Halfword Vector
    MIPS_subq_pw = idaapi.MIPS_subq_pw          # Subtract Fractional Word Vector
    MIPS_addu_s_ob = idaapi.MIPS_addu_s_ob        # Unsigned Add Octal Byte Vectors
    MIPS_raddu_l_ob = idaapi.MIPS_raddu_l_ob       # Unsigned Reduction Add Vector Octal Bytes
    MIPS_muleq_s_pw_qhl = idaapi.MIPS_muleq_s_pw_qhl   # Multiply Vector Fractional Left Halfwords to Expanded Width Products
    MIPS_subu_s_ob = idaapi.MIPS_subu_s_ob        # Subtract Unsigned Octal Byte Vector
    MIPS_muleq_s_pw_qhr = idaapi.MIPS_muleq_s_pw_qhr   # Multiply Vector Fractional Right Halfwords to Expanded Width Products
    MIPS_muleu_s_qh_obl = idaapi.MIPS_muleu_s_qh_obl   # Multiply Unsigned Vector Left Bytes by Halfwords to Halfword Products
    MIPS_addq_s_qh = idaapi.MIPS_addq_s_qh        # Add Fractional Halfword Vectors
    MIPS_addq_s_pw = idaapi.MIPS_addq_s_pw        # Add Fractional Word Vectors
    MIPS_muleu_s_qh_obr = idaapi.MIPS_muleu_s_qh_obr   # Multiply Unsigned Vector Right Bytes by Halfwords to Halfword Products
    MIPS_subq_s_qh = idaapi.MIPS_subq_s_qh        # Subtract Fractional Halfword Vector
    MIPS_subq_s_pw = idaapi.MIPS_subq_s_pw        # Subtract Fractional Word Vector
    MIPS_mulq_rs_qh = idaapi.MIPS_mulq_rs_qh       # Multiply Vector Fractional Halfwords to Fractional Halfword Products
    MIPS_cmpu_eq_qb = idaapi.MIPS_cmpu_eq_qb       # Compare Vectors of Unsigned Byte Values
    MIPS_cmp_eq_ph = idaapi.MIPS_cmp_eq_ph        # Compare Vectors of Signed Integer Halfword Values
    MIPS_cmpgdu_eq_qb = idaapi.MIPS_cmpgdu_eq_qb     # Compare Unsigned Vector of Four Bytes and Write Result to GPR and DSPControl
    MIPS_cmpu_lt_qb = idaapi.MIPS_cmpu_lt_qb       # Compare Vectors of Unsigned Byte Values
    MIPS_cmp_lt_ph = idaapi.MIPS_cmp_lt_ph        # Compare Vectors of Signed Integer Halfword Values
    MIPS_cmpgdu_lt_qb = idaapi.MIPS_cmpgdu_lt_qb     # Compare Unsigned Vector of Four Bytes and Write Result to GPR and DSPControl
    MIPS_cmpu_le_qb = idaapi.MIPS_cmpu_le_qb       # Compare Vectors of Unsigned Byte Values
    MIPS_cmp_le_ph = idaapi.MIPS_cmp_le_ph        # Compare Vectors of Signed Integer Halfword Values
    MIPS_cmpgdu_le_qb = idaapi.MIPS_cmpgdu_le_qb     # Compare Unsigned Vector of Four Bytes and Write Result to GPR and DSPControl
    MIPS_pick_qb = idaapi.MIPS_pick_qb          # Pick a Vector of Byte Values Based on Condition Code Bits
    MIPS_pick_ph = idaapi.MIPS_pick_ph          # Pick a Vector of Halfword Values Based on Condition Code Bits
    MIPS_cmpgu_eq_qb = idaapi.MIPS_cmpgu_eq_qb      # Compare Vectors of Unsigned Byte Values and Write Results to a GPR
    MIPS_precrq_qb_ph = idaapi.MIPS_precrq_qb_ph     # Precision Reduce Four Fractional Halfwords to Four Bytes
    MIPS_precrq_ph_w = idaapi.MIPS_precrq_ph_w      # Precision Reduce Fractional Words to Fractional Halfwords
    MIPS_cmpgu_lt_qb = idaapi.MIPS_cmpgu_lt_qb      # Compare Vectors of Unsigned Byte Values and Write Results to a GPR
    MIPS_precr_qb_ph = idaapi.MIPS_precr_qb_ph      # Precision Reduce Four Integer Halfwords to Four Bytes
    MIPS_precrq_rs_ph_w = idaapi.MIPS_precrq_rs_ph_w   # Precision Reduce Fractional Words to Halfwords With Rounding and Saturation
    MIPS_cmpgu_le_qb = idaapi.MIPS_cmpgu_le_qb      # Compare Vectors of Unsigned Byte Values and Write Results to a GPR
    MIPS_packrl_ph = idaapi.MIPS_packrl_ph        # Pack a Vector of Halfwords from Vector Halfword Sources
    MIPS_precr_sra_ph_w = idaapi.MIPS_precr_sra_ph_w   # Precision Reduce Two Integer Words to Halfwords after a Right Shift
    MIPS_precrqu_s_qb_ph = idaapi.MIPS_precrqu_s_qb_ph  # Precision Reduce Fractional Halfwords to Unsigned Bytes With Saturation
    MIPS_precr_sra_r_ph_w = idaapi.MIPS_precr_sra_r_ph_w, # Precision Reduce Two Integer Words to Halfwords after a Right Shif
    MIPS_cmpu_eq_ob = idaapi.MIPS_cmpu_eq_ob       # Compare Vectors of Unsigned Byte Values
    MIPS_cmp_eq_qh = idaapi.MIPS_cmp_eq_qh        # Compare Vectors of Signed Integer Halfword Values
    MIPS_cmp_eq_pw = idaapi.MIPS_cmp_eq_pw        # Compare Vectors of Signed Integer Word Values
    MIPS_cmpu_lt_ob = idaapi.MIPS_cmpu_lt_ob       # Compare Vectors of Unsigned Byte Values
    MIPS_cmp_lt_qh = idaapi.MIPS_cmp_lt_qh        # Compare Vectors of Signed Integer Halfword Values
    MIPS_cmp_lt_pw = idaapi.MIPS_cmp_lt_pw        # Compare Vectors of Signed Integer Word Values
    MIPS_cmpu_le_ob = idaapi.MIPS_cmpu_le_ob       # Compare Vectors of Unsigned Byte Values
    MIPS_cmp_le_qh = idaapi.MIPS_cmp_le_qh        # Compare Vectors of Signed Integer Halfword Values
    MIPS_cmp_le_pw = idaapi.MIPS_cmp_le_pw        # Compare Vectors of Signed Integer Word Values
    MIPS_pick_ob = idaapi.MIPS_pick_ob          # Pick a Vector of Byte Values Based on Condition Code Bits
    MIPS_pick_qh = idaapi.MIPS_pick_qh          # Pick a Vector of Halfword Values Based on Condition Code Bits
    MIPS_pick_pw = idaapi.MIPS_pick_pw          # Pick a Vector of Word Values Based on Condition Code Bits
    MIPS_cmpgu_eq_ob = idaapi.MIPS_cmpgu_eq_ob      # Compare Vectors of Unsigned Byte Values and Write Results to a GPR
    MIPS_precrq_ob_qh = idaapi.MIPS_precrq_ob_qh     # Precision Reduce Fractional Halfwords to Fractional Bytes
    MIPS_precrq_qh_pw = idaapi.MIPS_precrq_qh_pw     # Precision Reduce Fractional Words to Fractional Halfwords
    MIPS_precrq_pw_l = idaapi.MIPS_precrq_pw_l      # Precision Reduce Fractional Doublewords to Fractional Words
    MIPS_cmpgu_lt_ob = idaapi.MIPS_cmpgu_lt_ob      # Compare Vectors of Unsigned Byte Values and Write Results to a GPR
    MIPS_precrq_rs_qh_pw = idaapi.MIPS_precrq_rs_qh_pw  # Precision Reduce Fractional Words to Halfwords With Rounding and Saturation
    MIPS_cmpgu_le_ob = idaapi.MIPS_cmpgu_le_ob      # Compare Vectors of Unsigned Byte Values and Write Results to a GPR
    MIPS_packrl_pw = idaapi.MIPS_packrl_pw        # Pack a Vector of Words from Vector Word Sources
    MIPS_precrqu_s_ob_qh = idaapi.MIPS_precrqu_s_ob_qh  # Precision Reduce Fractional Halfwords to Unsigned Bytes With Saturation
    MIPS_absq_s_qb = idaapi.MIPS_absq_s_qb        # Find Absolute Value of Four Fractional Byte Values
    MIPS_absq_s_ph = idaapi.MIPS_absq_s_ph        # Find Absolute Value of Two Fractional Halfwords
    MIPS_absq_s_w = idaapi.MIPS_absq_s_w         # Find Absolute Value of Fractional Word
    MIPS_repl_qb = idaapi.MIPS_repl_qb          # Replicate Immediate Integer into all Vector Element Positions
    MIPS_repl_ph = idaapi.MIPS_repl_ph          # Replicate Immediate Integer into all Vector Element Positions
    MIPS_replv_qb = idaapi.MIPS_replv_qb         # Replicate Byte into all Vector Element Positions
    MIPS_replv_ph = idaapi.MIPS_replv_ph         # Replicate a Halfword into all Vector Element Positions
    MIPS_bitrev = idaapi.MIPS_bitrev           # Bit-Reverse Halfword
    MIPS_precequ_ph_qbl = idaapi.MIPS_precequ_ph_qbl   # Precision Expand two Unsigned Bytes to Fractional Halfword Values
    MIPS_preceq_w_phl = idaapi.MIPS_preceq_w_phl     # Precision Expand Fractional Halfword to Fractional Word Value
    MIPS_preceu_ph_qbl = idaapi.MIPS_preceu_ph_qbl    # Precision Expand Two Unsigned Bytes to Unsigned Halfword Values
    MIPS_precequ_ph_qbr = idaapi.MIPS_precequ_ph_qbr   # Precision Expand two Unsigned Bytes to Fractional Halfword Values
    MIPS_preceq_w_phr = idaapi.MIPS_preceq_w_phr     # Precision Expand Fractional Halfword to Fractional Word Value
    MIPS_preceu_ph_qbr = idaapi.MIPS_preceu_ph_qbr    # Precision Expand two Unsigned Bytes to Unsigned Halfword Values
    MIPS_precequ_ph_qbla = idaapi.MIPS_precequ_ph_qbla  # Precision Expand two Unsigned Bytes to Fractional Halfword Values
    MIPS_preceu_ph_qbla = idaapi.MIPS_preceu_ph_qbla   # Precision Expand Two Unsigned Bytes to Unsigned Halfword Values
    MIPS_precequ_ph_qbra = idaapi.MIPS_precequ_ph_qbra  # Precision Expand two Unsigned Bytes to Fractional Halfword Values
    MIPS_preceu_ph_qbra = idaapi.MIPS_preceu_ph_qbra   # Precision Expand Two Unsigned Bytes to Unsigned Halfword Values
    MIPS_absq_s_qh = idaapi.MIPS_absq_s_qh        # Find Absolute Value of Four Fractional Halfwords
    MIPS_absq_s_pw = idaapi.MIPS_absq_s_pw        # Find Absolute Value of Two Fractional Words
    MIPS_repl_ob = idaapi.MIPS_repl_ob          # Replicate Immediate Integer into all Vector Element Positions
    MIPS_repl_qh = idaapi.MIPS_repl_qh          # Replicate Immediate Integer into all Vector Element Positions
    MIPS_repl_pw = idaapi.MIPS_repl_pw          # Replicate Immediate Integer into all Vector Element Positions
    MIPS_replv_ob = idaapi.MIPS_replv_ob         # Replicate Byte into all Vector Element Positions
    MIPS_replv_qh = idaapi.MIPS_replv_qh         # Replicate a Halfword into all Vector Element Positions
    MIPS_replv_pw = idaapi.MIPS_replv_pw         # Replicate Word into all Vector Element Positions
    MIPS_precequ_pw_qhl = idaapi.MIPS_precequ_pw_qhl   # Precision Expand two Unsigned Bytes to Fractional Halfword Values
    MIPS_preceq_pw_qhl = idaapi.MIPS_preceq_pw_qhl    # Precision Expand Two Fractional Halfwords to Fractional Word Values
    MIPS_preceq_s_l_pwl = idaapi.MIPS_preceq_s_l_pwl   # Precision Expand Fractional Word to Fractional Doubleword Value
    MIPS_preceu_qh_obl = idaapi.MIPS_preceu_qh_obl    # Precision Expand Four Unsigned Bytes to Unsigned Halfword Values
    MIPS_precequ_pw_qhr = idaapi.MIPS_precequ_pw_qhr   # Precision Expand two Unsigned Bytes to Fractional Halfword Values
    MIPS_preceq_pw_qhr = idaapi.MIPS_preceq_pw_qhr    # Precision Expand Two Fractional Halfwords to Fractional Word Values
    MIPS_preceq_s_l_pwr = idaapi.MIPS_preceq_s_l_pwr   # Precision Expand Fractional Word to Fractional Doubleword Value
    MIPS_preceu_qh_obr = idaapi.MIPS_preceu_qh_obr    # Precision Expand Four Unsigned Bytes to Unsigned Halfword Values
    MIPS_precequ_pw_qhla = idaapi.MIPS_precequ_pw_qhla  # Precision Expand two Unsigned Bytes to Fractional Halfword Values
    MIPS_preceq_pw_qhla = idaapi.MIPS_preceq_pw_qhla   # Precision Expand Two Fractional Halfwords to Fractional Word Values
    MIPS_preceu_qh_obla = idaapi.MIPS_preceu_qh_obla   # Precision Expand Four Unsigned Bytes to Unsigned Halfword Values
    MIPS_precequ_pw_qhra = idaapi.MIPS_precequ_pw_qhra  # Precision Expand two Unsigned Bytes to Fractional Halfword Values
    MIPS_preceq_pw_qhra = idaapi.MIPS_preceq_pw_qhra   # Precision Expand Two Fractional Halfwords to Fractional Word Values
    MIPS_preceu_qh_obra = idaapi.MIPS_preceu_qh_obra   # Precision Expand Four Unsigned Bytes to Unsigned Halfword Values
    MIPS_shll_qb = idaapi.MIPS_shll_qb          # Shift Left Logical Vector Quad Bytes
    MIPS_shll_ph = idaapi.MIPS_shll_ph          # Shift Left Logical Vector Pair Halfwords
    MIPS_shrl_qb = idaapi.MIPS_shrl_qb          # Shift Right Logical Vector Quad Bytes
    MIPS_shra_ph = idaapi.MIPS_shra_ph          # Shift Right Arithmetic Vector Pair Halfwords
    MIPS_shrl_ph = idaapi.MIPS_shrl_ph          # Shift Right Logical Two Halfwords
    MIPS_shllv_qb = idaapi.MIPS_shllv_qb         # Shift Left Logical Variable Vector Quad Bytes
    MIPS_shllv_ph = idaapi.MIPS_shllv_ph         # Shift Left Logical Variable Vector Pair Halfwords
    MIPS_shrlv_qb = idaapi.MIPS_shrlv_qb         # Shift Right Logical Variable Vector Quad Bytes
    MIPS_shrav_ph = idaapi.MIPS_shrav_ph         # Shift Right Arithmetic Variable Vector Pair Halfwords
    MIPS_shrlv_ph = idaapi.MIPS_shrlv_ph         # Shift Variable Right Logical Pair of Halfwords
    MIPS_shra_qb = idaapi.MIPS_shra_qb          # Shift Right Arithmetic Vector of Four Bytes
    MIPS_shll_s_ph = idaapi.MIPS_shll_s_ph        # Shift Left Logical Vector Pair Halfwords
    MIPS_shll_s_w = idaapi.MIPS_shll_s_w         # Shift Left Logical Word with Saturation
    MIPS_shra_r_qb = idaapi.MIPS_shra_r_qb        # Shift Right Arithmetic Vector of Four Bytes
    MIPS_shra_r_ph = idaapi.MIPS_shra_r_ph        # Shift Right Arithmetic Vector Pair Halfwords
    MIPS_shra_r_w = idaapi.MIPS_shra_r_w         # Shift Right Arithmetic Word with Rounding
    MIPS_shrav_qb = idaapi.MIPS_shrav_qb         # Shift Right Arithmetic Variable Vector of Four Bytes
    MIPS_shllv_s_ph = idaapi.MIPS_shllv_s_ph       # Shift Left Logical Variable Vector Pair Halfwords
    MIPS_shllv_s_w = idaapi.MIPS_shllv_s_w        # Shift Left Logical Variable Vector Word
    MIPS_shrav_r_qb = idaapi.MIPS_shrav_r_qb       # Shift Right Arithmetic Variable Vector of Four Bytes
    MIPS_shrav_r_ph = idaapi.MIPS_shrav_r_ph       # Shift Right Arithmetic Variable Vector Pair Halfwords
    MIPS_shrav_r_w = idaapi.MIPS_shrav_r_w        # Shift Right Arithmetic Variable Word with Rounding
    MIPS_shll_ob = idaapi.MIPS_shll_ob          # Shift Left Logical Vector Octal Bytes
    MIPS_shll_qh = idaapi.MIPS_shll_qh          # Shift Left Logical Vector Quad Halfwords
    MIPS_shll_pw = idaapi.MIPS_shll_pw          # Shift Left Logical Vector Pair Words
    MIPS_shrl_ob = idaapi.MIPS_shrl_ob          # Shift Right Logical Vector Octal Bytes
    MIPS_shra_qh = idaapi.MIPS_shra_qh          # Shift Right Arithmetic Vector Quad Halfwords
    MIPS_shra_pw = idaapi.MIPS_shra_pw          # Shift Right Arithmetic Vector Pair Words
    MIPS_shllv_ob = idaapi.MIPS_shllv_ob         # Shift Left Logical Variable Vector Octal Bytes
    MIPS_shllv_qh = idaapi.MIPS_shllv_qh         # Shift Left Logical Variable Vector Quad Halfwords
    MIPS_shllv_pw = idaapi.MIPS_shllv_pw         # Shift Left Logical Variable Vector Pair Words
    MIPS_shrlv_ob = idaapi.MIPS_shrlv_ob         # Shift Right Logical Variable Vector Octal Bytes
    MIPS_shrav_qh = idaapi.MIPS_shrav_qh         # Shift Right Arithmetic Variable Vector Quad Halfwords
    MIPS_shrav_pw = idaapi.MIPS_shrav_pw         # Shift Right Arithmetic Variable Vector Pair Words
    MIPS_shll_s_qh = idaapi.MIPS_shll_s_qh        # Shift Left Logical Vector Quad Halfwords
    MIPS_shll_s_pw = idaapi.MIPS_shll_s_pw        # Shift Left Logical Vector Pair Words
    MIPS_shra_r_qh = idaapi.MIPS_shra_r_qh        # Shift Right Arithmetic Vector Quad Halfwords
    MIPS_shra_r_pw = idaapi.MIPS_shra_r_pw        # Shift Right Arithmetic Vector Pair Words
    MIPS_shllv_s_qh = idaapi.MIPS_shllv_s_qh       # Shift Left Logical Variable Vector Quad Halfwords
    MIPS_shllv_s_pw = idaapi.MIPS_shllv_s_pw       # Shift Left Logical Variable Vector Pair Words
    MIPS_shrav_r_qh = idaapi.MIPS_shrav_r_qh       # Shift Right Arithmetic Variable Vector Quad Halfwords
    MIPS_shrav_r_pw = idaapi.MIPS_shrav_r_pw       # Shift Right Arithmetic Variable Vector Pair Words
    MIPS_lwx = idaapi.MIPS_lwx              # Load Word Indexed
    MIPS_ldx = idaapi.MIPS_ldx              # Load Doubleword Indexed
    MIPS_lhx = idaapi.MIPS_lhx              # Load Halfword Indexed
    MIPS_lbux = idaapi.MIPS_lbux             # Load Unsigned Byte Indexed
    MIPS_dpa_w_ph = idaapi.MIPS_dpa_w_ph         # Dot Product with Accumulate on Vector Integer Halfword Elements
    MIPS_dpax_w_ph = idaapi.MIPS_dpax_w_ph        # Cross Dot Product with Accumulate on Vector Integer Halfword Elements
    MIPS_maq_sa_w_phl = idaapi.MIPS_maq_sa_w_phl     # Multiply with Accumulate Single Vector Fractional Halfword Element
    MIPS_dpaqx_s_w_ph = idaapi.MIPS_dpaqx_s_w_ph     # Cross Dot Product with Accumulation on Fractional Halfword Elements
    MIPS_dps_w_ph = idaapi.MIPS_dps_w_ph         # Dot Product with Subtract on Vector Integer Half-Word Elements
    MIPS_dpsx_w_ph = idaapi.MIPS_dpsx_w_ph        # Cross Dot Product with Subtract on Vector Integer Halfword Elements
    MIPS_dpsqx_s_w_ph = idaapi.MIPS_dpsqx_s_w_ph     # Cross Dot Product with Subtraction on Fractional Halfword Elements
    MIPS_mulsa_w_ph = idaapi.MIPS_mulsa_w_ph       # Multiply and Subtract Vector Integer Halfword Elements and Accumulate
    MIPS_maq_sa_w_phr = idaapi.MIPS_maq_sa_w_phr     # Multiply with Accumulate Single Vector Fractional Halfword Element
    MIPS_dpaqx_sa_w_ph = idaapi.MIPS_dpaqx_sa_w_ph    # Cross Dot Product with Accumulation on Fractional Halfword Elements
    MIPS_dpau_h_qbl = idaapi.MIPS_dpau_h_qbl       # Dot Product with Accumulate on Vector Unsigned Byte Elements
    MIPS_dpsu_h_qbl = idaapi.MIPS_dpsu_h_qbl       # Dot Product with Subtraction on Vector Unsigned Byte Elements
    MIPS_dpsqx_sa_w_ph = idaapi.MIPS_dpsqx_sa_w_ph    # Cross Dot Product with Subtraction on Fractional Halfword Elements
    MIPS_dpaq_s_w_ph = idaapi.MIPS_dpaq_s_w_ph      # Dot Product with Accumulation on Fractional Halfword Elements
    MIPS_dpaq_sa_l_w = idaapi.MIPS_dpaq_sa_l_w      # Dot Product with Accumulate on Fractional Word Element
    MIPS_maq_s_w_phl = idaapi.MIPS_maq_s_w_phl      # Multiply with Accumulate Single Vector Fractional Halfword Element
    MIPS_dpsq_s_w_ph = idaapi.MIPS_dpsq_s_w_ph      # Dot Product with Subtraction on Fractional Halfword Elements
    MIPS_dpsq_sa_l_w = idaapi.MIPS_dpsq_sa_l_w      # Dot Product with Subtraction on Fractional Word Element
    MIPS_mulsaq_s_w_ph = idaapi.MIPS_mulsaq_s_w_ph    # Multiply And Subtract Vector Fractional Halfwords And Accumulate
    MIPS_maq_s_w_phr = idaapi.MIPS_maq_s_w_phr      # Multiply with Accumulate Single Vector Fractional Halfword Element
    MIPS_dpau_h_qbr = idaapi.MIPS_dpau_h_qbr       # Dot Product with Accumulate on Vector Unsigned Byte Elements
    MIPS_dpsu_h_qbr = idaapi.MIPS_dpsu_h_qbr       # Dot Product with Subtraction on Vector Unsigned Byte Elements
    MIPS_maq_sa_w_qhll = idaapi.MIPS_maq_sa_w_qhll    # Multiply with Accumulate Single Vector Fractional Halfword Element
    MIPS_maq_sa_w_qhlr = idaapi.MIPS_maq_sa_w_qhlr    # Multiply with Accumulate Single Vector Fractional Halfword Element
    MIPS_dmadd = idaapi.MIPS_dmadd            # Multiply Vector Words And Accumulate
    MIPS_dmsub = idaapi.MIPS_dmsub            # Multiply Vector Words And Subtract From Accumulator
    MIPS_maq_sa_w_qhrl = idaapi.MIPS_maq_sa_w_qhrl    # Multiply with Accumulate Single Vector Fractional Halfword Element
    MIPS_dpau_h_obl = idaapi.MIPS_dpau_h_obl       # Dot Product with Accumulate on Vector Unsigned Byte Elements
    MIPS_dpsu_h_obl = idaapi.MIPS_dpsu_h_obl       # Dot Product with Subtract on Vector Unsigned Byte Elements
    MIPS_maq_sa_w_qhrr = idaapi.MIPS_maq_sa_w_qhrr    # Multiply with Accumulate Single Vector Fractional Halfword Element
    MIPS_dpaq_s_w_qh = idaapi.MIPS_dpaq_s_w_qh      # Dot Product with Accumulation on Fractional Halfword Elements
    MIPS_dpaq_sa_l_pw = idaapi.MIPS_dpaq_sa_l_pw     # Dot Product with Accumulate on Fractional Word Elements
    MIPS_maq_s_w_qhll = idaapi.MIPS_maq_s_w_qhll     # Multiply with Accumulate Single Vector Fractional Halfword Element
    MIPS_maq_s_l_pwl = idaapi.MIPS_maq_s_l_pwl      # Multiply with Accumulate Single Vector Fractional Word Element
    MIPS_dpsq_s_w_qh = idaapi.MIPS_dpsq_s_w_qh      # Dot Product with Subtraction on Fractional Halfword Elements
    MIPS_dpsq_sa_l_pw = idaapi.MIPS_dpsq_sa_l_pw     # Dot Product with Subtraction on Fractional Word Elements
    MIPS_maq_s_w_qhlr = idaapi.MIPS_maq_s_w_qhlr     # Multiply with Accumulate Single Vector Fractional Halfword Element
    MIPS_dmaddu = idaapi.MIPS_dmaddu           # Multiply Vector Unsigned Words And Accumulate
    MIPS_mulsaq_s_w_qh = idaapi.MIPS_mulsaq_s_w_qh    # Multiply And Subtract Vector Fractional Halfwords And Accumulate
    MIPS_mulsaq_s_l_pw = idaapi.MIPS_mulsaq_s_l_pw    # Multiply And Subtract Vector Fractional Words And Accumulate
    MIPS_maq_s_w_qhrl = idaapi.MIPS_maq_s_w_qhrl     # Multiply with Accumulate Single Vector Fractional Halfword Element
    MIPS_maq_s_l_pwr = idaapi.MIPS_maq_s_l_pwr      # Multiply with Accumulate Single Vector Fractional Word Element
    MIPS_dpau_h_obr = idaapi.MIPS_dpau_h_obr       # Dot Product with Accumulate on Vector Unsigned Byte Elements
    MIPS_dpsu_h_obr = idaapi.MIPS_dpsu_h_obr       # Dot Product with Subtract on Vector Unsigned Byte Elements
    MIPS_maq_s_w_qhrr = idaapi.MIPS_maq_s_w_qhrr     # Multiply with Accumulate Single Vector Fractional Halfword Element
    MIPS_dmsubu = idaapi.MIPS_dmsubu           # Multiply Vector Unsigned Words And Subtract From Accumulator
    MIPS_extr_w = idaapi.MIPS_extr_w           # Extract Word Value With Right Shift From Accumulator to GPR
    MIPS_extrv_w = idaapi.MIPS_extrv_w          # Extract Word Value With Variable Right Shift From Accumulator to GPR
    MIPS_extp = idaapi.MIPS_extp             # Extract Fixed Bitfield From Arbitrary Position in Accumulator to GPR
    MIPS_extpdp = idaapi.MIPS_extpdp           # Extract Fixed Bitfield From Arbitrary Position in Accumulator to GPR and Decrement Pos
    MIPS_rddsp = idaapi.MIPS_rddsp            # Read DSPControl Register Fields to a GPR
    MIPS_shilo = idaapi.MIPS_shilo            # Shift an Accumulator Value Leaving the Result in the Same Accumulator
    MIPS_extpv = idaapi.MIPS_extpv            # Extract Variable Bitfield From Arbitrary Position in Accumulator to GPR
    MIPS_extpdpv = idaapi.MIPS_extpdpv          # Extract Variable Bitfield From Arbitrary Position in Accumulator to GPR and Decrement Pos
    MIPS_wrdsp = idaapi.MIPS_wrdsp            # Write Fields to DSPControl Register from a GPR
    MIPS_shilov = idaapi.MIPS_shilov           # Variable Shift of Accumulator Value Leaving the Result in the Same Accumulator
    MIPS_extr_r_w = idaapi.MIPS_extr_r_w         # Extract Word Value With Right Shift And Rounding From Accumulator to GPR
    MIPS_extrv_r_w = idaapi.MIPS_extrv_r_w        # Extract Word Value With Variable Right Shift And Rounding From Accumulator to GPR
    MIPS_extr_rs_w = idaapi.MIPS_extr_rs_w        # Extract Word Value With Right Shift From Accumulator to GPR
    MIPS_extr_s_h = idaapi.MIPS_extr_s_h         # Extract Halfword Value From Accumulator to GPR With Right Shift and Saturate
    MIPS_extrv_rs_w = idaapi.MIPS_extrv_rs_w       # Extract Word Value With Variable Right Shift From Accumulator to GPR
    MIPS_extrv_s_h = idaapi.MIPS_extrv_s_h        # Extract Halfword Value Variable From Accumulator to GPR With Right Shift and Saturate
    MIPS_mthlip = idaapi.MIPS_mthlip           # Copy LO to HI and a GPR to LO and Increment Pos by 32
    MIPS_dextr_w = idaapi.MIPS_dextr_w          # Extract Word Value With Right Shift From Accumulator to GPR
    MIPS_dextr_l = idaapi.MIPS_dextr_l          # Extract Doubleword Value With Right Shift From Accumulator to GPR
    MIPS_dextrv_w = idaapi.MIPS_dextrv_w         # Extract Word Value With Variable Right Shift From Accumulator to GPR
    MIPS_dextrv_l = idaapi.MIPS_dextrv_l         # Extract Doubleword Value With Variable Right Shift From Accumulator to GPR
    MIPS_dextp = idaapi.MIPS_dextp            # Extract Fixed Bitfield From Arbitrary Position in Accumulator to GPR
    MIPS_dextpdp = idaapi.MIPS_dextpdp          # Extract Fixed Bitfield From Arbitrary Position in Accumulator to GPR and Decrement Pos
    MIPS_dshilo = idaapi.MIPS_dshilo           # Shift an Accumulator Value Leaving the Result in the Same Accumulator
    MIPS_dextpv = idaapi.MIPS_dextpv           # Extract Variable Bitfield From Arbitrary Position in Accumulator to GPR
    MIPS_dextpdpv = idaapi.MIPS_dextpdpv         # Extract Variable Bitfield From Arbitrary Position in Accumulator to GPR and Decrement Pos
    MIPS_dshilov = idaapi.MIPS_dshilov          # Variable Shift of Accumulator Value Leaving the Result in the Same Accumulator
    MIPS_dextr_r_w = idaapi.MIPS_dextr_r_w        # Extract Word Value With Right Shift And Rounding From Accumulator to GPR
    MIPS_dextr_r_l = idaapi.MIPS_dextr_r_l        # Extract Doubleword Value With Right Shift And Rounding From Accumulator to GPR
    MIPS_dextrv_r_w = idaapi.MIPS_dextrv_r_w       # Extract Word Value With Variable Right Shift And Rounding From Accumulator to GPR
    MIPS_dextrv_r_l = idaapi.MIPS_dextrv_r_l       # Extract Doubleword Value With Variable Right Shift And Rounding From Accumulator to GPR
    MIPS_dextr_rs_w = idaapi.MIPS_dextr_rs_w       # Extract Word Value With Right Shift From Accumulator to GPR
    MIPS_dextr_s_h = idaapi.MIPS_dextr_s_h        # Extract Halfword Value From Accumulator to GPR With Right Shift and Saturate
    MIPS_dextr_rs_l = idaapi.MIPS_dextr_rs_l       # Extract Doubleword Value With Right Shift From Accumulator to GPR
    MIPS_dextrv_rs_w = idaapi.MIPS_dextrv_rs_w      # Extract Word Value With Variable Right Shift From Accumulator to GPR
    MIPS_dextrv_s_h = idaapi.MIPS_dextrv_s_h       # Extract Halfword Value Variable From Accumulator to GPR With Right Shift and Saturate
    MIPS_dextrv_rs_l = idaapi.MIPS_dextrv_rs_l      # Extract Doubleword Value With Variable Right Shift From Accumulator to GPR
    MIPS_dmthlip = idaapi.MIPS_dmthlip          # Copy LO to HI and a GPR to LO and Increment Pos by 64
    MIPS_adduh_qb = idaapi.MIPS_adduh_qb         # Unsigned Add Vector Quad-Bytes And Right Shift to Halve Results
    MIPS_addqh_ph = idaapi.MIPS_addqh_ph         # Add Fractional Halfword Vectors And Shift Right to Halve Results
    MIPS_addqh_w = idaapi.MIPS_addqh_w          # Add Fractional Words And Shift Right to Halve Results
    MIPS_subuh_qb = idaapi.MIPS_subuh_qb         # Subtract Unsigned Bytes And Right Shift to Halve Results
    MIPS_subqh_ph = idaapi.MIPS_subqh_ph         # Subtract Fractional Halfword Vectors And Shift Right to Halve Results
    MIPS_subqh_w = idaapi.MIPS_subqh_w          # Subtract Fractional Words And Shift Right to Halve Results
    MIPS_adduh_r_qb = idaapi.MIPS_adduh_r_qb       # Unsigned Add Vector Quad-Bytes And Right Shift to Halve Results
    MIPS_addqh_r_ph = idaapi.MIPS_addqh_r_ph       # Add Fractional Halfword Vectors And Shift Right to Halve Results
    MIPS_addqh_r_w = idaapi.MIPS_addqh_r_w        # Add Fractional Words And Shift Right to Halve Results
    MIPS_subuh_r_qb = idaapi.MIPS_subuh_r_qb       # Subtract Unsigned Bytes And Right Shift to Halve Results
    MIPS_subqh_r_ph = idaapi.MIPS_subqh_r_ph       # Subtract Fractional Halfword Vectors And Shift Right to Halve Results
    MIPS_subqh_r_w = idaapi.MIPS_subqh_r_w        # Subtract Fractional Words And Shift Right to Halve Results
    MIPS_mul_ph = idaapi.MIPS_mul_ph           # Multiply Vector Integer HalfWords to Same Size Products
    MIPS_mul_s_ph = idaapi.MIPS_mul_s_ph         # Multiply Vector Integer HalfWords to Same Size Products
    MIPS_mulq_s_w = idaapi.MIPS_mulq_s_w         # Multiply Fractional Words to Same Size Product with Saturation
    MIPS_mulq_rs_w = idaapi.MIPS_mulq_rs_w        # Multiply Fractional Words to Same Size Product with Saturation and Rounding
    MIPS_append = idaapi.MIPS_append           # Left Shift and Append Bits to the LSB
    MIPS_balign = idaapi.MIPS_balign           # Byte Align Contents from Two Registers
    MIPS_prepend = idaapi.MIPS_prepend          # Right Shift and Prepend Bits to the MSB

    # Cavium Octeon II instructions
    MIPS_laa = idaapi.MIPS_laa      # Load Atomic Add Word
    MIPS_laad = idaapi.MIPS_laad     # Load Atomic Add Doubleword
    MIPS_lac = idaapi.MIPS_lac      # Load Atomic Clear Word
    MIPS_lacd = idaapi.MIPS_lacd     # Load Atomic Clear Doubleword
    MIPS_lad = idaapi.MIPS_lad      # Load Atomic Decrement Word
    MIPS_ladd = idaapi.MIPS_ladd     # Load Atomic Decrement Doubleword
    MIPS_lai = idaapi.MIPS_lai      # Load Atomic Increment Word
    MIPS_laid = idaapi.MIPS_laid     # Load Atomic Increment Doubleword
    MIPS_las = idaapi.MIPS_las      # Load Atomic Set Word
    MIPS_lasd = idaapi.MIPS_lasd     # Load Atomic Set Doubleword
    MIPS_law = idaapi.MIPS_law      # Load Atomic Swap Word
    MIPS_lawd = idaapi.MIPS_lawd     # Load Atomic Swap Doubleword
    # we don't know the following mnemonics for sure
    MIPS_lbx = idaapi.MIPS_lbx      # Load Byte Indexed
    MIPS_lhux = idaapi.MIPS_lhux     # Load Halfword Unsigned Indexed
    MIPS_lwux = idaapi.MIPS_lwux     # Load Word Unsigned Indexed
    MIPS_qmac_00 = idaapi.MIPS_qmac_00  # Q15 Multiply Accumulate
    MIPS_qmac_01 = idaapi.MIPS_qmac_01  # Q15 Multiply Accumulate
    MIPS_qmac_02 = idaapi.MIPS_qmac_02  # Q15 Multiply Accumulate
    MIPS_qmac_03 = idaapi.MIPS_qmac_03  # Q15 Multiply Accumulate
    MIPS_qmacs_00 = idaapi.MIPS_qmacs_00, # Q15 Multiply Accumulat
    MIPS_qmacs_01 = idaapi.MIPS_qmacs_01, # Q15 Multiply Accumulat
    MIPS_qmacs_02 = idaapi.MIPS_qmacs_02, # Q15 Multiply Accumulat
    MIPS_qmacs_03 = idaapi.MIPS_qmacs_03, # Q15 Multiply Accumulat
    MIPS_zcb = idaapi.MIPS_zcb      # Zero Cache Block
    MIPS_zcbt = idaapi.MIPS_zcbt     # Zero Cache Block

    # MSA ASE
    # some of these have the same name as existing mnemonics; to avoid ambiguity
    # we use an msa_ prefix on all of them
    MIPS_msa_sll_b = idaapi.MIPS_msa_sll_b      # Vector Shift Left
    MIPS_msa_sll_h = idaapi.MIPS_msa_sll_h      # Vector Shift Left
    MIPS_msa_sll_w = idaapi.MIPS_msa_sll_w      # Vector Shift Left
    MIPS_msa_sll_d = idaapi.MIPS_msa_sll_d      # Vector Shift Left
    MIPS_msa_slli_b = idaapi.MIPS_msa_slli_b     # Immediate Shift Left
    MIPS_msa_slli_h = idaapi.MIPS_msa_slli_h     # Immediate Shift Left
    MIPS_msa_slli_w = idaapi.MIPS_msa_slli_w     # Immediate Shift Left
    MIPS_msa_slli_d = idaapi.MIPS_msa_slli_d     # Immediate Shift Left
    MIPS_msa_sra_b = idaapi.MIPS_msa_sra_b      # Vector Shift Right Arithmetic
    MIPS_msa_sra_h = idaapi.MIPS_msa_sra_h      # Vector Shift Right Arithmetic
    MIPS_msa_sra_w = idaapi.MIPS_msa_sra_w      # Vector Shift Right Arithmetic
    MIPS_msa_sra_d = idaapi.MIPS_msa_sra_d      # Vector Shift Right Arithmetic
    MIPS_msa_srai_b = idaapi.MIPS_msa_srai_b     # Immediate Shift Right Arithmetic
    MIPS_msa_srai_h = idaapi.MIPS_msa_srai_h     # Immediate Shift Right Arithmetic
    MIPS_msa_srai_w = idaapi.MIPS_msa_srai_w     # Immediate Shift Right Arithmetic
    MIPS_msa_srai_d = idaapi.MIPS_msa_srai_d     # Immediate Shift Right Arithmetic
    MIPS_msa_srl_b = idaapi.MIPS_msa_srl_b      # Vector Shift Right Logical
    MIPS_msa_srl_h = idaapi.MIPS_msa_srl_h      # Vector Shift Right Logical
    MIPS_msa_srl_w = idaapi.MIPS_msa_srl_w      # Vector Shift Right Logical
    MIPS_msa_srl_d = idaapi.MIPS_msa_srl_d      # Vector Shift Right Logical
    MIPS_msa_srli_b = idaapi.MIPS_msa_srli_b     # Immediate Shift Right Logical
    MIPS_msa_srli_h = idaapi.MIPS_msa_srli_h     # Immediate Shift Right Logical
    MIPS_msa_srli_w = idaapi.MIPS_msa_srli_w     # Immediate Shift Right Logical
    MIPS_msa_srli_d = idaapi.MIPS_msa_srli_d     # Immediate Shift Right Logical
    MIPS_msa_bclr_b = idaapi.MIPS_msa_bclr_b     # Vector Bit Clear
    MIPS_msa_bclr_h = idaapi.MIPS_msa_bclr_h     # Vector Bit Clear
    MIPS_msa_bclr_w = idaapi.MIPS_msa_bclr_w     # Vector Bit Clear
    MIPS_msa_bclr_d = idaapi.MIPS_msa_bclr_d     # Vector Bit Clear
    MIPS_msa_bclri_b = idaapi.MIPS_msa_bclri_b    # Immediate Bit Clear
    MIPS_msa_bclri_h = idaapi.MIPS_msa_bclri_h    # Immediate Bit Clear
    MIPS_msa_bclri_w = idaapi.MIPS_msa_bclri_w    # Immediate Bit Clear
    MIPS_msa_bclri_d = idaapi.MIPS_msa_bclri_d    # Immediate Bit Clear
    MIPS_msa_bset_b = idaapi.MIPS_msa_bset_b     # Vector Bit Set
    MIPS_msa_bset_h = idaapi.MIPS_msa_bset_h     # Vector Bit Set
    MIPS_msa_bset_w = idaapi.MIPS_msa_bset_w     # Vector Bit Set
    MIPS_msa_bset_d = idaapi.MIPS_msa_bset_d     # Vector Bit Set
    MIPS_msa_bseti_b = idaapi.MIPS_msa_bseti_b    # Immediate Bit Set
    MIPS_msa_bseti_h = idaapi.MIPS_msa_bseti_h    # Immediate Bit Set
    MIPS_msa_bseti_w = idaapi.MIPS_msa_bseti_w    # Immediate Bit Set
    MIPS_msa_bseti_d = idaapi.MIPS_msa_bseti_d    # Immediate Bit Set
    MIPS_msa_bneg_b = idaapi.MIPS_msa_bneg_b     # Vector Bit Negate
    MIPS_msa_bneg_h = idaapi.MIPS_msa_bneg_h     # Vector Bit Negate
    MIPS_msa_bneg_w = idaapi.MIPS_msa_bneg_w     # Vector Bit Negate
    MIPS_msa_bneg_d = idaapi.MIPS_msa_bneg_d     # Vector Bit Negate
    MIPS_msa_bnegi_b = idaapi.MIPS_msa_bnegi_b    # Immediate Bit Negate
    MIPS_msa_bnegi_h = idaapi.MIPS_msa_bnegi_h    # Immediate Bit Negate
    MIPS_msa_bnegi_w = idaapi.MIPS_msa_bnegi_w    # Immediate Bit Negate
    MIPS_msa_bnegi_d = idaapi.MIPS_msa_bnegi_d    # Immediate Bit Negate
    MIPS_msa_binsl_b = idaapi.MIPS_msa_binsl_b    # Vector Bit Insert Left
    MIPS_msa_binsl_h = idaapi.MIPS_msa_binsl_h    # Vector Bit Insert Left
    MIPS_msa_binsl_w = idaapi.MIPS_msa_binsl_w    # Vector Bit Insert Left
    MIPS_msa_binsl_d = idaapi.MIPS_msa_binsl_d    # Vector Bit Insert Left
    MIPS_msa_binsli_b = idaapi.MIPS_msa_binsli_b   # Immediate Bit Insert Left
    MIPS_msa_binsli_h = idaapi.MIPS_msa_binsli_h   # Immediate Bit Insert Left
    MIPS_msa_binsli_w = idaapi.MIPS_msa_binsli_w   # Immediate Bit Insert Left
    MIPS_msa_binsli_d = idaapi.MIPS_msa_binsli_d   # Immediate Bit Insert Left
    MIPS_msa_binsr_b = idaapi.MIPS_msa_binsr_b    # Vector Bit Insert Right
    MIPS_msa_binsr_h = idaapi.MIPS_msa_binsr_h    # Vector Bit Insert Right
    MIPS_msa_binsr_w = idaapi.MIPS_msa_binsr_w    # Vector Bit Insert Right
    MIPS_msa_binsr_d = idaapi.MIPS_msa_binsr_d    # Vector Bit Insert Right
    MIPS_msa_binsri_b = idaapi.MIPS_msa_binsri_b   # Immediate Bit Insert Right
    MIPS_msa_binsri_h = idaapi.MIPS_msa_binsri_h   # Immediate Bit Insert Right
    MIPS_msa_binsri_w = idaapi.MIPS_msa_binsri_w   # Immediate Bit Insert Right
    MIPS_msa_binsri_d = idaapi.MIPS_msa_binsri_d   # Immediate Bit Insert Right
    MIPS_msa_addv_b = idaapi.MIPS_msa_addv_b     # Vector Add
    MIPS_msa_addv_h = idaapi.MIPS_msa_addv_h     # Vector Add
    MIPS_msa_addv_w = idaapi.MIPS_msa_addv_w     # Vector Add
    MIPS_msa_addv_d = idaapi.MIPS_msa_addv_d     # Vector Add
    MIPS_msa_addvi_b = idaapi.MIPS_msa_addvi_b    # Immediate Add
    MIPS_msa_addvi_h = idaapi.MIPS_msa_addvi_h    # Immediate Add
    MIPS_msa_addvi_w = idaapi.MIPS_msa_addvi_w    # Immediate Add
    MIPS_msa_addvi_d = idaapi.MIPS_msa_addvi_d    # Immediate Add
    MIPS_msa_subv_b = idaapi.MIPS_msa_subv_b     # Vector Subtract
    MIPS_msa_subv_h = idaapi.MIPS_msa_subv_h     # Vector Subtract
    MIPS_msa_subv_w = idaapi.MIPS_msa_subv_w     # Vector Subtract
    MIPS_msa_subv_d = idaapi.MIPS_msa_subv_d     # Vector Subtract
    MIPS_msa_subvi_b = idaapi.MIPS_msa_subvi_b    # Immediate Subtract
    MIPS_msa_subvi_h = idaapi.MIPS_msa_subvi_h    # Immediate Subtract
    MIPS_msa_subvi_w = idaapi.MIPS_msa_subvi_w    # Immediate Subtract
    MIPS_msa_subvi_d = idaapi.MIPS_msa_subvi_d    # Immediate Subtract
    MIPS_msa_max_s_b = idaapi.MIPS_msa_max_s_b    # Vector Signed Maximum
    MIPS_msa_max_s_h = idaapi.MIPS_msa_max_s_h    # Vector Signed Maximum
    MIPS_msa_max_s_w = idaapi.MIPS_msa_max_s_w    # Vector Signed Maximum
    MIPS_msa_max_s_d = idaapi.MIPS_msa_max_s_d    # Vector Signed Maximum
    MIPS_msa_maxi_s_b = idaapi.MIPS_msa_maxi_s_b   # Immediate Signed Maximum
    MIPS_msa_maxi_s_h = idaapi.MIPS_msa_maxi_s_h   # Immediate Signed Maximum
    MIPS_msa_maxi_s_w = idaapi.MIPS_msa_maxi_s_w   # Immediate Signed Maximum
    MIPS_msa_maxi_s_d = idaapi.MIPS_msa_maxi_s_d   # Immediate Signed Maximum
    MIPS_msa_max_u_b = idaapi.MIPS_msa_max_u_b    # Vector Unsigned Maximum
    MIPS_msa_max_u_h = idaapi.MIPS_msa_max_u_h    # Vector Unsigned Maximum
    MIPS_msa_max_u_w = idaapi.MIPS_msa_max_u_w    # Vector Unsigned Maximum
    MIPS_msa_max_u_d = idaapi.MIPS_msa_max_u_d    # Vector Unsigned Maximum
    MIPS_msa_maxi_u_b = idaapi.MIPS_msa_maxi_u_b   # Immediate Unsigned Maximum
    MIPS_msa_maxi_u_h = idaapi.MIPS_msa_maxi_u_h   # Immediate Unsigned Maximum
    MIPS_msa_maxi_u_w = idaapi.MIPS_msa_maxi_u_w   # Immediate Unsigned Maximum
    MIPS_msa_maxi_u_d = idaapi.MIPS_msa_maxi_u_d   # Immediate Unsigned Maximum
    MIPS_msa_min_s_b = idaapi.MIPS_msa_min_s_b    # Vector Signed Minimum
    MIPS_msa_min_s_h = idaapi.MIPS_msa_min_s_h    # Vector Signed Minimum
    MIPS_msa_min_s_w = idaapi.MIPS_msa_min_s_w    # Vector Signed Minimum
    MIPS_msa_min_s_d = idaapi.MIPS_msa_min_s_d    # Vector Signed Minimum
    MIPS_msa_mini_s_b = idaapi.MIPS_msa_mini_s_b   # Immediate Signed Minimum
    MIPS_msa_mini_s_h = idaapi.MIPS_msa_mini_s_h   # Immediate Signed Minimum
    MIPS_msa_mini_s_w = idaapi.MIPS_msa_mini_s_w   # Immediate Signed Minimum
    MIPS_msa_mini_s_d = idaapi.MIPS_msa_mini_s_d   # Immediate Signed Minimum
    MIPS_msa_min_u_b = idaapi.MIPS_msa_min_u_b    # Vector Unsigned Minimum
    MIPS_msa_min_u_h = idaapi.MIPS_msa_min_u_h    # Vector Unsigned Minimum
    MIPS_msa_min_u_w = idaapi.MIPS_msa_min_u_w    # Vector Unsigned Minimum
    MIPS_msa_min_u_d = idaapi.MIPS_msa_min_u_d    # Vector Unsigned Minimum
    MIPS_msa_mini_u_b = idaapi.MIPS_msa_mini_u_b   # Immediate Unsigned Minimum
    MIPS_msa_mini_u_h = idaapi.MIPS_msa_mini_u_h   # Immediate Unsigned Minimum
    MIPS_msa_mini_u_w = idaapi.MIPS_msa_mini_u_w   # Immediate Unsigned Minimum
    MIPS_msa_mini_u_d = idaapi.MIPS_msa_mini_u_d   # Immediate Unsigned Minimum
    MIPS_msa_max_a_b = idaapi.MIPS_msa_max_a_b    # Vector Maximum Based on Absolute Values
    MIPS_msa_max_a_h = idaapi.MIPS_msa_max_a_h    # Vector Maximum Based on Absolute Values
    MIPS_msa_max_a_w = idaapi.MIPS_msa_max_a_w    # Vector Maximum Based on Absolute Values
    MIPS_msa_max_a_d = idaapi.MIPS_msa_max_a_d    # Vector Maximum Based on Absolute Values
    MIPS_msa_min_a_b = idaapi.MIPS_msa_min_a_b    # Vector Minimum Based on Absolute Value
    MIPS_msa_min_a_h = idaapi.MIPS_msa_min_a_h    # Vector Minimum Based on Absolute Value
    MIPS_msa_min_a_w = idaapi.MIPS_msa_min_a_w    # Vector Minimum Based on Absolute Value
    MIPS_msa_min_a_d = idaapi.MIPS_msa_min_a_d    # Vector Minimum Based on Absolute Value
    MIPS_msa_ceq_b = idaapi.MIPS_msa_ceq_b      # Vector Compare Equal
    MIPS_msa_ceq_h = idaapi.MIPS_msa_ceq_h      # Vector Compare Equal
    MIPS_msa_ceq_w = idaapi.MIPS_msa_ceq_w      # Vector Compare Equal
    MIPS_msa_ceq_d = idaapi.MIPS_msa_ceq_d      # Vector Compare Equal
    MIPS_msa_ceqi_b = idaapi.MIPS_msa_ceqi_b     # Immediate Compare Equal
    MIPS_msa_ceqi_h = idaapi.MIPS_msa_ceqi_h     # Immediate Compare Equal
    MIPS_msa_ceqi_w = idaapi.MIPS_msa_ceqi_w     # Immediate Compare Equal
    MIPS_msa_ceqi_d = idaapi.MIPS_msa_ceqi_d     # Immediate Compare Equal
    MIPS_msa_clt_s_b = idaapi.MIPS_msa_clt_s_b    # Vector Compare Signed Less Than
    MIPS_msa_clt_s_h = idaapi.MIPS_msa_clt_s_h    # Vector Compare Signed Less Than
    MIPS_msa_clt_s_w = idaapi.MIPS_msa_clt_s_w    # Vector Compare Signed Less Than
    MIPS_msa_clt_s_d = idaapi.MIPS_msa_clt_s_d    # Vector Compare Signed Less Than
    MIPS_msa_clti_s_b = idaapi.MIPS_msa_clti_s_b   # Immediate Compare Signed Less Than
    MIPS_msa_clti_s_h = idaapi.MIPS_msa_clti_s_h   # Immediate Compare Signed Less Than
    MIPS_msa_clti_s_w = idaapi.MIPS_msa_clti_s_w   # Immediate Compare Signed Less Than
    MIPS_msa_clti_s_d = idaapi.MIPS_msa_clti_s_d   # Immediate Compare Signed Less Than
    MIPS_msa_clt_u_b = idaapi.MIPS_msa_clt_u_b    # Vector Compare Unsigned Less Than
    MIPS_msa_clt_u_h = idaapi.MIPS_msa_clt_u_h    # Vector Compare Unsigned Less Than
    MIPS_msa_clt_u_w = idaapi.MIPS_msa_clt_u_w    # Vector Compare Unsigned Less Than
    MIPS_msa_clt_u_d = idaapi.MIPS_msa_clt_u_d    # Vector Compare Unsigned Less Than
    MIPS_msa_clti_u_b = idaapi.MIPS_msa_clti_u_b   # Immediate Compare Unsigned Less Than
    MIPS_msa_clti_u_h = idaapi.MIPS_msa_clti_u_h   # Immediate Compare Unsigned Less Than
    MIPS_msa_clti_u_w = idaapi.MIPS_msa_clti_u_w   # Immediate Compare Unsigned Less Than
    MIPS_msa_clti_u_d = idaapi.MIPS_msa_clti_u_d   # Immediate Compare Unsigned Less Than
    MIPS_msa_cle_s_b = idaapi.MIPS_msa_cle_s_b    # Vector Compare Signed Less Than or Equal
    MIPS_msa_cle_s_h = idaapi.MIPS_msa_cle_s_h    # Vector Compare Signed Less Than or Equal
    MIPS_msa_cle_s_w = idaapi.MIPS_msa_cle_s_w    # Vector Compare Signed Less Than or Equal
    MIPS_msa_cle_s_d = idaapi.MIPS_msa_cle_s_d    # Vector Compare Signed Less Than or Equal
    MIPS_msa_clei_s_b = idaapi.MIPS_msa_clei_s_b   # Immediate Compare Signed Less Than or Equal
    MIPS_msa_clei_s_h = idaapi.MIPS_msa_clei_s_h   # Immediate Compare Signed Less Than or Equal
    MIPS_msa_clei_s_w = idaapi.MIPS_msa_clei_s_w   # Immediate Compare Signed Less Than or Equal
    MIPS_msa_clei_s_d = idaapi.MIPS_msa_clei_s_d   # Immediate Compare Signed Less Than or Equal
    MIPS_msa_cle_u_b = idaapi.MIPS_msa_cle_u_b    # Vector Compare Unsigned Less Than or Equal
    MIPS_msa_cle_u_h = idaapi.MIPS_msa_cle_u_h    # Vector Compare Unsigned Less Than or Equal
    MIPS_msa_cle_u_w = idaapi.MIPS_msa_cle_u_w    # Vector Compare Unsigned Less Than or Equal
    MIPS_msa_cle_u_d = idaapi.MIPS_msa_cle_u_d    # Vector Compare Unsigned Less Than or Equal
    MIPS_msa_clei_u_b = idaapi.MIPS_msa_clei_u_b   # Immediate Compare Unsigned Less Than or Equal
    MIPS_msa_clei_u_h = idaapi.MIPS_msa_clei_u_h   # Immediate Compare Unsigned Less Than or Equal
    MIPS_msa_clei_u_w = idaapi.MIPS_msa_clei_u_w   # Immediate Compare Unsigned Less Than or Equal
    MIPS_msa_clei_u_d = idaapi.MIPS_msa_clei_u_d   # Immediate Compare Unsigned Less Than or Equal
    MIPS_msa_ld_b = idaapi.MIPS_msa_ld_b       # Vector Load
    MIPS_msa_ld_h = idaapi.MIPS_msa_ld_h       # Vector Load
    MIPS_msa_ld_w = idaapi.MIPS_msa_ld_w       # Vector Load
    MIPS_msa_ld_d = idaapi.MIPS_msa_ld_d       # Vector Load
    MIPS_msa_st_b = idaapi.MIPS_msa_st_b       # Vector Store
    MIPS_msa_st_h = idaapi.MIPS_msa_st_h       # Vector Store
    MIPS_msa_st_w = idaapi.MIPS_msa_st_w       # Vector Store
    MIPS_msa_st_d = idaapi.MIPS_msa_st_d       # Vector Store
    MIPS_msa_sat_s_b = idaapi.MIPS_msa_sat_s_b    # Immediate Signed Saturate
    MIPS_msa_sat_s_h = idaapi.MIPS_msa_sat_s_h    # Immediate Signed Saturate
    MIPS_msa_sat_s_w = idaapi.MIPS_msa_sat_s_w    # Immediate Signed Saturate
    MIPS_msa_sat_s_d = idaapi.MIPS_msa_sat_s_d    # Immediate Signed Saturate
    MIPS_msa_sat_u_b = idaapi.MIPS_msa_sat_u_b    # Immediate Unsigned Saturate
    MIPS_msa_sat_u_h = idaapi.MIPS_msa_sat_u_h    # Immediate Unsigned Saturate
    MIPS_msa_sat_u_w = idaapi.MIPS_msa_sat_u_w    # Immediate Unsigned Saturate
    MIPS_msa_sat_u_d = idaapi.MIPS_msa_sat_u_d    # Immediate Unsigned Saturate
    MIPS_msa_add_a_b = idaapi.MIPS_msa_add_a_b    # Vector Add Absolute Values
    MIPS_msa_add_a_h = idaapi.MIPS_msa_add_a_h    # Vector Add Absolute Values
    MIPS_msa_add_a_w = idaapi.MIPS_msa_add_a_w    # Vector Add Absolute Values
    MIPS_msa_add_a_d = idaapi.MIPS_msa_add_a_d    # Vector Add Absolute Values
    MIPS_msa_adds_a_b = idaapi.MIPS_msa_adds_a_b   # Vector Saturated Add of Absolute Values
    MIPS_msa_adds_a_h = idaapi.MIPS_msa_adds_a_h   # Vector Saturated Add of Absolute Values
    MIPS_msa_adds_a_w = idaapi.MIPS_msa_adds_a_w   # Vector Saturated Add of Absolute Values
    MIPS_msa_adds_a_d = idaapi.MIPS_msa_adds_a_d   # Vector Saturated Add of Absolute Values
    MIPS_msa_adds_s_b = idaapi.MIPS_msa_adds_s_b   # Vector Signed Saturated Add of Signed Values
    MIPS_msa_adds_s_h = idaapi.MIPS_msa_adds_s_h   # Vector Signed Saturated Add of Signed Values
    MIPS_msa_adds_s_w = idaapi.MIPS_msa_adds_s_w   # Vector Signed Saturated Add of Signed Values
    MIPS_msa_adds_s_d = idaapi.MIPS_msa_adds_s_d   # Vector Signed Saturated Add of Signed Values
    MIPS_msa_adds_u_b = idaapi.MIPS_msa_adds_u_b   # Vector Unsigned Saturated Add of Unsigned Values
    MIPS_msa_adds_u_h = idaapi.MIPS_msa_adds_u_h   # Vector Unsigned Saturated Add of Unsigned Values
    MIPS_msa_adds_u_w = idaapi.MIPS_msa_adds_u_w   # Vector Unsigned Saturated Add of Unsigned Values
    MIPS_msa_adds_u_d = idaapi.MIPS_msa_adds_u_d   # Vector Unsigned Saturated Add of Unsigned Values
    MIPS_msa_ave_s_b = idaapi.MIPS_msa_ave_s_b    # Vector Signed Average
    MIPS_msa_ave_s_h = idaapi.MIPS_msa_ave_s_h    # Vector Signed Average
    MIPS_msa_ave_s_w = idaapi.MIPS_msa_ave_s_w    # Vector Signed Average
    MIPS_msa_ave_s_d = idaapi.MIPS_msa_ave_s_d    # Vector Signed Average
    MIPS_msa_ave_u_b = idaapi.MIPS_msa_ave_u_b    # Vector Unsigned Average
    MIPS_msa_ave_u_h = idaapi.MIPS_msa_ave_u_h    # Vector Unsigned Average
    MIPS_msa_ave_u_w = idaapi.MIPS_msa_ave_u_w    # Vector Unsigned Average
    MIPS_msa_ave_u_d = idaapi.MIPS_msa_ave_u_d    # Vector Unsigned Average
    MIPS_msa_aver_s_b = idaapi.MIPS_msa_aver_s_b   # Vector Signed Average Rounded
    MIPS_msa_aver_s_h = idaapi.MIPS_msa_aver_s_h   # Vector Signed Average Rounded
    MIPS_msa_aver_s_w = idaapi.MIPS_msa_aver_s_w   # Vector Signed Average Rounded
    MIPS_msa_aver_s_d = idaapi.MIPS_msa_aver_s_d   # Vector Signed Average Rounded
    MIPS_msa_aver_u_b = idaapi.MIPS_msa_aver_u_b   # Vector Unsigned Average Rounded
    MIPS_msa_aver_u_h = idaapi.MIPS_msa_aver_u_h   # Vector Unsigned Average Rounded
    MIPS_msa_aver_u_w = idaapi.MIPS_msa_aver_u_w   # Vector Unsigned Average Rounded
    MIPS_msa_aver_u_d = idaapi.MIPS_msa_aver_u_d   # Vector Unsigned Average Rounded
    MIPS_msa_subs_s_b = idaapi.MIPS_msa_subs_s_b   # Vector Signed Saturated Subtract of Signed Values
    MIPS_msa_subs_s_h = idaapi.MIPS_msa_subs_s_h   # Vector Signed Saturated Subtract of Signed Values
    MIPS_msa_subs_s_w = idaapi.MIPS_msa_subs_s_w   # Vector Signed Saturated Subtract of Signed Values
    MIPS_msa_subs_s_d = idaapi.MIPS_msa_subs_s_d   # Vector Signed Saturated Subtract of Signed Values
    MIPS_msa_subs_u_b = idaapi.MIPS_msa_subs_u_b   # Vector Unsigned Saturated Subtract of Unsigned Values
    MIPS_msa_subs_u_h = idaapi.MIPS_msa_subs_u_h   # Vector Unsigned Saturated Subtract of Unsigned Values
    MIPS_msa_subs_u_w = idaapi.MIPS_msa_subs_u_w   # Vector Unsigned Saturated Subtract of Unsigned Values
    MIPS_msa_subs_u_d = idaapi.MIPS_msa_subs_u_d   # Vector Unsigned Saturated Subtract of Unsigned Values
    MIPS_msa_subsus_u_b = idaapi.MIPS_msa_subsus_u_b # Vector Unsigned Saturated Subtract of Signed from Unsigned
    MIPS_msa_subsus_u_h = idaapi.MIPS_msa_subsus_u_h # Vector Unsigned Saturated Subtract of Signed from Unsigned
    MIPS_msa_subsus_u_w = idaapi.MIPS_msa_subsus_u_w # Vector Unsigned Saturated Subtract of Signed from Unsigned
    MIPS_msa_subsus_u_d = idaapi.MIPS_msa_subsus_u_d # Vector Unsigned Saturated Subtract of Signed from Unsigned
    MIPS_msa_subsuu_s_b = idaapi.MIPS_msa_subsuu_s_b # Vector Signed Saturated Subtract of Unsigned Values
    MIPS_msa_subsuu_s_h = idaapi.MIPS_msa_subsuu_s_h # Vector Signed Saturated Subtract of Unsigned Values
    MIPS_msa_subsuu_s_w = idaapi.MIPS_msa_subsuu_s_w # Vector Signed Saturated Subtract of Unsigned Values
    MIPS_msa_subsuu_s_d = idaapi.MIPS_msa_subsuu_s_d # Vector Signed Saturated Subtract of Unsigned Values
    MIPS_msa_asub_s_b = idaapi.MIPS_msa_asub_s_b   # Vector Absolute Values of Signed Subtract
    MIPS_msa_asub_s_h = idaapi.MIPS_msa_asub_s_h   # Vector Absolute Values of Signed Subtract
    MIPS_msa_asub_s_w = idaapi.MIPS_msa_asub_s_w   # Vector Absolute Values of Signed Subtract
    MIPS_msa_asub_s_d = idaapi.MIPS_msa_asub_s_d   # Vector Absolute Values of Signed Subtract
    MIPS_msa_asub_u_b = idaapi.MIPS_msa_asub_u_b   # Vector Absolute Values of Unsigned Subtract
    MIPS_msa_asub_u_h = idaapi.MIPS_msa_asub_u_h   # Vector Absolute Values of Unsigned Subtract
    MIPS_msa_asub_u_w = idaapi.MIPS_msa_asub_u_w   # Vector Absolute Values of Unsigned Subtract
    MIPS_msa_asub_u_d = idaapi.MIPS_msa_asub_u_d   # Vector Absolute Values of Unsigned Subtract
    MIPS_msa_mulv_b = idaapi.MIPS_msa_mulv_b     # Vector Multiply
    MIPS_msa_mulv_h = idaapi.MIPS_msa_mulv_h     # Vector Multiply
    MIPS_msa_mulv_w = idaapi.MIPS_msa_mulv_w     # Vector Multiply
    MIPS_msa_mulv_d = idaapi.MIPS_msa_mulv_d     # Vector Multiply
    MIPS_msa_maddv_b = idaapi.MIPS_msa_maddv_b    # Vector Multiply and Add
    MIPS_msa_maddv_h = idaapi.MIPS_msa_maddv_h    # Vector Multiply and Add
    MIPS_msa_maddv_w = idaapi.MIPS_msa_maddv_w    # Vector Multiply and Add
    MIPS_msa_maddv_d = idaapi.MIPS_msa_maddv_d    # Vector Multiply and Add
    MIPS_msa_msubv_b = idaapi.MIPS_msa_msubv_b    # Vector Multiply and Subtract
    MIPS_msa_msubv_h = idaapi.MIPS_msa_msubv_h    # Vector Multiply and Subtract
    MIPS_msa_msubv_w = idaapi.MIPS_msa_msubv_w    # Vector Multiply and Subtract
    MIPS_msa_msubv_d = idaapi.MIPS_msa_msubv_d    # Vector Multiply and Subtract
    MIPS_msa_div_s_b = idaapi.MIPS_msa_div_s_b    # Vector Signed Divide
    MIPS_msa_div_s_h = idaapi.MIPS_msa_div_s_h    # Vector Signed Divide
    MIPS_msa_div_s_w = idaapi.MIPS_msa_div_s_w    # Vector Signed Divide
    MIPS_msa_div_s_d = idaapi.MIPS_msa_div_s_d    # Vector Signed Divide
    MIPS_msa_div_u_b = idaapi.MIPS_msa_div_u_b    # Vector Unsigned Divide
    MIPS_msa_div_u_h = idaapi.MIPS_msa_div_u_h    # Vector Unsigned Divide
    MIPS_msa_div_u_w = idaapi.MIPS_msa_div_u_w    # Vector Unsigned Divide
    MIPS_msa_div_u_d = idaapi.MIPS_msa_div_u_d    # Vector Unsigned Divide
    MIPS_msa_mod_s_b = idaapi.MIPS_msa_mod_s_b    # Vector Signed Modulo
    MIPS_msa_mod_s_h = idaapi.MIPS_msa_mod_s_h    # Vector Signed Modulo
    MIPS_msa_mod_s_w = idaapi.MIPS_msa_mod_s_w    # Vector Signed Modulo
    MIPS_msa_mod_s_d = idaapi.MIPS_msa_mod_s_d    # Vector Signed Modulo
    MIPS_msa_mod_u_b = idaapi.MIPS_msa_mod_u_b    # Vector Unsigned Modulo
    MIPS_msa_mod_u_h = idaapi.MIPS_msa_mod_u_h    # Vector Unsigned Modulo
    MIPS_msa_mod_u_w = idaapi.MIPS_msa_mod_u_w    # Vector Unsigned Modulo
    MIPS_msa_mod_u_d = idaapi.MIPS_msa_mod_u_d    # Vector Unsigned Modulo
    MIPS_msa_dotp_s_h = idaapi.MIPS_msa_dotp_s_h   # Vector Signed Dot Product
    MIPS_msa_dotp_s_w = idaapi.MIPS_msa_dotp_s_w   # Vector Signed Dot Product
    MIPS_msa_dotp_s_d = idaapi.MIPS_msa_dotp_s_d   # Vector Signed Dot Product
    MIPS_msa_dotp_u_h = idaapi.MIPS_msa_dotp_u_h   # Vector Unsigned Dot Product
    MIPS_msa_dotp_u_w = idaapi.MIPS_msa_dotp_u_w   # Vector Unsigned Dot Product
    MIPS_msa_dotp_u_d = idaapi.MIPS_msa_dotp_u_d   # Vector Unsigned Dot Product
    MIPS_msa_dpadd_s_h = idaapi.MIPS_msa_dpadd_s_h  # Vector Signed Dot Product and Add
    MIPS_msa_dpadd_s_w = idaapi.MIPS_msa_dpadd_s_w  # Vector Signed Dot Product and Add
    MIPS_msa_dpadd_s_d = idaapi.MIPS_msa_dpadd_s_d  # Vector Signed Dot Product and Add
    MIPS_msa_dpadd_u_h = idaapi.MIPS_msa_dpadd_u_h  # Vector Unsigned Dot Product and Add
    MIPS_msa_dpadd_u_w = idaapi.MIPS_msa_dpadd_u_w  # Vector Unsigned Dot Product and Add
    MIPS_msa_dpadd_u_d = idaapi.MIPS_msa_dpadd_u_d  # Vector Unsigned Dot Product and Add
    MIPS_msa_dpsub_s_h = idaapi.MIPS_msa_dpsub_s_h  # Vector Signed Dot Product and Subtract
    MIPS_msa_dpsub_s_w = idaapi.MIPS_msa_dpsub_s_w  # Vector Signed Dot Product and Subtract
    MIPS_msa_dpsub_s_d = idaapi.MIPS_msa_dpsub_s_d  # Vector Signed Dot Product and Subtract
    MIPS_msa_dpsub_u_h = idaapi.MIPS_msa_dpsub_u_h  # Vector Unsigned Dot Product and Subtract
    MIPS_msa_dpsub_u_w = idaapi.MIPS_msa_dpsub_u_w  # Vector Unsigned Dot Product and Subtract
    MIPS_msa_dpsub_u_d = idaapi.MIPS_msa_dpsub_u_d  # Vector Unsigned Dot Product and Subtract
    MIPS_msa_sld_b = idaapi.MIPS_msa_sld_b      # GPR Columns Slide
    MIPS_msa_sld_h = idaapi.MIPS_msa_sld_h      # GPR Columns Slide
    MIPS_msa_sld_w = idaapi.MIPS_msa_sld_w      # GPR Columns Slide
    MIPS_msa_sld_d = idaapi.MIPS_msa_sld_d      # GPR Columns Slide
    MIPS_msa_sldi_b = idaapi.MIPS_msa_sldi_b     # Immediate Columns Slide
    MIPS_msa_sldi_h = idaapi.MIPS_msa_sldi_h     # Immediate Columns Slide
    MIPS_msa_sldi_w = idaapi.MIPS_msa_sldi_w     # Immediate Columns Slide
    MIPS_msa_sldi_d = idaapi.MIPS_msa_sldi_d     # Immediate Columns Slide
    MIPS_msa_splat_b = idaapi.MIPS_msa_splat_b    # GPR Element Splat
    MIPS_msa_splat_h = idaapi.MIPS_msa_splat_h    # GPR Element Splat
    MIPS_msa_splat_w = idaapi.MIPS_msa_splat_w    # GPR Element Splat
    MIPS_msa_splat_d = idaapi.MIPS_msa_splat_d    # GPR Element Splat
    MIPS_msa_splati_b = idaapi.MIPS_msa_splati_b   # Immediate Element Splat
    MIPS_msa_splati_h = idaapi.MIPS_msa_splati_h   # Immediate Element Splat
    MIPS_msa_splati_w = idaapi.MIPS_msa_splati_w   # Immediate Element Splat
    MIPS_msa_splati_d = idaapi.MIPS_msa_splati_d   # Immediate Element Splat
    MIPS_msa_pckev_b = idaapi.MIPS_msa_pckev_b    # Vector Pack Even
    MIPS_msa_pckev_h = idaapi.MIPS_msa_pckev_h    # Vector Pack Even
    MIPS_msa_pckev_w = idaapi.MIPS_msa_pckev_w    # Vector Pack Even
    MIPS_msa_pckev_d = idaapi.MIPS_msa_pckev_d    # Vector Pack Even
    MIPS_msa_pckod_b = idaapi.MIPS_msa_pckod_b    # Vector Pack Odd
    MIPS_msa_pckod_h = idaapi.MIPS_msa_pckod_h    # Vector Pack Odd
    MIPS_msa_pckod_w = idaapi.MIPS_msa_pckod_w    # Vector Pack Odd
    MIPS_msa_pckod_d = idaapi.MIPS_msa_pckod_d    # Vector Pack Odd
    MIPS_msa_ilvl_b = idaapi.MIPS_msa_ilvl_b     # Vector Interleave Left
    MIPS_msa_ilvl_h = idaapi.MIPS_msa_ilvl_h     # Vector Interleave Left
    MIPS_msa_ilvl_w = idaapi.MIPS_msa_ilvl_w     # Vector Interleave Left
    MIPS_msa_ilvl_d = idaapi.MIPS_msa_ilvl_d     # Vector Interleave Left
    MIPS_msa_ilvr_b = idaapi.MIPS_msa_ilvr_b     # Vector Interleave Right
    MIPS_msa_ilvr_h = idaapi.MIPS_msa_ilvr_h     # Vector Interleave Right
    MIPS_msa_ilvr_w = idaapi.MIPS_msa_ilvr_w     # Vector Interleave Right
    MIPS_msa_ilvr_d = idaapi.MIPS_msa_ilvr_d     # Vector Interleave Right
    MIPS_msa_ilvev_b = idaapi.MIPS_msa_ilvev_b    # Vector Interleave Even
    MIPS_msa_ilvev_h = idaapi.MIPS_msa_ilvev_h    # Vector Interleave Even
    MIPS_msa_ilvev_w = idaapi.MIPS_msa_ilvev_w    # Vector Interleave Even
    MIPS_msa_ilvev_d = idaapi.MIPS_msa_ilvev_d    # Vector Interleave Even
    MIPS_msa_ilvod_b = idaapi.MIPS_msa_ilvod_b    # Vector Interleave Odd
    MIPS_msa_ilvod_h = idaapi.MIPS_msa_ilvod_h    # Vector Interleave Odd
    MIPS_msa_ilvod_w = idaapi.MIPS_msa_ilvod_w    # Vector Interleave Odd
    MIPS_msa_ilvod_d = idaapi.MIPS_msa_ilvod_d    # Vector Interleave Odd
    MIPS_msa_vshf_b = idaapi.MIPS_msa_vshf_b     # Vector Data Preserving Shuffle
    MIPS_msa_vshf_h = idaapi.MIPS_msa_vshf_h     # Vector Data Preserving Shuffle
    MIPS_msa_vshf_w = idaapi.MIPS_msa_vshf_w     # Vector Data Preserving Shuffle
    MIPS_msa_vshf_d = idaapi.MIPS_msa_vshf_d     # Vector Data Preserving Shuffle
    MIPS_msa_srar_b = idaapi.MIPS_msa_srar_b     # Vector Shift Right Arithmetic Rounded
    MIPS_msa_srar_h = idaapi.MIPS_msa_srar_h     # Vector Shift Right Arithmetic Rounded
    MIPS_msa_srar_w = idaapi.MIPS_msa_srar_w     # Vector Shift Right Arithmetic Rounded
    MIPS_msa_srar_d = idaapi.MIPS_msa_srar_d     # Vector Shift Right Arithmetic Rounded
    MIPS_msa_srari_b = idaapi.MIPS_msa_srari_b    # Immediate Shift Right Arithmetic Rounded
    MIPS_msa_srari_h = idaapi.MIPS_msa_srari_h    # Immediate Shift Right Arithmetic Rounded
    MIPS_msa_srari_w = idaapi.MIPS_msa_srari_w    # Immediate Shift Right Arithmetic Rounded
    MIPS_msa_srari_d = idaapi.MIPS_msa_srari_d    # Immediate Shift Right Arithmetic Rounded
    MIPS_msa_srlr_b = idaapi.MIPS_msa_srlr_b     # Vector Shift Right Logical Rounded
    MIPS_msa_srlr_h = idaapi.MIPS_msa_srlr_h     # Vector Shift Right Logical Rounded
    MIPS_msa_srlr_w = idaapi.MIPS_msa_srlr_w     # Vector Shift Right Logical Rounded
    MIPS_msa_srlr_d = idaapi.MIPS_msa_srlr_d     # Vector Shift Right Logical Rounded
    MIPS_msa_srlri_b = idaapi.MIPS_msa_srlri_b    # Immediate Shift Right Logical Rounded
    MIPS_msa_srlri_h = idaapi.MIPS_msa_srlri_h    # Immediate Shift Right Logical Rounded
    MIPS_msa_srlri_w = idaapi.MIPS_msa_srlri_w    # Immediate Shift Right Logical Rounded
    MIPS_msa_srlri_d = idaapi.MIPS_msa_srlri_d    # Immediate Shift Right Logical Rounded
    MIPS_msa_hadd_s_h = idaapi.MIPS_msa_hadd_s_h   # Vector Signed Horizontal Add
    MIPS_msa_hadd_s_w = idaapi.MIPS_msa_hadd_s_w   # Vector Signed Horizontal Add
    MIPS_msa_hadd_s_d = idaapi.MIPS_msa_hadd_s_d   # Vector Signed Horizontal Add
    MIPS_msa_hadd_u_h = idaapi.MIPS_msa_hadd_u_h   # Vector Unsigned Horizontal Add
    MIPS_msa_hadd_u_w = idaapi.MIPS_msa_hadd_u_w   # Vector Unsigned Horizontal Add
    MIPS_msa_hadd_u_d = idaapi.MIPS_msa_hadd_u_d   # Vector Unsigned Horizontal Add
    MIPS_msa_hsub_s_h = idaapi.MIPS_msa_hsub_s_h   # Vector Signed Horizontal Subtract
    MIPS_msa_hsub_s_w = idaapi.MIPS_msa_hsub_s_w   # Vector Signed Horizontal Subtract
    MIPS_msa_hsub_s_d = idaapi.MIPS_msa_hsub_s_d   # Vector Signed Horizontal Subtract
    MIPS_msa_hsub_u_h = idaapi.MIPS_msa_hsub_u_h   # Vector Unsigned Horizontal Subtract
    MIPS_msa_hsub_u_w = idaapi.MIPS_msa_hsub_u_w   # Vector Unsigned Horizontal Subtract
    MIPS_msa_hsub_u_d = idaapi.MIPS_msa_hsub_u_d   # Vector Unsigned Horizontal Subtract
    MIPS_msa_and_v = idaapi.MIPS_msa_and_v      # Vector Logical And
    MIPS_msa_andi_b = idaapi.MIPS_msa_andi_b     # Immediate Logical And
    MIPS_msa_or_v = idaapi.MIPS_msa_or_v       # Vector Logical Or
    MIPS_msa_ori_b = idaapi.MIPS_msa_ori_b      # Immediate Logical Or
    MIPS_msa_nor_v = idaapi.MIPS_msa_nor_v      # Vector Logical Negated Or
    MIPS_msa_nori_b = idaapi.MIPS_msa_nori_b     # Immediate Logical Negated Or
    MIPS_msa_xor_v = idaapi.MIPS_msa_xor_v      # Vector Logical Exclusive Or
    MIPS_msa_xori_b = idaapi.MIPS_msa_xori_b     # Immediate Logical Exclusive Or
    MIPS_msa_bmnz_v = idaapi.MIPS_msa_bmnz_v     # Vector Bit Move If Not Zero
    MIPS_msa_bmnzi_b = idaapi.MIPS_msa_bmnzi_b    # Immediate Bit Move If Not Zero
    MIPS_msa_bmz_v = idaapi.MIPS_msa_bmz_v      # Vector Bit Move If Zero
    MIPS_msa_bmzi_b = idaapi.MIPS_msa_bmzi_b     # Immediate Bit Move If Zero
    MIPS_msa_bsel_v = idaapi.MIPS_msa_bsel_v     # Vector Bit Select
    MIPS_msa_bseli_b = idaapi.MIPS_msa_bseli_b    # Immediate Bit Select
    MIPS_msa_shf_b = idaapi.MIPS_msa_shf_b      # Immediate Set Shuffle Elements
    MIPS_msa_shf_h = idaapi.MIPS_msa_shf_h      # Immediate Set Shuffle Elements
    MIPS_msa_shf_w = idaapi.MIPS_msa_shf_w      # Immediate Set Shuffle Elements
    MIPS_msa_bnz_v = idaapi.MIPS_msa_bnz_v      # Immediate Branch If Not Zero (At Least One Element of Any Format Is Not Zero)
    MIPS_msa_bz_v = idaapi.MIPS_msa_bz_v       # Immediate Branch If Zero (All Elements of Any Format Are Zero)
    MIPS_msa_fill_b = idaapi.MIPS_msa_fill_b     # Vector Fill from GPR
    MIPS_msa_fill_h = idaapi.MIPS_msa_fill_h     # Vector Fill from GPR
    MIPS_msa_fill_w = idaapi.MIPS_msa_fill_w     # Vector Fill from GPR
    MIPS_msa_fill_d = idaapi.MIPS_msa_fill_d     # Vector Fill from GPR
    MIPS_msa_pcnt_b = idaapi.MIPS_msa_pcnt_b     # Vector Population Count
    MIPS_msa_pcnt_h = idaapi.MIPS_msa_pcnt_h     # Vector Population Count
    MIPS_msa_pcnt_w = idaapi.MIPS_msa_pcnt_w     # Vector Population Count
    MIPS_msa_pcnt_d = idaapi.MIPS_msa_pcnt_d     # Vector Population Count
    MIPS_msa_nloc_b = idaapi.MIPS_msa_nloc_b     # Vector Leading Ones Count
    MIPS_msa_nloc_h = idaapi.MIPS_msa_nloc_h     # Vector Leading Ones Count
    MIPS_msa_nloc_w = idaapi.MIPS_msa_nloc_w     # Vector Leading Ones Count
    MIPS_msa_nloc_d = idaapi.MIPS_msa_nloc_d     # Vector Leading Ones Count
    MIPS_msa_nlzc_b = idaapi.MIPS_msa_nlzc_b     # Vector Leading Zeros Count
    MIPS_msa_nlzc_h = idaapi.MIPS_msa_nlzc_h     # Vector Leading Zeros Count
    MIPS_msa_nlzc_w = idaapi.MIPS_msa_nlzc_w     # Vector Leading Zeros Count
    MIPS_msa_nlzc_d = idaapi.MIPS_msa_nlzc_d     # Vector Leading Zeros Count
    MIPS_msa_copy_s_b = idaapi.MIPS_msa_copy_s_b   # Element Copy to GPR Signed
    MIPS_msa_copy_s_h = idaapi.MIPS_msa_copy_s_h   # Element Copy to GPR Signed
    MIPS_msa_copy_s_w = idaapi.MIPS_msa_copy_s_w   # Element Copy to GPR Signed
    MIPS_msa_copy_s_d = idaapi.MIPS_msa_copy_s_d   # Element Copy to GPR Signed
    MIPS_msa_copy_u_b = idaapi.MIPS_msa_copy_u_b   # Element Copy to GPR Unsigned
    MIPS_msa_copy_u_h = idaapi.MIPS_msa_copy_u_h   # Element Copy to GPR Unsigned
    MIPS_msa_copy_u_w = idaapi.MIPS_msa_copy_u_w   # Element Copy to GPR Unsigned
    MIPS_msa_copy_u_d = idaapi.MIPS_msa_copy_u_d   # Element Copy to GPR Unsigned
    MIPS_msa_insert_b = idaapi.MIPS_msa_insert_b   # GPR Insert Element
    MIPS_msa_insert_h = idaapi.MIPS_msa_insert_h   # GPR Insert Element
    MIPS_msa_insert_w = idaapi.MIPS_msa_insert_w   # GPR Insert Element
    MIPS_msa_insert_d = idaapi.MIPS_msa_insert_d   # GPR Insert Element
    MIPS_msa_insve_b = idaapi.MIPS_msa_insve_b    # Element Insert Element
    MIPS_msa_insve_h = idaapi.MIPS_msa_insve_h    # Element Insert Element
    MIPS_msa_insve_w = idaapi.MIPS_msa_insve_w    # Element Insert Element
    MIPS_msa_insve_d = idaapi.MIPS_msa_insve_d    # Element Insert Element
    MIPS_msa_bnz_b = idaapi.MIPS_msa_bnz_b      # Immediate Branch If All Elements Are Not Zero
    MIPS_msa_bnz_h = idaapi.MIPS_msa_bnz_h      # Immediate Branch If All Elements Are Not Zero
    MIPS_msa_bnz_w = idaapi.MIPS_msa_bnz_w      # Immediate Branch If All Elements Are Not Zero
    MIPS_msa_bnz_d = idaapi.MIPS_msa_bnz_d      # Immediate Branch If All Elements Are Not Zero
    MIPS_msa_bz_b = idaapi.MIPS_msa_bz_b       # Immediate Branch If At Least One Element Is Zero
    MIPS_msa_bz_h = idaapi.MIPS_msa_bz_h       # Immediate Branch If At Least One Element Is Zero
    MIPS_msa_bz_w = idaapi.MIPS_msa_bz_w       # Immediate Branch If At Least One Element Is Zero
    MIPS_msa_bz_d = idaapi.MIPS_msa_bz_d       # Immediate Branch If At Least One Element Is Zero
    MIPS_msa_ldi_b = idaapi.MIPS_msa_ldi_b      # Immediate Load
    MIPS_msa_ldi_h = idaapi.MIPS_msa_ldi_h      # Immediate Load
    MIPS_msa_ldi_w = idaapi.MIPS_msa_ldi_w      # Immediate Load
    MIPS_msa_ldi_d = idaapi.MIPS_msa_ldi_d      # Immediate Load
    MIPS_msa_fcaf_w = idaapi.MIPS_msa_fcaf_w     # Vector Floating-Point Quiet Compare Always False
    MIPS_msa_fcaf_d = idaapi.MIPS_msa_fcaf_d     # Vector Floating-Point Quiet Compare Always False
    MIPS_msa_fcun_w = idaapi.MIPS_msa_fcun_w     # Vector Floating-Point Quiet Compare Unordered
    MIPS_msa_fcun_d = idaapi.MIPS_msa_fcun_d     # Vector Floating-Point Quiet Compare Unordered
    MIPS_msa_fceq_w = idaapi.MIPS_msa_fceq_w     # Vector Floating-Point Quiet Compare Equal
    MIPS_msa_fceq_d = idaapi.MIPS_msa_fceq_d     # Vector Floating-Point Quiet Compare Equal
    MIPS_msa_fcueq_w = idaapi.MIPS_msa_fcueq_w    # Vector Floating-Point Quiet Compare Unordered or Equal
    MIPS_msa_fcueq_d = idaapi.MIPS_msa_fcueq_d    # Vector Floating-Point Quiet Compare Unordered or Equal
    MIPS_msa_fclt_w = idaapi.MIPS_msa_fclt_w     # Vector Floating-Point Quiet Compare Less Than
    MIPS_msa_fclt_d = idaapi.MIPS_msa_fclt_d     # Vector Floating-Point Quiet Compare Less Than
    MIPS_msa_fcult_w = idaapi.MIPS_msa_fcult_w    # Vector Floating-Point Quiet Compare Unordered or Less Than
    MIPS_msa_fcult_d = idaapi.MIPS_msa_fcult_d    # Vector Floating-Point Quiet Compare Unordered or Less Than
    MIPS_msa_fcle_w = idaapi.MIPS_msa_fcle_w     # Vector Floating-Point Quiet Compare Less or Equal
    MIPS_msa_fcle_d = idaapi.MIPS_msa_fcle_d     # Vector Floating-Point Quiet Compare Less or Equal
    MIPS_msa_fcule_w = idaapi.MIPS_msa_fcule_w    # Vector Floating-Point Quiet Compare Unordered or Less or Equal
    MIPS_msa_fcule_d = idaapi.MIPS_msa_fcule_d    # Vector Floating-Point Quiet Compare Unordered or Less or Equal
    MIPS_msa_fsaf_w = idaapi.MIPS_msa_fsaf_w     # Vector Floating-Point Signaling Compare Always False
    MIPS_msa_fsaf_d = idaapi.MIPS_msa_fsaf_d     # Vector Floating-Point Signaling Compare Always False
    MIPS_msa_fsun_w = idaapi.MIPS_msa_fsun_w     # Vector Floating-Point Signaling Compare Unordered
    MIPS_msa_fsun_d = idaapi.MIPS_msa_fsun_d     # Vector Floating-Point Signaling Compare Unordered
    MIPS_msa_fseq_w = idaapi.MIPS_msa_fseq_w     # Vector Floating-Point Signaling Compare Equal
    MIPS_msa_fseq_d = idaapi.MIPS_msa_fseq_d     # Vector Floating-Point Signaling Compare Equal
    MIPS_msa_fsueq_w = idaapi.MIPS_msa_fsueq_w    # Vector Floating-Point Signaling Compare Unordered or Equal
    MIPS_msa_fsueq_d = idaapi.MIPS_msa_fsueq_d    # Vector Floating-Point Signaling Compare Unordered or Equal
    MIPS_msa_fslt_w = idaapi.MIPS_msa_fslt_w     # Vector Floating-Point Signaling Compare Less Than
    MIPS_msa_fslt_d = idaapi.MIPS_msa_fslt_d     # Vector Floating-Point Signaling Compare Less Than
    MIPS_msa_fsult_w = idaapi.MIPS_msa_fsult_w    # Vector Floating-Point Signaling Compare Unordered or Less Than
    MIPS_msa_fsult_d = idaapi.MIPS_msa_fsult_d    # Vector Floating-Point Signaling Compare Unordered or Less Than
    MIPS_msa_fsle_w = idaapi.MIPS_msa_fsle_w     # Vector Floating-Point Signaling Compare Less or Equal
    MIPS_msa_fsle_d = idaapi.MIPS_msa_fsle_d     # Vector Floating-Point Signaling Compare Less or Equal
    MIPS_msa_fsule_w = idaapi.MIPS_msa_fsule_w    # Vector Floating-Point Signaling Compare Unordered or Less or Equal
    MIPS_msa_fsule_d = idaapi.MIPS_msa_fsule_d    # Vector Floating-Point Signaling Compare Unordered or Less or Equal
    MIPS_msa_fadd_w = idaapi.MIPS_msa_fadd_w     # Vector Floating-Point Addition
    MIPS_msa_fadd_d = idaapi.MIPS_msa_fadd_d     # Vector Floating-Point Addition
    MIPS_msa_fsub_w = idaapi.MIPS_msa_fsub_w     # Vector Floating-Point Subtraction
    MIPS_msa_fsub_d = idaapi.MIPS_msa_fsub_d     # Vector Floating-Point Subtraction
    MIPS_msa_fmul_w = idaapi.MIPS_msa_fmul_w     # Vector Floating-Point Multiplication
    MIPS_msa_fmul_d = idaapi.MIPS_msa_fmul_d     # Vector Floating-Point Multiplication
    MIPS_msa_fdiv_w = idaapi.MIPS_msa_fdiv_w     # Vector Floating-Point Division
    MIPS_msa_fdiv_d = idaapi.MIPS_msa_fdiv_d     # Vector Floating-Point Division
    MIPS_msa_fmadd_w = idaapi.MIPS_msa_fmadd_w    # Vector Floating-Point Multiply-Add
    MIPS_msa_fmadd_d = idaapi.MIPS_msa_fmadd_d    # Vector Floating-Point Multiply-Add
    MIPS_msa_fmsub_w = idaapi.MIPS_msa_fmsub_w    # Vector Floating-Point Multiply-Sub
    MIPS_msa_fmsub_d = idaapi.MIPS_msa_fmsub_d    # Vector Floating-Point Multiply-Sub
    MIPS_msa_fexp2_w = idaapi.MIPS_msa_fexp2_w    # Vector Floating-Point Base 2 Exponentiation
    MIPS_msa_fexp2_d = idaapi.MIPS_msa_fexp2_d    # Vector Floating-Point Base 2 Exponentiation
    MIPS_msa_fexdo_h = idaapi.MIPS_msa_fexdo_h    # Vector Floating-Point Down-Convert Interchange Format
    MIPS_msa_fexdo_w = idaapi.MIPS_msa_fexdo_w    # Vector Floating-Point Down-Convert Interchange Format
    MIPS_msa_ftq_h = idaapi.MIPS_msa_ftq_h      # Vector Floating-Point Convert to Fixed-Point
    MIPS_msa_ftq_w = idaapi.MIPS_msa_ftq_w      # Vector Floating-Point Convert to Fixed-Point
    MIPS_msa_fmin_w = idaapi.MIPS_msa_fmin_w     # Vector Floating-Point Minimum
    MIPS_msa_fmin_d = idaapi.MIPS_msa_fmin_d     # Vector Floating-Point Minimum
    MIPS_msa_fmin_a_w = idaapi.MIPS_msa_fmin_a_w   # Vector Floating-Point Minimum Based on Absolute Values
    MIPS_msa_fmin_a_d = idaapi.MIPS_msa_fmin_a_d   # Vector Floating-Point Minimum Based on Absolute Values
    MIPS_msa_fmax_w = idaapi.MIPS_msa_fmax_w     # Vector Floating-Point Maximum
    MIPS_msa_fmax_d = idaapi.MIPS_msa_fmax_d     # Vector Floating-Point Maximum
    MIPS_msa_fmax_a_w = idaapi.MIPS_msa_fmax_a_w   # Vector Floating-Point Maximum Based on Absolute Values
    MIPS_msa_fmax_a_d = idaapi.MIPS_msa_fmax_a_d   # Vector Floating-Point Maximum Based on Absolute Values
    MIPS_msa_fcor_w = idaapi.MIPS_msa_fcor_w     # Vector Floating-Point Quiet Compare Ordered
    MIPS_msa_fcor_d = idaapi.MIPS_msa_fcor_d     # Vector Floating-Point Quiet Compare Ordered
    MIPS_msa_fcune_w = idaapi.MIPS_msa_fcune_w    # Vector Floating-Point Quiet Compare Unordered or Not Equal
    MIPS_msa_fcune_d = idaapi.MIPS_msa_fcune_d    # Vector Floating-Point Quiet Compare Unordered or Not Equal
    MIPS_msa_fcne_w = idaapi.MIPS_msa_fcne_w     # Vector Floating-Point Quiet Compare Not Equal
    MIPS_msa_fcne_d = idaapi.MIPS_msa_fcne_d     # Vector Floating-Point Quiet Compare Not Equal
    MIPS_msa_mul_q_h = idaapi.MIPS_msa_mul_q_h    # Vector Fixed-Point Multiply
    MIPS_msa_mul_q_w = idaapi.MIPS_msa_mul_q_w    # Vector Fixed-Point Multiply
    MIPS_msa_madd_q_h = idaapi.MIPS_msa_madd_q_h   # Vector Fixed-Point Multiply and Add
    MIPS_msa_madd_q_w = idaapi.MIPS_msa_madd_q_w   # Vector Fixed-Point Multiply and Add
    MIPS_msa_msub_q_h = idaapi.MIPS_msa_msub_q_h   # Vector Fixed-Point Multiply and Subtract
    MIPS_msa_msub_q_w = idaapi.MIPS_msa_msub_q_w   # Vector Fixed-Point Multiply and Subtract
    MIPS_msa_fsor_w = idaapi.MIPS_msa_fsor_w     # Vector Floating-Point Signaling Compare Ordered
    MIPS_msa_fsor_d = idaapi.MIPS_msa_fsor_d     # Vector Floating-Point Signaling Compare Ordered
    MIPS_msa_fsune_w = idaapi.MIPS_msa_fsune_w    # Vector Floating-Point Signaling Compare Unordered or Not Equal
    MIPS_msa_fsune_d = idaapi.MIPS_msa_fsune_d    # Vector Floating-Point Signaling Compare Unordered or Not Equal
    MIPS_msa_fsne_w = idaapi.MIPS_msa_fsne_w     # Vector Floating-Point Signaling Compare Not Equal
    MIPS_msa_fsne_d = idaapi.MIPS_msa_fsne_d     # Vector Floating-Point Signaling Compare Not Equal
    MIPS_msa_mulr_q_h = idaapi.MIPS_msa_mulr_q_h   # Vector Fixed-Point Multiply Rounded
    MIPS_msa_mulr_q_w = idaapi.MIPS_msa_mulr_q_w   # Vector Fixed-Point Multiply Rounded
    MIPS_msa_maddr_q_h = idaapi.MIPS_msa_maddr_q_h  # Vector Fixed-Point Multiply and Add Rounded
    MIPS_msa_maddr_q_w = idaapi.MIPS_msa_maddr_q_w  # Vector Fixed-Point Multiply and Add Rounded
    MIPS_msa_msubr_q_h = idaapi.MIPS_msa_msubr_q_h  # Vector Fixed-Point Multiply and Subtract Rounded
    MIPS_msa_msubr_q_w = idaapi.MIPS_msa_msubr_q_w  # Vector Fixed-Point Multiply and Subtract Rounded
    MIPS_msa_fclass_w = idaapi.MIPS_msa_fclass_w   # Vector Floating-Point Class Mask
    MIPS_msa_fclass_d = idaapi.MIPS_msa_fclass_d   # Vector Floating-Point Class Mask
    MIPS_msa_ftrunc_s_w = idaapi.MIPS_msa_ftrunc_s_w # Vector Floating-Point Truncate and Convert to Signed Integer
    MIPS_msa_ftrunc_s_d = idaapi.MIPS_msa_ftrunc_s_d # Vector Floating-Point Truncate and Convert to Signed Integer
    MIPS_msa_ftrunc_u_w = idaapi.MIPS_msa_ftrunc_u_w # Vector Floating-Point Truncate and Convert to Unsigned Integer
    MIPS_msa_ftrunc_u_d = idaapi.MIPS_msa_ftrunc_u_d # Vector Floating-Point Truncate and Convert to Unsigned Integer
    MIPS_msa_fsqrt_w = idaapi.MIPS_msa_fsqrt_w    # Vector Floating-Point Square Root
    MIPS_msa_fsqrt_d = idaapi.MIPS_msa_fsqrt_d    # Vector Floating-Point Square Root
    MIPS_msa_frsqrt_w = idaapi.MIPS_msa_frsqrt_w   # Vector Approximate Floating-Point Reciprocal of Square Root
    MIPS_msa_frsqrt_d = idaapi.MIPS_msa_frsqrt_d   # Vector Approximate Floating-Point Reciprocal of Square Root
    MIPS_msa_frcp_w = idaapi.MIPS_msa_frcp_w     # Vector Approximate Floating-Point Reciprocal
    MIPS_msa_frcp_d = idaapi.MIPS_msa_frcp_d     # Vector Approximate Floating-Point Reciprocal
    MIPS_msa_frint_w = idaapi.MIPS_msa_frint_w    # Vector Floating-Point Round to Integer
    MIPS_msa_frint_d = idaapi.MIPS_msa_frint_d    # Vector Floating-Point Round to Integer
    MIPS_msa_flog2_w = idaapi.MIPS_msa_flog2_w    # Vector Floating-Point Base 2 Logarithm
    MIPS_msa_flog2_d = idaapi.MIPS_msa_flog2_d    # Vector Floating-Point Base 2 Logarithm
    MIPS_msa_fexupl_w = idaapi.MIPS_msa_fexupl_w   # Vector Floating-Point Up-Convert Interchange Format Left
    MIPS_msa_fexupl_d = idaapi.MIPS_msa_fexupl_d   # Vector Floating-Point Up-Convert Interchange Format Left
    MIPS_msa_fexupr_w = idaapi.MIPS_msa_fexupr_w   # Vector Floating-Point Up-Convert Interchange Format Right
    MIPS_msa_fexupr_d = idaapi.MIPS_msa_fexupr_d   # Vector Floating-Point Up-Convert Interchange Format Right
    MIPS_msa_ffql_w = idaapi.MIPS_msa_ffql_w     # Vector Floating-Point Convert from Fixed-Point Left
    MIPS_msa_ffql_d = idaapi.MIPS_msa_ffql_d     # Vector Floating-Point Convert from Fixed-Point Left
    MIPS_msa_ffqr_w = idaapi.MIPS_msa_ffqr_w     # Vector Floating-Point Convert from Fixed-Point Right
    MIPS_msa_ffqr_d = idaapi.MIPS_msa_ffqr_d     # Vector Floating-Point Convert from Fixed-Point Right
    MIPS_msa_ftint_s_w = idaapi.MIPS_msa_ftint_s_w  # Vector Floating-Point Convert to Signed Integer
    MIPS_msa_ftint_s_d = idaapi.MIPS_msa_ftint_s_d  # Vector Floating-Point Convert to Signed Integer
    MIPS_msa_ftint_u_w = idaapi.MIPS_msa_ftint_u_w  # Vector Floating-Point Round and Convert to Unsigned Integer
    MIPS_msa_ftint_u_d = idaapi.MIPS_msa_ftint_u_d  # Vector Floating-Point Round and Convert to Unsigned Integer
    MIPS_msa_ffint_s_w = idaapi.MIPS_msa_ffint_s_w  # Vector Floating-Point Round and Convert from Signed Integer
    MIPS_msa_ffint_s_d = idaapi.MIPS_msa_ffint_s_d  # Vector Floating-Point Round and Convert from Signed Integer
    MIPS_msa_ffint_u_w = idaapi.MIPS_msa_ffint_u_w  # Vector Floating-Point Convert from Unsigned Integer
    MIPS_msa_ffint_u_d = idaapi.MIPS_msa_ffint_u_d  # Vector Floating-Point Convert from Unsigned Integer
    MIPS_msa_ctcmsa = idaapi.MIPS_msa_ctcmsa     # GPR Copy to MSA Control Register
    MIPS_msa_cfcmsa = idaapi.MIPS_msa_cfcmsa     # GPR Copy from MSA Control Register
    MIPS_msa_move_v = idaapi.MIPS_msa_move_v     # Vector Move

    # MIPS R6 (LSA is also part of MSA)
    MIPS_lsa = idaapi.MIPS_lsa            # Left Shift Add
    MIPS_dlsa = idaapi.MIPS_dlsa           # Doubleword Left Shift Add

    ZERO = 0
    AT = 1
    V0 = 2
    V1 = 3
    A0 = 4
    A1 = 5
    A2 = 6
    A3 = 7
    T0 = 8
    T1 = 9
    T2 = 10
    T3 = 11
    T4 = 12 
    T5 = 13
    T6 = 14
    T7 = 15
    S0 = 16
    S1 = 17
    S2 = 18
    S3 = 19
    S4 = 20
    S5 = 21
    S6 = 22
    S7 = 23
    T8 = 24
    T9 = 25
    #GPR26 = 26
    #GPR27 = 27
    GP = 28
    SP = 29
    FP = 30
    RA = 31

    TOTAL_GPR = 32      # Number of general purpose registers.

    GPR_NAMES = {
        ZERO : "$zero",
        AT : "$at",
        V0 : "$v0",
        V1 : "$v1",
        A0 : "$a0",
        A1 : "$a1",
        A2 : "$a2",
        A3 : "$a3",
        T0 : "$t0",
        T1 : "$t1",
        T2 : "$t2",
        T3 : "$t3",
        T4 : "$t4",
        T5 : "$t5",
        T6 : "$t6",
        T7 : "$t7",
        S0 : "$s0",
        S1 : "$s1",
        S2 : "$s2",
        S3 : "$s3",
        S4 : "$s4",
        S5 : "$s5",
        S6 : "$s6",
        S7 : "$s7",
        T8 : "$t8",
        T9 : "$t9",
        #GPR
        #GPR
        GP : "$gp",
        SP : "$sp",
        FP : "$fp",
        RA : "$ra",
        }

    SPR_NAMES = {
        # MIPS does not have any of those in IDA-Python according to idc.py
    }

    ARGUMENT_REGISTERS = [A0, A1, A2, A3]

    RETURN_REGISTERS = [V0, V1]

    VOLATILE_REGISTERS = ARGUMENT_REGISTERS + RETURN_REGISTERS + [
        T0, T1, T2, T3, T4, T5, T6, T7, T8, T9]


    #
    #  Helper methods
    #

    def is_branch(self, inst_type):
        """Indicate if the specified instruction is some kind of branch
        instruction.

        """
        return inst_type in CONDITIONAL_BRANCH_TYPES or \
            inst_type in UNCONDITIONAL_BRANCH_TYPES


"""
MIPS labels registers in two different ways. Integer registers are labelled from $r0 to $r31.
However, for the purposes of writing functions, it's often easier to label registers with mnemonics.

In particular, MIPS uses the following alternate names.

$zero This is hardwired 0 register. It's value is always zero no matter what you do with it.
$a0, $a1, $a2, $a3 There are the argument registers, and are used for passing up to four arguments to a function.
Additional arguments use the stack. In addition, if the argument isn't 32 bits (a structure, for example), it must be passed on the stack.

$t0, $t1, ..., $t9 These are temporary registers. When you make a subroutine call (i.e., jal), the callee does not need to save these registers if it wants to use these registers. However, if the caller wants to use the temporary registers after a jal call, it must push the temporary registers on the stack, just so the callee doesn't overwrite those registers.
$s0, $s1, ..., $s7 These are saved registers. If a callee wants to use these registers, it must first push the register value onto the stack. Once it's done using the register, it must pop it from the stack and restore the value of the saved register.
This is a convention only, meaning that assembly language programmers and compilers should observe these conventions, so code will work properly. However, the saving of these registers is not done automatically by the hardware.

$v0, $v1 These are return value registers. Usually only $v0 is use for the return value. However, if there's a need for 64 bits of result, there's a second register.
$sp The stack pointer points to the top of the stack. Stacks grow to smaller addresses, and the stack pointer contains the address of valid data (thus, $sp - 1 is an address of garbage data). It's assumed addresses smaller than $sp contain garbage data. However, it is possible for the stack to overflow, i.e., to have an address that becomes invalid.
$fp The frame pointer is a secondary pointer for function/subroutine calls. Usually, once jal occurs, you set $fp to $sp. Then, you adjust $sp for local variables. Once done, you can assign $sp back to $fp to quickly "pop" off everything from the stack used by a function.
$gp The global pointer is used to reference global variables. In general, we won't use it much in the course.
$ra Stores return address for jal calls.
Chart of Corresponding Registers

All of the registers listed in the previous section correspond to some register labelled $r0 up to $r31.
Here's a chart. It's the same as the one on page 140 of Patterson and Hennessy.

Name	Register Number	Usage	Preserved by callee
$zero	0	hardwired 0	N/A
$v0-$v1	2-3	return value and expression evaluation	no
$a0-$a3	4-7	arguments	no
$t0-$t7	8-15	temporary values	no
$s0-$s7	16-23	saved values	YES
$t8-$t9	24-25	more temporary values	no
$gp	28	global pointer	YES
$sp	29	stack pointer	YES
$fp	30	frame pointer	YES
$ra	31	return address	YES
There are a few registers not listed. $at, which is register 1, is used by the assembler. $k0-$k1 which is registers 26-27 is used by the operating system.

"""

ASSIGNMENT_TYPES = [
    InstructionSet.MIPS_add,         # Add
    InstructionSet.MIPS_addu,        # Add Unsigned
    InstructionSet.MIPS_and,         # AND
    InstructionSet.MIPS_dadd,        # Doubleword Add
    InstructionSet.MIPS_daddu,       # Doubleword Add Unsigned
    InstructionSet.MIPS_dsub,        # Doubleword Subtract
    InstructionSet.MIPS_dsubu,       # Doubleword Subtract Unsigned
    InstructionSet.MIPS_nor,         # NOR
    InstructionSet.MIPS_or,          # OR
    InstructionSet.MIPS_slt,         # Set on Less Than
    InstructionSet.MIPS_sltu,        # Set on Less Than Unsigned
    InstructionSet.MIPS_sub,         # Subtract
    InstructionSet.MIPS_subu,        # Subtract Unsigned
    InstructionSet.MIPS_xor,         # Exclusive OR
    InstructionSet.MIPS_dsll,        # Doubleword Shift Left Logical
    InstructionSet.MIPS_dsll32,      # Doubleword Shift Left Logical + 32
    InstructionSet.MIPS_dsra,        # Doubleword Shift Right Arithmetic
    InstructionSet.MIPS_dsra32,      # Doubleword Shift Right Arithmetic + 32
    InstructionSet.MIPS_dsrl,        # Doubleword Shift Right Logical
    InstructionSet.MIPS_dsrl32,      # Doubleword Shift Right Logical + 32
    InstructionSet.MIPS_sll,         # Shift Left Logical
    InstructionSet.MIPS_sra,         # Shift Right Arithmetic
    InstructionSet.MIPS_srl,         # Shift Right Logical
    InstructionSet.MIPS_dsllv,       # Doubleword Shift Left Logical Variable
    InstructionSet.MIPS_dsrav,       # Doubleword Shift Right Arithmetic Variable
    InstructionSet.MIPS_dsrlv,       # Doubleword Shift Right Logical Variable
    InstructionSet.MIPS_sllv,        # Shift Left Logical Variable
    InstructionSet.MIPS_srav,        # Shift Right Arithmetic Variable
    InstructionSet.MIPS_srlv,        # Shift Right Logical Variable
    InstructionSet.MIPS_addi,        # Add Immediate
    InstructionSet.MIPS_addiu,       # Add Immediate Unsigned
    InstructionSet.MIPS_daddi,       # Doubleword Add Immediate
    InstructionSet.MIPS_daddiu,      # Doubleword Add Immediate Unsigned
    InstructionSet.MIPS_slti,        # Set on Less Than Immediate
    InstructionSet.MIPS_sltiu,       # Set on Less Than Immediate Unsigned
    InstructionSet.MIPS_andi,        # AND Immediate
    InstructionSet.MIPS_ori,         # OR Immediate
    InstructionSet.MIPS_xori,        # Exclusive OR Immediate
    #...
    InstructionSet.MIPS_cfc1,        # Move Control From FPU
    InstructionSet.MIPS_cfc2,        # Move Control From Coprocessor 2
    InstructionSet.MIPS_ctc1,        # Move Control to FPU
    InstructionSet.MIPS_ctc2,        # Move Control to Coprocessor 2
    InstructionSet.MIPS_dmfc0,       # Doubleword Move From CP0
    InstructionSet.MIPS_qmfc2,       # Quadword Move From CP2
    InstructionSet.MIPS_dmtc0,       # Doubleword Move To CP0
    InstructionSet.MIPS_qmtc2,       # Quadword Move To CP2
    InstructionSet.MIPS_mfc0,        # Move from CP0
    InstructionSet.MIPS_mfc1,        # Move from FPU
    InstructionSet.MIPS_mfc2,        # Move from CP2
    InstructionSet.MIPS_mtc0,        # Move to CP0
    InstructionSet.MIPS_mtc1,        # Move to FPU
    InstructionSet.MIPS_mtc2,        # Move to CP2
    InstructionSet.MIPS_teqi,        # Trap if Equal Immediate
    InstructionSet.MIPS_tgei,        # Trap if Greater Than or Equal Immediate
    InstructionSet.MIPS_tgeiu,       # Trap if Greater Than or Equal Immediate Unsigned
    InstructionSet.MIPS_tlti,        # Trap if Less Than Immediate
    InstructionSet.MIPS_tltiu,       # Trap if Less Than Immediate Unsigned
    InstructionSet.MIPS_tnei,        # Trap if Not Equal Immediate
    InstructionSet.MIPS_ddiv,        # Doubleword Divide
    InstructionSet.MIPS_ddivu,       # Doubleword Divide Unsigned
    InstructionSet.MIPS_div,         # Divide
    InstructionSet.MIPS_divu,        # Divide Unsigned
    InstructionSet.MIPS_dmult,       # Doubleword Multiply
    InstructionSet.MIPS_dmultu,      # Doubleword Multiply Unsigned
    InstructionSet.MIPS_mult,        # Multiply
    InstructionSet.MIPS_multu,       # Multiply Unsigned
    InstructionSet.MIPS_mthi,        # Move To HI
    InstructionSet.MIPS_mtlo,        # Move To LO
    InstructionSet.MIPS_mfhi,        # Move From HI
    InstructionSet.MIPS_mflo,        # Move From LO
    InstructionSet.MIPS_cop0,        # Coprocessor 0 Operation
    InstructionSet.MIPS_cop1,        # FPU Operation
    InstructionSet.MIPS_cop2,        # Coprocessor 2 Operation
    # ...
    InstructionSet.MIPS_cache,       # Cache Operation
    InstructionSet.MIPS_lb,          # Load Byte
    InstructionSet.MIPS_lbu,         # Load Byte Unsigned
    InstructionSet.MIPS_ldl,         # Load Doubleword Left
    InstructionSet.MIPS_ldr,         # Load Doubleword Right
    InstructionSet.MIPS_lwl,         # Load Word Left
    InstructionSet.MIPS_lwr,         # Load Word Right
    InstructionSet.MIPS_ld,          # Load Doubleword
    InstructionSet.MIPS_lld,         # Load Linked Doubleword
    InstructionSet.MIPS_ldc1,        # Load Double FPU
    InstructionSet.MIPS_ldc2,        # Load Double Coprocessor 2
    InstructionSet.MIPS_ll,          # Load Linked
    InstructionSet.MIPS_lw,          # Load Word
    InstructionSet.MIPS_lwu,         # Load Word Unsigned
    InstructionSet.MIPS_lh,          # Load Halfword
    InstructionSet.MIPS_lhu,         # Load Halfword Unsigned
    InstructionSet.MIPS_lui,         # Load Upper Immediate
    InstructionSet.MIPS_lwc1,        # Load Word to FPU
    InstructionSet.MIPS_lwc2,        # Load Word to Coprocessor 2
    InstructionSet.MIPS_sb,          # Store Byte
    InstructionSet.MIPS_sdl,         # Store Doubleword Left
    InstructionSet.MIPS_sdr,         # Store Doubleword Right
    InstructionSet.MIPS_swl,         # Store Word Left
    InstructionSet.MIPS_swr,         # Store Word Right
    InstructionSet.MIPS_scd,         # Store Conditional Doubleword
    InstructionSet.MIPS_sd,          # Store Doubleword
    InstructionSet.MIPS_sdc1,        # Store Double FPU
    InstructionSet.MIPS_sdc2,        # Store Double Coprocessor 2
    InstructionSet.MIPS_sc,          # Store Conditional
    InstructionSet.MIPS_sw,          # Store Word
    InstructionSet.MIPS_sh,          # Store Halfword
    InstructionSet.MIPS_swc1,        # Store Word from FPU
    InstructionSet.MIPS_swc2,        # Store Word from Coprocessor 2
    InstructionSet.MIPS_sync,        # Sync

    # Coprocessor 0 instructions

    InstructionSet.MIPS_tlbp,        # Probe TLB for Matching Entry
    InstructionSet.MIPS_tlbr,        # Read Indexed TLB Entry
    InstructionSet.MIPS_tlbwi,       # Write Indexed TLB Entry
    InstructionSet.MIPS_tlbwr,       # Write Random TLB Entry


    # Coprocessor 1 (FPU) instructions

    InstructionSet.MIPS_fadd,        # Floating-point Add
    InstructionSet.MIPS_fsub,        # Floating-point Subtract
    InstructionSet.MIPS_fmul,        # Floating-point Multiply
    InstructionSet.MIPS_fdiv,        # Floating-point Divide
    InstructionSet.MIPS_fabs,        # Floating-point Absolute Value
    InstructionSet.MIPS_fcvt_s,      # Floating-point Convert to Single Fixed-Point Format
    InstructionSet.MIPS_fcvt_d,      # Floating-point Convert to Double Floating-Point Format
    InstructionSet.MIPS_fcvt_w,      # Floating-point Convert to Fixed-Point Format
    InstructionSet.MIPS_fcvt_l,      # Floating-point Convert to Long Fixed-Point Format
    InstructionSet.MIPS_fround_l,    # Floating-point Round to Long Fixed-Point Format
    InstructionSet.MIPS_ftrunc_l,    # Floating-point Truncate to Long Fixed-Point Format
    InstructionSet.MIPS_fceil_l,     # Floating-point Ceiling to Long Fixed-Point Format
    InstructionSet.MIPS_ffloor_l,    # Floating-point Floor to Long Fixed-Point Format
    InstructionSet.MIPS_fround_w,    # Floating-point Round to Single Fixed-Point Format
    InstructionSet.MIPS_ftrunc_w,    # Floating-point Truncate to Single Fixed-Point Format
    InstructionSet.MIPS_fceil_w,     # Floating-point Ceiling to Single Fixed-Point Format
    InstructionSet.MIPS_ffloor_w,    # Floating-point Floor to Single Fixed-Point Format
    InstructionSet.MIPS_fmov,        # Floating-point Move
    InstructionSet.MIPS_fneg,        # Floating-point Negate
    InstructionSet.MIPS_fsqrt,       # Floating-point Square Root
    InstructionSet.MIPS_fc_f,        # Floating-point Compare
    InstructionSet.MIPS_fc_un,       # Floating-point Compare
    InstructionSet.MIPS_fc_eq,       # Floating-point Compare
    InstructionSet.MIPS_fc_ueq,      # Floating-point Compare
    InstructionSet.MIPS_fc_olt,      # Floating-point Compare
    InstructionSet.MIPS_fc_ult,      # Floating-point Compare
    InstructionSet.MIPS_fc_ole,      # Floating-point Compare
    InstructionSet.MIPS_fc_ule,      # Floating-point Compare
    InstructionSet.MIPS_fc_sf,       # Floating-point Compare
    InstructionSet.MIPS_fc_ngle,     # Floating-point Compare
    InstructionSet.MIPS_fc_seq,      # Floating-point Compare
    InstructionSet.MIPS_fc_ngl,      # Floating-point Compare
    InstructionSet.MIPS_fc_lt,       # Floating-point Compare
    InstructionSet.MIPS_fc_nge,      # Floating-point Compare
    InstructionSet.MIPS_fc_le,       # Floating-point Compare
    InstructionSet.MIPS_fc_ngt,      # Floating-point Compare

    # Pseudo instructions

    InstructionSet.MIPS_nop,         # No operation
    InstructionSet.MIPS_mov,         # Move register
    InstructionSet.MIPS_neg,         # Negate
    InstructionSet.MIPS_negu,        # Negate Unsigned

    InstructionSet.MIPS_li,          # Load Immediate
    InstructionSet.MIPS_la,          # Load Address

]

UNCONDITIONAL_BRANCH_TYPES = [
    InstructionSet.MIPS_teq,         # Trap if Equal
    InstructionSet.MIPS_tge,         # Trap if Greater Than or Equal
    InstructionSet.MIPS_tgeu,        # Trap if Greater Than or Equal Unsigned
    InstructionSet.MIPS_tlt,         # Trap if Less Than
    InstructionSet.MIPS_tltu,        # Trap if Less Than Unsigned
    InstructionSet.MIPS_tne,         # Trap if Not Equal

    InstructionSet.MIPS_break,       # Break
    InstructionSet.MIPS_syscall,     # System Call

    InstructionSet.MIPS_jalr,        # Jump And Link Register
    InstructionSet.MIPS_j,           # Jump
    InstructionSet.MIPS_jr,          # Jump Register
    InstructionSet.MIPS_jal,         # Jump And Link
    InstructionSet.MIPS_jalx,        # Jump And Link And Exchange

    # Coprocessor 0 instructions

    InstructionSet.MIPS_eret,        # Exception Return

    # Pseudo instructions
    InstructionSet.MIPS_b,           # Branch Always
    InstructionSet.MIPS_bal,         # Branch Always and Link
]

CONDITIONAL_BRANCH_TYPES = [
    InstructionSet.MIPS_bc0f,        # Branch on Coprocessor 0 False
    InstructionSet.MIPS_bc1f,        # Branch on FPU False
    InstructionSet.MIPS_bc2f,        # Branch on Coprocessor 2 False
    InstructionSet.MIPS_bc3f,        # Branch on Coprocessor 3 False
    InstructionSet.MIPS_bc0fl,       # Branch on Coprocessor 0 False Likely
    InstructionSet.MIPS_bc1fl,       # Branch on FPU False Likely
    InstructionSet.MIPS_bc2fl,       # Branch on Coprocessor 2 False Likely
    InstructionSet.MIPS_bc3fl,       # Branch on Coprocessor 3 False Likely
    InstructionSet.MIPS_bc0t,        # Branch on Coprocessor 0 True
    InstructionSet.MIPS_bc1t,        # Branch on FPU True
    InstructionSet.MIPS_bc2t,        # Branch on Coprocessor 2 True
    InstructionSet.MIPS_bc3t,        # Branch on Coprocessor 3 True
    InstructionSet.MIPS_bc0tl,       # Branch on Coprocessor 0 True Likely
    InstructionSet.MIPS_bc1tl,       # Branch on FPU True Likely
    InstructionSet.MIPS_bc2tl,       # Branch on Coprocessor 2 True Likely
    InstructionSet.MIPS_bc3tl,       # Branch on Coprocessor 3 True Likely
    InstructionSet.MIPS_bgez,        # Branch on Greater Than or Equal to Zero
    InstructionSet.MIPS_bgezal,      # Branch on Greater Than or Equal to Zero And Link
    InstructionSet.MIPS_bgezall,     # Branch on Greater Than or Equal to Zero And Link Likely
    InstructionSet.MIPS_bgezl,       # Branch on Greater Than or Equal to Zero Likely
    InstructionSet.MIPS_bgtz,        # Branch on Greater Than Zero
    InstructionSet.MIPS_bgtzl,       # Branch on Greater Than Zero Likely
    InstructionSet.MIPS_blez,        # Branch on Less Than or Equal to Zero
    InstructionSet.MIPS_blezl,       # Branch on Less Than or Equal to Zero Likely
    InstructionSet.MIPS_bltz,        # Branch on Less Than Zero
    InstructionSet.MIPS_bltzal,      # Branch on Less Than Zero And Link
    InstructionSet.MIPS_bltzall,     # Branch on Less Than Zero And Link Likely
    InstructionSet.MIPS_bltzl,       # Branch on Less Than Zero Likely
    InstructionSet.MIPS_beq,         # Branch on Equal
    InstructionSet.MIPS_beql,        # Branch on Equal Likely
    InstructionSet.MIPS_bne,         # Branch on Not Equal
    InstructionSet.MIPS_bnel,        # Branch on Not Equal Likely

    InstructionSet.MIPS_bnez,        # Branch on Not Zero
    InstructionSet.MIPS_bnezl,       # Branch on Not Zero Likely
    InstructionSet.MIPS_beqz,        # Branch on Zero
    InstructionSet.MIPS_beqzl,       # Branch on Zero Likely
]

UNIMPLEMENTED_TYPES = [
]

