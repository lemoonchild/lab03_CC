# Generated from TerraformSubset.g4 by ANTLR 4.13.1
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,15,94,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,1,0,1,0,5,0,25,8,0,10,0,12,0,
        28,9,0,1,0,1,0,1,1,1,1,1,1,1,1,1,1,3,1,37,8,1,1,2,1,2,1,2,1,2,1,
        2,1,2,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,4,1,4,1,4,1,4,1,4,1,4,1,5,1,
        5,1,5,1,5,1,5,1,5,1,6,1,6,1,6,1,6,1,6,1,7,1,7,5,7,71,8,7,10,7,12,
        7,74,9,7,1,8,1,8,1,8,1,8,1,9,1,9,1,9,1,9,3,9,84,8,9,1,10,1,10,1,
        10,5,10,89,8,10,10,10,12,10,92,9,10,1,10,0,0,11,0,2,4,6,8,10,12,
        14,16,18,20,0,0,94,0,26,1,0,0,0,2,36,1,0,0,0,4,38,1,0,0,0,6,44,1,
        0,0,0,8,51,1,0,0,0,10,57,1,0,0,0,12,63,1,0,0,0,14,72,1,0,0,0,16,
        75,1,0,0,0,18,83,1,0,0,0,20,85,1,0,0,0,22,25,3,2,1,0,23,25,5,14,
        0,0,24,22,1,0,0,0,24,23,1,0,0,0,25,28,1,0,0,0,26,24,1,0,0,0,26,27,
        1,0,0,0,27,29,1,0,0,0,28,26,1,0,0,0,29,30,5,0,0,1,30,1,1,0,0,0,31,
        37,3,4,2,0,32,37,3,6,3,0,33,37,3,8,4,0,34,37,3,10,5,0,35,37,3,12,
        6,0,36,31,1,0,0,0,36,32,1,0,0,0,36,33,1,0,0,0,36,34,1,0,0,0,36,35,
        1,0,0,0,37,3,1,0,0,0,38,39,5,1,0,0,39,40,5,12,0,0,40,41,5,2,0,0,
        41,42,3,14,7,0,42,43,5,3,0,0,43,5,1,0,0,0,44,45,5,4,0,0,45,46,5,
        12,0,0,46,47,5,12,0,0,47,48,5,2,0,0,48,49,3,14,7,0,49,50,5,3,0,0,
        50,7,1,0,0,0,51,52,5,5,0,0,52,53,5,12,0,0,53,54,5,2,0,0,54,55,3,
        14,7,0,55,56,5,3,0,0,56,9,1,0,0,0,57,58,5,6,0,0,58,59,5,12,0,0,59,
        60,5,2,0,0,60,61,3,14,7,0,61,62,5,3,0,0,62,11,1,0,0,0,63,64,5,7,
        0,0,64,65,5,2,0,0,65,66,3,14,7,0,66,67,5,3,0,0,67,13,1,0,0,0,68,
        71,3,16,8,0,69,71,5,14,0,0,70,68,1,0,0,0,70,69,1,0,0,0,71,74,1,0,
        0,0,72,70,1,0,0,0,72,73,1,0,0,0,73,15,1,0,0,0,74,72,1,0,0,0,75,76,
        5,13,0,0,76,77,5,8,0,0,77,78,3,18,9,0,78,17,1,0,0,0,79,84,5,12,0,
        0,80,84,5,11,0,0,81,84,5,10,0,0,82,84,3,20,10,0,83,79,1,0,0,0,83,
        80,1,0,0,0,83,81,1,0,0,0,83,82,1,0,0,0,84,19,1,0,0,0,85,90,5,13,
        0,0,86,87,5,9,0,0,87,89,5,13,0,0,88,86,1,0,0,0,89,92,1,0,0,0,90,
        88,1,0,0,0,90,91,1,0,0,0,91,21,1,0,0,0,92,90,1,0,0,0,7,24,26,36,
        70,72,83,90
    ]

