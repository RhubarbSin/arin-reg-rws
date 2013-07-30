# ./ErrorPayload.py
# -*- coding: utf-8 -*-
# PyXB bindings for NM:514f13e3f1b2b4088cde1fa16b1c0c6121fb4d3d
# Generated 2013-07-11 15:18:56.914735 by PyXB version 1.2.2
# Namespace http://www.arin.net/regrws/core/v1

import pyxb
import pyxb.binding
import pyxb.binding.saxer
import StringIO
import pyxb.utils.utility
import pyxb.utils.domutils
import sys

# Unique identifier for bindings created at the same time
_GenerationUID = pyxb.utils.utility.UniqueIdentifier('urn:uuid:bb859a91-ea5e-11e2-bff3-10ddb19be936')

# Version of PyXB used to generate the bindings
_PyXBVersion = '1.2.2'
# Generated bindings are not compatible across PyXB versions
if pyxb.__version__ != _PyXBVersion:
    raise pyxb.PyXBVersionError(_PyXBVersion)

# Import bindings for namespaces imported into schema
import pyxb.binding.datatypes

# NOTE: All namespace declarations are reserved within the binding
Namespace = pyxb.namespace.NamespaceForURI(u'http://www.arin.net/regrws/core/v1', create_if_missing=True)
Namespace.configureCategories(['typeBinding', 'elementBinding'])

def CreateFromDocument (xml_text, default_namespace=None, location_base=None):
    """Parse the given XML and use the document element to create a
    Python instance.
    
    @kw default_namespace The L{pyxb.Namespace} instance to use as the
    default namespace where there is no default namespace in scope.
    If unspecified or C{None}, the namespace of the module containing
    this function will be used.

    @keyword location_base: An object to be recorded as the base of all
    L{pyxb.utils.utility.Location} instances associated with events and
    objects handled by the parser.  You might pass the URI from which
    the document was obtained.
    """

    if pyxb.XMLStyle_saxer != pyxb._XMLStyle:
        dom = pyxb.utils.domutils.StringToDOM(xml_text)
        return CreateFromDOM(dom.documentElement)
    if default_namespace is None:
        default_namespace = Namespace.fallbackNamespace()
    saxer = pyxb.binding.saxer.make_parser(fallback_namespace=default_namespace, location_base=location_base)
    handler = saxer.getContentHandler()
    saxer.parse(StringIO.StringIO(xml_text))
    instance = handler.rootObject()
    return instance

def CreateFromDOM (node, default_namespace=None):
    """Create a Python instance from the given DOM node.
    The node tag must correspond to an element declaration in this module.

    @deprecated: Forcing use of DOM interface is unnecessary; use L{CreateFromDocument}."""
    if default_namespace is None:
        default_namespace = Namespace.fallbackNamespace()
    return pyxb.binding.basis.element.AnyCreateFromDOM(node, default_namespace)


# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/Users/blb/Downloads/regrws-rnc/ErrorPayload.xsd', 4, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.arin.net/regrws/core/v1}components uses Python identifier components
    __components = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'components'), 'components', '__httpwww_arin_netregrwscorev1_CTD_ANON_httpwww_arin_netregrwscorev1components', True, pyxb.utils.utility.Location('/Users/blb/Downloads/regrws-rnc/ErrorPayload.xsd', 23, 2), )

    
    components = property(__components.value, __components.set, None, None)

    
    # Element {http://www.arin.net/regrws/core/v1}additionalInfo uses Python identifier additionalInfo
    __additionalInfo = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'additionalInfo'), 'additionalInfo', '__httpwww_arin_netregrwscorev1_CTD_ANON_httpwww_arin_netregrwscorev1additionalInfo', True, pyxb.utils.utility.Location('/Users/blb/Downloads/regrws-rnc/ErrorPayload.xsd', 30, 2), )

    
    additionalInfo = property(__additionalInfo.value, __additionalInfo.set, None, None)

    
    # Element {http://www.arin.net/regrws/core/v1}message uses Python identifier message
    __message = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'message'), 'message', '__httpwww_arin_netregrwscorev1_CTD_ANON_httpwww_arin_netregrwscorev1message', True, pyxb.utils.utility.Location('/Users/blb/Downloads/regrws-rnc/ErrorPayload.xsd', 37, 2), )

    
    message = property(__message.value, __message.set, None, None)

    
    # Element {http://www.arin.net/regrws/core/v1}code uses Python identifier code
    __code = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'code'), 'code', '__httpwww_arin_netregrwscorev1_CTD_ANON_httpwww_arin_netregrwscorev1code', True, pyxb.utils.utility.Location('/Users/blb/Downloads/regrws-rnc/ErrorPayload.xsd', 38, 2), )

    
    code = property(__code.value, __code.set, None, None)

    _HasWildcardElement = True
    _ElementMap.update({
        __components.name() : __components,
        __additionalInfo.name() : __additionalInfo,
        __message.name() : __message,
        __code.name() : __code
    })
    _AttributeMap.update({
        
    })



# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_ (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/Users/blb/Downloads/regrws-rnc/ErrorPayload.xsd', 15, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.arin.net/regrws/core/v1}message uses Python identifier message
    __message = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'message'), 'message', '__httpwww_arin_netregrwscorev1_CTD_ANON__httpwww_arin_netregrwscorev1message', True, pyxb.utils.utility.Location('/Users/blb/Downloads/regrws-rnc/ErrorPayload.xsd', 37, 2), )

    
    message = property(__message.value, __message.set, None, None)

    
    # Element {http://www.arin.net/regrws/core/v1}name uses Python identifier name
    __name = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'name'), 'name', '__httpwww_arin_netregrwscorev1_CTD_ANON__httpwww_arin_netregrwscorev1name', True, pyxb.utils.utility.Location('/Users/blb/Downloads/regrws-rnc/ErrorPayload.xsd', 44, 2), )

    
    name = property(__name.value, __name.set, None, None)

    _HasWildcardElement = True
    _ElementMap.update({
        __message.name() : __message,
        __name.name() : __name
    })
    _AttributeMap.update({
        
    })



# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_2 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/Users/blb/Downloads/regrws-rnc/ErrorPayload.xsd', 24, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.arin.net/regrws/core/v1}component uses Python identifier component
    __component = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'component'), 'component', '__httpwww_arin_netregrwscorev1_CTD_ANON_2_httpwww_arin_netregrwscorev1component', True, pyxb.utils.utility.Location('/Users/blb/Downloads/regrws-rnc/ErrorPayload.xsd', 14, 2), )

    
    component = property(__component.value, __component.set, None, None)

    _ElementMap.update({
        __component.name() : __component
    })
    _AttributeMap.update({
        
    })



# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_3 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/Users/blb/Downloads/regrws-rnc/ErrorPayload.xsd', 31, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.arin.net/regrws/core/v1}message uses Python identifier message
    __message = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'message'), 'message', '__httpwww_arin_netregrwscorev1_CTD_ANON_3_httpwww_arin_netregrwscorev1message', True, pyxb.utils.utility.Location('/Users/blb/Downloads/regrws-rnc/ErrorPayload.xsd', 37, 2), )

    
    message = property(__message.value, __message.set, None, None)

    _ElementMap.update({
        __message.name() : __message
    })
    _AttributeMap.update({
        
    })



message = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'message'), pyxb.binding.datatypes.string, location=pyxb.utils.utility.Location('/Users/blb/Downloads/regrws-rnc/ErrorPayload.xsd', 37, 2))
Namespace.addCategoryObject('elementBinding', message.name().localName(), message)

code = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'code'), pyxb.binding.datatypes.string, location=pyxb.utils.utility.Location('/Users/blb/Downloads/regrws-rnc/ErrorPayload.xsd', 38, 2))
Namespace.addCategoryObject('elementBinding', code.name().localName(), code)

name = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'name'), pyxb.binding.datatypes.string, location=pyxb.utils.utility.Location('/Users/blb/Downloads/regrws-rnc/ErrorPayload.xsd', 44, 2))
Namespace.addCategoryObject('elementBinding', name.name().localName(), name)

error = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'error'), CTD_ANON, location=pyxb.utils.utility.Location('/Users/blb/Downloads/regrws-rnc/ErrorPayload.xsd', 3, 2))
Namespace.addCategoryObject('elementBinding', error.name().localName(), error)

component = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'component'), CTD_ANON_, location=pyxb.utils.utility.Location('/Users/blb/Downloads/regrws-rnc/ErrorPayload.xsd', 14, 2))
Namespace.addCategoryObject('elementBinding', component.name().localName(), component)

components = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'components'), CTD_ANON_2, location=pyxb.utils.utility.Location('/Users/blb/Downloads/regrws-rnc/ErrorPayload.xsd', 23, 2))
Namespace.addCategoryObject('elementBinding', components.name().localName(), components)

additionalInfo = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'additionalInfo'), CTD_ANON_3, location=pyxb.utils.utility.Location('/Users/blb/Downloads/regrws-rnc/ErrorPayload.xsd', 30, 2))
Namespace.addCategoryObject('elementBinding', additionalInfo.name().localName(), additionalInfo)



CTD_ANON._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'components'), CTD_ANON_2, scope=CTD_ANON, location=pyxb.utils.utility.Location('/Users/blb/Downloads/regrws-rnc/ErrorPayload.xsd', 23, 2)))

