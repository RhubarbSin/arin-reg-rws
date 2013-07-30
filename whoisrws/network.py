# ./network.py
# -*- coding: utf-8 -*-
# PyXB bindings for NM:731c564ed33c3937edbc70509e15a215587be0e4
# Generated 2013-07-12 14:22:45.841007 by PyXB version 1.2.2
# Namespace http://www.arin.net/whoisrws/core/v1

import pyxb
import pyxb.binding
import pyxb.binding.saxer
import StringIO
import pyxb.utils.utility
import pyxb.utils.domutils
import sys

# Unique identifier for bindings created at the same time
_GenerationUID = pyxb.utils.utility.UniqueIdentifier('urn:uuid:0c990478-eb20-11e2-8970-10ddb19be936')

# Version of PyXB used to generate the bindings
_PyXBVersion = '1.2.2'
# Generated bindings are not compatible across PyXB versions
if pyxb.__version__ != _PyXBVersion:
    raise pyxb.PyXBVersionError(_PyXBVersion)

# Import bindings for namespaces imported into schema
import pyxb.binding.datatypes

# NOTE: All namespace declarations are reserved within the binding
Namespace = pyxb.namespace.NamespaceForURI(u'http://www.arin.net/whoisrws/core/v1', create_if_missing=True)
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
    _XSDLocation = pyxb.utils.utility.Location('/Users/blb/Downloads/whoisrws-relaxng-compact-schemas/network.xsd', 4, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.arin.net/whoisrws/core/v1}registrationDate uses Python identifier registrationDate
    __registrationDate = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'registrationDate'), 'registrationDate', '__httpwww_arin_netwhoisrwscorev1_CTD_ANON_httpwww_arin_netwhoisrwscorev1registrationDate', True, pyxb.utils.utility.Location('/Users/blb/Downloads/whoisrws-relaxng-compact-schemas/network.xsd', 30, 2), )

    
    registrationDate = property(__registrationDate.value, __registrationDate.set, None, None)

    
    # Element {http://www.arin.net/whoisrws/core/v1}ref uses Python identifier ref
    __ref = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'ref'), 'ref', '__httpwww_arin_netwhoisrwscorev1_CTD_ANON_httpwww_arin_netwhoisrwscorev1ref', True, pyxb.utils.utility.Location('/Users/blb/Downloads/whoisrws-relaxng-compact-schemas/network.xsd', 31, 2), )

    
    ref = property(__ref.value, __ref.set, None, None)

    
    # Element {http://www.arin.net/whoisrws/core/v1}customerRef uses Python identifier customerRef
    __customerRef = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'customerRef'), 'customerRef', '__httpwww_arin_netwhoisrwscorev1_CTD_ANON_httpwww_arin_netwhoisrwscorev1customerRef', True, pyxb.utils.utility.Location('/Users/blb/Downloads/whoisrws-relaxng-compact-schemas/network.xsd', 32, 2), )

    
    customerRef = property(__customerRef.value, __customerRef.set, None, None)

    
    # Element {http://www.arin.net/whoisrws/core/v1}endAddress uses Python identifier endAddress
    __endAddress = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'endAddress'), 'endAddress', '__httpwww_arin_netwhoisrwscorev1_CTD_ANON_httpwww_arin_netwhoisrwscorev1endAddress', True, pyxb.utils.utility.Location('/Users/blb/Downloads/whoisrws-relaxng-compact-schemas/network.xsd', 42, 2), )

    
    endAddress = property(__endAddress.value, __endAddress.set, None, None)

    
    # Element {http://www.arin.net/whoisrws/core/v1}handle uses Python identifier handle
    __handle = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'handle'), 'handle', '__httpwww_arin_netwhoisrwscorev1_CTD_ANON_httpwww_arin_netwhoisrwscorev1handle', True, pyxb.utils.utility.Location('/Users/blb/Downloads/whoisrws-relaxng-compact-schemas/network.xsd', 43, 2), )

    
    handle = property(__handle.value, __handle.set, None, None)

    
    # Element {http://www.arin.net/whoisrws/core/v1}name uses Python identifier name
    __name = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'name'), 'name', '__httpwww_arin_netwhoisrwscorev1_CTD_ANON_httpwww_arin_netwhoisrwscorev1name', True, pyxb.utils.utility.Location('/Users/blb/Downloads/whoisrws-relaxng-compact-schemas/network.xsd', 44, 2), )

    
    name = property(__name.value, __name.set, None, None)

    
    # Element {http://www.arin.net/whoisrws/core/v1}nameservers uses Python identifier nameservers
    __nameservers = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'nameservers'), 'nameservers', '__httpwww_arin_netwhoisrwscorev1_CTD_ANON_httpwww_arin_netwhoisrwscorev1nameservers', True, pyxb.utils.utility.Location('/Users/blb/Downloads/whoisrws-relaxng-compact-schemas/network.xsd', 45, 2), )

    
    nameservers = property(__nameservers.value, __nameservers.set, None, None)

    
    # Element {http://www.arin.net/whoisrws/core/v1}netBlocks uses Python identifier netBlocks
    __netBlocks = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'netBlocks'), 'netBlocks', '__httpwww_arin_netwhoisrwscorev1_CTD_ANON_httpwww_arin_netwhoisrwscorev1netBlocks', True, pyxb.utils.utility.Location('/Users/blb/Downloads/whoisrws-relaxng-compact-schemas/network.xsd', 52, 2), )

    
    netBlocks = property(__netBlocks.value, __netBlocks.set, None, None)

    
    # Element {http://www.arin.net/whoisrws/core/v1}originASes uses Python identifier originASes
    __originASes = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'originASes'), 'originASes', '__httpwww_arin_netwhoisrwscorev1_CTD_ANON_httpwww_arin_netwhoisrwscorev1originASes', True, pyxb.utils.utility.Location('/Users/blb/Downloads/whoisrws-relaxng-compact-schemas/network.xsd', 59, 2), )

    
    originASes = property(__originASes.value, __originASes.set, None, None)

    
    # Element {http://www.arin.net/whoisrws/core/v1}pocs uses Python identifier pocs
    __pocs = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'pocs'), 'pocs', '__httpwww_arin_netwhoisrwscorev1_CTD_ANON_httpwww_arin_netwhoisrwscorev1pocs', True, pyxb.utils.utility.Location('/Users/blb/Downloads/whoisrws-relaxng-compact-schemas/network.xsd', 66, 2), )

    
    pocs = property(__pocs.value, __pocs.set, None, None)

    
    # Element {http://www.arin.net/whoisrws/core/v1}orgRef uses Python identifier orgRef
    __orgRef = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'orgRef'), 'orgRef', '__httpwww_arin_netwhoisrwscorev1_CTD_ANON_httpwww_arin_netwhoisrwscorev1orgRef', True, pyxb.utils.utility.Location('/Users/blb/Downloads/whoisrws-relaxng-compact-schemas/network.xsd', 79, 2), )

    
    orgRef = property(__orgRef.value, __orgRef.set, None, None)

    
    # Element {http://www.arin.net/whoisrws/core/v1}comment uses Python identifier comment
    __comment = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'comment'), 'comment', '__httpwww_arin_netwhoisrwscorev1_CTD_ANON_httpwww_arin_netwhoisrwscorev1comment', True, pyxb.utils.utility.Location('/Users/blb/Downloads/whoisrws-relaxng-compact-schemas/network.xsd', 89, 2), )

    
    comment = property(__comment.value, __comment.set, None, None)

    
    # Element {http://www.arin.net/whoisrws/core/v1}parentNetRef uses Python identifier parentNetRef
    __parentNetRef = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'parentNetRef'), 'parentNetRef', '__httpwww_arin_netwhoisrwscorev1_CTD_ANON_httpwww_arin_netwhoisrwscorev1parentNetRef', True, pyxb.utils.utility.Location('/Users/blb/Downloads/whoisrws-relaxng-compact-schemas/network.xsd', 96, 2), )

    
    parentNetRef = property(__parentNetRef.value, __parentNetRef.set, None, None)

    
    # Element {http://www.arin.net/whoisrws/core/v1}startAddress uses Python identifier startAddress
    __startAddress = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'startAddress'), 'startAddress', '__httpwww_arin_netwhoisrwscorev1_CTD_ANON_httpwww_arin_netwhoisrwscorev1startAddress', True, pyxb.utils.utility.Location('/Users/blb/Downloads/whoisrws-relaxng-compact-schemas/network.xsd', 106, 2), )

    
    startAddress = property(__startAddress.value, __startAddress.set, None, None)

    
    # Element {http://www.arin.net/whoisrws/core/v1}updateDate uses Python identifier updateDate
    __updateDate = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'updateDate'), 'updateDate', '__httpwww_arin_netwhoisrwscorev1_CTD_ANON_httpwww_arin_netwhoisrwscorev1updateDate', True, pyxb.utils.utility.Location('/Users/blb/Downloads/whoisrws-relaxng-compact-schemas/network.xsd', 107, 2), )

    
    updateDate = property(__updateDate.value, __updateDate.set, None, None)

    
    # Element {http://www.arin.net/whoisrws/core/v1}version uses Python identifier version
    __version = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'version'), 'version', '__httpwww_arin_netwhoisrwscorev1_CTD_ANON_httpwww_arin_netwhoisrwscorev1version', True, pyxb.utils.utility.Location('/Users/blb/Downloads/whoisrws-relaxng-compact-schemas/network.xsd', 108, 2), )

    
    version = property(__version.value, __version.set, None, None)

    
    # Attribute termsOfUse uses Python identifier termsOfUse
    __termsOfUse = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'termsOfUse'), 'termsOfUse', '__httpwww_arin_netwhoisrwscorev1_CTD_ANON_termsOfUse', pyxb.binding.datatypes.anyURI)
    __termsOfUse._DeclarationLocation = pyxb.utils.utility.Location('/Users/blb/Downloads/whoisrws-relaxng-compact-schemas/network.xsd', 27, 6)
    __termsOfUse._UseLocation = pyxb.utils.utility.Location('/Users/blb/Downloads/whoisrws-relaxng-compact-schemas/network.xsd', 27, 6)
    
    termsOfUse = property(__termsOfUse.value, __termsOfUse.set, None, None)

    _HasWildcardElement = True
    _ElementMap.update({
        __registrationDate.name() : __registrationDate,
        __ref.name() : __ref,
        __customerRef.name() : __customerRef,
        __endAddress.name() : __endAddress,
        __handle.name() : __handle,
        __name.name() : __name,
        __nameservers.name() : __nameservers,
        __netBlocks.name() : __netBlocks,
        __originASes.name() : __originASes,
        __pocs.name() : __pocs,
        __orgRef.name() : __orgRef,
        __comment.name() : __comment,
        __parentNetRef.name() : __parentNetRef,
        __startAddress.name() : __startAddress,
        __updateDate.name() : __updateDate,
        __version.name() : __version
    })
    _AttributeMap.update({
        __termsOfUse.name() : __termsOfUse
    })



