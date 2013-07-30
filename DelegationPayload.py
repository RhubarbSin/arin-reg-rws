# ./DelegationPayload.py
# -*- coding: utf-8 -*-
# PyXB bindings for NM:514f13e3f1b2b4088cde1fa16b1c0c6121fb4d3d
# Generated 2013-07-11 15:18:35.262335 by PyXB version 1.2.2
# Namespace http://www.arin.net/regrws/core/v1

import pyxb
import pyxb.binding
import pyxb.binding.saxer
import StringIO
import pyxb.utils.utility
import pyxb.utils.domutils
import sys

# Unique identifier for bindings created at the same time
_GenerationUID = pyxb.utils.utility.UniqueIdentifier('urn:uuid:ae9d8a23-ea5e-11e2-a9fb-10ddb19be936')

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
    _XSDLocation = pyxb.utils.utility.Location('/Users/blb/Downloads/regrws-rnc/DelegationPayload.xsd', 4, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.arin.net/regrws/core/v1}name uses Python identifier name
    __name = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'name'), 'name', '__httpwww_arin_netregrwscorev1_CTD_ANON_httpwww_arin_netregrwscorev1name', True, pyxb.utils.utility.Location('/Users/blb/Downloads/regrws-rnc/DelegationPayload.xsd', 23, 2), )

    
    name = property(__name.value, __name.set, None, None)

    
    # Element {http://www.arin.net/regrws/core/v1}nameservers uses Python identifier nameservers
    __nameservers = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'nameservers'), 'nameservers', '__httpwww_arin_netregrwscorev1_CTD_ANON_httpwww_arin_netregrwscorev1nameservers', True, pyxb.utils.utility.Location('/Users/blb/Downloads/regrws-rnc/DelegationPayload.xsd', 24, 2), )

    
    nameservers = property(__nameservers.value, __nameservers.set, None, None)

    
    # Element {http://www.arin.net/regrws/core/v1}delegationKeys uses Python identifier delegationKeys
    __delegationKeys = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'delegationKeys'), 'delegationKeys', '__httpwww_arin_netregrwscorev1_CTD_ANON_httpwww_arin_netregrwscorev1delegationKeys', True, pyxb.utils.utility.Location('/Users/blb/Downloads/regrws-rnc/DelegationPayload.xsd', 31, 2), )

    
    delegationKeys = property(__delegationKeys.value, __delegationKeys.set, None, None)

    _HasWildcardElement = True
    _ElementMap.update({
        __name.name() : __name,
        __nameservers.name() : __nameservers,
        __delegationKeys.name() : __delegationKeys
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
    _XSDLocation = pyxb.utils.utility.Location('/Users/blb/Downloads/regrws-rnc/DelegationPayload.xsd', 14, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.arin.net/regrws/core/v1}algorithm uses Python identifier algorithm
    __algorithm = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'algorithm'), 'algorithm', '__httpwww_arin_netregrwscorev1_CTD_ANON__httpwww_arin_netregrwscorev1algorithm', True, pyxb.utils.utility.Location('/Users/blb/Downloads/regrws-rnc/DelegationPayload.xsd', 43, 2), )

    
    algorithm = property(__algorithm.value, __algorithm.set, None, None)

    
    # Element {http://www.arin.net/regrws/core/v1}digest uses Python identifier digest
    __digest = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'digest'), 'digest', '__httpwww_arin_netregrwscorev1_CTD_ANON__httpwww_arin_netregrwscorev1digest', True, pyxb.utils.utility.Location('/Users/blb/Downloads/regrws-rnc/DelegationPayload.xsd', 52, 2), )

    
    digest = property(__digest.value, __digest.set, None, None)

    
    # Element {http://www.arin.net/regrws/core/v1}digestType uses Python identifier digestType
    __digestType = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'digestType'), 'digestType', '__httpwww_arin_netregrwscorev1_CTD_ANON__httpwww_arin_netregrwscorev1digestType', True, pyxb.utils.utility.Location('/Users/blb/Downloads/regrws-rnc/DelegationPayload.xsd', 53, 2), )

    
    digestType = property(__digestType.value, __digestType.set, None, None)

    
    # Element {http://www.arin.net/regrws/core/v1}keyTag uses Python identifier keyTag
    __keyTag = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'keyTag'), 'keyTag', '__httpwww_arin_netregrwscorev1_CTD_ANON__httpwww_arin_netregrwscorev1keyTag', True, pyxb.utils.utility.Location('/Users/blb/Downloads/regrws-rnc/DelegationPayload.xsd', 62, 2), )

    
    keyTag = property(__keyTag.value, __keyTag.set, None, None)

    _ElementMap.update({
        __algorithm.name() : __algorithm,
        __digest.name() : __digest,
        __digestType.name() : __digestType,
        __keyTag.name() : __keyTag
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
    _XSDLocation = pyxb.utils.utility.Location('/Users/blb/Downloads/regrws-rnc/DelegationPayload.xsd', 25, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.arin.net/regrws/core/v1}nameserver uses Python identifier nameserver
    __nameserver = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'nameserver'), 'nameserver', '__httpwww_arin_netregrwscorev1_CTD_ANON_2_httpwww_arin_netregrwscorev1nameserver', True, pyxb.utils.utility.Location('/Users/blb/Downloads/regrws-rnc/DelegationPayload.xsd', 63, 2), )

    
    nameserver = property(__nameserver.value, __nameserver.set, None, None)

    _ElementMap.update({
        __nameserver.name() : __nameserver
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
    _XSDLocation = pyxb.utils.utility.Location('/Users/blb/Downloads/regrws-rnc/DelegationPayload.xsd', 32, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.arin.net/regrws/core/v1}delegationKey uses Python identifier delegationKey
    __delegationKey = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'delegationKey'), 'delegationKey', '__httpwww_arin_netregrwscorev1_CTD_ANON_3_httpwww_arin_netregrwscorev1delegationKey', True, pyxb.utils.utility.Location('/Users/blb/Downloads/regrws-rnc/DelegationPayload.xsd', 13, 2), )

    
    delegationKey = property(__delegationKey.value, __delegationKey.set, None, None)

    _ElementMap.update({
        __delegationKey.name() : __delegationKey
    })
    _AttributeMap.update({
        
    })