CTD_ANON._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'additionalInfo'), CTD_ANON_3, scope=CTD_ANON, location=pyxb.utils.utility.Location('/Users/blb/Downloads/regrws-rnc/ErrorPayload.xsd', 30, 2)))

CTD_ANON._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'message'), pyxb.binding.datatypes.string, scope=CTD_ANON, location=pyxb.utils.utility.Location('/Users/blb/Downloads/regrws-rnc/ErrorPayload.xsd', 37, 2)))

CTD_ANON._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'code'), pyxb.binding.datatypes.string, scope=CTD_ANON, location=pyxb.utils.utility.Location('/Users/blb/Downloads/regrws-rnc/ErrorPayload.xsd', 38, 2)))

def _BuildAutomaton ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton
    del _BuildAutomaton
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location('/Users/blb/Downloads/regrws-rnc/ErrorPayload.xsd', 5, 6))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'components')), pyxb.utils.utility.Location('/Users/blb/Downloads/regrws-rnc/ErrorPayload.xsd', 6, 8))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'additionalInfo')), pyxb.utils.utility.Location('/Users/blb/Downloads/regrws-rnc/ErrorPayload.xsd', 7, 8))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'message')), pyxb.utils.utility.Location('/Users/blb/Downloads/regrws-rnc/ErrorPayload.xsd', 8, 8))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'code')), pyxb.utils.utility.Location('/Users/blb/Downloads/regrws-rnc/ErrorPayload.xsd', 9, 8))
    st_3 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.WildcardUse(pyxb.binding.content.Wildcard(process_contents=pyxb.binding.content.Wildcard.PC_skip, namespace_constraint=pyxb.binding.content.Wildcard.NC_any), pyxb.utils.utility.Location('/Users/blb/Downloads/regrws-rnc/ErrorPayload.xsd', 41, 6))
    st_4 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_4._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
CTD_ANON._Automaton = _BuildAutomaton()




CTD_ANON_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'message'), pyxb.binding.datatypes.string, scope=CTD_ANON_, location=pyxb.utils.utility.Location('/Users/blb/Downloads/regrws-rnc/ErrorPayload.xsd', 37, 2)))

CTD_ANON_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'name'), pyxb.binding.datatypes.string, scope=CTD_ANON_, location=pyxb.utils.utility.Location('/Users/blb/Downloads/regrws-rnc/ErrorPayload.xsd', 44, 2)))

def _BuildAutomaton_ ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_
    del _BuildAutomaton_
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location('/Users/blb/Downloads/regrws-rnc/ErrorPayload.xsd', 16, 6))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'message')), pyxb.utils.utility.Location('/Users/blb/Downloads/regrws-rnc/ErrorPayload.xsd', 17, 8))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'name')), pyxb.utils.utility.Location('/Users/blb/Downloads/regrws-rnc/ErrorPayload.xsd', 18, 8))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.WildcardUse(pyxb.binding.content.Wildcard(process_contents=pyxb.binding.content.Wildcard.PC_skip, namespace_constraint=pyxb.binding.content.Wildcard.NC_any), pyxb.utils.utility.Location('/Users/blb/Downloads/regrws-rnc/ErrorPayload.xsd', 47, 6))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_2._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
CTD_ANON_._Automaton = _BuildAutomaton_()




CTD_ANON_2._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'component'), CTD_ANON_, scope=CTD_ANON_2, location=pyxb.utils.utility.Location('/Users/blb/Downloads/regrws-rnc/ErrorPayload.xsd', 14, 2)))

def _BuildAutomaton_2 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_2
    del _BuildAutomaton_2
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location('/Users/blb/Downloads/regrws-rnc/ErrorPayload.xsd', 26, 8))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_2._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'component')), pyxb.utils.utility.Location('/Users/blb/Downloads/regrws-rnc/ErrorPayload.xsd', 26, 8))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
CTD_ANON_2._Automaton = _BuildAutomaton_2()




CTD_ANON_3._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'message'), pyxb.binding.datatypes.string, scope=CTD_ANON_3, location=pyxb.utils.utility.Location('/Users/blb/Downloads/regrws-rnc/ErrorPayload.xsd', 37, 2)))

def _BuildAutomaton_3 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_3
    del _BuildAutomaton_3
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location('/Users/blb/Downloads/regrws-rnc/ErrorPayload.xsd', 33, 8))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_3._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'message')), pyxb.utils.utility.Location('/Users/blb/Downloads/regrws-rnc/ErrorPayload.xsd', 33, 8))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
CTD_ANON_3._Automaton = _BuildAutomaton_3()