class TerraformSubsetParser ( Parser ):

    grammarFileName = "TerraformSubset.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'provider'", "'{'", "'}'", "'resource'", 
                     "'variable'", "'output'", "'destroy'", "'='", "'.'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "BOOLEAN", "NUMBER", "STRING", 
                      "IDENTIFIER", "COMMENT", "WS" ]

    RULE_terraform = 0
    RULE_block = 1
    RULE_provider = 2
    RULE_resource = 3
    RULE_variable = 4
    RULE_output = 5
    RULE_destroy = 6
    RULE_body = 7
    RULE_keyValue = 8
    RULE_expr = 9
    RULE_reference = 10

    ruleNames =  [ "terraform", "block", "provider", "resource", "variable", 
                   "output", "destroy", "body", "keyValue", "expr", "reference" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    T__6=7
    T__7=8
    T__8=9
    BOOLEAN=10
    NUMBER=11
    STRING=12
    IDENTIFIER=13
    COMMENT=14
    WS=15

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.1")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class TerraformContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EOF(self):
            return self.getToken(TerraformSubsetParser.EOF, 0)

        def block(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(TerraformSubsetParser.BlockContext)
            else:
                return self.getTypedRuleContext(TerraformSubsetParser.BlockContext,i)


        def COMMENT(self, i:int=None):
            if i is None:
                return self.getTokens(TerraformSubsetParser.COMMENT)
            else:
                return self.getToken(TerraformSubsetParser.COMMENT, i)

        def getRuleIndex(self):
            return TerraformSubsetParser.RULE_terraform

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTerraform" ):
                listener.enterTerraform(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTerraform" ):
                listener.exitTerraform(self)




    def terraform(self):

        localctx = TerraformSubsetParser.TerraformContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_terraform)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 26
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 16626) != 0):
                self.state = 24
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [1, 4, 5, 6, 7]:
                    self.state = 22
                    self.block()
                    pass
                elif token in [14]:
                    self.state = 23
                    self.match(TerraformSubsetParser.COMMENT)
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 28
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 29
            self.match(TerraformSubsetParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BlockContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def provider(self):
            return self.getTypedRuleContext(TerraformSubsetParser.ProviderContext,0)


        def resource(self):
            return self.getTypedRuleContext(TerraformSubsetParser.ResourceContext,0)


        def variable(self):
            return self.getTypedRuleContext(TerraformSubsetParser.VariableContext,0)


        def output(self):
            return self.getTypedRuleContext(TerraformSubsetParser.OutputContext,0)


        def destroy(self):
            return self.getTypedRuleContext(TerraformSubsetParser.DestroyContext,0)


        def getRuleIndex(self):
            return TerraformSubsetParser.RULE_block

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBlock" ):
                listener.enterBlock(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBlock" ):
                listener.exitBlock(self)




    def block(self):

        localctx = TerraformSubsetParser.BlockContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_block)
        try:
            self.state = 36
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [1]:
                self.enterOuterAlt(localctx, 1)
                self.state = 31
                self.provider()
                pass
            elif token in [4]:
                self.enterOuterAlt(localctx, 2)
                self.state = 32
                self.resource()
                pass
            elif token in [5]:
                self.enterOuterAlt(localctx, 3)
                self.state = 33
                self.variable()
                pass
            elif token in [6]:
                self.enterOuterAlt(localctx, 4)
                self.state = 34
                self.output()
                pass
            elif token in [7]:
                self.enterOuterAlt(localctx, 5)
                self.state = 35
                self.destroy()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ProviderContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def STRING(self):
            return self.getToken(TerraformSubsetParser.STRING, 0)

        def body(self):
            return self.getTypedRuleContext(TerraformSubsetParser.BodyContext,0)


        def getRuleIndex(self):
            return TerraformSubsetParser.RULE_provider

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProvider" ):
                listener.enterProvider(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProvider" ):
                listener.exitProvider(self)




    def provider(self):

        localctx = TerraformSubsetParser.ProviderContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_provider)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 38
            self.match(TerraformSubsetParser.T__0)
            self.state = 39
            self.match(TerraformSubsetParser.STRING)
            self.state = 40
            self.match(TerraformSubsetParser.T__1)
            self.state = 41
            self.body()
            self.state = 42
            self.match(TerraformSubsetParser.T__2)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ResourceContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def STRING(self, i:int=None):
            if i is None:
                return self.getTokens(TerraformSubsetParser.STRING)
            else:
                return self.getToken(TerraformSubsetParser.STRING, i)

        def body(self):
            return self.getTypedRuleContext(TerraformSubsetParser.BodyContext,0)


        def getRuleIndex(self):
            return TerraformSubsetParser.RULE_resource

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterResource" ):
                listener.enterResource(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitResource" ):
                listener.exitResource(self)




    def resource(self):

        localctx = TerraformSubsetParser.ResourceContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_resource)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 44
            self.match(TerraformSubsetParser.T__3)
            self.state = 45
            self.match(TerraformSubsetParser.STRING)
            self.state = 46
            self.match(TerraformSubsetParser.STRING)
            self.state = 47
            self.match(TerraformSubsetParser.T__1)
            self.state = 48
            self.body()
            self.state = 49
            self.match(TerraformSubsetParser.T__2)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class VariableContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def STRING(self):
            return self.getToken(TerraformSubsetParser.STRING, 0)

        def body(self):
            return self.getTypedRuleContext(TerraformSubsetParser.BodyContext,0)


        def getRuleIndex(self):
            return TerraformSubsetParser.RULE_variable

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterVariable" ):
                listener.enterVariable(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitVariable" ):
                listener.exitVariable(self)




    def variable(self):

        localctx = TerraformSubsetParser.VariableContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_variable)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 51
            self.match(TerraformSubsetParser.T__4)
            self.state = 52
            self.match(TerraformSubsetParser.STRING)
            self.state = 53
            self.match(TerraformSubsetParser.T__1)
            self.state = 54
            self.body()
            self.state = 55
            self.match(TerraformSubsetParser.T__2)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class OutputContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def STRING(self):
            return self.getToken(TerraformSubsetParser.STRING, 0)

        def body(self):
            return self.getTypedRuleContext(TerraformSubsetParser.BodyContext,0)


        def getRuleIndex(self):
            return TerraformSubsetParser.RULE_output

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterOutput" ):
                listener.enterOutput(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitOutput" ):
                listener.exitOutput(self)




    def output(self):

        localctx = TerraformSubsetParser.OutputContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_output)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 57
            self.match(TerraformSubsetParser.T__5)
            self.state = 58
            self.match(TerraformSubsetParser.STRING)
            self.state = 59
            self.match(TerraformSubsetParser.T__1)
            self.state = 60
            self.body()
            self.state = 61
            self.match(TerraformSubsetParser.T__2)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DestroyContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def body(self):
            return self.getTypedRuleContext(TerraformSubsetParser.BodyContext,0)


        def getRuleIndex(self):
            return TerraformSubsetParser.RULE_destroy

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDestroy" ):
                listener.enterDestroy(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDestroy" ):
                listener.exitDestroy(self)




    def destroy(self):

        localctx = TerraformSubsetParser.DestroyContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_destroy)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 63
            self.match(TerraformSubsetParser.T__6)
            self.state = 64
            self.match(TerraformSubsetParser.T__1)
            self.state = 65
            self.body()
            self.state = 66
            self.match(TerraformSubsetParser.T__2)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BodyContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def keyValue(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(TerraformSubsetParser.KeyValueContext)
            else:
                return self.getTypedRuleContext(TerraformSubsetParser.KeyValueContext,i)


        def COMMENT(self, i:int=None):
            if i is None:
                return self.getTokens(TerraformSubsetParser.COMMENT)
            else:
                return self.getToken(TerraformSubsetParser.COMMENT, i)

        def getRuleIndex(self):
            return TerraformSubsetParser.RULE_body

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBody" ):
                listener.enterBody(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBody" ):
                listener.exitBody(self)




    def body(self):

        localctx = TerraformSubsetParser.BodyContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_body)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 72
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==13 or _la==14:
                self.state = 70
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [13]:
                    self.state = 68
                    self.keyValue()
                    pass
                elif token in [14]:
                    self.state = 69
                    self.match(TerraformSubsetParser.COMMENT)
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 74
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class KeyValueContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self):
            return self.getToken(TerraformSubsetParser.IDENTIFIER, 0)

        def expr(self):
            return self.getTypedRuleContext(TerraformSubsetParser.ExprContext,0)


        def getRuleIndex(self):
            return TerraformSubsetParser.RULE_keyValue

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterKeyValue" ):
                listener.enterKeyValue(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitKeyValue" ):
                listener.exitKeyValue(self)




    def keyValue(self):

        localctx = TerraformSubsetParser.KeyValueContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_keyValue)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 75
            self.match(TerraformSubsetParser.IDENTIFIER)
            self.state = 76
            self.match(TerraformSubsetParser.T__7)
            self.state = 77
            self.expr()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def STRING(self):
            return self.getToken(TerraformSubsetParser.STRING, 0)

        def NUMBER(self):
            return self.getToken(TerraformSubsetParser.NUMBER, 0)

        def BOOLEAN(self):
            return self.getToken(TerraformSubsetParser.BOOLEAN, 0)

        def reference(self):
            return self.getTypedRuleContext(TerraformSubsetParser.ReferenceContext,0)


        def getRuleIndex(self):
            return TerraformSubsetParser.RULE_expr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpr" ):
                listener.enterExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpr" ):
                listener.exitExpr(self)




    def expr(self):

        localctx = TerraformSubsetParser.ExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_expr)
        try:
            self.state = 83
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [12]:
                self.enterOuterAlt(localctx, 1)
                self.state = 79
                self.match(TerraformSubsetParser.STRING)
                pass
            elif token in [11]:
                self.enterOuterAlt(localctx, 2)
                self.state = 80
                self.match(TerraformSubsetParser.NUMBER)
                pass
            elif token in [10]:
                self.enterOuterAlt(localctx, 3)
                self.state = 81
                self.match(TerraformSubsetParser.BOOLEAN)
                pass
            elif token in [13]:
                self.enterOuterAlt(localctx, 4)
                self.state = 82
                self.reference()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ReferenceContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self, i:int=None):
            if i is None:
                return self.getTokens(TerraformSubsetParser.IDENTIFIER)
            else:
                return self.getToken(TerraformSubsetParser.IDENTIFIER, i)

        def getRuleIndex(self):
            return TerraformSubsetParser.RULE_reference

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterReference" ):
                listener.enterReference(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitReference" ):
                listener.exitReference(self)




    def reference(self):

        localctx = TerraformSubsetParser.ReferenceContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_reference)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 85
            self.match(TerraformSubsetParser.IDENTIFIER)
            self.state = 90
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==9:
                self.state = 86
                self.match(TerraformSubsetParser.T__8)
                self.state = 87
                self.match(TerraformSubsetParser.IDENTIFIER)
                self.state = 92
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





