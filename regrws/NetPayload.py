# ./NetPayload.py
# -*- coding: utf-8 -*-
# PyXB bindings for NM:514f13e3f1b2b4088cde1fa16b1c0c6121fb4d3d
# Generated 2013-07-11 15:17:53.206489 by PyXB version 1.2.2
# Namespace http://www.arin.net/regrws/core/v1

import pyxb
import pyxb.binding
import pyxb.binding.saxer
import StringIO
import pyxb.utils.utility
import pyxb.utils.domutils
import sys

# Unique identifier for bindings created at the same time
_GenerationUID = pyxb.utils.utility.UniqueIdentifier('urn:uuid:9589a982-ea5e-11e2-8b90-10ddb19be936')

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


# Atomic simple type: [anonymous]
class STD_ANON (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/Users/blb/Downloads/regrws-rnc/NetPayload.xsd', 37, 8)
    _Documentation = None
STD_ANON._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=STD_ANON, enum_prefix=None)
STD_ANON.AD = STD_ANON._CF_enumeration.addEnumeration(unicode_value=u'AD', tag=u'AD')
STD_ANON.AB = STD_ANON._CF_enumeration.addEnumeration(unicode_value=u'AB', tag=u'AB')
STD_ANON.N = STD_ANON._CF_enumeration.addEnumeration(unicode_value=u'N', tag=u'N')
STD_ANON.T = STD_ANON._CF_enumeration.addEnumeration(unicode_value=u'T', tag=u'T')
STD_ANON._InitializeFacetMap(STD_ANON._CF_enumeration)

# Atomic simple type: [anonymous]
class STD_ANON_ (pyxb.binding.datatypes.token, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/Users/blb/Downloads/regrws-rnc/NetPayload.xsd', 77, 4)
    _Documentation = None
STD_ANON_._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=STD_ANON_, enum_prefix=None)
STD_ANON_.n4 = STD_ANON_._CF_enumeration.addEnumeration(unicode_value=u'4', tag=u'n4')
STD_ANON_.n6 = STD_ANON_._CF_enumeration.addEnumeration(unicode_value=u'6', tag=u'n6')
STD_ANON_._InitializeFacetMap(STD_ANON_._CF_enumeration)

# Atomic simple type: [anonymous]
class STD_ANON_2 (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/Users/blb/Downloads/regrws-rnc/NetPayload.xsd', 101, 4)
    _Documentation = None
STD_ANON_2._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=STD_ANON_2, enum_prefix=None)
STD_ANON_2.IU = STD_ANON_2._CF_enumeration.addEnumeration(unicode_value=u'IU', tag=u'IU')
STD_ANON_2.IR = STD_ANON_2._CF_enumeration.addEnumeration(unicode_value=u'IR', tag=u'IR')
STD_ANON_2.AF = STD_ANON_2._CF_enumeration.addEnumeration(unicode_value=u'AF', tag=u'AF')
STD_ANON_2.AP = STD_ANON_2._CF_enumeration.addEnumeration(unicode_value=u'AP', tag=u'AP')
STD_ANON_2.AR = STD_ANON_2._CF_enumeration.addEnumeration(unicode_value=u'AR', tag=u'AR')
STD_ANON_2.LN = STD_ANON_2._CF_enumeration.addEnumeration(unicode_value=u'LN', tag=u'LN')
STD_ANON_2.RN = STD_ANON_2._CF_enumeration.addEnumeration(unicode_value=u'RN', tag=u'RN')
STD_ANON_2.RD = STD_ANON_2._CF_enumeration.addEnumeration(unicode_value=u'RD', tag=u'RD')
STD_ANON_2.PV = STD_ANON_2._CF_enumeration.addEnumeration(unicode_value=u'PV', tag=u'PV')
STD_ANON_2.AV = STD_ANON_2._CF_enumeration.addEnumeration(unicode_value=u'AV', tag=u'AV')
STD_ANON_2.RV = STD_ANON_2._CF_enumeration.addEnumeration(unicode_value=u'RV', tag=u'RV')
STD_ANON_2.LX = STD_ANON_2._CF_enumeration.addEnumeration(unicode_value=u'LX', tag=u'LX')
STD_ANON_2.PX = STD_ANON_2._CF_enumeration.addEnumeration(unicode_value=u'PX', tag=u'PX')
STD_ANON_2.RX = STD_ANON_2._CF_enumeration.addEnumeration(unicode_value=u'RX', tag=u'RX')
STD_ANON_2.FX = STD_ANON_2._CF_enumeration.addEnumeration(unicode_value=u'FX', tag=u'FX')
STD_ANON_2.DA = STD_ANON_2._CF_enumeration.addEnumeration(unicode_value=u'DA', tag=u'DA')
STD_ANON_2.DS = STD_ANON_2._CF_enumeration.addEnumeration(unicode_value=u'DS', tag=u'DS')
STD_ANON_2.A = STD_ANON_2._CF_enumeration.addEnumeration(unicode_value=u'A', tag=u'A')
STD_ANON_2.S = STD_ANON_2._CF_enumeration.addEnumeration(unicode_value=u'S', tag=u'S')
STD_ANON_2._InitializeFacetMap(STD_ANON_2._CF_enumeration)

# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/Users/blb/Downloads/regrws-rnc/NetPayload.xsd', 4, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.arin.net/regrws/core/v1}customerHandle uses Python identifier customerHandle
    __customerHandle = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'customerHandle'), 'customerHandle', '__httpwww_arin_netregrwscorev1_CTD_ANON_httpwww_arin_netregrwscorev1customerHandle', True, pyxb.utils.utility.Location('/Users/blb/Downloads/regrws-rnc/NetPayload.xsd', 49, 2), )

    
    customerHandle = property(__customerHandle.value, __customerHandle.set, None, None)

    
    # Element {http://www.arin.net/regrws/core/v1}netBlocks uses Python identifier netBlocks
    __netBlocks = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'netBlocks'), 'netBlocks', '__httpwww_arin_netregrwscorev1_CTD_ANON_httpwww_arin_netregrwscorev1netBlocks', True, pyxb.utils.utility.Location('/Users/blb/Downloads/regrws-rnc/NetPayload.xsd', 50, 2), )

    
    netBlocks = property(__netBlocks.value, __netBlocks.set, None, None)

    
    # Element {http://www.arin.net/regrws/core/v1}handle uses Python identifier handle
    __handle = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'handle'), 'handle', '__httpwww_arin_netregrwscorev1_CTD_ANON_httpwww_arin_netregrwscorev1handle', True, pyxb.utils.utility.Location('/Users/blb/Downloads/regrws-rnc/NetPayload.xsd', 57, 2), )

    
    handle = property(__handle.value, __handle.set, None, None)

    
    # Element {http://www.arin.net/regrws/core/v1}netName uses Python identifier netName
    __netName = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'netName'), 'netName', '__httpwww_arin_netregrwscorev1_CTD_ANON_httpwww_arin_netregrwscorev1netName', True, pyxb.utils.utility.Location('/Users/blb/Downloads/regrws-rnc/NetPayload.xsd', 58, 2), )

    
    netName = property(__netName.value, __netName.set, None, None)

    
    # Element {http://www.arin.net/regrws/core/v1}orgHandle uses Python identifier orgHandle
    __orgHandle = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'orgHandle'), 'orgHandle', '__httpwww_arin_netregrwscorev1_CTD_ANON_httpwww_arin_netregrwscorev1orgHandle', True, pyxb.utils.utility.Location('/Users/blb/Downloads/regrws-rnc/NetPayload.xsd', 59, 2), )

    
    orgHandle = property(__orgHandle.value, __orgHandle.set, None, None)

    
    # Element {http://www.arin.net/regrws/core/v1}originASes uses Python identifier originASes
    __originASes = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'originASes'), 'originASes', '__httpwww_arin_netregrwscorev1_CTD_ANON_httpwww_arin_netregrwscorev1originASes', True, pyxb.utils.utility.Location('/Users/blb/Downloads/regrws-rnc/NetPayload.xsd', 60, 2), )

    
    originASes = property(__originASes.value, __originASes.set, None, None)

    
    # Element {http://www.arin.net/regrws/core/v1}parentNetHandle uses Python identifier parentNetHandle
    __parentNetHandle = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'parentNetHandle'), 'parentNetHandle', '__httpwww_arin_netregrwscorev1_CTD_ANON_httpwww_arin_netregrwscorev1parentNetHandle', True, pyxb.utils.utility.Location('/Users/blb/Downloads/regrws-rnc/NetPayload.xsd', 67, 2), )

    
    parentNetHandle = property(__parentNetHandle.value, __parentNetHandle.set, None, None)

    
    # Element {http://www.arin.net/regrws/core/v1}registrationDate uses Python identifier registrationDate
    __registrationDate = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'registrationDate'), 'registrationDate', '__httpwww_arin_netregrwscorev1_CTD_ANON_httpwww_arin_netregrwscorev1registrationDate', True, pyxb.utils.utility.Location('/Users/blb/Downloads/regrws-rnc/NetPayload.xsd', 68, 2), )

    
    registrationDate = property(__registrationDate.value, __registrationDate.set, None, None)

    
    # Element {http://www.arin.net/regrws/core/v1}pocLinks uses Python identifier pocLinks
    __pocLinks = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'pocLinks'), 'pocLinks', '__httpwww_arin_netregrwscorev1_CTD_ANON_httpwww_arin_netregrwscorev1pocLinks', True, pyxb.utils.utility.Location('/Users/blb/Downloads/regrws-rnc/NetPayload.xsd', 69, 2), )

    
    pocLinks = property(__pocLinks.value, __pocLinks.set, None, None)

    
    # Element {http://www.arin.net/regrws/core/v1}version uses Python identifier version
    __version = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'version'), 'version', '__httpwww_arin_netregrwscorev1_CTD_ANON_httpwww_arin_netregrwscorev1version', True, pyxb.utils.utility.Location('/Users/blb/Downloads/regrws-rnc/NetPayload.xsd', 76, 2), )

    
    version = property(__version.value, __version.set, None, None)

    
    # Element {http://www.arin.net/regrws/core/v1}comment uses Python identifier comment
    __comment = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'comment'), 'comment', '__httpwww_arin_netregrwscorev1_CTD_ANON_httpwww_arin_netregrwscorev1comment', True, pyxb.utils.utility.Location('/Users/blb/Downloads/regrws-rnc/NetPayload.xsd', 84, 2), )

    
    comment = property(__comment.value, __comment.set, None, None)

    _HasWildcardElement = True
    _ElementMap.update({
        __customerHandle.name() : __customerHandle,
        __netBlocks.name() : __netBlocks,
        __handle.name() : __handle,
        __netName.name() : __netName,
        __orgHandle.name() : __orgHandle,
        __originASes.name() : __originASes,
        __parentNetHandle.name() : __parentNetHandle,
        __registrationDate.name() : __registrationDate,
        __pocLinks.name() : __pocLinks,
        __version.name() : __version,
        __comment.name() : __comment
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
    _XSDLocation = pyxb.utils.utility.Location('/Users/blb/Downloads/regrws-rnc/NetPayload.xsd', 22, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.arin.net/regrws/core/v1}cidrLength uses Python identifier cidrLength
    __cidrLength = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'cidrLength'), 'cidrLength', '__httpwww_arin_netregrwscorev1_CTD_ANON__httpwww_arin_netregrwscorev1cidrLength', True, pyxb.utils.utility.Location('/Users/blb/Downloads/regrws-rnc/NetPayload.xsd', 96, 2), )

    
    cidrLength = property(__cidrLength.value, __cidrLength.set, None, None)

    
    # Element {http://www.arin.net/regrws/core/v1}description uses Python identifier description
    __description = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'description'), 'description', '__httpwww_arin_netregrwscorev1_CTD_ANON__httpwww_arin_netregrwscorev1description', True, pyxb.utils.utility.Location('/Users/blb/Downloads/regrws-rnc/NetPayload.xsd', 97, 2), )

    
    description = property(__description.value, __description.set, None, None)

    
    # Element {http://www.arin.net/regrws/core/v1}endAddress uses Python identifier endAddress
    __endAddress = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'endAddress'), 'endAddress', '__httpwww_arin_netregrwscorev1_CTD_ANON__httpwww_arin_netregrwscorev1endAddress', True, pyxb.utils.utility.Location('/Users/blb/Downloads/regrws-rnc/NetPayload.xsd', 98, 2), )

    
    endAddress = property(__endAddress.value, __endAddress.set, None, None)

    
    # Element {http://www.arin.net/regrws/core/v1}startAddress uses Python identifier startAddress
    __startAddress = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'startAddress'), 'startAddress', '__httpwww_arin_netregrwscorev1_CTD_ANON__httpwww_arin_netregrwscorev1startAddress', True, pyxb.utils.utility.Location('/Users/blb/Downloads/regrws-rnc/NetPayload.xsd', 99, 2), )

    
    startAddress = property(__startAddress.value, __startAddress.set, None, None)

    
    # Element {http://www.arin.net/regrws/core/v1}type uses Python identifier type
    __type = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'type'), 'type', '__httpwww_arin_netregrwscorev1_CTD_ANON__httpwww_arin_netregrwscorev1type', True, pyxb.utils.utility.Location('/Users/blb/Downloads/regrws-rnc/NetPayload.xsd', 100, 2), )

    
    type = property(__type.value, __type.set, None, None)

    _HasWildcardElement = True
    _ElementMap.update({
        __cidrLength.name() : __cidrLength,
        __description.name() : __description,
        __endAddress.name() : __endAddress,
        __startAddress.name() : __startAddress,
        __type.name() : __type
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
    _XSDLocation = pyxb.utils.utility.Location('/Users/blb/Downloads/regrws-rnc/NetPayload.xsd', 51, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.arin.net/regrws/core/v1}netBlock uses Python identifier netBlock
    __netBlock = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'netBlock'), 'netBlock', '__httpwww_arin_netregrwscorev1_CTD_ANON_2_httpwww_arin_netregrwscorev1netBlock', True, pyxb.utils.utility.Location('/Users/blb/Downloads/regrws-rnc/NetPayload.xsd', 21, 2), )

    
    netBlock = property(__netBlock.value, __netBlock.set, None, None)

    _ElementMap.update({
        __netBlock.name() : __netBlock
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
    _XSDLocation = pyxb.utils.utility.Location('/Users/blb/Downloads/regrws-rnc/NetPayload.xsd', 61, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.arin.net/regrws/core/v1}originAS uses Python identifier originAS
    __originAS = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'originAS'), 'originAS', '__httpwww_arin_netregrwscorev1_CTD_ANON_3_httpwww_arin_netregrwscorev1originAS', True, pyxb.utils.utility.Location('/Users/blb/Downloads/regrws-rnc/NetPayload.xsd', 130, 2), )

    
    originAS = property(__originAS.value, __originAS.set, None, None)

    _ElementMap.update({
        __originAS.name() : __originAS
    })
    _AttributeMap.update({
        
    })



# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_4 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/Users/blb/Downloads/regrws-rnc/NetPayload.xsd', 70, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.arin.net/regrws/core/v1}pocLinkRef uses Python identifier pocLinkRef
    __pocLinkRef = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'pocLinkRef'), 'pocLinkRef', '__httpwww_arin_netregrwscorev1_CTD_ANON_4_httpwww_arin_netregrwscorev1pocLinkRef', True, pyxb.utils.utility.Location('/Users/blb/Downloads/regrws-rnc/NetPayload.xsd', 33, 2), )

    
    pocLinkRef = property(__pocLinkRef.value, __pocLinkRef.set, None, None)

    _ElementMap.update({
        __pocLinkRef.name() : __pocLinkRef
    })
    _AttributeMap.update({
        
    })



# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_5 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/Users/blb/Downloads/regrws-rnc/NetPayload.xsd', 85, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.arin.net/regrws/core/v1}line uses Python identifier line
    __line = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'line'), 'line', '__httpwww_arin_netregrwscorev1_CTD_ANON_5_httpwww_arin_netregrwscorev1line', True, pyxb.utils.utility.Location('/Users/blb/Downloads/regrws-rnc/NetPayload.xsd', 131, 2), )

    
    line = property(__line.value, __line.set, None, None)

    _ElementMap.update({
        __line.name() : __line
    })
    _AttributeMap.update({
        
    })