# Complex type [anonymous] with content type SIMPLE
class CTD_ANON_ (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type SIMPLE"""
    _TypeDefinition = pyxb.binding.datatypes.anyURI
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/Users/blb/Downloads/whoisrws-relaxng-compact-schemas/network.xsd', 33, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyURI
    
    # Attribute handle uses Python identifier handle
    __handle = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'handle'), 'handle', '__httpwww_arin_netwhoisrwscorev1_CTD_ANON__handle', pyxb.binding.datatypes.anySimpleType, required=True)
    __handle._DeclarationLocation = pyxb.utils.utility.Location('/Users/blb/Downloads/whoisrws-relaxng-compact-schemas/network.xsd', 36, 10)
    __handle._UseLocation = pyxb.utils.utility.Location('/Users/blb/Downloads/whoisrws-relaxng-compact-schemas/network.xsd', 36, 10)
    
    handle = property(__handle.value, __handle.set, None, None)

    
    # Attribute name uses Python identifier name
    __name = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'name'), 'name', '__httpwww_arin_netwhoisrwscorev1_CTD_ANON__name', pyxb.binding.datatypes.anySimpleType, required=True)
    __name._DeclarationLocation = pyxb.utils.utility.Location('/Users/blb/Downloads/whoisrws-relaxng-compact-schemas/network.xsd', 37, 10)
    __name._UseLocation = pyxb.utils.utility.Location('/Users/blb/Downloads/whoisrws-relaxng-compact-schemas/network.xsd', 37, 10)
    
    name = property(__name.value, __name.set, None, None)

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __handle.name() : __handle,
        __name.name() : __name
    })



# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_2 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/Users/blb/Downloads/whoisrws-relaxng-compact-schemas/network.xsd', 46, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.arin.net/whoisrws/core/v1}nameserver uses Python identifier nameserver
    __nameserver = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'nameserver'), 'nameserver', '__httpwww_arin_netwhoisrwscorev1_CTD_ANON_2_httpwww_arin_netwhoisrwscorev1nameserver', True, pyxb.utils.utility.Location('/Users/blb/Downloads/whoisrws-relaxng-compact-schemas/network.xsd', 114, 2), )

    
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
    _XSDLocation = pyxb.utils.utility.Location('/Users/blb/Downloads/whoisrws-relaxng-compact-schemas/network.xsd', 53, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.arin.net/whoisrws/core/v1}netBlock uses Python identifier netBlock
    __netBlock = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'netBlock'), 'netBlock', '__httpwww_arin_netwhoisrwscorev1_CTD_ANON_3_httpwww_arin_netwhoisrwscorev1netBlock', True, pyxb.utils.utility.Location('/Users/blb/Downloads/whoisrws-relaxng-compact-schemas/network.xsd', 115, 2), )

    
    netBlock = property(__netBlock.value, __netBlock.set, None, None)

    _ElementMap.update({
        __netBlock.name() : __netBlock
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
    _XSDLocation = pyxb.utils.utility.Location('/Users/blb/Downloads/whoisrws-relaxng-compact-schemas/network.xsd', 60, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.arin.net/whoisrws/core/v1}originAS uses Python identifier originAS
    __originAS = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'originAS'), 'originAS', '__httpwww_arin_netwhoisrwscorev1_CTD_ANON_4_httpwww_arin_netwhoisrwscorev1originAS', True, pyxb.utils.utility.Location('/Users/blb/Downloads/whoisrws-relaxng-compact-schemas/network.xsd', 135, 2), )

    
    originAS = property(__originAS.value, __originAS.set, None, None)

    _ElementMap.update({
        __originAS.name() : __originAS
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
    _XSDLocation = pyxb.utils.utility.Location('/Users/blb/Downloads/whoisrws-relaxng-compact-schemas/network.xsd', 67, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.arin.net/whoisrws/core/v1}limitExceeded uses Python identifier limitExceeded
    __limitExceeded = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'limitExceeded'), 'limitExceeded', '__httpwww_arin_netwhoisrwscorev1_CTD_ANON_5_httpwww_arin_netwhoisrwscorev1limitExceeded', True, pyxb.utils.utility.Location('/Users/blb/Downloads/whoisrws-relaxng-compact-schemas/network.xsd', 136, 2), )

    
    limitExceeded = property(__limitExceeded.value, __limitExceeded.set, None, None)

    
    # Element {http://www.arin.net/whoisrws/core/v1}pocRef uses Python identifier pocRef
    __pocRef = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'pocRef'), 'pocRef', '__httpwww_arin_netwhoisrwscorev1_CTD_ANON_5_httpwww_arin_netwhoisrwscorev1pocRef', True, pyxb.utils.utility.Location('/Users/blb/Downloads/whoisrws-relaxng-compact-schemas/network.xsd', 145, 2), )

    
    pocRef = property(__pocRef.value, __pocRef.set, None, None)

    
    # Element {http://www.arin.net/whoisrws/core/v1}pocLinkRef uses Python identifier pocLinkRef
    __pocLinkRef = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'pocLinkRef'), 'pocLinkRef', '__httpwww_arin_netwhoisrwscorev1_CTD_ANON_5_httpwww_arin_netwhoisrwscorev1pocLinkRef', True, pyxb.utils.utility.Location('/Users/blb/Downloads/whoisrws-relaxng-compact-schemas/network.xsd', 155, 2), )

    
    pocLinkRef = property(__pocLinkRef.value, __pocLinkRef.set, None, None)

    
    # Attribute termsOfUse uses Python identifier termsOfUse
    __termsOfUse = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'termsOfUse'), 'termsOfUse', '__httpwww_arin_netwhoisrwscorev1_CTD_ANON_5_termsOfUse', pyxb.binding.datatypes.anyURI)
    __termsOfUse._DeclarationLocation = pyxb.utils.utility.Location('/Users/blb/Downloads/whoisrws-relaxng-compact-schemas/network.xsd', 76, 6)
    __termsOfUse._UseLocation = pyxb.utils.utility.Location('/Users/blb/Downloads/whoisrws-relaxng-compact-schemas/network.xsd', 76, 6)
    
    termsOfUse = property(__termsOfUse.value, __termsOfUse.set, None, None)

    _HasWildcardElement = True
    _ElementMap.update({
        __limitExceeded.name() : __limitExceeded,
        __pocRef.name() : __pocRef,
        __pocLinkRef.name() : __pocLinkRef
    })
    _AttributeMap.update({
        __termsOfUse.name() : __termsOfUse
    })



# Complex type [anonymous] with content type SIMPLE
class CTD_ANON_6 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type SIMPLE"""
    _TypeDefinition = pyxb.binding.datatypes.anyURI
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/Users/blb/Downloads/whoisrws-relaxng-compact-schemas/network.xsd', 80, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyURI
    
    # Attribute handle uses Python identifier handle
    __handle = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'handle'), 'handle', '__httpwww_arin_netwhoisrwscorev1_CTD_ANON_6_handle', pyxb.binding.datatypes.anySimpleType, required=True)
    __handle._DeclarationLocation = pyxb.utils.utility.Location('/Users/blb/Downloads/whoisrws-relaxng-compact-schemas/network.xsd', 83, 10)
    __handle._UseLocation = pyxb.utils.utility.Location('/Users/blb/Downloads/whoisrws-relaxng-compact-schemas/network.xsd', 83, 10)
    
    handle = property(__handle.value, __handle.set, None, None)

    
    # Attribute name uses Python identifier name
    __name = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'name'), 'name', '__httpwww_arin_netwhoisrwscorev1_CTD_ANON_6_name', pyxb.binding.datatypes.anySimpleType)
    __name._DeclarationLocation = pyxb.utils.utility.Location('/Users/blb/Downloads/whoisrws-relaxng-compact-schemas/network.xsd', 84, 10)
    __name._UseLocation = pyxb.utils.utility.Location('/Users/blb/Downloads/whoisrws-relaxng-compact-schemas/network.xsd', 84, 10)
    
    name = property(__name.value, __name.set, None, None)

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __handle.name() : __handle,
        __name.name() : __name
    })



# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_7 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/Users/blb/Downloads/whoisrws-relaxng-compact-schemas/network.xsd', 90, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.arin.net/whoisrws/core/v1}line uses Python identifier line
    __line = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'line'), 'line', '__httpwww_arin_netwhoisrwscorev1_CTD_ANON_7_httpwww_arin_netwhoisrwscorev1line', True, pyxb.utils.utility.Location('/Users/blb/Downloads/whoisrws-relaxng-compact-schemas/network.xsd', 171, 2), )

    
    line = property(__line.value, __line.set, None, None)

    _ElementMap.update({
        __line.name() : __line
    })
    _AttributeMap.update({
        
    })



# Complex type [anonymous] with content type SIMPLE
class CTD_ANON_8 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type SIMPLE"""
    _TypeDefinition = pyxb.binding.datatypes.anyURI
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/Users/blb/Downloads/whoisrws-relaxng-compact-schemas/network.xsd', 97, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyURI
    
    # Attribute handle uses Python identifier handle
    __handle = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'handle'), 'handle', '__httpwww_arin_netwhoisrwscorev1_CTD_ANON_8_handle', pyxb.binding.datatypes.anySimpleType, required=True)
    __handle._DeclarationLocation = pyxb.utils.utility.Location('/Users/blb/Downloads/whoisrws-relaxng-compact-schemas/network.xsd', 100, 10)
    __handle._UseLocation = pyxb.utils.utility.Location('/Users/blb/Downloads/whoisrws-relaxng-compact-schemas/network.xsd', 100, 10)
    
    handle = property(__handle.value, __handle.set, None, None)

    
    # Attribute name uses Python identifier name
    __name = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'name'), 'name', '__httpwww_arin_netwhoisrwscorev1_CTD_ANON_8_name', pyxb.binding.datatypes.anySimpleType)
    __name._DeclarationLocation = pyxb.utils.utility.Location('/Users/blb/Downloads/whoisrws-relaxng-compact-schemas/network.xsd', 101, 10)
    __name._UseLocation = pyxb.utils.utility.Location('/Users/blb/Downloads/whoisrws-relaxng-compact-schemas/network.xsd', 101, 10)
    
    name = property(__name.value, __name.set, None, None)

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __handle.name() : __handle,
        __name.name() : __name
    })



# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_9 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/Users/blb/Downloads/whoisrws-relaxng-compact-schemas/network.xsd', 116, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.arin.net/whoisrws/core/v1}ref uses Python identifier ref
    __ref = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'ref'), 'ref', '__httpwww_arin_netwhoisrwscorev1_CTD_ANON_9_httpwww_arin_netwhoisrwscorev1ref', True, pyxb.utils.utility.Location('/Users/blb/Downloads/whoisrws-relaxng-compact-schemas/network.xsd', 31, 2), )

    
    ref = property(__ref.value, __ref.set, None, None)

    
    # Element {http://www.arin.net/whoisrws/core/v1}endAddress uses Python identifier endAddress
    __endAddress = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'endAddress'), 'endAddress', '__httpwww_arin_netwhoisrwscorev1_CTD_ANON_9_httpwww_arin_netwhoisrwscorev1endAddress', True, pyxb.utils.utility.Location('/Users/blb/Downloads/whoisrws-relaxng-compact-schemas/network.xsd', 42, 2), )

    
    endAddress = property(__endAddress.value, __endAddress.set, None, None)

    
    # Element {http://www.arin.net/whoisrws/core/v1}startAddress uses Python identifier startAddress
    __startAddress = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'startAddress'), 'startAddress', '__httpwww_arin_netwhoisrwscorev1_CTD_ANON_9_httpwww_arin_netwhoisrwscorev1startAddress', True, pyxb.utils.utility.Location('/Users/blb/Downloads/whoisrws-relaxng-compact-schemas/network.xsd', 106, 2), )

    
    startAddress = property(__startAddress.value, __startAddress.set, None, None)

    
    # Element {http://www.arin.net/whoisrws/core/v1}addressRange uses Python identifier addressRange
    __addressRange = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'addressRange'), 'addressRange', '__httpwww_arin_netwhoisrwscorev1_CTD_ANON_9_httpwww_arin_netwhoisrwscorev1addressRange', True, pyxb.utils.utility.Location('/Users/blb/Downloads/whoisrws-relaxng-compact-schemas/network.xsd', 181, 2), )

    
    addressRange = property(__addressRange.value, __addressRange.set, None, None)

    
    # Element {http://www.arin.net/whoisrws/core/v1}netRef uses Python identifier netRef
    __netRef = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'netRef'), 'netRef', '__httpwww_arin_netwhoisrwscorev1_CTD_ANON_9_httpwww_arin_netwhoisrwscorev1netRef', True, pyxb.utils.utility.Location('/Users/blb/Downloads/whoisrws-relaxng-compact-schemas/network.xsd', 192, 2), )

    
    netRef = property(__netRef.value, __netRef.set, None, None)

    
    # Element {http://www.arin.net/whoisrws/core/v1}cidrLength uses Python identifier cidrLength
    __cidrLength = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'cidrLength'), 'cidrLength', '__httpwww_arin_netwhoisrwscorev1_CTD_ANON_9_httpwww_arin_netwhoisrwscorev1cidrLength', True, pyxb.utils.utility.Location('/Users/blb/Downloads/whoisrws-relaxng-compact-schemas/network.xsd', 204, 2), )

    
    cidrLength = property(__cidrLength.value, __cidrLength.set, None, None)

    
    # Element {http://www.arin.net/whoisrws/core/v1}description uses Python identifier description
    __description = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'description'), 'description', '__httpwww_arin_netwhoisrwscorev1_CTD_ANON_9_httpwww_arin_netwhoisrwscorev1description', True, pyxb.utils.utility.Location('/Users/blb/Downloads/whoisrws-relaxng-compact-schemas/network.xsd', 205, 2), )

    
    description = property(__description.value, __description.set, None, None)

    
    # Element {http://www.arin.net/whoisrws/core/v1}type uses Python identifier type
    __type = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'type'), 'type', '__httpwww_arin_netwhoisrwscorev1_CTD_ANON_9_httpwww_arin_netwhoisrwscorev1type', True, pyxb.utils.utility.Location('/Users/blb/Downloads/whoisrws-relaxng-compact-schemas/network.xsd', 206, 2), )

    
    type = property(__type.value, __type.set, None, None)

    
    # Attribute termsOfUse uses Python identifier termsOfUse
    __termsOfUse = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'termsOfUse'), 'termsOfUse', '__httpwww_arin_netwhoisrwscorev1_CTD_ANON_9_termsOfUse', pyxb.binding.datatypes.anyURI)
    __termsOfUse._DeclarationLocation = pyxb.utils.utility.Location('/Users/blb/Downloads/whoisrws-relaxng-compact-schemas/network.xsd', 132, 6)
    __termsOfUse._UseLocation = pyxb.utils.utility.Location('/Users/blb/Downloads/whoisrws-relaxng-compact-schemas/network.xsd', 132, 6)
    
    termsOfUse = property(__termsOfUse.value, __termsOfUse.set, None, None)

    _HasWildcardElement = True
    _ElementMap.update({
        __ref.name() : __ref,
        __endAddress.name() : __endAddress,
        __startAddress.name() : __startAddress,
        __addressRange.name() : __addressRange,
        __netRef.name() : __netRef,
        __cidrLength.name() : __cidrLength,
        __description.name() : __description,
        __type.name() : __type
    })
    _AttributeMap.update({
        __termsOfUse.name() : __termsOfUse
    })



# Complex type [anonymous] with content type SIMPLE
class CTD_ANON_10 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type SIMPLE"""
    _TypeDefinition = pyxb.binding.datatypes.boolean
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/Users/blb/Downloads/whoisrws-relaxng-compact-schemas/network.xsd', 137, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.boolean
    
    # Attribute limit uses Python identifier limit
    __limit = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'limit'), 'limit', '__httpwww_arin_netwhoisrwscorev1_CTD_ANON_10_limit', pyxb.binding.datatypes.integer, required=True)
    __limit._DeclarationLocation = pyxb.utils.utility.Location('/Users/blb/Downloads/whoisrws-relaxng-compact-schemas/network.xsd', 140, 10)
    __limit._UseLocation = pyxb.utils.utility.Location('/Users/blb/Downloads/whoisrws-relaxng-compact-schemas/network.xsd', 140, 10)
    
    limit = property(__limit.value, __limit.set, None, None)

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __limit.name() : __limit
    })



