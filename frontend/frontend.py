# 
# Copyright (c) 2014 Sebastian Muniz
# 
# This code is part of point source decompiler
#
import abc
from traceback import format_exc

import actionplan
reload(actionplan)
from actionplan import Action, ActionPlan, ActionPlanException

from idioms import IdiomAnalyzerException

from misc.prerequisites import require

#reload(output_media.graph_output_media)
require("output_media.graph_output_media.graph_output_media")
from output_media.graph_output_media.graph_output_media import \
    BasicBlockGraphOutput, BasicBlockGraphOutputException

##reload(frontend.generic_disasm.base)
#require("frontend.generic_disasm.base")
#from frontend.generic_disasm.base import BaseDebuggerException

#reload(frontend.idioms_factory)
require("frontend.idioms_factory")
from idioms_factory import IdiomsFactory, IdiomsFactoryException

#
# ############################# Middle-End ####################################
#

#reload(middleend.mir_exception)
require("middleend.mir_exception")
from middleend.mir_exception import MiddleIrException

#reload(middleend.mir.mir_module)
require("middleend.mir.mir_module")
from middleend.mir.mir_module import MiddleIrModule, MiddleIrModuleException

#reload(middleend.mir.mir_basicblock)
require("middleend.mir.mir_basicblock")
from middleend.mir.mir_basicblock import MiddleIrBasicBlock

#reload(middleend.mir.mir_instruction)
require("middleend.mir.mir_instruction")
from middleend.mir.mir_instruction import MiddleIrInstructionBuilder, \
                                            MiddleIrInstruction

#reload(middleend.mir.mir_function)
require("middleend.mir.mir_function")
from middleend.mir.mir_function import *

#reload(middleend.mir.mir_constants)
#require("middleend.mir.mir_constants")
from middleend.mir.mir_constants import MiddleIrBaseConstant

#reload(middleend.mir.mir_global_variable)
#require("middleend.mir.mir_global_variable")
from middleend.mir.mir_global_variable import MiddleIrGlobalVariable

#import middleend.mir.mir_type
#reload(middleend.mir.mir_type)
#require("middleend.mir.mir_type")
from middleend.mir.mir_type import *

__all__ = ["FrontEnd", "FrontEndException"]


class FrontEndException(Exception):
    """Front-end base exception class."""
    pass


