# 
# Copyright (c) 2017 Sebastian Muniz
# 
# This code is part of point source decompiler
#

import idaapi


class InstructionSet:
    ARM_ret = idaapi.ARM_ret                # Return from Subroutine
    ARM_nop = idaapi.ARM_nop                # No Operation
    ARM_b = idaapi.ARM_b                  # Branch
    ARM_bl = idaapi.ARM_bl                 # Branch with Link
    ARM_asr = idaapi.ARM_asr                # Arithmetic Shift Right
    ARM_lsl = idaapi.ARM_lsl                # Logical Shift Left
    ARM_lsr = idaapi.ARM_lsr                # Logical Shift Right
    ARM_ror = idaapi.ARM_ror                # Rotate Right
    ARM_neg = idaapi.ARM_neg                # Negate
    ARM_and = idaapi.ARM_and                # 0 Rd = Op1 & Op2
    ARM_eor = idaapi.ARM_eor                # 1 Rd = Op1 ^ Op2
    ARM_sub = idaapi.ARM_sub                # 2 Rd = Op1 - Op2
    ARM_rsb = idaapi.ARM_rsb                # 3 Rd = Op2 - Op1
    ARM_add = idaapi.ARM_add                # 4 Rd = Op1 + Op2
    ARM_adc = idaapi.ARM_adc                # 5 Rd = Op1 + Op2 + C
    ARM_sbc = idaapi.ARM_sbc                # 6 Rd = Op1 - Op2 + C - 1
    ARM_rsc = idaapi.ARM_rsc                # 7 Rd = Op2 - Op1 + C - 1
    ARM_tst = idaapi.ARM_tst                # 8 Set cond. codes on Op1 & Op2
    ARM_teq = idaapi.ARM_teq                # 9 Set cond. codes on Op1 ^ Op2
    ARM_cmp = idaapi.ARM_cmp                # A Set cond. codes on Op1 - Op2
    ARM_cmn = idaapi.ARM_cmn                # B Set cond. codes on Op1 + Op2
    ARM_orr = idaapi.ARM_orr                # C Rd = Op1 | Op2
    ARM_mov = idaapi.ARM_mov                # D Rd = Op2
    ARM_bic = idaapi.ARM_bic                # E Rd = Op1 & ~Op2
    ARM_mvn = idaapi.ARM_mvn                # F Rd = ~Op2
    ARM_mrs = idaapi.ARM_mrs                # Transfer PSR to Register
    ARM_msr = idaapi.ARM_msr                # Transfer Register to PSR
    ARM_mul = idaapi.ARM_mul                # Multiply
    ARM_mla = idaapi.ARM_mla                # Multiply-Accumulate
    ARM_ldr = idaapi.ARM_ldr                # Load from Memory
    ARM_ldrpc = idaapi.ARM_ldrpc              # Indirect Jump
    ARM_str = idaapi.ARM_str                # Store to Memory
    ARM_ldm = idaapi.ARM_ldm                # Load Block from Memory
    ARM_stm = idaapi.ARM_stm                # Store Block to Memory
    ARM_swp = idaapi.ARM_swp                # Single Data Swap
    ARM_svc = idaapi.ARM_svc                # Supervisor call

    # Version 4

    ARM_smull = idaapi.ARM_smull              # Signed Multiply long
    ARM_smlal = idaapi.ARM_smlal              # Signed Multiply-Accumulate long
    ARM_umull = idaapi.ARM_umull              # Unsigned Multiply long
    ARM_umlal = idaapi.ARM_umlal              # Unsigned Multiply-Accumulate long
    ARM_bx = idaapi.ARM_bx                 # Branch to/from Thumb mode
    ARM_pop = idaapi.ARM_pop                # Pop registers
    ARM_push = idaapi.ARM_push               # Push registers
    ARM_adr = idaapi.ARM_adr                # Load address

    # Version 5

    ARM_bkpt = idaapi.ARM_bkpt               # Breakpoint
    ARM_blx1 = idaapi.ARM_blx1               # Branch with Link and Exchange (immediate address)
    ARM_blx2 = idaapi.ARM_blx2               # Branch with Link and Exchange (register indirect)
    ARM_clz = idaapi.ARM_clz                # Count Leading Zeros

    # Version 5E

    ARM_ldrd = idaapi.ARM_ldrd               # Load pair of registers
    ARM_pld = idaapi.ARM_pld                # Prepare to load data
    ARM_qadd = idaapi.ARM_qadd               # Saturated addition
    ARM_qdadd = idaapi.ARM_qdadd              # Saturated addition with doubling
    ARM_qdsub = idaapi.ARM_qdsub              # Saturated subtraction with doubling
    ARM_qsub = idaapi.ARM_qsub               # Saturated subtraction
    ARM_smlabb = idaapi.ARM_smlabb             # Signed multiply-accumulate (bottom*bottom)
    ARM_smlatb = idaapi.ARM_smlatb             # Signed multiply-accumulate (top*bottom)
    ARM_smlabt = idaapi.ARM_smlabt             # Signed multiply-accumulate (bottom*top)
    ARM_smlatt = idaapi.ARM_smlatt             # Signed multiply-accumulate (top*top)
    ARM_smlalbb = idaapi.ARM_smlalbb            # Long signed multiply-accumulate (bottom*bottom)
    ARM_smlaltb = idaapi.ARM_smlaltb            # Long signed multiply-accumulate (top*bottom)
    ARM_smlalbt = idaapi.ARM_smlalbt            # Long signed multiply-accumulate (bottom*top)
    ARM_smlaltt = idaapi.ARM_smlaltt            # Long signed multiply-accumulate (top*top)
    ARM_smlawb = idaapi.ARM_smlawb             # Wide signed multiply-accumulate (bottom)
    ARM_smulwb = idaapi.ARM_smulwb             # Wide signed multiply (bottom)
    ARM_smlawt = idaapi.ARM_smlawt             # Wide signed multiply-accumulate (top)
    ARM_smulwt = idaapi.ARM_smulwt             # Wide signed multiply (top)
    ARM_smulbb = idaapi.ARM_smulbb             # Signed multiply (bottom*bottom)
    ARM_smultb = idaapi.ARM_smultb             # Signed multiply (top*bottom)
    ARM_smulbt = idaapi.ARM_smulbt             # Signed multiply (bottom*top)
    ARM_smultt = idaapi.ARM_smultt             # Signed multiply (top*top)
    ARM_strd = idaapi.ARM_strd               # Store pair of registers

    # Macro instructions

    ARM_movl = idaapi.ARM_movl               # Move immediate to register
    ARM_adrl = idaapi.ARM_adrl               # Load address
    ARM_swbkpt = idaapi.ARM_swbkpt             # WinCE Debugger break

    # Coprocessor instructions

    ARM_cdp = idaapi.ARM_cdp                # Coprocessor Data Processing
    ARM_cdp2 = idaapi.ARM_cdp2               # Coprocessor Data Processing
    ARM_ldc = idaapi.ARM_ldc                # Load Coprocessor Register
    ARM_ldc2 = idaapi.ARM_ldc2               # Load Coprocessor Register
    ARM_stc = idaapi.ARM_stc                # Store Coprocessor Register
    ARM_stc2 = idaapi.ARM_stc2               # Store Coprocessor Register
    ARM_mrc = idaapi.ARM_mrc                # Move from Coprocessor to ARM Register
    ARM_mrc2 = idaapi.ARM_mrc2               # Move from Coprocessor to ARM Register
    ARM_mcr = idaapi.ARM_mcr                # Move from ARM = idaapi.ARM to Coprocessor Register
    ARM_mcr2 = idaapi.ARM_mcr2               # Move from ARM = idaapi.ARM to Coprocessor Register
    ARM_mcrr = idaapi.ARM_mcrr               # Copy pair of registers to coprocessor (5E)
    ARM_mrrc = idaapi.ARM_mrrc               # Copy pair of registers from coprocessor (5E)

    # VFP instructions

    ARM_fabsd = idaapi.ARM_fabsd              # Floating point Absolute Value, Double precision
    ARM_fabss = idaapi.ARM_fabss              # Floating point Absolute Value, Single precision
    ARM_faddd = idaapi.ARM_faddd              # Floating point Addition, Double precision
    ARM_fadds = idaapi.ARM_fadds              # Floating point Addition, Single precision
    ARM_fcmpd = idaapi.ARM_fcmpd              # Floating point Compare, Double precision
    ARM_fcmps = idaapi.ARM_fcmps              # Floating point Compare, Single precision
    ARM_fcmped = idaapi.ARM_fcmped             # Floating point Compare (NaN Exceptions), Double precision
    ARM_fcmpes = idaapi.ARM_fcmpes             # Floating point Compare (NaN Exceptions), Single precision
    ARM_fcmpezd = idaapi.ARM_fcmpezd            # Floating point Compare (NaN Exceptions) with Zero, Double precision
    ARM_fcmpezs = idaapi.ARM_fcmpezs            # Floating point Compare (NaN Exceptions) with Zero, Single precision
    ARM_fcmpzd = idaapi.ARM_fcmpzd             # Floating point Compare with Zero, Double precision
    ARM_fcmpzs = idaapi.ARM_fcmpzs             # Floating point Compare with Zero, Single precision
    ARM_fcpyd = idaapi.ARM_fcpyd              # Floating point Copy, Double precision
    ARM_fcpys = idaapi.ARM_fcpys              # Floating point Copy, Single precision
    ARM_fcvtsd = idaapi.ARM_fcvtsd             # Floating point Convert to Single precision from Double precision
    ARM_fcvtds = idaapi.ARM_fcvtds             # Floating point Convert to Double precision from Single precision
    ARM_fdivd = idaapi.ARM_fdivd              # Floating point Divide, Double precision
    ARM_fdivs = idaapi.ARM_fdivs              # Floating point Divide, Single precision
    ARM_fldd = idaapi.ARM_fldd               # Floating point Load, Double precision
    ARM_flds = idaapi.ARM_flds               # Floating point Load, Single precision
    ARM_fldmd = idaapi.ARM_fldmd              # Floating point Load Multiple, Double precision
    ARM_fldms = idaapi.ARM_fldms              # Floating point Load Multiple, Single precision
    ARM_fldmx = idaapi.ARM_fldmx              # Floating point Load Multiple, Unknown precision
    ARM_fmacd = idaapi.ARM_fmacd              # Floating point Multiply and Accumulate, Double precision
    ARM_fmacs = idaapi.ARM_fmacs              # Floating point Multiply and Accumulate, Single precision
    ARM_fmscd = idaapi.ARM_fmscd              # Floating point Multiply and Subtract, Double precision
    ARM_fmscs = idaapi.ARM_fmscs              # Floating point Multiply and Subtract, Single precision
    ARM_fmstat = idaapi.ARM_fmstat             # Floating point Move Status
    ARM_fmuld = idaapi.ARM_fmuld              # Floating point Multiply, Double precision
    ARM_fmuls = idaapi.ARM_fmuls              # Floating point Multiply, Single precision
    ARM_fnegd = idaapi.ARM_fnegd              # Floating point Negate, Double precision
    ARM_fnegs = idaapi.ARM_fnegs              # Floating point Negate, Single precision
    ARM_fnmacd = idaapi.ARM_fnmacd             # Floating point Negated Multiply and Accumulate, Double precision
    ARM_fnmacs = idaapi.ARM_fnmacs             # Floating point Negated Multiply and Accumulate, Single precision
    ARM_fnmscd = idaapi.ARM_fnmscd             # Floating point Negated Multiply and Subtract, Double precision
    ARM_fnmscs = idaapi.ARM_fnmscs             # Floating point Negated Multiply and Subtract, Single precision
    ARM_fnmuld = idaapi.ARM_fnmuld             # Floating point Negated Multiply, Double precision
    ARM_fnmuls = idaapi.ARM_fnmuls             # Floating point Negated Multiply, Single precision
    ARM_fsitod = idaapi.ARM_fsitod             # Floating point Convert Signed Integer to Double precision
    ARM_fsitos = idaapi.ARM_fsitos             # Floating point Convert Signed Integer to Single precision
    ARM_fsqrtd = idaapi.ARM_fsqrtd             # Floating point Square Root, Double precision
    ARM_fsqrts = idaapi.ARM_fsqrts             # Floating point Square Root, Single precision
    ARM_fstd = idaapi.ARM_fstd               # Floating point Store, Double precision
    ARM_fsts = idaapi.ARM_fsts               # Floating point Store, Single precision
    ARM_fstmd = idaapi.ARM_fstmd              # Floating point Store Multiple, Double precision
    ARM_fstms = idaapi.ARM_fstms              # Floating point Store Multiple, Single precision
    ARM_fstmx = idaapi.ARM_fstmx              # Floating point Store Multiple, Unknown precision
    ARM_fsubd = idaapi.ARM_fsubd              # Floating point Subtract, Double precision
    ARM_fsubs = idaapi.ARM_fsubs              # Floating point Subtract, Single precision
    ARM_ftosid = idaapi.ARM_ftosid             # Floating point Convert to Signed Integer from Double precision
    ARM_ftosis = idaapi.ARM_ftosis             # Floating point Convert to Signed Integer from Single precision
    ARM_ftosizd = idaapi.ARM_ftosizd            # Floating point Convert to Signed Integer from Double precision, RZ mode
    ARM_ftosizs = idaapi.ARM_ftosizs            # Floating point Convert to Signed Integer from Single precision, RZ mode
    ARM_ftouid = idaapi.ARM_ftouid             # Floating point Convert to Unsigned Integer from Double precision
    ARM_ftouis = idaapi.ARM_ftouis             # Floating point Convert to Unsigned Integer from Single precision
    ARM_ftouizd = idaapi.ARM_ftouizd            # Floating point Convert to Unsigned Integer from Double precision, RZ mode
    ARM_ftouizs = idaapi.ARM_ftouizs            # Floating point Convert to Unsigned Integer from Single precision, RZ mode
    ARM_fuitod = idaapi.ARM_fuitod             # Floating point Convert Unsigned Integer to Double precision
    ARM_fuitos = idaapi.ARM_fuitos             # Floating point Convert Unsigned Integer to Single precision
    ARM_fmdhr = idaapi.ARM_fmdhr              # Floating point Move to Double precision High from Register
    ARM_fmrdh = idaapi.ARM_fmrdh              # Floating point Move to Register from Double precision High
    ARM_fmdlr = idaapi.ARM_fmdlr              # Floating point Move to Double precision Low from Register
    ARM_fmrdl = idaapi.ARM_fmrdl              # Floating point Move to Register from Double precision Low
    ARM_fmxr = idaapi.ARM_fmxr               # Floating point Move to System Register from Register
    ARM_fmrx = idaapi.ARM_fmrx               # Floating point Move to Register from System Register
    ARM_fmsr = idaapi.ARM_fmsr               # Floating point Move to Single precision from Register
    ARM_fmrs = idaapi.ARM_fmrs               # Floating point Move to Register from Single precision

    # VFP ARMv5TE = idaapi.ARMv5TE extensions

    ARM_fmdrr = idaapi.ARM_fmdrr              # Floating point Move to Double precision from two Registers
    ARM_fmrrd = idaapi.ARM_fmrrd              # Floating point Move to two Registers from Double precision
    ARM_fmsrr = idaapi.ARM_fmsrr              # Floating point Move to two Single precision from two Registers
    ARM_fmrrs = idaapi.ARM_fmrrs              # Floating point Move to two Registers from two Single precision

    # ARM = idaapi.ARM v5J instructions

    ARM_bxj = idaapi.ARM_bxj                # Branch to Jazelle

    # ARM = idaapi.ARM v6 instructions

    ARM_mcrr2 = idaapi.ARM_mcrr2              # Move to Coprocessor from two ARM Registers
    ARM_mrrc2 = idaapi.ARM_mrrc2              # Move to two ARM = idaapi.ARM Registers from Coprocessor
    ARM_cps = idaapi.ARM_cps                # Change Processor State
    ARM_cpsid = idaapi.ARM_cpsid              # Disable Interrupts
    ARM_cpsie = idaapi.ARM_cpsie              # Enable Interrupts
    ARM_ldrex = idaapi.ARM_ldrex              # Load Register Exclusive
    ARM_pkhbt = idaapi.ARM_pkhbt              # Pack halfword bottom + top
    ARM_pkhtb = idaapi.ARM_pkhtb              # Pack halfword top + bottom
    ARM_qadd16 = idaapi.ARM_qadd16             # Signed saturating arithmetic hafword-wise addition
    ARM_qadd8 = idaapi.ARM_qadd8              # Signed saturating arithmetic byte-wise addition
    ARM_qaddsubx = idaapi.ARM_qaddsubx           # Signed saturating arithmetic exchange, add, substract
    ARM_qsub16 = idaapi.ARM_qsub16             # Signed saturating arithmetic hafword-wise substraction
    ARM_qsub8 = idaapi.ARM_qsub8              # Signed saturating arithmetic byte-wise substraction
    ARM_qsubaddx = idaapi.ARM_qsubaddx           # Signed saturating arithmetic exchange, substract, add
    ARM_rev = idaapi.ARM_rev                # Byte Reverse Word
    ARM_rev16 = idaapi.ARM_rev16              # Byte Reverse Packed Halfword
    ARM_revsh = idaapi.ARM_revsh              # Byte Reverse Signed Halfword
    ARM_rfe = idaapi.ARM_rfe                # Return from exception
    ARM_sadd16 = idaapi.ARM_sadd16             # Signed arithmetic modulo hafword-wise addition
    ARM_sadd8 = idaapi.ARM_sadd8              # Signed arithmetic modulo byte-wise addition
    ARM_saddsubx = idaapi.ARM_saddsubx           # Signed arithmetic modulo exchange, add, substract
    ARM_sel = idaapi.ARM_sel                # Select bytes
    ARM_setend = idaapi.ARM_setend             # Set Byte Endianness
    ARM_shadd16 = idaapi.ARM_shadd16            # Signed arithmetic hafword-wise addition, halving results
    ARM_shadd8 = idaapi.ARM_shadd8             # Signed arithmetic byte-wise addition, halving results
    ARM_shaddsubx = idaapi.ARM_shaddsubx          # Signed arithmetic exchange, add, substract, halving results
    ARM_shsub16 = idaapi.ARM_shsub16            # Signed arithmetic hafword-wise substraction, halving results
    ARM_shsub8 = idaapi.ARM_shsub8             # Signed arithmetic byte-wise substraction, halving results
    ARM_shsubaddx = idaapi.ARM_shsubaddx          # Signed arithmetic exchange, substract, add, halving results
    ARM_smlad = idaapi.ARM_smlad              # Dual signed multiply, add and accumulate
    ARM_smladx = idaapi.ARM_smladx             # Dual signed multiply, add and accumulate crossed
    ARM_smuad = idaapi.ARM_smuad              # Dual signed multiply and add
    ARM_smuadx = idaapi.ARM_smuadx             # Dual signed multiply and add crossed
    ARM_smlald = idaapi.ARM_smlald             # Dual signed multiply, add and accumulate long
    ARM_smlaldx = idaapi.ARM_smlaldx            # Dual signed multiply, add and accumulate long crossed
    ARM_smlsd = idaapi.ARM_smlsd              # Dual signed multiply, substract and accumulate
    ARM_smlsdx = idaapi.ARM_smlsdx             # Dual signed multiply, substract and accumulate crossed
    ARM_smusd = idaapi.ARM_smusd              # Dual signed multiply and substract
    ARM_smusdx = idaapi.ARM_smusdx             # Dual signed multiply and substract crossed
    ARM_smlsld = idaapi.ARM_smlsld             # Dual signed multiply, substract and accumulate long
    ARM_smlsldx = idaapi.ARM_smlsldx            # Dual signed multiply, substract and accumulate long crossed
    ARM_smmla = idaapi.ARM_smmla              # Signed most significant word multiply and accumulate truncated
    ARM_smmlar = idaapi.ARM_smmlar             # Signed most significant word multiply and accumulate rounded
    ARM_smmul = idaapi.ARM_smmul              # Signed most significant word multiply truncated
    ARM_smmulr = idaapi.ARM_smmulr             # Signed most significant word multiply rounded
    ARM_smmls = idaapi.ARM_smmls              # Signed most significant word multiply and substract truncated
    ARM_smmlsr = idaapi.ARM_smmlsr             # Signed most significant word multiply and substract rounded
    ARM_srs = idaapi.ARM_srs                # Store Return State
    ARM_ssat = idaapi.ARM_ssat               # Signed Saturate
    ARM_ssat16 = idaapi.ARM_ssat16             # Signed saturate two halfwords
    ARM_ssub16 = idaapi.ARM_ssub16             # Signed arithmetic hafword-wise substraction
    ARM_ssub8 = idaapi.ARM_ssub8              # Signed arithmetic byte-wise substraction
    ARM_ssubaddx = idaapi.ARM_ssubaddx           # Signed arithmetic exchange, substract, add
    ARM_strex = idaapi.ARM_strex              # Store Register Exclusive
    ARM_sxtab = idaapi.ARM_sxtab              # Signed extend byte to word, add
    ARM_sxtb = idaapi.ARM_sxtb               # Signed extend byte to word
    ARM_sxtab16 = idaapi.ARM_sxtab16            # Signed extend two bytes to halfwords, add
    ARM_sxtb16 = idaapi.ARM_sxtb16             # Signed extend two bytes to halfwords
    ARM_sxtah = idaapi.ARM_sxtah              # Signed extend halfword to word, add
    ARM_sxth = idaapi.ARM_sxth               # Signed extend halfword to word
    ARM_uadd16 = idaapi.ARM_uadd16             # Unsigned arithmetic modulo hafword-wise addition
    ARM_uadd8 = idaapi.ARM_uadd8              # Unsigned arithmetic modulo byte-wise addition
    ARM_uaddsubx = idaapi.ARM_uaddsubx           # Unsigned arithmetic modulo exchange, add, substract
    ARM_uhadd16 = idaapi.ARM_uhadd16            # Unsigned arithmetic hafword-wise addition, halving results
    ARM_uhadd8 = idaapi.ARM_uhadd8             # Unsigned arithmetic byte-wise addition, halving results
    ARM_uhaddsubx = idaapi.ARM_uhaddsubx          # Unsigned arithmetic exchange, add, substract, halving results
    ARM_uhsub16 = idaapi.ARM_uhsub16            # Unsigned arithmetic hafword-wise substraction, halving results
    ARM_uhsub8 = idaapi.ARM_uhsub8             # Unsigned arithmetic byte-wise substraction, halving results
    ARM_uhsubaddx = idaapi.ARM_uhsubaddx          # Unsigned arithmetic exchange, substract, add, halving results
    ARM_umaal = idaapi.ARM_umaal              # Multiply unsigned double accumulate long
    ARM_uqadd16 = idaapi.ARM_uqadd16            # Unsigned saturating arithmetic hafword-wise addition
    ARM_uqadd8 = idaapi.ARM_uqadd8             # Unsigned saturating arithmetic byte-wise addition
    ARM_uqaddsubx = idaapi.ARM_uqaddsubx          # Unsigned saturating arithmetic exchange, add, substract
    ARM_uqsub16 = idaapi.ARM_uqsub16            # Unsigned saturating arithmetic hafword-wise substraction
    ARM_uqsub8 = idaapi.ARM_uqsub8             # Unsigned saturating arithmetic byte-wise substraction
    ARM_uqsubaddx = idaapi.ARM_uqsubaddx          # Unsigned saturating arithmetic exchange, substract, add
    ARM_usada8 = idaapi.ARM_usada8             # Unsigned sum of absolute differences and accumulate
    ARM_usad8 = idaapi.ARM_usad8              # Unsigned sum of absolute differences
    ARM_usat = idaapi.ARM_usat               # Unsigned saturate word
    ARM_usat16 = idaapi.ARM_usat16             # Unsigned saturate two halfwords
    ARM_usub16 = idaapi.ARM_usub16             # Unsigned arithmetic hafword-wise substraction
    ARM_usub8 = idaapi.ARM_usub8              # Unsigned arithmetic byte-wise substraction
    ARM_usubaddx = idaapi.ARM_usubaddx           # Unsigned arithmetic exchange, substract, add
    ARM_uxtab = idaapi.ARM_uxtab              # Unsigned extend byte to word, add
    ARM_uxtb = idaapi.ARM_uxtb               # Unsigned extend byte to word
    ARM_uxtab16 = idaapi.ARM_uxtab16            # Unsigned extend two bytes to halfwords, add
    ARM_uxtb16 = idaapi.ARM_uxtb16             # Unsigned extend two bytes to halfwords
    ARM_uxtah = idaapi.ARM_uxtah              # Unsigned extend halfword to word, add
    ARM_uxth = idaapi.ARM_uxth               # Unsigned extend halfword to word

    # ARM = idaapi.ARM v6zk instructions

    ARM_clrex = idaapi.ARM_clrex              # Clear Exclusive
    ARM_ldrexb = idaapi.ARM_ldrexb             # Load Byte Exclusive
    ARM_ldrexd = idaapi.ARM_ldrexd             # Load DoubleWord Exclusive
    ARM_ldrexh = idaapi.ARM_ldrexh             # Load Halfword Exclusive
    ARM_strexb = idaapi.ARM_strexb             # Store Byte Exclusive
    ARM_strexd = idaapi.ARM_strexd             # Store DoubleWord Exclusive
    ARM_strexh = idaapi.ARM_strexh             # Store Halfword Exclusive
    ARM_yield = idaapi.ARM_yield              # Yield (hint)
    ARM_sev = idaapi.ARM_sev                # Send Event (hint)
    ARM_wfe = idaapi.ARM_wfe                # Wait For Event (hint)
    ARM_wfi = idaapi.ARM_wfi                # Wait For Interrupt (hint)
    ARM_smc = idaapi.ARM_smc                # Secure Monitor Call

    # ARM = idaapi.ARM Thumb32 instructions

    ARM_orn = idaapi.ARM_orn                # Rd = Op1 | ~Op2
    ARM_movt = idaapi.ARM_movt               # Move Top
    ARM_sbfx = idaapi.ARM_sbfx               # Signed Bit Field Extract
    ARM_ubfx = idaapi.ARM_ubfx               # Unsigned Bit Field Extract
    ARM_bfi = idaapi.ARM_bfi                # Bit Field Insert
    ARM_bfc = idaapi.ARM_bfc                # Bit Field Clear
    ARM_tbb = idaapi.ARM_tbb                # Table Branch Byte
    ARM_tbh = idaapi.ARM_tbh                # Table Branch Halfword
    ARM_pli = idaapi.ARM_pli                # Prepare to load code
    ARM_rbit = idaapi.ARM_rbit               # Reverse Bits
    ARM_it = idaapi.ARM_it                 # If Then
    ARM_mls = idaapi.ARM_mls                # Multiply and Subtract
    ARM_sdiv = idaapi.ARM_sdiv               # Signed Divide
    ARM_udiv = idaapi.ARM_udiv               # Unsigned Divide
    ARM_cbz = idaapi.ARM_cbz                # Compare and Branch on Zero
    ARM_cbnz = idaapi.ARM_cbnz               # Compare and Branch on Non-Zero
    ARM_dsb = idaapi.ARM_dsb                # Data Synchronization Barrier
    ARM_dmb = idaapi.ARM_dmb                # Data Memory Barrier
    ARM_isb = idaapi.ARM_isb                # Instruction Synchronization Barrier
    ARM_dbg = idaapi.ARM_dbg                # Debug Hint

    ARM_und = idaapi.ARM_und                # Architecturally undefined instruction

    # missing instructions (not yet decoded)

    ARM_rrx = idaapi.ARM_rrx                # Rotate Right with Extend
    ARM_enterx = idaapi.ARM_enterx             # Enter ThumbEE state
    ARM_leavex = idaapi.ARM_leavex             # Leave ThumbEE state
    ARM_chka = idaapi.ARM_chka               # Check Array
    ARM_hb = idaapi.ARM_hb                 # Handler Branch
    ARM_hbl = idaapi.ARM_hbl                # Handler Branch with Link
    ARM_hblp = idaapi.ARM_hblp               # Handler Branch with Link and Parameter
    ARM_hbp = idaapi.ARM_hbp                # Handler Branch with Parameter

    # NEON (Advanced SIMD) and extra VFP instructions

    ARM_vaba = idaapi.ARM_vaba               # Vector Absolute Difference and Accumulate
    ARM_vabal = idaapi.ARM_vabal              # Vector Absolute Difference and Accumulate Long
    ARM_vabd = idaapi.ARM_vabd               # Vector Absolute Difference
    ARM_vabdl = idaapi.ARM_vabdl              # Vector Absolute Difference Long
    ARM_vabs = idaapi.ARM_vabs               # Vector Absolute
    ARM_vacge = idaapi.ARM_vacge              # Vector Absolute Compare Greater Than or Equal
    ARM_vacgt = idaapi.ARM_vacgt              # Vector Absolute Compare Greater Than
    ARM_vacle = idaapi.ARM_vacle              # Vector Absolute Compare Less Than or Equal
    ARM_vaclt = idaapi.ARM_vaclt              # Vector Absolute Compare Less Than
    ARM_vadd = idaapi.ARM_vadd               # Vector Add
    ARM_vaddhn = idaapi.ARM_vaddhn             # Vector Add and Narrow, returning High Half
    ARM_vaddl = idaapi.ARM_vaddl              # Vector Add Long
    ARM_vaddw = idaapi.ARM_vaddw              # Vector Add Wide
    ARM_vand = idaapi.ARM_vand               # Vector Bitwise AND
    ARM_vbic = idaapi.ARM_vbic               # Vector Bitwise Bit Clear
    ARM_vbif = idaapi.ARM_vbif               # Vector Bitwise Insert if False
    ARM_vbit = idaapi.ARM_vbit               # Vector Bitwise Insert if True
    ARM_vbsl = idaapi.ARM_vbsl               # Vector Bitwise Select
    ARM_vceq = idaapi.ARM_vceq               # Vector Compare Equal
    ARM_vcge = idaapi.ARM_vcge               # Vector Compare Greater Than or Equal
    ARM_vcgt = idaapi.ARM_vcgt               # Vector Compare Greater Than
    ARM_vcle = idaapi.ARM_vcle               # Vector Compare Less Than or Equal
    ARM_vcls = idaapi.ARM_vcls               # Vector Count Leading Sign Bits
    ARM_vclt = idaapi.ARM_vclt               # Vector Compare Less Than
    ARM_vclz = idaapi.ARM_vclz               # Vector Count Leading Zeros
    ARM_vcmp = idaapi.ARM_vcmp               # Vector Compare
    ARM_vcmpe = idaapi.ARM_vcmpe              # Vector Compare (Quiet NaNs trigger Exception)
    ARM_vcnt = idaapi.ARM_vcnt               # Vector Count Number of Bits
    ARM_vcvt = idaapi.ARM_vcvt               # Vector Convert
    ARM_vcvtr = idaapi.ARM_vcvtr              # Vector Convert Rounding
    ARM_vcvtb = idaapi.ARM_vcvtb              # Vector Convert Half-Precision Bottom
    ARM_vcvtt = idaapi.ARM_vcvtt              # Vector Convert Half-Precision Top
    ARM_vdiv = idaapi.ARM_vdiv               # Vector Divide
    ARM_vdup = idaapi.ARM_vdup               # Vector Duplicate
    ARM_veor = idaapi.ARM_veor               # Vector Bitwise Exclusive OR
    ARM_vext = idaapi.ARM_vext               # Vector Extract
    ARM_vfma = idaapi.ARM_vfma               # Vector Fused Multiply Accumulate
    ARM_vfms = idaapi.ARM_vfms               # Vector Fused Multiply Substract
    ARM_vfnma = idaapi.ARM_vfnma              # Vector Fused Negated Multiply Accumulate
    ARM_vfnms = idaapi.ARM_vfnms              # Vector Fused Negated Multiply Substract
    ARM_vhadd = idaapi.ARM_vhadd              # Vector Halving Add
    ARM_vhsub = idaapi.ARM_vhsub              # Vector Halving Sub
    ARM_vld1 = idaapi.ARM_vld1               # Vector Load Single Element
    ARM_vld2 = idaapi.ARM_vld2               # Vector Load Two-Element Structures
    ARM_vld3 = idaapi.ARM_vld3               # Vector Load Three-Element Structures
    ARM_vld4 = idaapi.ARM_vld4               # Vector Load Four-Element Structures
    ARM_vldm = idaapi.ARM_vldm               # Vector Load Multiple
    ARM_vldr = idaapi.ARM_vldr               # Vector Load Register
    ARM_vmax = idaapi.ARM_vmax               # Vector Maximum
    ARM_vmin = idaapi.ARM_vmin               # Vector Minimum
    ARM_vmla = idaapi.ARM_vmla               # Vector Multiply Accumulate
    ARM_vmlal = idaapi.ARM_vmlal              # Vector Multiply Accumulate Long
    ARM_vmls = idaapi.ARM_vmls               # Vector Multiply Subtract
    ARM_vmlsl = idaapi.ARM_vmlsl              # Vector Multiply Subtract Long
    ARM_vmov = idaapi.ARM_vmov               # Vector Move
    ARM_vmovl = idaapi.ARM_vmovl              # Vector Move Long
    ARM_vmovn = idaapi.ARM_vmovn              # Vector Move and Narrow
    ARM_vmrs = idaapi.ARM_vmrs               # Move FPSCR to ARM = idaapi.ARM Register
    ARM_vmsr = idaapi.ARM_vmsr               # Move to FPSCR from ARM = idaapi.ARM Register 
    ARM_vmul = idaapi.ARM_vmul               # Vector Multiply
    ARM_vmull = idaapi.ARM_vmull              # Vector Multiply Long
    ARM_vmvn = idaapi.ARM_vmvn               # Vector Bitwise NOT
    ARM_vneg = idaapi.ARM_vneg               # Vector Negate
    ARM_vnmla = idaapi.ARM_vnmla              # Vector Multiply Add Negated
    ARM_vnmls = idaapi.ARM_vnmls              # Vector Multiply Substract Negated
    ARM_vnmul = idaapi.ARM_vnmul              # Vector Multiply Negated
    ARM_vorn = idaapi.ARM_vorn               # Vector Bitwise OR NOT
    ARM_vorr = idaapi.ARM_vorr               # Vector Bitwise OR
    ARM_vpadal = idaapi.ARM_vpadal             # Vector Pairwise Add and Accumulate Long
    ARM_vpadd = idaapi.ARM_vpadd              # Vector Pairwise Add
    ARM_vpaddl = idaapi.ARM_vpaddl             # Vector Pairwise Add Long
    ARM_vpmax = idaapi.ARM_vpmax              # Vector Pairwise Maximum
    ARM_vpmin = idaapi.ARM_vpmin              # Vector Pairwise Minimum
    ARM_vpop = idaapi.ARM_vpop               # Vector Pop
    ARM_vpush = idaapi.ARM_vpush              # Vector Push
    ARM_vqabs = idaapi.ARM_vqabs              # Vector Saturating Absolute
    ARM_vqadd = idaapi.ARM_vqadd              # Vector Saturating Add
    ARM_vqdmlal = idaapi.ARM_vqdmlal            # Vector Saturating Doubling Multiply Accumulate Long
    ARM_vqdmlsl = idaapi.ARM_vqdmlsl            # Vector Saturating Doubling Multiply Subtract Long
    ARM_vqdmulh = idaapi.ARM_vqdmulh            # Vector Saturating Doubling Multiply Returning High Half
    ARM_vqdmull = idaapi.ARM_vqdmull            # Vector Saturating Doubling Multiply Long
    ARM_vqmovn = idaapi.ARM_vqmovn             # Vector Saturating Move and Narrow
    ARM_vqmovun = idaapi.ARM_vqmovun            # Vector Saturating Move and Narrow, Unsigned result
    ARM_vqneg = idaapi.ARM_vqneg              # Vector Saturating Negate
    ARM_vqrdmulh = idaapi.ARM_vqrdmulh           # Vector Saturating Rounding Doubling Multiply Returning High Half
    ARM_vqrshl = idaapi.ARM_vqrshl             # Vector Saturating Rounding Shift Left
    ARM_vqrshrn = idaapi.ARM_vqrshrn            # Vector Saturating Rounding Shift Right, Narrow
    ARM_vqrshrun = idaapi.ARM_vqrshrun           # Vector Saturating Rounding Shift Right, Narrow, Unsigned result
    ARM_vqshl = idaapi.ARM_vqshl              # Vector Saturating Shift Left
    ARM_vqshlu = idaapi.ARM_vqshlu             # Vector Saturating Shift Left, Unsigned result
    ARM_vqshrn = idaapi.ARM_vqshrn             # Vector Saturating Shift Right, Narrow
    ARM_vqshrun = idaapi.ARM_vqshrun            # Vector Saturating Shift Right, Narrow, Unsigned result
    ARM_vqsub = idaapi.ARM_vqsub              # Vector Saturating Subtract
    ARM_vraddhn = idaapi.ARM_vraddhn            # Vector Rounding Add and Narrow, returning High Half
    ARM_vrecpe = idaapi.ARM_vrecpe             # Vector Reciprocal Estimate
    ARM_vrecps = idaapi.ARM_vrecps             # Vector Reciprocal Step
    ARM_vrev16 = idaapi.ARM_vrev16             # Vector Reverse in halfwords
    ARM_vrev32 = idaapi.ARM_vrev32             # Vector Reverse in words
    ARM_vrev64 = idaapi.ARM_vrev64             # Vector Reverse in doublewords
    ARM_vrhadd = idaapi.ARM_vrhadd             # Vector Rounding Halving Add
    ARM_vrshl = idaapi.ARM_vrshl              # Vector Rounding Shift Left
    ARM_vrshr = idaapi.ARM_vrshr              # Vector Rounding Shift Right
    ARM_vrshrn = idaapi.ARM_vrshrn             # Vector Rounding Shift Right and Narrow
    ARM_vrsqrte = idaapi.ARM_vrsqrte            # Vector Reciprocal Square Root Estimate
    ARM_vrsqrts = idaapi.ARM_vrsqrts            # Vector Reciprocal Square Root Step
    ARM_vrsra = idaapi.ARM_vrsra              # Vector Rounding Shift Right and Accumulate
    ARM_vrsubhn = idaapi.ARM_vrsubhn            # Vector Rounding Subtract and Narrow, returning High Half
    ARM_vshl = idaapi.ARM_vshl               # Vector Shift Left
    ARM_vshll = idaapi.ARM_vshll              # Vector Shift Left Long
    ARM_vshr = idaapi.ARM_vshr               # Vector Shift Right
    ARM_vshrn = idaapi.ARM_vshrn              # Vector Shift Right Narrow
    ARM_vsli = idaapi.ARM_vsli               # Vector Shift Left and Insert
    ARM_vsqrt = idaapi.ARM_vsqrt              # Vector Square Root
    ARM_vsra = idaapi.ARM_vsra               # Vector Shift Right and Accumulate
    ARM_vsri = idaapi.ARM_vsri               # Vector Shift Right and Insert
    ARM_vst1 = idaapi.ARM_vst1               # Vector Store Single Element
    ARM_vst2 = idaapi.ARM_vst2               # Vector Store Two-Element Structures
    ARM_vst3 = idaapi.ARM_vst3               # Vector Store Three-Element Structures
    ARM_vst4 = idaapi.ARM_vst4               # Vector Store Four-Element Structures
    ARM_vstm = idaapi.ARM_vstm               # Vector Store Multiple
    ARM_vstr = idaapi.ARM_vstr               # Vector Store Register
    ARM_vsub = idaapi.ARM_vsub               # Vector Subtract
    ARM_vsubhn = idaapi.ARM_vsubhn             # Vector Subtract and Narrow, returning High Half
    ARM_vsubl = idaapi.ARM_vsubl              # Vector Subtract Long
    ARM_vsubw = idaapi.ARM_vsubw              # Vector Subtract Wide
    ARM_vswp = idaapi.ARM_vswp               # Vector Swap
    ARM_vtbl = idaapi.ARM_vtbl               # Vector Table Lookup
    ARM_vtbx = idaapi.ARM_vtbx               # Vector Table Extension
    ARM_vtrn = idaapi.ARM_vtrn               # Vector Transpose
    ARM_vtst = idaapi.ARM_vtst               # Vector Test Bits
    ARM_vuzp = idaapi.ARM_vuzp               # Vector Unzip
    ARM_vzip = idaapi.ARM_vzip               # Vector Zip


    R0    = 0
    R1    = 1
    R2    = 2
    R3    = 3
    R4    = 4
    R5    = 5
    R6    = 6
    R7    = 7
    R8    = 8
    R9    = 9
    R10   = 10
    R11   = 11
    R12   = 12
    SP    = 13
    LR    = 14
    PC    = 15
    CPSR  = 16
    CPSR_FLG = 17
    SPSR  = 18
    SPSR_FLG = 19
    T     = 20
    CS    = 21
    DS    = 22
    ACC0  = 23
    FPSID = 24
    FPSCR = 25
    FPEXC = 26
    FPINST = 27
    FPINST2 = 28
    MVFR0 = 29
    MVFR1 = 30
    APSR  = 31
    IAPSR = 32
    EAPSR = 33
    XPSR  = 34
    IPSR  = 35
    EPSR  = 36
    IEPSR = 37
    MSP   = 38
    PSP   = 39
    PRIMASK = 40
    BASEPRI = 41
    BASEPRI_MAX = 42
    FAULTMASK = 43
    CONTROL = 44
    Q0    = 45
    Q1    = 46
    Q2    = 47
    Q3    = 48
    Q4    = 49
    Q5    = 50
    Q6    = 51
    Q7    = 52
    Q8    = 53
    Q9    = 54
    Q10   = 55
    Q11   = 56
    Q12   = 57
    Q13   = 58
    Q14   = 59
    Q15   = 60
    D0    = 61
    D1    = 62
    D2    = 63
    D3    = 64
    D4    = 65
    D5    = 66
    D6    = 67
    D7    = 68
    D8    = 69
    D9    = 70
    D10   = 71
    D11   = 72
    D12   = 73
    D13   = 74
    D14   = 75
    D15   = 76
    D16   = 77
    D17   = 78
    D18   = 79
    D19   = 80
    D20   = 81
    D21   = 82
    D22   = 83
    D23   = 84
    D24   = 85
    D25   = 86
    D26   = 87
    D27   = 88
    D28   = 89
    D29   = 90
    D30   = 91
    D31   = 92
    S0    = 93
    S1    = 94
    S2    = 95
    S3    = 96
    S4    = 97
    S5    = 98
    S6    = 99
    S7    = 100
    S8    = 101
    S9    = 102
    S10   = 103
    S11   = 104
    S12   = 105
    S13   = 106
    S14   = 107
    S15   = 108
    S16   = 109
    S17   = 110
    S18   = 111
    S19   = 112
    S20   = 113
    S21   = 114
    S22   = 115
    S23   = 116
    S24   = 117
    S25   = 118
    S26   = 119
    S27   = 120
    S28   = 121
    S29   = 122
    S30   = 123
    S31   = 124
    CF    = 125
    ZF    = 126
    NF    = 127
    VF    = 128
    X0    = 129
    X1    = 130
    X2    = 131
    X3    = 132
    X4    = 133
    X5    = 134
    X6    = 135
    X7    = 136
    X8    = 137
    X9    = 138
    X10   = 139
    X11   = 140
    X12   = 141
    X13   = 142
    X14   = 143
    X15   = 144
    X16   = 145
    X17   = 146
    X18   = 147
    X19   = 148
    X20   = 149
    X21   = 150
    X22   = 151
    X23   = 152
    X24   = 153
    X25   = 154
    X26   = 155
    X27   = 156
    X28   = 157
    X29   = 158
    X30   = 159
    XZR   = 160
    SP    = 161
    PC    = 162
    V0    = 163
    V1    = 164
    V2    = 165
    V3    = 166
    V4    = 167
    V5    = 168
    V6    = 169
    V7    = 170
    V8    = 171
    V9    = 172
    V10   = 173
    V11   = 174
    V12   = 175
    V13   = 176
    V14   = 177
    V15   = 178
    V16   = 179
    V17   = 180
    V18   = 181
    V19   = 182
    V20   = 183
    V21   = 184
    V22   = 185
    V23   = 186
    V24   = 187
    V25   = 188
    V26   = 189
    V27   = 190
    V28   = 191
    V29   = 192
    V30   = 193
    V31   = 194

    TOTAL_GPR = 195

    GPR_NAMES = {
        R0    : "R0",
        R1    : "R1",
        R2    : "R2",
        R3    : "R3",
        R4    : "R4",
        R5    : "R5",
        R6    : "R6",
        R7    : "R7",
        R8    : "R8",
        R9    : "R9",
        R10   : "R10",
        R11   : "R11",
        R12   : "R12",
        SP    : "SP",
        LR    : "LR",
        PC    : "PC",
        CPSR  : "CPSR",
        CPSR_FLG : "CPSR_flg",
        SPSR  : "SPSR",
        SPSR_FLG : "SPSR_flg",
        T     : "T",
        CS    : "CS",
        DS    : "DS",
        ACC0  : "acc0",
        FPSID : "FPSID",
        FPSCR : "FPSCR",
        FPEXC : "FPEXC",
        FPINST : "FPINST",
        FPINST2 : "FPINST2",
        MVFR0 : "MVFR0",
        MVFR1 : "MVFR1",
        APSR  : "APSR",
        IAPSR : "IAPSR",
        EAPSR : "EAPSR",
        XPSR  : "XPSR",
        IPSR  : "IPSR",
        EPSR  : "EPSR",
        IEPSR : "IEPSR",
        MSP   : "MSP",
        PSP   : "PSP",
        PRIMASK : "PRIMASK",
        BASEPRI : "BASEPRI",
        BASEPRI_MAX : "BASEPRI_MAX",
        FAULTMASK : "FAULTMASK",
        CONTROL : "CONTROL",
        Q0    : "Q0",
        Q1    : "Q1",
        Q2    : "Q2",
        Q3    : "Q3",
        Q4    : "Q4",
        Q5    : "Q5",
        Q6    : "Q6",
        Q7    : "Q7",
        Q8    : "Q8",
        Q9    : "Q9",
        Q10   : "Q10",
        Q11   : "Q11",
        Q12   : "Q12",
        Q13   : "Q13",
        Q14   : "Q14",
        Q15   : "Q15",
        D0    : "D0",
        D1    : "D1",
        D2    : "D2",
        D3    : "D3",
        D4    : "D4",
        D5    : "D5",
        D6    : "D6",
        D7    : "D7",
        D8    : "D8",
        D9    : "D9",
        D10   : "D10",
        D11   : "D11",
        D12   : "D12",
        D13   : "D13",
        D14   : "D14",
        D15   : "D15",
        D16   : "D16",
        D17   : "D17",
        D18   : "D18",
        D19   : "D19",
        D20   : "D20",
        D21   : "D21",
        D22   : "D22",
        D23   : "D23",
        D24   : "D24",
        D25   : "D25",
        D26   : "D26",
        D27   : "D27",
        D28   : "D28",
        D29   : "D29",
        D30   : "D30",
        D31   : "D31",
        S0    : "S0",
        S1    : "S1",
        S2    : "S2",
        S3    : "S3",
        S4    : "S4",
        S5    : "S5",
        S6    : "S6",
        S7    : "S7",
        S8    : "S8",
        S9    : "S9",
        S10   : "S10",
        S11   : "S11",
        S12   : "S12",
        S13   : "S13",
        S14   : "S14",
        S15   : "S15",
        S16   : "S16",
        S17   : "S17",
        S18   : "S18",
        S19   : "S19",
        S20   : "S20",
        S21   : "S21",
        S22   : "S22",
        S23   : "S23",
        S24   : "S24",
        S25   : "S25",
        S26   : "S26",
        S27   : "S27",
        S28   : "S28",
        S29   : "S29",
        S30   : "S30",
        S31   : "S31",
        CF    : "CF",
        ZF    : "ZF",
        NF    : "NF",
        VF    : "VF",
        X0    : "X0",
        X1    : "X1",
        X2    : "X2",
        X3    : "X3",
        X4    : "X4",
        X5    : "X5",
        X6    : "X6",
        X7    : "X7",
        X8    : "X8",
        X9    : "X9",
        X10   : "X10",
        X11   : "X11",
        X12   : "X12",
        X13   : "X13",
        X14   : "X14",
        X15   : "X15",
        X16   : "X16",
        X17   : "X17",
        X18   : "X18",
        X19   : "X19",
        X20   : "X20",
        X21   : "X21",
        X22   : "X22",
        X23   : "X23",
        X24   : "X24",
        X25   : "X25",
        X26   : "X26",
        X27   : "X27",
        X28   : "X28",
        X29   : "X29",
        X30   : "X30",
        XZR   : "XZR",
        SP    : "SP",
        PC    : "PC",
        V0    : "V0",
        V1    : "V1",
        V2    : "V2",
        V3    : "V3",
        V4    : "V4",
        V5    : "V5",
        V6    : "V6",
        V7    : "V7",
        V8    : "V8",
        V9    : "V9",
        V10   : "V10",
        V11   : "V11",
        V12   : "V12",
        V13   : "V13",
        V14   : "V14",
        V15   : "V15",
        V16   : "V16",
        V17   : "V17",
        V18   : "V18",
        V19   : "V19",
        V20   : "V20",
        V21   : "V21",
        V22   : "V22",
        V23   : "V23",
        V24   : "V24",
        V25   : "V25",
        V26   : "V26",
        V27   : "V27",
        V28   : "V28",
        V29   : "V29",
        V30   : "V30",
        V31   : "V31",

    }

    # Taken from idc.py

    #
    # Special purpose registers in ARM
    #
    REGLIST  =     idaapi.o_idpspec1      # Register list (for LDM/STM)
    CREGLIST  =    idaapi.o_idpspec2      # Coprocessor register list (for CDP)
    CREG  =        idaapi.o_idpspec3      # Coprocessor register (for LDC/STC)
    FPREG_ARM  =   idaapi.o_idpspec4      # Floating point register
    FPREGLIST  =   idaapi.o_idpspec5      # Floating point register list
    TEXT  =        (idaapi.o_idpspec5+1)  # Arbitrary text stored in the operand

    SPR_NAMES = {
        REGLIST  :     "REGLIST",
        CREGLIST  :    "CREGLIST",
        CREG  :        "CREG",
        FPREG_ARM  :   "FPREG_ARM",
        FPREGLIST  :   "FPREGLIST",
        TEXT  :        "TEXT",
    }

    ARGUMENT_REGISTERS = []

    RETURN_REGISTERS = []

    VOLATILE_REGISTERS = ARGUMENT_REGISTERS + RETURN_REGISTERS + [
    ]

    #
    #  Helper methods
    #

    def is_branch(self, inst_type):
        """Indicate if the specified instruction is some kind of branch
        instruction.

        """
        return inst_type in CONDITIONAL_BRANCH_TYPES or \
            inst_type in UNCONDITIONAL_BRANCH_TYPES


ASSIGNMENT_TYPES = [
]

UNCONDITIONAL_BRANCH_TYPES = [
]

CONDITIONAL_BRANCH_TYPES = [
]

UNIMPLEMENTED_TYPES = [
]