# Complex type [anonymous] with content type SIMPLE
class CTD_ANON_11 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type SIMPLE"""
    _TypeDefinition = pyxb.binding.datatypes.anyURI
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/Users/blb/Downloads/whoisrws-relaxng-compact-schemas/network.xsd', 146, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyURI
    
    # Attribute handle uses Python identifier handle
    __handle = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'handle'), 'handle', '__httpwww_arin_netwhoisrwscorev1_CTD_ANON_11_handle', pyxb.binding.datatypes.anySimpleType, required=True)
    __handle._DeclarationLocation = pyxb.utils.utility.Location('/Users/blb/Downloads/whoisrws-relaxng-compact-schemas/network.xsd', 149, 10)
    __handle._UseLocation = pyxb.utils.utility.Location('/Users/blb/Downloads/whoisrws-relaxng-compact-schemas/network.xsd', 149, 10)
    
    handle = property(__handle.value, __handle.set, None, None)

    
    # Attribute name uses Python identifier name
    __name = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'name'), 'name', '__httpwww_arin_netwhoisrwscorev1_CTD_ANON_11_name', pyxb.binding.datatypes.anySimpleType)
    __name._DeclarationLocation = pyxb.utils.utility.Location('/Users/blb/Downloads/whoisrws-relaxng-compact-schemas/network.xsd', 150, 10)
    __name._UseLocation = pyxb.utils.utility.Location('/Users/blb/Downloads/whoisrws-relaxng-compact-schemas/network.xsd', 150, 10)
    
    name = property(__name.value, __name.set, None, None)

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __handle.name() : __handle,
        __name.name() : __name
    })



# Complex type [anonymous] with content type SIMPLE
class CTD_ANON_12 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type SIMPLE"""
    _TypeDefinition = pyxb.binding.datatypes.anyURI
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/Users/blb/Downloads/whoisrws-relaxng-compact-schemas/network.xsd', 156, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyURI
    
    # Attribute handle uses Python identifier handle
    __handle = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'handle'), 'handle', '__httpwww_arin_netwhoisrwscorev1_CTD_ANON_12_handle', pyxb.binding.datatypes.anySimpleType, required=True)
    __handle._DeclarationLocation = pyxb.utils.utility.Location('/Users/blb/Downloads/whoisrws-relaxng-compact-schemas/network.xsd', 159, 10)
    __handle._UseLocation = pyxb.utils.utility.Location('/Users/blb/Downloads/whoisrws-relaxng-compact-schemas/network.xsd', 159, 10)
    
    handle = property(__handle.value, __handle.set, None, None)

    
    # Attribute function uses Python identifier function
    __function = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'function'), 'function', '__httpwww_arin_netwhoisrwscorev1_CTD_ANON_12_function', pyxb.binding.datatypes.anySimpleType)
    __function._DeclarationLocation = pyxb.utils.utility.Location('/Users/blb/Downloads/whoisrws-relaxng-compact-schemas/network.xsd', 160, 10)
    __function._UseLocation = pyxb.utils.utility.Location('/Users/blb/Downloads/whoisrws-relaxng-compact-schemas/network.xsd', 160, 10)
    
    function = property(__function.value, __function.set, None, None)

    
    # Attribute description uses Python identifier description
    __description = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'description'), 'description', '__httpwww_arin_netwhoisrwscorev1_CTD_ANON_12_description', pyxb.binding.datatypes.anySimpleType)
    __description._DeclarationLocation = pyxb.utils.utility.Location('/Users/blb/Downloads/whoisrws-relaxng-compact-schemas/network.xsd', 161, 10)
    __description._UseLocation = pyxb.utils.utility.Location('/Users/blb/Downloads/whoisrws-relaxng-compact-schemas/network.xsd', 161, 10)
    
    description = property(__description.value, __description.set, None, None)

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __handle.name() : __handle,
        __function.name() : __function,
        __description.name() : __description
    })



# Complex type [anonymous] with content type MIXED
class CTD_ANON_13 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type MIXED"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_MIXED
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/Users/blb/Downloads/whoisrws-relaxng-compact-schemas/network.xsd', 172, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Attribute number uses Python identifier number
    __number = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'number'), 'number', '__httpwww_arin_netwhoisrwscorev1_CTD_ANON_13_number', pyxb.binding.datatypes.integer, required=True)
    __number._DeclarationLocation = pyxb.utils.utility.Location('/Users/blb/Downloads/whoisrws-relaxng-compact-schemas/network.xsd', 173, 6)
    __number._UseLocation = pyxb.utils.utility.Location('/Users/blb/Downloads/whoisrws-relaxng-compact-schemas/network.xsd', 173, 6)
    
    number = property(__number.value, __number.set, None, None)

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __number.name() : __number
    })



# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_14 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/Users/blb/Downloads/whoisrws-relaxng-compact-schemas/network.xsd', 182, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.arin.net/whoisrws/core/v1}endAddress uses Python identifier endAddress
    __endAddress = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'endAddress'), 'endAddress', '__httpwww_arin_netwhoisrwscorev1_CTD_ANON_14_httpwww_arin_netwhoisrwscorev1endAddress', False, pyxb.utils.utility.Location('/Users/blb/Downloads/whoisrws-relaxng-compact-schemas/network.xsd', 42, 2), )

    
    endAddress = property(__endAddress.value, __endAddress.set, None, None)

    
    # Element {http://www.arin.net/whoisrws/core/v1}startAddress uses Python identifier startAddress
    __startAddress = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'startAddress'), 'startAddress', '__httpwww_arin_netwhoisrwscorev1_CTD_ANON_14_httpwww_arin_netwhoisrwscorev1startAddress', False, pyxb.utils.utility.Location('/Users/blb/Downloads/whoisrws-relaxng-compact-schemas/network.xsd', 106, 2), )

    
    startAddress = property(__startAddress.value, __startAddress.set, None, None)

    
    # Element {http://www.arin.net/whoisrws/core/v1}cidrLength uses Python identifier cidrLength
    __cidrLength = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'cidrLength'), 'cidrLength', '__httpwww_arin_netwhoisrwscorev1_CTD_ANON_14_httpwww_arin_netwhoisrwscorev1cidrLength', False, pyxb.utils.utility.Location('/Users/blb/Downloads/whoisrws-relaxng-compact-schemas/network.xsd', 204, 2), )

    
    cidrLength = property(__cidrLength.value, __cidrLength.set, None, None)

    
    # Element {http://www.arin.net/whoisrws/core/v1}description uses Python identifier description
    __description = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'description'), 'description', '__httpwww_arin_netwhoisrwscorev1_CTD_ANON_14_httpwww_arin_netwhoisrwscorev1description', False, pyxb.utils.utility.Location('/Users/blb/Downloads/whoisrws-relaxng-compact-schemas/network.xsd', 205, 2), )

    
    description = property(__description.value, __description.set, None, None)

    
    # Element {http://www.arin.net/whoisrws/core/v1}type uses Python identifier type
    __type = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'type'), 'type', '__httpwww_arin_netwhoisrwscorev1_CTD_ANON_14_httpwww_arin_netwhoisrwscorev1type', False, pyxb.utils.utility.Location('/Users/blb/Downloads/whoisrws-relaxng-compact-schemas/network.xsd', 206, 2), )

    
    type = property(__type.value, __type.set, None, None)

    _ElementMap.update({
        __endAddress.name() : __endAddress,
        __startAddress.name() : __startAddress,
        __cidrLength.name() : __cidrLength,
        __description.name() : __description,
        __type.name() : __type
    })
    _AttributeMap.update({
        
    })