# Complex type [anonymous] with content type SIMPLE
class CTD_ANON_4 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type SIMPLE"""
    _TypeDefinition = pyxb.binding.datatypes.string
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/Users/blb/Downloads/regrws-rnc/DelegationPayload.xsd', 44, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.string
    
    # Attribute name uses Python identifier name
    __name = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'name'), 'name', '__httpwww_arin_netregrwscorev1_CTD_ANON_4_name', pyxb.binding.datatypes.string)
    __name._DeclarationLocation = pyxb.utils.utility.Location('/Users/blb/Downloads/regrws-rnc/DelegationPayload.xsd', 47, 10)
    __name._UseLocation = pyxb.utils.utility.Location('/Users/blb/Downloads/regrws-rnc/DelegationPayload.xsd', 47, 10)
    
    name = property(__name.value, __name.set, None, None)

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __name.name() : __name
    })



# Complex type [anonymous] with content type SIMPLE
class CTD_ANON_5 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type SIMPLE"""
    _TypeDefinition = pyxb.binding.datatypes.string
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/Users/blb/Downloads/regrws-rnc/DelegationPayload.xsd', 54, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.string
    
    # Attribute name uses Python identifier name
    __name = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'name'), 'name', '__httpwww_arin_netregrwscorev1_CTD_ANON_5_name', pyxb.binding.datatypes.string)
    __name._DeclarationLocation = pyxb.utils.utility.Location('/Users/blb/Downloads/regrws-rnc/DelegationPayload.xsd', 57, 10)
    __name._UseLocation = pyxb.utils.utility.Location('/Users/blb/Downloads/regrws-rnc/DelegationPayload.xsd', 57, 10)
    
    name = property(__name.value, __name.set, None, None)

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __name.name() : __name
    })



name = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'name'), pyxb.binding.datatypes.string, location=pyxb.utils.utility.Location('/Users/blb/Downloads/regrws-rnc/DelegationPayload.xsd', 23, 2))
Namespace.addCategoryObject('elementBinding', name.name().localName(), name)

digest = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'digest'), pyxb.binding.datatypes.string, location=pyxb.utils.utility.Location('/Users/blb/Downloads/regrws-rnc/DelegationPayload.xsd', 52, 2))
Namespace.addCategoryObject('elementBinding', digest.name().localName(), digest)

keyTag = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'keyTag'), pyxb.binding.datatypes.string, location=pyxb.utils.utility.Location('/Users/blb/Downloads/regrws-rnc/DelegationPayload.xsd', 62, 2))
Namespace.addCategoryObject('elementBinding', keyTag.name().localName(), keyTag)

nameserver = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'nameserver'), pyxb.binding.datatypes.string, location=pyxb.utils.utility.Location('/Users/blb/Downloads/regrws-rnc/DelegationPayload.xsd', 63, 2))
Namespace.addCategoryObject('elementBinding', nameserver.name().localName(), nameserver)

delegation = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'delegation'), CTD_ANON, location=pyxb.utils.utility.Location('/Users/blb/Downloads/regrws-rnc/DelegationPayload.xsd', 3, 2))
Namespace.addCategoryObject('elementBinding', delegation.name().localName(), delegation)

delegationKey = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'delegationKey'), CTD_ANON_, location=pyxb.utils.utility.Location('/Users/blb/Downloads/regrws-rnc/DelegationPayload.xsd', 13, 2))
Namespace.addCategoryObject('elementBinding', delegationKey.name().localName(), delegationKey)

nameservers = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'nameservers'), CTD_ANON_2, location=pyxb.utils.utility.Location('/Users/blb/Downloads/regrws-rnc/DelegationPayload.xsd', 24, 2))
Namespace.addCategoryObject('elementBinding', nameservers.name().localName(), nameservers)

delegationKeys = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'delegationKeys'), CTD_ANON_3, location=pyxb.utils.utility.Location('/Users/blb/Downloads/regrws-rnc/DelegationPayload.xsd', 31, 2))
Namespace.addCategoryObject('elementBinding', delegationKeys.name().localName(), delegationKeys)

algorithm = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'algorithm'), CTD_ANON_4, location=pyxb.utils.utility.Location('/Users/blb/Downloads/regrws-rnc/DelegationPayload.xsd', 43, 2))
Namespace.addCategoryObject('elementBinding', algorithm.name().localName(), algorithm)

digestType = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'digestType'), CTD_ANON_5, location=pyxb.utils.utility.Location('/Users/blb/Downloads/regrws-rnc/DelegationPayload.xsd', 53, 2))
Namespace.addCategoryObject('elementBinding', digestType.name().localName(), digestType)



CTD_ANON._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'name'), pyxb.binding.datatypes.string, scope=CTD_ANON, location=pyxb.utils.utility.Location('/Users/blb/Downloads/regrws-rnc/DelegationPayload.xsd', 23, 2)))

CTD_ANON._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'nameservers'), CTD_ANON_2, scope=CTD_ANON, location=pyxb.utils.utility.Location('/Users/blb/Downloads/regrws-rnc/DelegationPayload.xsd', 24, 2)))

CTD_ANON._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'delegationKeys'), CTD_ANON_3, scope=CTD_ANON, location=pyxb.utils.utility.Location('/Users/blb/Downloads/regrws-rnc/DelegationPayload.xsd', 31, 2)))