class FrontEnd(object):
    """
    Base class for different Front-Ends to support multiple decompilable
    architectures.

    All the generic operations related to the front-end will be performed by
    the FrontEnd class leaving architecture specific operations to the derived
    class.

    """
    __metaclass__ = abc.ABCMeta

    def __init__(self, debugger):
        """Perform base front-end instance initialization."""
        # Debug flag for verbose output (useful during development).
        self.debug = True

        self.action_plan = ActionPlan()

        # Current debugger application
        self.debugger = debugger

        # Storage for all the different types of low level groups of
        # operations for current architecture.
        self.unimplemented_types = debugger.unimplemented_types
        self.conditional_branch_types = debugger.conditional_branch_types
        self.unconditional_branch_types = debugger.unconditional_branch_types
        self.assignment_types = debugger.assignment_types

        # Low-level IR of the current function being decompiled. This is an
        # abstraction from the debugger structures to represent the
        # disassembled code.
        self.lir_function = None

        # Store the MIR function being decompiled.
        self.mir_function = None

        # Create a Middle level intermediate representation of the current
        # module that posses the function being decompiled if it wasn't already
        # created and associate a function IR to it.
        #
        # This will return always the same module in case we specify the same
        # filename on the input file.
        #
        self.mir_module = MiddleIrModule.new(self.debugger.get_input_file())

        # Setup symbol table for local/global variables references, etc..
        self.symbols_manager = None

        # Development flags
        self.debug_inst_info = True

        # Current architectures instruction set to work with.
        self.iset = self.debugger.instruction_set

        # This dictionary contains all the LIR function analyzed during this
        # run to avoid wasting resources by analyzing the same function twice.
        self.lir_functions_cache = dict()

        # And last but not least set the module in charge of idiom analysis.
        # Invoke the appropriate idiom analyzer for the current architecture
        # based on the detected compiler.
        #
        if not self.detect_compiler():
            raise FrontEndException(
                "Unable to detect current compiler to initialize idiom analyzer.")

        compiler_name = self.debugger.get_compiler_name(self.compiler)
        compiler_name = "GCC"
        print "    Compiler detected: %s" % compiler_name

        # Now if the current compiler was detected then we instantiate the
        # specific idiom analyzer for it.
        try:
            arch_name = self.debugger.architecture_name
            self.idiom_analyzer = IdiomsFactory.build(
                (compiler_name, arch_name), (self.debugger, ))

        except IdiomsFactoryException, err :
            raise FrontEndException(
                "Unable to detect architecture (%(arch_name)s) : %(err)s" % \
                vars())

    def detect_compiler(self):
        """Obtain the name and type of the compiler used to generate the code
        being analyzed.

        In case the compiler is unknown to the debugger, try to guess it.

        """
        print "Detecting compiler..."

        # Let the debugger try first and check if the compiler was successfully
        # detected.
        self.compiler = self.debugger.get_default_compiler()

        if not self.is_compiler_unknown:
            return True

        # Try to guess the compiler when the debugger cannot provide such
        # information.
        return self.guess_compiler_type()

    @property
    def is_compiler_gcc(self):
        """Indicate if the compiler used to generate the current binary code is
        GCC or not.

        """
        return self.compiler == self.debugger.COMPILER_GNU

    @property
    def is_compiler_unknown(self):
        """Indicate if the compiler used to generate the current binary code is
        unknown or not.

        """
        return self.compiler == self.debugger.COMPILER_UNK

    def guess_compiler_type(self):
        """Try to determine the compiler."""
        # TODO / FIXME: Improve this "analysis".
        print "    Guessing compiler...",

        if self.lir_function.stack_restore in ["IOS", "Linux"]:
            self.compiler = self.debugger.COMPILER_GNU
            return True

        return False

    @property
    def compiler(self):
        """Return the compiler type."""
        return self._compiler

    @compiler.setter
    def compiler(self, compiler):
        """Store the compiler type."""
        self._compiler = compiler

    @property
    def architecture_name(self):
        """Return the name of the current architecture.""" 
        return self.TARGET_ARCH

    @property
    def name(self):
        """Return the formatted name of the current front-end."""
        return "FrontEnd%s" % self.TARGET_ARCH

    @property
    def symbols_manager(self):
        """Return the symbols manager instance for the current application."""
        return self._symbols_manager

    @symbols_manager.setter
    def symbols_manager(self, symbols_manager):
        """Store the symbols manager instance for the current application."""
        self._symbols_manager = symbols_manager

    @property
    def debugger(self):
        """Return the debugger instance for the current application."""
        return self._debugger

    @debugger.setter
    def debugger(self, debugger):
        """Store the debugger instance for the current application."""
        self._debugger = debugger

    def generate_mir_skeleton(self):
        """
        Create the basic MIR structure (function with its basic blocks) in
        order to facilitate the first phase of the idioms analysis.

        Further analysis should discard idioms and as a result a more compact
        and accurate IR will be obtained to feed the decompiler final phase
        known as the Back-end.

        """
        #
        # Initialize internal MIR members for further usage.
        #
        if self.lir_function.return_type == 0:
            return_type = MiddleIrTypeVoid()
        elif self.lir_function.return_type == 1:
            return_type = MiddleIrTypeInt()
        else:
            raise FrontEndException("Unknown return type (%r)" % \
                self.lir_function.return_type)

        self.mir_function = MiddleIrFunction.get(self.mir_module, self.lir_function.name)

        # Delete the previously created function and create a new one. This
        # is what the user requested so do it (definition might have
        # changed, etc.).
        if self.mir_function is not None:
            if self.mir_function in self.symbols_manager:
                del self.symbols_manager[self.mir_function.name]
            self.mir_function.delete()

        # Seems like the function doesn't already exists in our store so
        # we'll create a new one.
        param_regs = list()
        address = self.lir_function.start_address

        for idx, (param_reg, mir_param) in self.lir_function.param_regs.iteritems():
            #print "------- Argument %02d : %s <-> %s" % (
            #    idx, self.iset.GPR_NAMES[param_reg],
            #    mir_param)
            param_regs.append(
                self.current_symbols_table.parameters[idx].item
                )

        self.mir_function = MiddleIrFunction.new(
            self.mir_module, self.lir_function.name, return_type, param_regs)

        for idx, (param_reg, mir_param) in self.lir_function.param_regs.iteritems():
            print "|==> Name : ", self.mir_function.arguments[idx].name,
            self.mir_function.arguments[idx].name = "i_arg%d" % idx
        print ""

        # Set the default calling convention.
        #self.mir_function.set_calling_convention(CALL_CONV_C)

        self.mir_inst_builder = None

        # Just create a function prototype for an external function so the rest
        # of the MIR code can invoke it without having to function body.
        if self.lir_function.is_extern:
            return

        #
        # Iterate through LIR to transform it into its MIR representation (this
        # is a first pass, so just the basic skeleton will be created and
        # further passes will create the rest).
        #
        for lir_basic_block in self.lir_function:

            # Create the MIR basic block instance and add a label to it
            # using an existing one (if any) or creating a new one.
            mir_basic_block = MiddleIrBasicBlock()

            # Get the name of the local label only if the address doesn't
            # belong to the first instruction (in this case IDA returns
            # the name of the function and we don't want this.).

            if lir_basic_block == self.lir_function[0]:
                label = "entry"  # LLVM convention

            else:
                label = self.debugger.get_address_label(
                    lir_basic_block.start_address)

                if not label:
                    # TODO: Will not work on functions with multiple ending
                    # basic blocks.
                    if lir_basic_block != self.lir_function[-1]:

                        # We try to obtain the name as it's already visible because
                        # the user might have changed it.
                        # It could happen that some locations do not have a local
                        # label because it's via a direct flow that the location is
                        # reached so we create a label name similar to the ones
                        # produced by IDA and use it instead.
                        #label = "loc_%X" % lir_basic_block.start_address
                        label = "loc_%X" % lir_basic_block[0].address

                    else:
                        label = "return"
                        #label = "ret_loc_%X" % lir_basic_block.start_address

            #
            # Setup additional basic block information and finally store the
            # filled block in the current function instance.
            #
            self.mir_function.add_basic_block(mir_basic_block)

            mir_basic_block.label = label

            mir_basic_block.instruction_builder = \
                MiddleIrInstructionBuilder(mir_basic_block)

            # TODO/FIXME: This is a horrible kludge!
            #
            # We set this here because the phase 0/1 idiom analysis need to
            # know basic block boundaries in order to obtain the instruction
            # builder for specific instruction addresses.
            #
            # Normally the basic block boundaries should be set according to
            # its instruction addresses.
            mir_basic_block.start_address = lir_basic_block.start_address
            mir_basic_block.end_address = lir_basic_block.end_address

    def populate_mir(self):
        """Convert all the function's instructions represented by the LIR to a
        higher IR called MIR (Middle-end Intermediate Representation) as an
        initial step.

        """
        # Propagate addresses by adding each prologue and epilogue address to
        # the list of addresses in the MIR function in order to keep track of
        # assembly->MIR addresses during translation.
        print "[+] Propagating LIR-to-MIR prologue and epilogue addresses."

        for address in self.lir_function.prologue_addresses:
            self.mir_function.add_prologue_address(address)

        self.mir_function.add_address(self.lir_function.start_address)

        for address in self.lir_function.epilogue_addresses:
            self.mir_function.add_epilogue_address(address)

        self.mir_function.add_address(self.lir_function.start_address)

        #
        # Initiate instruction translation phase.
        #
        for lir_basic_block_index, lir_basic_block in enumerate(self.lir_function):

            address = lir_basic_block.start_address

            self.mir_inst_builder = \
                self.mir_function.get_instruction_builder_by_address(
                    address, False)

            mir_basic_block = self.mir_function[lir_basic_block_index]

            for lir_inst_idx, lir_inst in enumerate(lir_basic_block):
                # Avoid already detected instructions in idioms and other
                # analysis.
                if lir_inst.analyzed:
                    #print "---> inst %d at 0x%X was already analyzed..." \
                    #    "skipping" % (lir_inst_idx, lir_inst.address)
                    continue
                else:
                    pass
                    #print "---> inst %d at 0x%X being analyzed." % (
                    #    lir_inst_idx, lir_inst.address)

                #
                # This step is very important. This is where most of the LIR 
                # instruction are translated to its MIR equivalents for
                # further usage.
                #
                try:
                    mir_inst = self.transform_to_mir_instruction(lir_inst)
                except FrontEndException, err:
                    print format_exc()
                    raise FrontEndException(
                        "Unable to transform LIR instruction at "
                        "0x%08X (%s) : %s" % (
                            lir_inst.address, lir_inst, err))

                if mir_inst:

                    # Set MIR instruction address equal to the LIR instruction
                    # used to get it,
                    # Store the instruction address for debugging purposes.
                    # Some LLVM IR code are not instructions but declarations
                    # or other stuff that doesn't support add_address method.
                    mir_inst.add_address(lir_inst.address)

                    # Now the newly created instruction is stored in a basic
                    # block, whose purpose is to represent a group of
                    # instructions altogether.
                    mir_basic_block.add_instruction(mir_inst)

                    self.__display_instruction_information(
                        lir_inst, lir_inst.group_name)

                    # Copy all graph information from low-level representation to the
                    # intermediate-level language.
                    #self.__propagate_graph_information()
                    #print "Added inst %d" % lir_inst_idx

    def transform_to_mir_instruction(self, lir_inst):
        """Get the corresponding MIR instruction according to the LIR
        instruction.

        This is architecture-specific so the opcodes are grouped by type and
        this is done inside the front-end of every architecture.

        """
        #
        # First we check if the instruction at the current address was
        # previously analyzed and marked for conversion by the idiom analyzer.
        #
        if self.action_plan.has_plan_for_address(lir_inst.address):
            pass

        #
        # Dispatch the current LIR instruction to be appropriate type
        # conversion routine to be transformed into its equivalent MIR
        # instruction(s).
        #
        mir_inst = None
        group = lir_inst.group_name

        try:
            if lir_inst.type in self.assignment_types:
                mir_inst = self.on_assignment(lir_inst)

            elif lir_inst.type in self.unconditional_branch_types:
                mir_inst = self.on_unconditional_branch(lir_inst)

            elif lir_inst.type in self.conditional_branch_types:
                mir_inst = self.on_conditional_branch(lir_inst)

            elif lir_inst.type in self.unimplemented_types:
                #mir_inst = self.on_unknown(lir_inst)
                raise FrontEndException(
                    "Unknown instruction \"%s\" at 0x%08X" % (
                    lir_inst.mnemonic, lir_inst.address))

            else:
                raise FrontEndException(
                    "Unidentified instruction (type %r - group %s) at 0x%08X" % (
                        lir_inst.type, group, lir_inst.address))

        except FrontEndException, err:
            raise FrontEndException(err)

        except Exception, err:
            print format_exc()
            raise FrontEndException(err)

        return mir_inst

    def __propagate_graph_information(self):
        """Propagate control flow graph information from LIR to MIR."""
        #
        # With all the function instructions and basic blocks created, the
        # information from the basic blocks referencing each other is set.
        #
        # This is used for the function graph analysis and other analysis.
        #
        for lir_bb_idx, lir_bb in enumerate(self.lir_function):

            for edge_ea in self.lir_function[lir_bb_idx].get_in_edges():

                # TODO : Clean this mess
                bblock = self.lir_function.get_basic_block_by_address(edge_ea)
                bblock_index = self.lir_function.get_basic_block_index(bblock)

                #block = self.mir_function[bblock_index]

                self.mir_function[lir_bb_idx].add_in_edge(bblock_index)

    def analyze(self, func_address, depth=0):
        """Start the analysis phase by gathering information about all the
        instructions contained inside the function being analyzed and also
        store information about call graph for further operations.

        @func_address : The address of the function to analyze.
        """
        if self.debug:
            print "Current depth is %d" % depth

        try:
            print "-" * 80
            print "[+] Generating Low level IR for function '%s'" % \
                self.debugger.get_function_name(func_address)
            self.lir_function = self.debugger.generate_lir(func_address)

            # Add this function to the cache list for further usage.
            self.lir_functions_cache.setdefault(func_address, self.lir_function)

            print "[+] Found %d basic block(s) on function \'%s\' containing %d " \
                "instruction(s)" % (
                self.lir_function.get_basic_blocks_count(),
                self.lir_function.name,
                self.lir_function.instructions_count)

        except Exception, err:
            print format_exc()
            raise FrontEndException(
                "Unable to generate Low Level IR: %s" % err)

        try:
            # Store the current symbol table to use.
            self.current_symbols_table = \
                self.symbols_manager.symbols(self.lir_function.start_address)

            print "[+] Initializing idioms analyser..."
            self.idiom_analyzer.init(
                self.lir_function, None, self.symbols_manager)

            #
            # Step x
            #
            # Invoke the appropriate idiom analyzer for the current architecture.
            if self.lir_function.is_extern:
                print "[+] Skipping idioms analyzer phase 0 for 0x%X" % \
                    self.lir_function.start_address
            else:
                print "[+] Initiating idioms analysis phase 0..."
                self.idiom_analyzer.perform_phase0_analysis()

            #
            # Step x
            #
            # Initialize internal MIR members for further usage.
            #
            print "[+] Creating Middle level IR skeleton..."
            if self.debug:
                print "Depth %d" % depth
            self.generate_mir_skeleton()

            # Exit at this point if the function body cannot be analyzed or this
            # is the first milestone on the analysis (depth 1)
            if self.lir_function.is_extern or depth == 1:
                print "-" * 80
                return

            #
            # Perform live analysis
            #
            old_total = len(self.lir_functions_cache)
            self.perform_live_variable_analysis(self.lir_function, depth)

            print "[+] Total functions added : %d" % (
                len(self.lir_functions_cache) - old_total)

            #
            # Step x
            #
            # Clean any internal state from previous analysis.
            #
            print "[+] Initializing idioms analyser..."
            #self.idiom_analyzer.mir_function = self.mir_function
            #self.idiom_analyzer.mir_module = self.mir_function.module
            self.idiom_analyzer.init(
                self.lir_function, self.mir_function, self.symbols_manager)

            # Output LIR for debugging purposes.
            self.generate_output(True)

            #
            # Step x
            #
            # Invoke the appropriate idiom analyzer for the current architecture.
            print "[+] Initiating idioms analysis phase 1..."
            self.idiom_analyzer.perform_phase1_analysis()

            #
            # Step x
            #
            # With the middle level IR created proceed to the idioms analysis
            # using the newly created IR and filling it with all the
            # appropriate code representation.
            #
            print "[+] Populating Middle level IR..."
            self.populate_mir()

            #
            # Step x
            #
            # Invoke the appropriate idiom analyzer for the current architecture.
            #
            print "[+] Initiating idioms analysis phase 2..."
            self.idiom_analyzer.perform_phase2_analysis()

            print "[+] Displaying current symbols table:"
            print str(self.current_symbols_table)

        except IdiomAnalyzerException, err:
            print format_exc() + '\n'
            raise FrontEndException("Idioms analysis failed (%s)" % err)

        except MiddleIrException, err:
            print format_exc() + '\n'
            raise FrontEndException("Middle IR error (%s)" % err)

        #
        # Step x
        #
        # Perform a series of verifications in the MIR to make sure all the
        # operations were correctly (this is done internally by LLVM).
        #
        print "[+] Verifying Middle level IR code..."
        self.mir_module.verify()
        print "-" * 80

    def perform_live_variable_analysis(self, lir_function, depth):
        """Perform live analysis on variables based on their usage in called
        functions.

        """
        if depth > 0:
            return
        # Iterate through every instruction present in the function in order to
        # get information about the parameters usage and return values of the
        # called functions.
        for lir_basic_block in lir_function:
            for lir_inst in lir_basic_block:

                callee_address = self._extract_callee_address(lir_inst)
                
                if callee_address is None:
                    # In case that the call instruction didn't use a guessable
                    # address we just move on.
                    continue

                if callee_address in self.lir_functions_cache:
                    continue

                #print "2 Callee address 0x%X" % callee_address, depth # XXX
                # Save the context for further usage.
                cur_lir = self.lir_function 
                cur_mir = self.mir_function
                cur_sym = self.current_symbols_table

                # FIXME This should go
                # Recursively move into callees until we reach the specified level
                # (in case it was specified).
                #print "1 Callee address 0x%X" % callee_address, depth # XXX
                #if depth == 0:
                #    #continue
                #    #pass
                #    depth += 1
                #elif depth > 0:
                #    depth -= 1
                #else:
                #    continue
                #depth += 1
                #if depth > 0:
                #    return
                #else:
                #    depth += 1

                # Analyze the called function in order to obtain parameters and
                # return registers information. This will produce a new LIR
                # function and basic function information because of the
                # execution of phase 0 analysis.
                self.analyze(callee_address, depth+1)

                # Restore the context of the main function being analyzed.
                self.lir_function = cur_lir
                self.mir_function = cur_mir
                self.current_symbols_table = cur_sym

                lir_callee = self.lir_functions_cache.get(callee_address, None)

                if lir_callee:
                    # Analyse the callee function and its callees (if
                    # appropriate according to the depth level).
                    self.perform_live_variable_analysis(lir_callee, depth)
                else:
                    print "[+] Skipping live analysis for callee 0x%X" % \
                        lir_callee.start_address

    #@abc.abstractmethod
    #def analyze_callee(self, callee_address):
    #    """Analyze the callee function by performing a live analysis on it."""
    #    return

    @abc.abstractmethod
    def _extract_callee_address(self, lir_inst):
        """Return the callee address from a call instruction, if any."""
        return

    @property
    def mir(self):
        """Return the intermediate level presentation ofthe current function
        being decompiled.
        
        """
        return self.mir_module

    @mir.setter
    def mir(self, mir_module):
        """Store the intermediate level presentation ofthe current function
        being decompiled.
        
        """
        self.mir_module = mir_module

    def __display_instruction_information(self, lir_inst, lir_group):
        """Print information about the assembler instruction specified which
        belong to the group parameter.

        """
        if self.debug_inst_info:

            address = lir_inst.address
            arch = self.TARGET_ARCH
            group = lir_group.capitalize()
            inst_repr = str(lir_inst)
            inst_numb = lir_inst.type

            print "\t0x%(address)08X - %(arch)s %(group)15s " \
                  "(type %(inst_numb)3d) - %(inst_repr)-25s" % vars()

    def _create_local_variable(self, address, dest_offset, update_symbols_table=True):
        """Create a local variable for further usage."""
        try:
            mir_inst_builder = \
                self.mir_function.get_instruction_builder_by_address(
                    address, False)

            var_type_preffix = "i"
            var_name = "%(var_type_preffix)s_0x%(dest_offset)X" % vars()
            #int_ptr = MiddleIrTypePointer(MiddleIrTypeInt())
            int_ptr = MiddleIrTypeInt()

            mir_var = mir_inst_builder.alloca(
                int_ptr, None, var_name)

            if update_symbols_table:
                #print "---> Adding local variable offset %d (%s) : %s" % \
                #    (address, var_name, mir_var)
                self.current_symbols_table.add_local_variable(
                    dest_offset, var_name, mir_var)

            return mir_var

        except MiddleIrException, err:
            print format_exc() + '\n'
            raise PowerPc32GccIdiomAnalyzerException(err)

    @abc.abstractmethod
    def _is_stack_destination(self, lir_inst):
        """Check that destination of the operation is the stack."""
        return

    def _array_char_to_int(self, mir_src_param, mir_dst_param):
        mir_inst = None
        #print "--> SRC : %s" % mir_src_param
        #print "--> DST : %s" % mir_dst_param
        mir_inst = self.mir_inst_builder.ptrtoint(mir_src_param, mir_dst_param)
        #print "--> CST : %s" % mir_inst
        return mir_inst

    # TODO / FIXME : Complete all the possible conversion combinations.
    conversion_table = {
            #MiddleIrTypeChar : {
            #    #MiddleIrTypeChar : None,
            #    #MiddleIrTypeInt : None,
            #    },
            #MiddleIrTypeInt : {
            #    MiddleIrTypeArray : _array_char_to_int,

            #"conv_array_to_int" : _array_char_to_int,
            "conv_MiddleIrTypeInt_to_MiddleIrTypeArray_MiddleIrTypeChar" : _array_char_to_int,

            #    },
            #MiddleIrTypeFloat : {},
            #MiddleIrTypeDouble : {},
            #MiddleIrTypeX86Fp80 : {},
            #MiddleIrTypePpcFp128 : {},
            #MiddleIrTypeFp128 : {},

            #MiddleIrTypeFunction : {},
            #MiddleIrTypeOpaque : {},
            #MiddleIrTypeStruct : {},
            #MiddleIrTypePackedStruct: {},
            #MiddleIrTypeArray : {},
            #MiddleIrTypePointer : {},
            #MiddleIrTypeVector : {},
            #MiddleIrTypeLabel : {},
            #MiddleIrTypeVoid : {},
        }

    def _argument_requires_conversion(self, mir_src_param, mir_dst_param):
        """..."""
        inner_type = self.__get_inner_type(mir_src_param)

        if type(inner_type) is list:
            print "Final type contained in %s is %s" % (
                self._class_name(inner_type[0]),
                self._class_name(inner_type[1]))

            inner_type_k = "%s_%s" % (
                self._class_name(inner_type[0]),
                self._class_name(inner_type[1]))
        else:
            print "Final type is %r" % inner_type #self._class_name(inner_type)
            inner_type_k = "%s" % self._class_name(inner_type)

        dest_type_key = "conv_%s_to_%s" % (
            self._class_name(mir_dst_param), inner_type_k)

        avail_conversions = self.conversion_table.get(dest_type_key, None)

        print "Conversion available (key %s) for %s -> %s: %s" % (
            dest_type_key,
            self._class_name(mir_src_param), 
            self._class_name(mir_dst_param), 
            str(bool(avail_conversions is not None)).upper())

        if avail_conversions is None:
            return None

        #conv_func = avail_conversions.get(inner_type, False)
        #return conv_func
        return avail_conversions

    def __get_inner_type(self, mir_obj, indent=0):
        """..."""
        indent += 1
        src = "undef"

        if isinstance(mir_obj, MiddleIrInstruction):
            src = "instruction"
            inner_type = mir_obj.yields
        elif isinstance(mir_obj, MiddleIrBaseConstant):
            src = "constant"
            inner_type = mir_obj.type
        elif isinstance(mir_obj, MiddleIrGlobalVariable):
            src = "global"
            inner_type = mir_obj.type
        elif isinstance(mir_obj, MiddleIrBaseType):
            src = "type"
            inner_type = mir_obj.type

            if self.__is_container_type(mir_obj):
                print "%s+---> Con (%s) : %s" % (
                    ("    " * indent), src, self._class_name(mir_obj))
                return [mir_obj, mir_obj.type]#self.__get_inner_type(inner_type, indent)]

        else:
            raise FrontEndException(
                "Unimplemented conversion evaluation type : %r (%s)" % (
                mir_obj, mir_obj))

        print "%s+---> Src (%s) : %s" % (("    " * indent), src, self._class_name(mir_obj))

        if not self.__is_basic_type(inner_type):
            inner_type = self.__get_inner_type(inner_type, indent)

        return inner_type

    def __is_basic_type(self, mir_type):
        if isinstance(mir_type, MiddleIrTypeChar) or \
            isinstance(mir_type, MiddleIrTypeInt) or \
            isinstance(mir_type, MiddleIrTypeFloat) or \
            isinstance(mir_type, MiddleIrTypeDouble): 
            return True
        return False

    def __is_container_type(self, mir_type):
        if isinstance(mir_type, MiddleIrTypeFunction) or \
            isinstance(mir_type, MiddleIrTypeStruct) or \
            isinstance(mir_type, MiddleIrTypeArray) or \
            isinstance(mir_type, MiddleIrTypePointer) or \
            isinstance(mir_type, MiddleIrTypeVoid):
            #isinstance(mir_type, MiddleIrTypeOpaque) or \
            #isinstance(mir_type, MiddleIrTypePackedStruct) or \
            #isinstance(mir_type, MiddleIrTypeVector) or \
            #isinstance(mir_type, MiddleIrTypeLabel) or \
            return True
        return False

    def _class_name(self, mir_obj):
        """Return the plain MIR class name."""
        print repr(mir_obj)
        return repr(mir_obj).split(" ")[0].split(".")[-1]

    def is_parameter_register(self, lir_inst, op_idx):
        """Indicate if the operand in the specified LIR instruction refers to a
        parameter register.

        """
        op = lir_inst[op_idx].value

        du_address = self.lir_function.ud_chain.get(lir_inst.address, None)

        try:
            if du_address is not None and \
                op in du_address and \
                du_address[op] == self.lir_function.start_address and \
                op not in self.lir_function[du_address[op]]:
                print "Op %d Xrefd and NOT defined at 0x%08X" % (op, du_address[op])
                return True
        except Exception, err:
            print format_exc()
        return False

    def generate_output(self, graph_view=False):
        """Dump the current LIR function to the debugger output."""
        print "[+] Generating LIR representation..."
        if not graph_view:
            print self.lir_function
        else:
            print self.lir_function
            lir_output = BasicBlockGraphOutput(self.lir_function)
            lir_output.generate_output("Low Level IR output")


