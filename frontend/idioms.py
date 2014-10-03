# 
# Copyright (c) 2013 Sebastian Muniz
# 
# This code is part of point source decompiler
#


class IdiomAnalyzerException(Exception):
    pass


class IdiomAnalyzer(object):
    """Base class to facilitate idioms analysis."""

    def __init__(self, debugger, lir_function, mir_module, mir_function,
        symbol_tables):
        """Initialize idiom analyzer base class."""
        self.debugger = debugger
        self.lir_function = lir_function  # Function low-level representation
        self.mir_module = mir_module    # Current module's IR
        self.mir_function = mir_function

        self.nv_regs = list()        # Non-volatile registers list
        self.param_regs = dict()        # Regsiters used as functions parameters
        self.ret_to_caller = False
        self.stack_size = 0
        self.stack_restore = "Unknown"

        self.compiler_type = self.debugger.COMPILER_UNK

        # Current architectures instruction set to work with.
        self.iset = self.debugger.instruction_set

        # Store the current MIR function in the symbol tables dict and keep a
        # reference as the current one being used for further analysis.
        self.symbol_tables = symbol_tables
        self.current_symbol_table = self.symbol_tables[mir_function]

        self.return_registers = list()

    @property
    def symbol_tables(self):
        """Get a reference to all the symbol tables analyzed."""
        return self._symbol_tables

    @symbol_tables.setter
    def symbol_tables(self, _symbol_tables):
        """Store a reference to all the symbol tables analyzed."""
        self._symbol_tables = _symbol_tables

    @property
    def current_symbol_table(self):
        """Get a reference to the current the symbol table being analyzed."""
        return self._current_symbol_table

    @current_symbol_table.setter
    def current_symbol_table(self, _symbol_table):
        """Store a reference to all the symbol tables analyzed."""
        self._current_symbol_table = _symbol_table

    def get_signed_value(self, value):
        """..."""
        return (value + 2**31) % 2**32 - 2**31 # WTF?

    def perform_phase1_analysis(self):
        """Execute the basic idiom analysis on current function previous to MIR
        generation.

        """
        # Perform a series of analysis which will try locate regular
        # instructions inserted by the compilerer and/or the optimizer.
        #
        # Along the execution of these steps, we'll start recovering
        # information about the compiled code which will facilitate the
        # reconstruction of the source code.
        #
        # To do that, we'll process the assembly instructions and it's
        # references and store them in a high-level intermediate
        # representation to easy further analysis and final reconstruction.
        #
        self.__raise(self.perform_phase1_analysis)

    def perform_phase2_analysis(self):
        """Execute the basic idiom analysis on current function after to MIR
        generation procedure.

        """
        self.__raise(self.perform_phase2_analysis)

    def detect_prologue(self):
        """Check wheater the function prologue is present or not."""
        self.__raise(self.detect_prologue)

    def detect_epilogue(self):
        """Check wheater the function epilogue is present or not."""
        self.__raise(self.detect_epilogue)

    def detect_calling_convention(self):
        """Obtain the calling convention detected by the compiler."""
        self.__raise(self.detect_calling_convention)

    def detect_unoptimized_code_sequences(self):
        """When the source code is compiled without any optimization flag
        enabled, the code generated by the compiler might contain redundant
        instructions which were not changed/removed by the optimizer.

        The porpuse of this method is to locate such instructions sequence and
        handle them appropriately.

        """
        self.__raise(self.detect_unoptimized_code_sequences)

    def get_string_by_address(self, address, is_unicode_string=False):
        """Return the string pointer by the specified address."""

        if is_unicode_string:
            # TODO: fixme
            #is_unicode(int(address))
            string = self.debugger.get_string(
                address, None, self.debugger.STRING_TYPE_UNICODE)
        else:
            string = self.debugger.get_string(address)

        if string is not None:
            return string
        else:
            return None

    def mark_instruction_analyzed(self, lir_inst, analyzed=True, remove=True):
        """Given a LIR instruction, mark it as 'analyzed' and optionally remove
        the statement representing that instruction.

        This is done because idioms are a set of architecture specific
        instructions that can be more easily represented by certain MIR
        statements than the ones that individually represente each LIR
        instruction.

        """
        lir_inst.analyzed = analyzed

        # TODO / FIXME
        #if remove:
        #    pass
            #print "[===] Pending remove MIR at 0x%X" % lir_inst.address
            #self.mir_module.remove_statement_by_address(lir_inst.address)

    def is_compiler_unknown(self):
        """Return a boolean indicating if the compiler used to generate the
        current binary code is unknown or not.

        """
        return self.compiler_type == self.debugger.COMPILER_UNK

    def detect_compiler(self):
        """Obtain the name and type of the compiler used to generate the code
        being analyzed.

        In case the compiler is unknown to the debugger, try to guess it.

        """
        # Let the debugger try first and check if the compiler was successfully
        # detected.
        self.compiler_type = self.debugger.get_default_compiler()

        if self.is_compiler_unknown():
            # Try to guess the compiler
            if not self.guess_compiler_type():
                print "Unsupported %s compiler" % \
                    self.debugger.get_compiler_name(self.compiler_type)
                return False

        print "    Compiler detected: %s" % \
            self.debugger.get_compiler_name(self.compiler_type)

        return True

    @property
    def compiler_type(self):
        """Return the compiler type."""
        return self.compiler

    @compiler_type.setter
    def compiler_type(self, comp):
        """Store the compiler type."""
        self.compiler = comp

    def guess_compiler_type(self):
        """Determine the compiler for the current binary."""
        self.__raise(self.guess_compiler_type)

    def __raise(self, method):
        classname  = self.__class__.__name__
        methodname = method.__name__
        message    = "Method %s in class %s was not implemented."
        raise IdiomAnalyzerException(message % (methodname, classname))