def _BuildAutomaton ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton
    del _BuildAutomaton
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location('/Users/blb/Downloads/regrws-rnc/DelegationPayload.xsd', 5, 6))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'name')), pyxb.utils.utility.Location('/Users/blb/Downloads/regrws-rnc/DelegationPayload.xsd', 6, 8))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'nameservers')), pyxb.utils.utility.Location('/Users/blb/Downloads/regrws-rnc/DelegationPayload.xsd', 7, 8))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'delegationKeys')), pyxb.utils.utility.Location('/Users/blb/Downloads/regrws-rnc/DelegationPayload.xsd', 8, 8))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.WildcardUse(pyxb.binding.content.Wildcard(process_contents=pyxb.binding.content.Wildcard.PC_skip, namespace_constraint=pyxb.binding.content.Wildcard.NC_any), pyxb.utils.utility.Location('/Users/blb/Downloads/regrws-rnc/DelegationPayload.xsd', 40, 6))
    st_3 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_3, [
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
    st_3._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
CTD_ANON._Automaton = _BuildAutomaton()




CTD_ANON_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'algorithm'), CTD_ANON_4, scope=CTD_ANON_, location=pyxb.utils.utility.Location('/Users/blb/Downloads/regrws-rnc/DelegationPayload.xsd', 43, 2)))

CTD_ANON_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'digest'), pyxb.binding.datatypes.string, scope=CTD_ANON_, location=pyxb.utils.utility.Location('/Users/blb/Downloads/regrws-rnc/DelegationPayload.xsd', 52, 2)))

CTD_ANON_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'digestType'), CTD_ANON_5, scope=CTD_ANON_, location=pyxb.utils.utility.Location('/Users/blb/Downloads/regrws-rnc/DelegationPayload.xsd', 53, 2)))

CTD_ANON_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'keyTag'), pyxb.binding.datatypes.string, scope=CTD_ANON_, location=pyxb.utils.utility.Location('/Users/blb/Downloads/regrws-rnc/DelegationPayload.xsd', 62, 2)))

def _BuildAutomaton_ ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_
    del _BuildAutomaton_
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location('/Users/blb/Downloads/regrws-rnc/DelegationPayload.xsd', 15, 6))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'algorithm')), pyxb.utils.utility.Location('/Users/blb/Downloads/regrws-rnc/DelegationPayload.xsd', 16, 8))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'digest')), pyxb.utils.utility.Location('/Users/blb/Downloads/regrws-rnc/DelegationPayload.xsd', 17, 8))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'digestType')), pyxb.utils.utility.Location('/Users/blb/Downloads/regrws-rnc/DelegationPayload.xsd', 18, 8))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'keyTag')), pyxb.utils.utility.Location('/Users/blb/Downloads/regrws-rnc/DelegationPayload.xsd', 19, 8))
    st_3 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_3, [
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
    st_3._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
CTD_ANON_._Automaton = _BuildAutomaton_()




CTD_ANON_2._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'nameserver'), pyxb.binding.datatypes.string, scope=CTD_ANON_2, location=pyxb.utils.utility.Location('/Users/blb/Downloads/regrws-rnc/DelegationPayload.xsd', 63, 2)))

def _BuildAutomaton_2 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_2
    del _BuildAutomaton_2
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location('/Users/blb/Downloads/regrws-rnc/DelegationPayload.xsd', 27, 8))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_2._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'nameserver')), pyxb.utils.utility.Location('/Users/blb/Downloads/regrws-rnc/DelegationPayload.xsd', 27, 8))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
CTD_ANON_2._Automaton = _BuildAutomaton_2()




CTD_ANON_3._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'delegationKey'), CTD_ANON_, scope=CTD_ANON_3, location=pyxb.utils.utility.Location('/Users/blb/Downloads/regrws-rnc/DelegationPayload.xsd', 13, 2)))

def _BuildAutomaton_3 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_3
    del _BuildAutomaton_3
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location('/Users/blb/Downloads/regrws-rnc/DelegationPayload.xsd', 34, 8))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_3._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'delegationKey')), pyxb.utils.utility.Location('/Users/blb/Downloads/regrws-rnc/DelegationPayload.xsd', 34, 8))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
CTD_ANON_3._Automaton = _BuildAutomaton_3()