# Complex type [anonymous] with content type SIMPLE
class CTD_ANON_6 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type SIMPLE"""
    _TypeDefinition = pyxb.binding.datatypes.string
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/Users/blb/Downloads/regrws-rnc/NetPayload.xsd', 132, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.string
    
    # Attribute number uses Python identifier number
    __number = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'number'), 'number', '__httpwww_arin_netregrwscorev1_CTD_ANON_6_number', pyxb.binding.datatypes.integer, required=True)
    __number._DeclarationLocation = pyxb.utils.utility.Location('/Users/blb/Downloads/regrws-rnc/NetPayload.xsd', 135, 10)
    __number._UseLocation = pyxb.utils.utility.Location('/Users/blb/Downloads/regrws-rnc/NetPayload.xsd', 135, 10)
    
    number = property(__number.value, __number.set, None, None)

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __number.name() : __number
    })



# Complex type [anonymous] with content type EMPTY
class CTD_ANON_7 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type EMPTY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_EMPTY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/Users/blb/Downloads/regrws-rnc/NetPayload.xsd', 34, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Attribute handle uses Python identifier handle
    __handle = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'handle'), 'handle', '__httpwww_arin_netregrwscorev1_CTD_ANON_7_handle', pyxb.binding.datatypes.string)
    __handle._DeclarationLocation = pyxb.utils.utility.Location('/Users/blb/Downloads/regrws-rnc/NetPayload.xsd', 35, 6)
    __handle._UseLocation = pyxb.utils.utility.Location('/Users/blb/Downloads/regrws-rnc/NetPayload.xsd', 35, 6)
    
    handle = property(__handle.value, __handle.set, None, None)

    
    # Attribute function uses Python identifier function
    __function = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'function'), 'function', '__httpwww_arin_netregrwscorev1_CTD_ANON_7_function', STD_ANON, required=True)
    __function._DeclarationLocation = pyxb.utils.utility.Location('/Users/blb/Downloads/regrws-rnc/NetPayload.xsd', 36, 6)
    __function._UseLocation = pyxb.utils.utility.Location('/Users/blb/Downloads/regrws-rnc/NetPayload.xsd', 36, 6)
    
    function = property(__function.value, __function.set, None, None)

    
    # Attribute description uses Python identifier description
    __description = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'description'), 'description', '__httpwww_arin_netregrwscorev1_CTD_ANON_7_description', pyxb.binding.datatypes.string)
    __description._DeclarationLocation = pyxb.utils.utility.Location('/Users/blb/Downloads/regrws-rnc/NetPayload.xsd', 46, 6)
    __description._UseLocation = pyxb.utils.utility.Location('/Users/blb/Downloads/regrws-rnc/NetPayload.xsd', 46, 6)
    
    description = property(__description.value, __description.set, None, None)

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __handle.name() : __handle,
        __function.name() : __function,
        __description.name() : __description
    })



customerHandle = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'customerHandle'), pyxb.binding.datatypes.string, location=pyxb.utils.utility.Location('/Users/blb/Downloads/regrws-rnc/NetPayload.xsd', 49, 2))
Namespace.addCategoryObject('elementBinding', customerHandle.name().localName(), customerHandle)

handle = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'handle'), pyxb.binding.datatypes.string, location=pyxb.utils.utility.Location('/Users/blb/Downloads/regrws-rnc/NetPayload.xsd', 57, 2))
Namespace.addCategoryObject('elementBinding', handle.name().localName(), handle)

netName = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'netName'), pyxb.binding.datatypes.string, location=pyxb.utils.utility.Location('/Users/blb/Downloads/regrws-rnc/NetPayload.xsd', 58, 2))
Namespace.addCategoryObject('elementBinding', netName.name().localName(), netName)

orgHandle = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'orgHandle'), pyxb.binding.datatypes.string, location=pyxb.utils.utility.Location('/Users/blb/Downloads/regrws-rnc/NetPayload.xsd', 59, 2))
Namespace.addCategoryObject('elementBinding', orgHandle.name().localName(), orgHandle)

parentNetHandle = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'parentNetHandle'), pyxb.binding.datatypes.string, location=pyxb.utils.utility.Location('/Users/blb/Downloads/regrws-rnc/NetPayload.xsd', 67, 2))
Namespace.addCategoryObject('elementBinding', parentNetHandle.name().localName(), parentNetHandle)

registrationDate = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'registrationDate'), pyxb.binding.datatypes.string, location=pyxb.utils.utility.Location('/Users/blb/Downloads/regrws-rnc/NetPayload.xsd', 68, 2))
Namespace.addCategoryObject('elementBinding', registrationDate.name().localName(), registrationDate)

cidrLength = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'cidrLength'), pyxb.binding.datatypes.string, location=pyxb.utils.utility.Location('/Users/blb/Downloads/regrws-rnc/NetPayload.xsd', 96, 2))
Namespace.addCategoryObject('elementBinding', cidrLength.name().localName(), cidrLength)

description = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'description'), pyxb.binding.datatypes.string, location=pyxb.utils.utility.Location('/Users/blb/Downloads/regrws-rnc/NetPayload.xsd', 97, 2))
Namespace.addCategoryObject('elementBinding', description.name().localName(), description)

endAddress = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'endAddress'), pyxb.binding.datatypes.string, location=pyxb.utils.utility.Location('/Users/blb/Downloads/regrws-rnc/NetPayload.xsd', 98, 2))
Namespace.addCategoryObject('elementBinding', endAddress.name().localName(), endAddress)

startAddress = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'startAddress'), pyxb.binding.datatypes.string, location=pyxb.utils.utility.Location('/Users/blb/Downloads/regrws-rnc/NetPayload.xsd', 99, 2))
Namespace.addCategoryObject('elementBinding', startAddress.name().localName(), startAddress)

originAS = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'originAS'), pyxb.binding.datatypes.string, location=pyxb.utils.utility.Location('/Users/blb/Downloads/regrws-rnc/NetPayload.xsd', 130, 2))
Namespace.addCategoryObject('elementBinding', originAS.name().localName(), originAS)

net = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'net'), CTD_ANON, location=pyxb.utils.utility.Location('/Users/blb/Downloads/regrws-rnc/NetPayload.xsd', 3, 2))
Namespace.addCategoryObject('elementBinding', net.name().localName(), net)

netBlock = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'netBlock'), CTD_ANON_, location=pyxb.utils.utility.Location('/Users/blb/Downloads/regrws-rnc/NetPayload.xsd', 21, 2))
Namespace.addCategoryObject('elementBinding', netBlock.name().localName(), netBlock)

netBlocks = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'netBlocks'), CTD_ANON_2, location=pyxb.utils.utility.Location('/Users/blb/Downloads/regrws-rnc/NetPayload.xsd', 50, 2))
Namespace.addCategoryObject('elementBinding', netBlocks.name().localName(), netBlocks)

originASes = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'originASes'), CTD_ANON_3, location=pyxb.utils.utility.Location('/Users/blb/Downloads/regrws-rnc/NetPayload.xsd', 60, 2))
Namespace.addCategoryObject('elementBinding', originASes.name().localName(), originASes)

pocLinks = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'pocLinks'), CTD_ANON_4, location=pyxb.utils.utility.Location('/Users/blb/Downloads/regrws-rnc/NetPayload.xsd', 69, 2))
Namespace.addCategoryObject('elementBinding', pocLinks.name().localName(), pocLinks)

version = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'version'), STD_ANON_, location=pyxb.utils.utility.Location('/Users/blb/Downloads/regrws-rnc/NetPayload.xsd', 76, 2))
Namespace.addCategoryObject('elementBinding', version.name().localName(), version)

comment = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'comment'), CTD_ANON_5, location=pyxb.utils.utility.Location('/Users/blb/Downloads/regrws-rnc/NetPayload.xsd', 84, 2))
Namespace.addCategoryObject('elementBinding', comment.name().localName(), comment)

type = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'type'), STD_ANON_2, location=pyxb.utils.utility.Location('/Users/blb/Downloads/regrws-rnc/NetPayload.xsd', 100, 2))
Namespace.addCategoryObject('elementBinding', type.name().localName(), type)

line = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'line'), CTD_ANON_6, location=pyxb.utils.utility.Location('/Users/blb/Downloads/regrws-rnc/NetPayload.xsd', 131, 2))
Namespace.addCategoryObject('elementBinding', line.name().localName(), line)

pocLinkRef = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'pocLinkRef'), CTD_ANON_7, location=pyxb.utils.utility.Location('/Users/blb/Downloads/regrws-rnc/NetPayload.xsd', 33, 2))
Namespace.addCategoryObject('elementBinding', pocLinkRef.name().localName(), pocLinkRef)



CTD_ANON._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'customerHandle'), pyxb.binding.datatypes.string, scope=CTD_ANON, location=pyxb.utils.utility.Location('/Users/blb/Downloads/regrws-rnc/NetPayload.xsd', 49, 2)))

CTD_ANON._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'netBlocks'), CTD_ANON_2, scope=CTD_ANON, location=pyxb.utils.utility.Location('/Users/blb/Downloads/regrws-rnc/NetPayload.xsd', 50, 2)))

CTD_ANON._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'handle'), pyxb.binding.datatypes.string, scope=CTD_ANON, location=pyxb.utils.utility.Location('/Users/blb/Downloads/regrws-rnc/NetPayload.xsd', 57, 2)))

CTD_ANON._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'netName'), pyxb.binding.datatypes.string, scope=CTD_ANON, location=pyxb.utils.utility.Location('/Users/blb/Downloads/regrws-rnc/NetPayload.xsd', 58, 2)))

CTD_ANON._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'orgHandle'), pyxb.binding.datatypes.string, scope=CTD_ANON, location=pyxb.utils.utility.Location('/Users/blb/Downloads/regrws-rnc/NetPayload.xsd', 59, 2)))

CTD_ANON._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'originASes'), CTD_ANON_3, scope=CTD_ANON, location=pyxb.utils.utility.Location('/Users/blb/Downloads/regrws-rnc/NetPayload.xsd', 60, 2)))

CTD_ANON._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'parentNetHandle'), pyxb.binding.datatypes.string, scope=CTD_ANON, location=pyxb.utils.utility.Location('/Users/blb/Downloads/regrws-rnc/NetPayload.xsd', 67, 2)))

CTD_ANON._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'registrationDate'), pyxb.binding.datatypes.string, scope=CTD_ANON, location=pyxb.utils.utility.Location('/Users/blb/Downloads/regrws-rnc/NetPayload.xsd', 68, 2)))

CTD_ANON._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'pocLinks'), CTD_ANON_4, scope=CTD_ANON, location=pyxb.utils.utility.Location('/Users/blb/Downloads/regrws-rnc/NetPayload.xsd', 69, 2)))

CTD_ANON._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'version'), STD_ANON_, scope=CTD_ANON, location=pyxb.utils.utility.Location('/Users/blb/Downloads/regrws-rnc/NetPayload.xsd', 76, 2)))

CTD_ANON._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'comment'), CTD_ANON_5, scope=CTD_ANON, location=pyxb.utils.utility.Location('/Users/blb/Downloads/regrws-rnc/NetPayload.xsd', 84, 2)))

def _BuildAutomaton ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton
    del _BuildAutomaton
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location('/Users/blb/Downloads/regrws-rnc/NetPayload.xsd', 5, 6))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'customerHandle')), pyxb.utils.utility.Location('/Users/blb/Downloads/regrws-rnc/NetPayload.xsd', 6, 8))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'netBlocks')), pyxb.utils.utility.Location('/Users/blb/Downloads/regrws-rnc/NetPayload.xsd', 7, 8))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'handle')), pyxb.utils.utility.Location('/Users/blb/Downloads/regrws-rnc/NetPayload.xsd', 8, 8))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'netName')), pyxb.utils.utility.Location('/Users/blb/Downloads/regrws-rnc/NetPayload.xsd', 9, 8))
    st_3 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'orgHandle')), pyxb.utils.utility.Location('/Users/blb/Downloads/regrws-rnc/NetPayload.xsd', 10, 8))
    st_4 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'originASes')), pyxb.utils.utility.Location('/Users/blb/Downloads/regrws-rnc/NetPayload.xsd', 11, 8))
    st_5 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'parentNetHandle')), pyxb.utils.utility.Location('/Users/blb/Downloads/regrws-rnc/NetPayload.xsd', 12, 8))
    st_6 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_6)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'registrationDate')), pyxb.utils.utility.Location('/Users/blb/Downloads/regrws-rnc/NetPayload.xsd', 13, 8))
    st_7 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_7)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'pocLinks')), pyxb.utils.utility.Location('/Users/blb/Downloads/regrws-rnc/NetPayload.xsd', 14, 8))
    st_8 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_8)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'version')), pyxb.utils.utility.Location('/Users/blb/Downloads/regrws-rnc/NetPayload.xsd', 15, 8))
    st_9 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_9)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'comment')), pyxb.utils.utility.Location('/Users/blb/Downloads/regrws-rnc/NetPayload.xsd', 16, 8))
    st_10 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_10)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.WildcardUse(pyxb.binding.content.Wildcard(process_contents=pyxb.binding.content.Wildcard.PC_skip, namespace_constraint=pyxb.binding.content.Wildcard.NC_any), pyxb.utils.utility.Location('/Users/blb/Downloads/regrws-rnc/NetPayload.xsd', 93, 6))
    st_11 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_11)
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
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_11, [
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
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_11, [
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
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_11, [
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
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_11, [
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
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_4._set_transitionSet(transitions)
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
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_5._set_transitionSet(transitions)
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
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_6._set_transitionSet(transitions)
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
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_7._set_transitionSet(transitions)
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
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_8._set_transitionSet(transitions)
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
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_9._set_transitionSet(transitions)
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
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_10._set_transitionSet(transitions)
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
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_11._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
CTD_ANON._Automaton = _BuildAutomaton()




CTD_ANON_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'cidrLength'), pyxb.binding.datatypes.string, scope=CTD_ANON_, location=pyxb.utils.utility.Location('/Users/blb/Downloads/regrws-rnc/NetPayload.xsd', 96, 2)))

CTD_ANON_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'description'), pyxb.binding.datatypes.string, scope=CTD_ANON_, location=pyxb.utils.utility.Location('/Users/blb/Downloads/regrws-rnc/NetPayload.xsd', 97, 2)))

CTD_ANON_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'endAddress'), pyxb.binding.datatypes.string, scope=CTD_ANON_, location=pyxb.utils.utility.Location('/Users/blb/Downloads/regrws-rnc/NetPayload.xsd', 98, 2)))

CTD_ANON_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'startAddress'), pyxb.binding.datatypes.string, scope=CTD_ANON_, location=pyxb.utils.utility.Location('/Users/blb/Downloads/regrws-rnc/NetPayload.xsd', 99, 2)))

CTD_ANON_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'type'), STD_ANON_2, scope=CTD_ANON_, location=pyxb.utils.utility.Location('/Users/blb/Downloads/regrws-rnc/NetPayload.xsd', 100, 2)))

def _BuildAutomaton_ ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_
    del _BuildAutomaton_
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location('/Users/blb/Downloads/regrws-rnc/NetPayload.xsd', 23, 6))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'cidrLength')), pyxb.utils.utility.Location('/Users/blb/Downloads/regrws-rnc/NetPayload.xsd', 24, 8))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'description')), pyxb.utils.utility.Location('/Users/blb/Downloads/regrws-rnc/NetPayload.xsd', 25, 8))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'endAddress')), pyxb.utils.utility.Location('/Users/blb/Downloads/regrws-rnc/NetPayload.xsd', 26, 8))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'startAddress')), pyxb.utils.utility.Location('/Users/blb/Downloads/regrws-rnc/NetPayload.xsd', 27, 8))
    st_3 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'type')), pyxb.utils.utility.Location('/Users/blb/Downloads/regrws-rnc/NetPayload.xsd', 28, 8))
    st_4 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.WildcardUse(pyxb.binding.content.Wildcard(process_contents=pyxb.binding.content.Wildcard.PC_skip, namespace_constraint=pyxb.binding.content.Wildcard.NC_any), pyxb.utils.utility.Location('/Users/blb/Downloads/regrws-rnc/NetPayload.xsd', 127, 6))
    st_5 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
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
    transitions.append(fac.Transition(st_5, [
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
    transitions.append(fac.Transition(st_5, [
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
    transitions.append(fac.Transition(st_5, [
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
    transitions.append(fac.Transition(st_5, [
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
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_4._set_transitionSet(transitions)
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
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_5._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
CTD_ANON_._Automaton = _BuildAutomaton_()




CTD_ANON_2._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'netBlock'), CTD_ANON_, scope=CTD_ANON_2, location=pyxb.utils.utility.Location('/Users/blb/Downloads/regrws-rnc/NetPayload.xsd', 21, 2)))

def _BuildAutomaton_2 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_2
    del _BuildAutomaton_2
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location('/Users/blb/Downloads/regrws-rnc/NetPayload.xsd', 53, 8))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_2._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'netBlock')), pyxb.utils.utility.Location('/Users/blb/Downloads/regrws-rnc/NetPayload.xsd', 53, 8))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
CTD_ANON_2._Automaton = _BuildAutomaton_2()




CTD_ANON_3._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'originAS'), pyxb.binding.datatypes.string, scope=CTD_ANON_3, location=pyxb.utils.utility.Location('/Users/blb/Downloads/regrws-rnc/NetPayload.xsd', 130, 2)))

def _BuildAutomaton_3 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_3
    del _BuildAutomaton_3
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location('/Users/blb/Downloads/regrws-rnc/NetPayload.xsd', 63, 8))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_3._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'originAS')), pyxb.utils.utility.Location('/Users/blb/Downloads/regrws-rnc/NetPayload.xsd', 63, 8))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
CTD_ANON_3._Automaton = _BuildAutomaton_3()




CTD_ANON_4._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'pocLinkRef'), CTD_ANON_7, scope=CTD_ANON_4, location=pyxb.utils.utility.Location('/Users/blb/Downloads/regrws-rnc/NetPayload.xsd', 33, 2)))

def _BuildAutomaton_4 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_4
    del _BuildAutomaton_4
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location('/Users/blb/Downloads/regrws-rnc/NetPayload.xsd', 72, 8))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_4._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'pocLinkRef')), pyxb.utils.utility.Location('/Users/blb/Downloads/regrws-rnc/NetPayload.xsd', 72, 8))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
CTD_ANON_4._Automaton = _BuildAutomaton_4()




CTD_ANON_5._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'line'), CTD_ANON_6, scope=CTD_ANON_5, location=pyxb.utils.utility.Location('/Users/blb/Downloads/regrws-rnc/NetPayload.xsd', 131, 2)))

def _BuildAutomaton_5 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_5
    del _BuildAutomaton_5
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location('/Users/blb/Downloads/regrws-rnc/NetPayload.xsd', 87, 8))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_5._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'line')), pyxb.utils.utility.Location('/Users/blb/Downloads/regrws-rnc/NetPayload.xsd', 87, 8))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
CTD_ANON_5._Automaton = _BuildAutomaton_5()