# Complex type [anonymous] with content type SIMPLE
class CTD_ANON_15 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type SIMPLE"""
    _TypeDefinition = pyxb.binding.datatypes.anyURI
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/Users/blb/Downloads/whoisrws-relaxng-compact-schemas/network.xsd', 193, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyURI
    
    # Attribute endAddress uses Python identifier endAddress
    __endAddress = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'endAddress'), 'endAddress', '__httpwww_arin_netwhoisrwscorev1_CTD_ANON_15_endAddress', pyxb.binding.datatypes.anySimpleType)
    __endAddress._DeclarationLocation = pyxb.utils.utility.Location('/Users/blb/Downloads/whoisrws-relaxng-compact-schemas/network.xsd', 196, 10)
    __endAddress._UseLocation = pyxb.utils.utility.Location('/Users/blb/Downloads/whoisrws-relaxng-compact-schemas/network.xsd', 196, 10)
    
    endAddress = property(__endAddress.value, __endAddress.set, None, None)

    
    # Attribute handle uses Python identifier handle
    __handle = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'handle'), 'handle', '__httpwww_arin_netwhoisrwscorev1_CTD_ANON_15_handle', pyxb.binding.datatypes.anySimpleType, required=True)
    __handle._DeclarationLocation = pyxb.utils.utility.Location('/Users/blb/Downloads/whoisrws-relaxng-compact-schemas/network.xsd', 197, 10)
    __handle._UseLocation = pyxb.utils.utility.Location('/Users/blb/Downloads/whoisrws-relaxng-compact-schemas/network.xsd', 197, 10)
    
    handle = property(__handle.value, __handle.set, None, None)

    
    # Attribute name uses Python identifier name
    __name = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'name'), 'name', '__httpwww_arin_netwhoisrwscorev1_CTD_ANON_15_name', pyxb.binding.datatypes.anySimpleType)
    __name._DeclarationLocation = pyxb.utils.utility.Location('/Users/blb/Downloads/whoisrws-relaxng-compact-schemas/network.xsd', 198, 10)
    __name._UseLocation = pyxb.utils.utility.Location('/Users/blb/Downloads/whoisrws-relaxng-compact-schemas/network.xsd', 198, 10)
    
    name = property(__name.value, __name.set, None, None)

    
    # Attribute startAddress uses Python identifier startAddress
    __startAddress = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'startAddress'), 'startAddress', '__httpwww_arin_netwhoisrwscorev1_CTD_ANON_15_startAddress', pyxb.binding.datatypes.anySimpleType)
    __startAddress._DeclarationLocation = pyxb.utils.utility.Location('/Users/blb/Downloads/whoisrws-relaxng-compact-schemas/network.xsd', 199, 10)
    __startAddress._UseLocation = pyxb.utils.utility.Location('/Users/blb/Downloads/whoisrws-relaxng-compact-schemas/network.xsd', 199, 10)
    
    startAddress = property(__startAddress.value, __startAddress.set, None, None)

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __endAddress.name() : __endAddress,
        __handle.name() : __handle,
        __name.name() : __name,
        __startAddress.name() : __startAddress
    })



registrationDate = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'registrationDate'), pyxb.binding.datatypes.dateTime, location=pyxb.utils.utility.Location('/Users/blb/Downloads/whoisrws-relaxng-compact-schemas/network.xsd', 30, 2))
Namespace.addCategoryObject('elementBinding', registrationDate.name().localName(), registrationDate)

ref = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'ref'), pyxb.binding.datatypes.anyURI, location=pyxb.utils.utility.Location('/Users/blb/Downloads/whoisrws-relaxng-compact-schemas/network.xsd', 31, 2))
Namespace.addCategoryObject('elementBinding', ref.name().localName(), ref)

endAddress = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'endAddress'), pyxb.binding.datatypes.string, location=pyxb.utils.utility.Location('/Users/blb/Downloads/whoisrws-relaxng-compact-schemas/network.xsd', 42, 2))
Namespace.addCategoryObject('elementBinding', endAddress.name().localName(), endAddress)

handle = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'handle'), pyxb.binding.datatypes.string, location=pyxb.utils.utility.Location('/Users/blb/Downloads/whoisrws-relaxng-compact-schemas/network.xsd', 43, 2))
Namespace.addCategoryObject('elementBinding', handle.name().localName(), handle)

name = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'name'), pyxb.binding.datatypes.string, location=pyxb.utils.utility.Location('/Users/blb/Downloads/whoisrws-relaxng-compact-schemas/network.xsd', 44, 2))
Namespace.addCategoryObject('elementBinding', name.name().localName(), name)

startAddress = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'startAddress'), pyxb.binding.datatypes.string, location=pyxb.utils.utility.Location('/Users/blb/Downloads/whoisrws-relaxng-compact-schemas/network.xsd', 106, 2))
Namespace.addCategoryObject('elementBinding', startAddress.name().localName(), startAddress)

updateDate = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'updateDate'), pyxb.binding.datatypes.dateTime, location=pyxb.utils.utility.Location('/Users/blb/Downloads/whoisrws-relaxng-compact-schemas/network.xsd', 107, 2))
Namespace.addCategoryObject('elementBinding', updateDate.name().localName(), updateDate)

version = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'version'), pyxb.binding.datatypes.integer, location=pyxb.utils.utility.Location('/Users/blb/Downloads/whoisrws-relaxng-compact-schemas/network.xsd', 108, 2))
Namespace.addCategoryObject('elementBinding', version.name().localName(), version)

nameserver = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'nameserver'), pyxb.binding.datatypes.string, location=pyxb.utils.utility.Location('/Users/blb/Downloads/whoisrws-relaxng-compact-schemas/network.xsd', 114, 2))
Namespace.addCategoryObject('elementBinding', nameserver.name().localName(), nameserver)

originAS = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'originAS'), pyxb.binding.datatypes.string, location=pyxb.utils.utility.Location('/Users/blb/Downloads/whoisrws-relaxng-compact-schemas/network.xsd', 135, 2))
Namespace.addCategoryObject('elementBinding', originAS.name().localName(), originAS)

cidrLength = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'cidrLength'), pyxb.binding.datatypes.integer, location=pyxb.utils.utility.Location('/Users/blb/Downloads/whoisrws-relaxng-compact-schemas/network.xsd', 204, 2))
Namespace.addCategoryObject('elementBinding', cidrLength.name().localName(), cidrLength)

description = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'description'), pyxb.binding.datatypes.string, location=pyxb.utils.utility.Location('/Users/blb/Downloads/whoisrws-relaxng-compact-schemas/network.xsd', 205, 2))
Namespace.addCategoryObject('elementBinding', description.name().localName(), description)

type = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'type'), pyxb.binding.datatypes.string, location=pyxb.utils.utility.Location('/Users/blb/Downloads/whoisrws-relaxng-compact-schemas/network.xsd', 206, 2))
Namespace.addCategoryObject('elementBinding', type.name().localName(), type)

net = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'net'), CTD_ANON, location=pyxb.utils.utility.Location('/Users/blb/Downloads/whoisrws-relaxng-compact-schemas/network.xsd', 3, 2))
Namespace.addCategoryObject('elementBinding', net.name().localName(), net)

customerRef = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'customerRef'), CTD_ANON_, location=pyxb.utils.utility.Location('/Users/blb/Downloads/whoisrws-relaxng-compact-schemas/network.xsd', 32, 2))
Namespace.addCategoryObject('elementBinding', customerRef.name().localName(), customerRef)

nameservers = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'nameservers'), CTD_ANON_2, location=pyxb.utils.utility.Location('/Users/blb/Downloads/whoisrws-relaxng-compact-schemas/network.xsd', 45, 2))
Namespace.addCategoryObject('elementBinding', nameservers.name().localName(), nameservers)

netBlocks = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'netBlocks'), CTD_ANON_3, location=pyxb.utils.utility.Location('/Users/blb/Downloads/whoisrws-relaxng-compact-schemas/network.xsd', 52, 2))
Namespace.addCategoryObject('elementBinding', netBlocks.name().localName(), netBlocks)

originASes = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'originASes'), CTD_ANON_4, location=pyxb.utils.utility.Location('/Users/blb/Downloads/whoisrws-relaxng-compact-schemas/network.xsd', 59, 2))
Namespace.addCategoryObject('elementBinding', originASes.name().localName(), originASes)

pocs = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'pocs'), CTD_ANON_5, location=pyxb.utils.utility.Location('/Users/blb/Downloads/whoisrws-relaxng-compact-schemas/network.xsd', 66, 2))
Namespace.addCategoryObject('elementBinding', pocs.name().localName(), pocs)

orgRef = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'orgRef'), CTD_ANON_6, location=pyxb.utils.utility.Location('/Users/blb/Downloads/whoisrws-relaxng-compact-schemas/network.xsd', 79, 2))
Namespace.addCategoryObject('elementBinding', orgRef.name().localName(), orgRef)

comment = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'comment'), CTD_ANON_7, location=pyxb.utils.utility.Location('/Users/blb/Downloads/whoisrws-relaxng-compact-schemas/network.xsd', 89, 2))
Namespace.addCategoryObject('elementBinding', comment.name().localName(), comment)

parentNetRef = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'parentNetRef'), CTD_ANON_8, location=pyxb.utils.utility.Location('/Users/blb/Downloads/whoisrws-relaxng-compact-schemas/network.xsd', 96, 2))
Namespace.addCategoryObject('elementBinding', parentNetRef.name().localName(), parentNetRef)

netBlock = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'netBlock'), CTD_ANON_9, location=pyxb.utils.utility.Location('/Users/blb/Downloads/whoisrws-relaxng-compact-schemas/network.xsd', 115, 2))
Namespace.addCategoryObject('elementBinding', netBlock.name().localName(), netBlock)

limitExceeded = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'limitExceeded'), CTD_ANON_10, location=pyxb.utils.utility.Location('/Users/blb/Downloads/whoisrws-relaxng-compact-schemas/network.xsd', 136, 2))
Namespace.addCategoryObject('elementBinding', limitExceeded.name().localName(), limitExceeded)

pocRef = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'pocRef'), CTD_ANON_11, location=pyxb.utils.utility.Location('/Users/blb/Downloads/whoisrws-relaxng-compact-schemas/network.xsd', 145, 2))
Namespace.addCategoryObject('elementBinding', pocRef.name().localName(), pocRef)

pocLinkRef = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'pocLinkRef'), CTD_ANON_12, location=pyxb.utils.utility.Location('/Users/blb/Downloads/whoisrws-relaxng-compact-schemas/network.xsd', 155, 2))
Namespace.addCategoryObject('elementBinding', pocLinkRef.name().localName(), pocLinkRef)

line = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'line'), CTD_ANON_13, location=pyxb.utils.utility.Location('/Users/blb/Downloads/whoisrws-relaxng-compact-schemas/network.xsd', 171, 2))
Namespace.addCategoryObject('elementBinding', line.name().localName(), line)

addressRange = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'addressRange'), CTD_ANON_14, location=pyxb.utils.utility.Location('/Users/blb/Downloads/whoisrws-relaxng-compact-schemas/network.xsd', 181, 2))
Namespace.addCategoryObject('elementBinding', addressRange.name().localName(), addressRange)

netRef = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'netRef'), CTD_ANON_15, location=pyxb.utils.utility.Location('/Users/blb/Downloads/whoisrws-relaxng-compact-schemas/network.xsd', 192, 2))
Namespace.addCategoryObject('elementBinding', netRef.name().localName(), netRef)



CTD_ANON._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'registrationDate'), pyxb.binding.datatypes.dateTime, scope=CTD_ANON, location=pyxb.utils.utility.Location('/Users/blb/Downloads/whoisrws-relaxng-compact-schemas/network.xsd', 30, 2)))

CTD_ANON._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'ref'), pyxb.binding.datatypes.anyURI, scope=CTD_ANON, location=pyxb.utils.utility.Location('/Users/blb/Downloads/whoisrws-relaxng-compact-schemas/network.xsd', 31, 2)))

CTD_ANON._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'customerRef'), CTD_ANON_, scope=CTD_ANON, location=pyxb.utils.utility.Location('/Users/blb/Downloads/whoisrws-relaxng-compact-schemas/network.xsd', 32, 2)))

CTD_ANON._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'endAddress'), pyxb.binding.datatypes.string, scope=CTD_ANON, location=pyxb.utils.utility.Location('/Users/blb/Downloads/whoisrws-relaxng-compact-schemas/network.xsd', 42, 2)))

CTD_ANON._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'handle'), pyxb.binding.datatypes.string, scope=CTD_ANON, location=pyxb.utils.utility.Location('/Users/blb/Downloads/whoisrws-relaxng-compact-schemas/network.xsd', 43, 2)))

CTD_ANON._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'name'), pyxb.binding.datatypes.string, scope=CTD_ANON, location=pyxb.utils.utility.Location('/Users/blb/Downloads/whoisrws-relaxng-compact-schemas/network.xsd', 44, 2)))

CTD_ANON._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'nameservers'), CTD_ANON_2, scope=CTD_ANON, location=pyxb.utils.utility.Location('/Users/blb/Downloads/whoisrws-relaxng-compact-schemas/network.xsd', 45, 2)))

CTD_ANON._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'netBlocks'), CTD_ANON_3, scope=CTD_ANON, location=pyxb.utils.utility.Location('/Users/blb/Downloads/whoisrws-relaxng-compact-schemas/network.xsd', 52, 2)))

CTD_ANON._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'originASes'), CTD_ANON_4, scope=CTD_ANON, location=pyxb.utils.utility.Location('/Users/blb/Downloads/whoisrws-relaxng-compact-schemas/network.xsd', 59, 2)))

CTD_ANON._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'pocs'), CTD_ANON_5, scope=CTD_ANON, location=pyxb.utils.utility.Location('/Users/blb/Downloads/whoisrws-relaxng-compact-schemas/network.xsd', 66, 2)))

CTD_ANON._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'orgRef'), CTD_ANON_6, scope=CTD_ANON, location=pyxb.utils.utility.Location('/Users/blb/Downloads/whoisrws-relaxng-compact-schemas/network.xsd', 79, 2)))

CTD_ANON._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'comment'), CTD_ANON_7, scope=CTD_ANON, location=pyxb.utils.utility.Location('/Users/blb/Downloads/whoisrws-relaxng-compact-schemas/network.xsd', 89, 2)))

CTD_ANON._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'parentNetRef'), CTD_ANON_8, scope=CTD_ANON, location=pyxb.utils.utility.Location('/Users/blb/Downloads/whoisrws-relaxng-compact-schemas/network.xsd', 96, 2)))

CTD_ANON._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'startAddress'), pyxb.binding.datatypes.string, scope=CTD_ANON, location=pyxb.utils.utility.Location('/Users/blb/Downloads/whoisrws-relaxng-compact-schemas/network.xsd', 106, 2)))

CTD_ANON._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'updateDate'), pyxb.binding.datatypes.dateTime, scope=CTD_ANON, location=pyxb.utils.utility.Location('/Users/blb/Downloads/whoisrws-relaxng-compact-schemas/network.xsd', 107, 2)))

CTD_ANON._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'version'), pyxb.binding.datatypes.integer, scope=CTD_ANON, location=pyxb.utils.utility.Location('/Users/blb/Downloads/whoisrws-relaxng-compact-schemas/network.xsd', 108, 2)))

def _BuildAutomaton ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton
    del _BuildAutomaton
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location('/Users/blb/Downloads/whoisrws-relaxng-compact-schemas/network.xsd', 5, 6))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'registrationDate')), pyxb.utils.utility.Location('/Users/blb/Downloads/whoisrws-relaxng-compact-schemas/network.xsd', 7, 10))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'ref')), pyxb.utils.utility.Location('/Users/blb/Downloads/whoisrws-relaxng-compact-schemas/network.xsd', 8, 10))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'customerRef')), pyxb.utils.utility.Location('/Users/blb/Downloads/whoisrws-relaxng-compact-schemas/network.xsd', 9, 10))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'endAddress')), pyxb.utils.utility.Location('/Users/blb/Downloads/whoisrws-relaxng-compact-schemas/network.xsd', 10, 10))
    st_3 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'handle')), pyxb.utils.utility.Location('/Users/blb/Downloads/whoisrws-relaxng-compact-schemas/network.xsd', 11, 10))
    st_4 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'name')), pyxb.utils.utility.Location('/Users/blb/Downloads/whoisrws-relaxng-compact-schemas/network.xsd', 12, 10))
    st_5 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'nameservers')), pyxb.utils.utility.Location('/Users/blb/Downloads/whoisrws-relaxng-compact-schemas/network.xsd', 13, 10))
    st_6 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_6)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'netBlocks')), pyxb.utils.utility.Location('/Users/blb/Downloads/whoisrws-relaxng-compact-schemas/network.xsd', 14, 10))
    st_7 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_7)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'originASes')), pyxb.utils.utility.Location('/Users/blb/Downloads/whoisrws-relaxng-compact-schemas/network.xsd', 15, 10))
    st_8 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_8)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'pocs')), pyxb.utils.utility.Location('/Users/blb/Downloads/whoisrws-relaxng-compact-schemas/network.xsd', 16, 10))
    st_9 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_9)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'orgRef')), pyxb.utils.utility.Location('/Users/blb/Downloads/whoisrws-relaxng-compact-schemas/network.xsd', 17, 10))
    st_10 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_10)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'comment')), pyxb.utils.utility.Location('/Users/blb/Downloads/whoisrws-relaxng-compact-schemas/network.xsd', 18, 10))
    st_11 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_11)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'parentNetRef')), pyxb.utils.utility.Location('/Users/blb/Downloads/whoisrws-relaxng-compact-schemas/network.xsd', 19, 10))
    st_12 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_12)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'comment')), pyxb.utils.utility.Location('/Users/blb/Downloads/whoisrws-relaxng-compact-schemas/network.xsd', 20, 10))
    st_13 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_13)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'startAddress')), pyxb.utils.utility.Location('/Users/blb/Downloads/whoisrws-relaxng-compact-schemas/network.xsd', 21, 10))
    st_14 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_14)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'updateDate')), pyxb.utils.utility.Location('/Users/blb/Downloads/whoisrws-relaxng-compact-schemas/network.xsd', 22, 10))
    st_15 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_15)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'version')), pyxb.utils.utility.Location('/Users/blb/Downloads/whoisrws-relaxng-compact-schemas/network.xsd', 23, 10))
    st_16 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_16)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.WildcardUse(pyxb.binding.content.Wildcard(process_contents=pyxb.binding.content.Wildcard.PC_skip, namespace_constraint=(pyxb.binding.content.Wildcard.NC_not, u'http://www.arin.net/whoisrws/core/v1')), pyxb.utils.utility.Location('/Users/blb/Downloads/whoisrws-relaxng-compact-schemas/network.xsd', 111, 6))
    st_17 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_17)
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
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_17, [
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
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_17, [
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
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_17, [
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
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_17, [
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
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_17, [
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
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_17, [
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
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_17, [
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
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_17, [
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
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_17, [
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
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_17, [
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
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_17, [
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
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_11._set_transitionSet(transitions)
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
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_12._set_transitionSet(transitions)
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
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_13._set_transitionSet(transitions)
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
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_14._set_transitionSet(transitions)
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
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_15._set_transitionSet(transitions)
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
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_16._set_transitionSet(transitions)
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
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_17._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
CTD_ANON._Automaton = _BuildAutomaton()




CTD_ANON_2._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'nameserver'), pyxb.binding.datatypes.string, scope=CTD_ANON_2, location=pyxb.utils.utility.Location('/Users/blb/Downloads/whoisrws-relaxng-compact-schemas/network.xsd', 114, 2)))

def _BuildAutomaton_ ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_
    del _BuildAutomaton_
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location('/Users/blb/Downloads/whoisrws-relaxng-compact-schemas/network.xsd', 48, 8))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_2._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'nameserver')), pyxb.utils.utility.Location('/Users/blb/Downloads/whoisrws-relaxng-compact-schemas/network.xsd', 48, 8))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
CTD_ANON_2._Automaton = _BuildAutomaton_()




CTD_ANON_3._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'netBlock'), CTD_ANON_9, scope=CTD_ANON_3, location=pyxb.utils.utility.Location('/Users/blb/Downloads/whoisrws-relaxng-compact-schemas/network.xsd', 115, 2)))

def _BuildAutomaton_2 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_2
    del _BuildAutomaton_2
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location('/Users/blb/Downloads/whoisrws-relaxng-compact-schemas/network.xsd', 55, 8))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_3._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'netBlock')), pyxb.utils.utility.Location('/Users/blb/Downloads/whoisrws-relaxng-compact-schemas/network.xsd', 55, 8))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
CTD_ANON_3._Automaton = _BuildAutomaton_2()




CTD_ANON_4._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'originAS'), pyxb.binding.datatypes.string, scope=CTD_ANON_4, location=pyxb.utils.utility.Location('/Users/blb/Downloads/whoisrws-relaxng-compact-schemas/network.xsd', 135, 2)))

def _BuildAutomaton_3 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_3
    del _BuildAutomaton_3
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_4._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'originAS')), pyxb.utils.utility.Location('/Users/blb/Downloads/whoisrws-relaxng-compact-schemas/network.xsd', 62, 8))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
         ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON_4._Automaton = _BuildAutomaton_3()




CTD_ANON_5._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'limitExceeded'), CTD_ANON_10, scope=CTD_ANON_5, location=pyxb.utils.utility.Location('/Users/blb/Downloads/whoisrws-relaxng-compact-schemas/network.xsd', 136, 2)))

CTD_ANON_5._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'pocRef'), CTD_ANON_11, scope=CTD_ANON_5, location=pyxb.utils.utility.Location('/Users/blb/Downloads/whoisrws-relaxng-compact-schemas/network.xsd', 145, 2)))

CTD_ANON_5._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'pocLinkRef'), CTD_ANON_12, scope=CTD_ANON_5, location=pyxb.utils.utility.Location('/Users/blb/Downloads/whoisrws-relaxng-compact-schemas/network.xsd', 155, 2)))

def _BuildAutomaton_4 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_4
    del _BuildAutomaton_4
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location('/Users/blb/Downloads/whoisrws-relaxng-compact-schemas/network.xsd', 68, 6))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_5._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'limitExceeded')), pyxb.utils.utility.Location('/Users/blb/Downloads/whoisrws-relaxng-compact-schemas/network.xsd', 70, 10))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_5._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'pocRef')), pyxb.utils.utility.Location('/Users/blb/Downloads/whoisrws-relaxng-compact-schemas/network.xsd', 71, 10))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_5._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'pocLinkRef')), pyxb.utils.utility.Location('/Users/blb/Downloads/whoisrws-relaxng-compact-schemas/network.xsd', 72, 10))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.WildcardUse(pyxb.binding.content.Wildcard(process_contents=pyxb.binding.content.Wildcard.PC_skip, namespace_constraint=(pyxb.binding.content.Wildcard.NC_not, u'http://www.arin.net/whoisrws/core/v1')), pyxb.utils.utility.Location('/Users/blb/Downloads/whoisrws-relaxng-compact-schemas/network.xsd', 168, 6))
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
CTD_ANON_5._Automaton = _BuildAutomaton_4()




CTD_ANON_7._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'line'), CTD_ANON_13, scope=CTD_ANON_7, location=pyxb.utils.utility.Location('/Users/blb/Downloads/whoisrws-relaxng-compact-schemas/network.xsd', 171, 2)))

def _BuildAutomaton_5 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_5
    del _BuildAutomaton_5
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_7._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'line')), pyxb.utils.utility.Location('/Users/blb/Downloads/whoisrws-relaxng-compact-schemas/network.xsd', 92, 8))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
         ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON_7._Automaton = _BuildAutomaton_5()




CTD_ANON_9._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'ref'), pyxb.binding.datatypes.anyURI, scope=CTD_ANON_9, location=pyxb.utils.utility.Location('/Users/blb/Downloads/whoisrws-relaxng-compact-schemas/network.xsd', 31, 2)))

CTD_ANON_9._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'endAddress'), pyxb.binding.datatypes.string, scope=CTD_ANON_9, location=pyxb.utils.utility.Location('/Users/blb/Downloads/whoisrws-relaxng-compact-schemas/network.xsd', 42, 2)))

CTD_ANON_9._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'startAddress'), pyxb.binding.datatypes.string, scope=CTD_ANON_9, location=pyxb.utils.utility.Location('/Users/blb/Downloads/whoisrws-relaxng-compact-schemas/network.xsd', 106, 2)))

CTD_ANON_9._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'addressRange'), CTD_ANON_14, scope=CTD_ANON_9, location=pyxb.utils.utility.Location('/Users/blb/Downloads/whoisrws-relaxng-compact-schemas/network.xsd', 181, 2)))

CTD_ANON_9._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'netRef'), CTD_ANON_15, scope=CTD_ANON_9, location=pyxb.utils.utility.Location('/Users/blb/Downloads/whoisrws-relaxng-compact-schemas/network.xsd', 192, 2)))

CTD_ANON_9._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'cidrLength'), pyxb.binding.datatypes.integer, scope=CTD_ANON_9, location=pyxb.utils.utility.Location('/Users/blb/Downloads/whoisrws-relaxng-compact-schemas/network.xsd', 204, 2)))

CTD_ANON_9._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'description'), pyxb.binding.datatypes.string, scope=CTD_ANON_9, location=pyxb.utils.utility.Location('/Users/blb/Downloads/whoisrws-relaxng-compact-schemas/network.xsd', 205, 2)))

CTD_ANON_9._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'type'), pyxb.binding.datatypes.string, scope=CTD_ANON_9, location=pyxb.utils.utility.Location('/Users/blb/Downloads/whoisrws-relaxng-compact-schemas/network.xsd', 206, 2)))

def _BuildAutomaton_6 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_6
    del _BuildAutomaton_6
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location('/Users/blb/Downloads/whoisrws-relaxng-compact-schemas/network.xsd', 117, 6))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_9._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'ref')), pyxb.utils.utility.Location('/Users/blb/Downloads/whoisrws-relaxng-compact-schemas/network.xsd', 119, 10))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_9._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'addressRange')), pyxb.utils.utility.Location('/Users/blb/Downloads/whoisrws-relaxng-compact-schemas/network.xsd', 121, 12))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_9._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'netRef')), pyxb.utils.utility.Location('/Users/blb/Downloads/whoisrws-relaxng-compact-schemas/network.xsd', 122, 12))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_9._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'cidrLength')), pyxb.utils.utility.Location('/Users/blb/Downloads/whoisrws-relaxng-compact-schemas/network.xsd', 124, 10))
    st_3 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_9._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'endAddress')), pyxb.utils.utility.Location('/Users/blb/Downloads/whoisrws-relaxng-compact-schemas/network.xsd', 125, 10))
    st_4 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_9._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'description')), pyxb.utils.utility.Location('/Users/blb/Downloads/whoisrws-relaxng-compact-schemas/network.xsd', 126, 10))
    st_5 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_9._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'type')), pyxb.utils.utility.Location('/Users/blb/Downloads/whoisrws-relaxng-compact-schemas/network.xsd', 127, 10))
    st_6 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_6)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_9._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'startAddress')), pyxb.utils.utility.Location('/Users/blb/Downloads/whoisrws-relaxng-compact-schemas/network.xsd', 128, 10))
    st_7 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_7)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.WildcardUse(pyxb.binding.content.Wildcard(process_contents=pyxb.binding.content.Wildcard.PC_skip, namespace_constraint=(pyxb.binding.content.Wildcard.NC_not, u'http://www.arin.net/whoisrws/core/v1')), pyxb.utils.utility.Location('/Users/blb/Downloads/whoisrws-relaxng-compact-schemas/network.xsd', 209, 6))
    st_8 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_8)
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
    st_8._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
CTD_ANON_9._Automaton = _BuildAutomaton_6()




def _BuildAutomaton_7 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_7
    del _BuildAutomaton_7
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    return fac.Automaton(states, counters, True, containing_state=None)
CTD_ANON_13._Automaton = _BuildAutomaton_7()




CTD_ANON_14._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'endAddress'), pyxb.binding.datatypes.string, scope=CTD_ANON_14, location=pyxb.utils.utility.Location('/Users/blb/Downloads/whoisrws-relaxng-compact-schemas/network.xsd', 42, 2)))

CTD_ANON_14._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'startAddress'), pyxb.binding.datatypes.string, scope=CTD_ANON_14, location=pyxb.utils.utility.Location('/Users/blb/Downloads/whoisrws-relaxng-compact-schemas/network.xsd', 106, 2)))

CTD_ANON_14._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'cidrLength'), pyxb.binding.datatypes.integer, scope=CTD_ANON_14, location=pyxb.utils.utility.Location('/Users/blb/Downloads/whoisrws-relaxng-compact-schemas/network.xsd', 204, 2)))

CTD_ANON_14._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'description'), pyxb.binding.datatypes.string, scope=CTD_ANON_14, location=pyxb.utils.utility.Location('/Users/blb/Downloads/whoisrws-relaxng-compact-schemas/network.xsd', 205, 2)))

CTD_ANON_14._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'type'), pyxb.binding.datatypes.string, scope=CTD_ANON_14, location=pyxb.utils.utility.Location('/Users/blb/Downloads/whoisrws-relaxng-compact-schemas/network.xsd', 206, 2)))

def _BuildAutomaton_8 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_8
    del _BuildAutomaton_8
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location('/Users/blb/Downloads/whoisrws-relaxng-compact-schemas/network.xsd', 184, 8))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location('/Users/blb/Downloads/whoisrws-relaxng-compact-schemas/network.xsd', 185, 8))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location('/Users/blb/Downloads/whoisrws-relaxng-compact-schemas/network.xsd', 186, 8))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location('/Users/blb/Downloads/whoisrws-relaxng-compact-schemas/network.xsd', 187, 8))
    counters.add(cc_3)
    cc_4 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location('/Users/blb/Downloads/whoisrws-relaxng-compact-schemas/network.xsd', 188, 8))
    counters.add(cc_4)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_14._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'cidrLength')), pyxb.utils.utility.Location('/Users/blb/Downloads/whoisrws-relaxng-compact-schemas/network.xsd', 184, 8))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_14._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'endAddress')), pyxb.utils.utility.Location('/Users/blb/Downloads/whoisrws-relaxng-compact-schemas/network.xsd', 185, 8))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_14._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'description')), pyxb.utils.utility.Location('/Users/blb/Downloads/whoisrws-relaxng-compact-schemas/network.xsd', 186, 8))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_3, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_14._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'type')), pyxb.utils.utility.Location('/Users/blb/Downloads/whoisrws-relaxng-compact-schemas/network.xsd', 187, 8))
    st_3 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_4, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_14._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'startAddress')), pyxb.utils.utility.Location('/Users/blb/Downloads/whoisrws-relaxng-compact-schemas/network.xsd', 188, 8))
    st_4 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_2, False) ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_3, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_3, False) ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_4, True) ]))
    st_4._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
CTD_ANON_14._Automaton = _BuildAutomaton_8()

