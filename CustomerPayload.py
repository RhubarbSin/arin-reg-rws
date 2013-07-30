# ./CustomerPayload.py
# -*- coding: utf-8 -*-
# PyXB bindings for NM:514f13e3f1b2b4088cde1fa16b1c0c6121fb4d3d
# Generated 2013-07-11 15:18:44.235575 by PyXB version 1.2.2
# Namespace http://www.arin.net/regrws/core/v1

import pyxb
import pyxb.binding
import pyxb.binding.saxer
import StringIO
import pyxb.utils.utility
import pyxb.utils.domutils
import sys

# Unique identifier for bindings created at the same time
_GenerationUID = pyxb.utils.utility.UniqueIdentifier('urn:uuid:b3f5e566-ea5e-11e2-afd8-10ddb19be936')

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
    _XSDLocation = pyxb.utils.utility.Location('/Users/blb/Downloads/regrws-rnc/CustomerPayload.xsd', 4, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.arin.net/regrws/core/v1}city uses Python identifier city
    __city = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'city'), 'city', '__httpwww_arin_netregrwscorev1_CTD_ANON_httpwww_arin_netregrwscorev1city', True, pyxb.utils.utility.Location('/Users/blb/Downloads/regrws-rnc/CustomerPayload.xsd', 21, 2), )

    
    city = property(__city.value, __city.set, None, None)

    
    # Element {http://www.arin.net/regrws/core/v1}iso3166-1 uses Python identifier iso3166_1
    __iso3166_1 = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'iso3166-1'), 'iso3166_1', '__httpwww_arin_netregrwscorev1_CTD_ANON_httpwww_arin_netregrwscorev1iso3166_1', True, pyxb.utils.utility.Location('/Users/blb/Downloads/regrws-rnc/CustomerPayload.xsd', 22, 2), )

    
    iso3166_1 = property(__iso3166_1.value, __iso3166_1.set, None, None)

    
    # Element {http://www.arin.net/regrws/core/v1}handle uses Python identifier handle
    __handle = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'handle'), 'handle', '__httpwww_arin_netregrwscorev1_CTD_ANON_httpwww_arin_netregrwscorev1handle', True, pyxb.utils.utility.Location('/Users/blb/Downloads/regrws-rnc/CustomerPayload.xsd', 33, 2), )

    
    handle = property(__handle.value, __handle.set, None, None)

    
    # Element {http://www.arin.net/regrws/core/v1}customerName uses Python identifier customerName
    __customerName = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'customerName'), 'customerName', '__httpwww_arin_netregrwscorev1_CTD_ANON_httpwww_arin_netregrwscorev1customerName', True, pyxb.utils.utility.Location('/Users/blb/Downloads/regrws-rnc/CustomerPayload.xsd', 34, 2), )

    
    customerName = property(__customerName.value, __customerName.set, None, None)

    
    # Element {http://www.arin.net/regrws/core/v1}parentOrgHandle uses Python identifier parentOrgHandle
    __parentOrgHandle = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'parentOrgHandle'), 'parentOrgHandle', '__httpwww_arin_netregrwscorev1_CTD_ANON_httpwww_arin_netregrwscorev1parentOrgHandle', True, pyxb.utils.utility.Location('/Users/blb/Downloads/regrws-rnc/CustomerPayload.xsd', 35, 2), )

    
    parentOrgHandle = property(__parentOrgHandle.value, __parentOrgHandle.set, None, None)

    
    # Element {http://www.arin.net/regrws/core/v1}postalCode uses Python identifier postalCode
    __postalCode = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'postalCode'), 'postalCode', '__httpwww_arin_netregrwscorev1_CTD_ANON_httpwww_arin_netregrwscorev1postalCode', True, pyxb.utils.utility.Location('/Users/blb/Downloads/regrws-rnc/CustomerPayload.xsd', 36, 2), )

    
    postalCode = property(__postalCode.value, __postalCode.set, None, None)

    
    # Element {http://www.arin.net/regrws/core/v1}privateCustomer uses Python identifier privateCustomer
    __privateCustomer = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'privateCustomer'), 'privateCustomer', '__httpwww_arin_netregrwscorev1_CTD_ANON_httpwww_arin_netregrwscorev1privateCustomer', True, pyxb.utils.utility.Location('/Users/blb/Downloads/regrws-rnc/CustomerPayload.xsd', 37, 2), )

    
    privateCustomer = property(__privateCustomer.value, __privateCustomer.set, None, None)

    
    # Element {http://www.arin.net/regrws/core/v1}comment uses Python identifier comment
    __comment = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'comment'), 'comment', '__httpwww_arin_netregrwscorev1_CTD_ANON_httpwww_arin_netregrwscorev1comment', True, pyxb.utils.utility.Location('/Users/blb/Downloads/regrws-rnc/CustomerPayload.xsd', 38, 2), )

    
    comment = property(__comment.value, __comment.set, None, None)

    
    # Element {http://www.arin.net/regrws/core/v1}registrationDate uses Python identifier registrationDate
    __registrationDate = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'registrationDate'), 'registrationDate', '__httpwww_arin_netregrwscorev1_CTD_ANON_httpwww_arin_netregrwscorev1registrationDate', True, pyxb.utils.utility.Location('/Users/blb/Downloads/regrws-rnc/CustomerPayload.xsd', 45, 2), )

    
    registrationDate = property(__registrationDate.value, __registrationDate.set, None, None)

    
    # Element {http://www.arin.net/regrws/core/v1}iso3166-2 uses Python identifier iso3166_2
    __iso3166_2 = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'iso3166-2'), 'iso3166_2', '__httpwww_arin_netregrwscorev1_CTD_ANON_httpwww_arin_netregrwscorev1iso3166_2', True, pyxb.utils.utility.Location('/Users/blb/Downloads/regrws-rnc/CustomerPayload.xsd', 46, 2), )

    
    iso3166_2 = property(__iso3166_2.value, __iso3166_2.set, None, None)

    
    # Element {http://www.arin.net/regrws/core/v1}streetAddress uses Python identifier streetAddress
    __streetAddress = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'streetAddress'), 'streetAddress', '__httpwww_arin_netregrwscorev1_CTD_ANON_httpwww_arin_netregrwscorev1streetAddress', True, pyxb.utils.utility.Location('/Users/blb/Downloads/regrws-rnc/CustomerPayload.xsd', 47, 2), )

    
    streetAddress = property(__streetAddress.value, __streetAddress.set, None, None)

    _HasWildcardElement = True
    _ElementMap.update({
        __city.name() : __city,
        __iso3166_1.name() : __iso3166_1,
        __handle.name() : __handle,
        __customerName.name() : __customerName,
        __parentOrgHandle.name() : __parentOrgHandle,
        __postalCode.name() : __postalCode,
        __privateCustomer.name() : __privateCustomer,
        __comment.name() : __comment,
        __registrationDate.name() : __registrationDate,
        __iso3166_2.name() : __iso3166_2,
        __streetAddress.name() : __streetAddress
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
    _XSDLocation = pyxb.utils.utility.Location('/Users/blb/Downloads/regrws-rnc/CustomerPayload.xsd', 23, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.arin.net/regrws/core/v1}code2 uses Python identifier code2
    __code2 = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'code2'), 'code2', '__httpwww_arin_netregrwscorev1_CTD_ANON__httpwww_arin_netregrwscorev1code2', True, pyxb.utils.utility.Location('/Users/blb/Downloads/regrws-rnc/CustomerPayload.xsd', 59, 2), )

    
    code2 = property(__code2.value, __code2.set, None, None)

    
    # Element {http://www.arin.net/regrws/core/v1}code3 uses Python identifier code3
    __code3 = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'code3'), 'code3', '__httpwww_arin_netregrwscorev1_CTD_ANON__httpwww_arin_netregrwscorev1code3', True, pyxb.utils.utility.Location('/Users/blb/Downloads/regrws-rnc/CustomerPayload.xsd', 60, 2), )

    
    code3 = property(__code3.value, __code3.set, None, None)

    
    # Element {http://www.arin.net/regrws/core/v1}name uses Python identifier name
    __name = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'name'), 'name', '__httpwww_arin_netregrwscorev1_CTD_ANON__httpwww_arin_netregrwscorev1name', True, pyxb.utils.utility.Location('/Users/blb/Downloads/regrws-rnc/CustomerPayload.xsd', 61, 2), )

    
    name = property(__name.value, __name.set, None, None)

    
    # Element {http://www.arin.net/regrws/core/v1}e164 uses Python identifier e164
    __e164 = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'e164'), 'e164', '__httpwww_arin_netregrwscorev1_CTD_ANON__httpwww_arin_netregrwscorev1e164', True, pyxb.utils.utility.Location('/Users/blb/Downloads/regrws-rnc/CustomerPayload.xsd', 62, 2), )

    
    e164 = property(__e164.value, __e164.set, None, None)

    _HasWildcardElement = True
    _ElementMap.update({
        __code2.name() : __code2,
        __code3.name() : __code3,
        __name.name() : __name,
        __e164.name() : __e164
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
    _XSDLocation = pyxb.utils.utility.Location('/Users/blb/Downloads/regrws-rnc/CustomerPayload.xsd', 39, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.arin.net/regrws/core/v1}line uses Python identifier line
    __line = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'line'), 'line', '__httpwww_arin_netregrwscorev1_CTD_ANON_2_httpwww_arin_netregrwscorev1line', True, pyxb.utils.utility.Location('/Users/blb/Downloads/regrws-rnc/CustomerPayload.xsd', 68, 2), )

    
    line = property(__line.value, __line.set, None, None)

    _ElementMap.update({
        __line.name() : __line
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
    _XSDLocation = pyxb.utils.utility.Location('/Users/blb/Downloads/regrws-rnc/CustomerPayload.xsd', 48, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.arin.net/regrws/core/v1}line uses Python identifier line
    __line = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'line'), 'line', '__httpwww_arin_netregrwscorev1_CTD_ANON_3_httpwww_arin_netregrwscorev1line', True, pyxb.utils.utility.Location('/Users/blb/Downloads/regrws-rnc/CustomerPayload.xsd', 68, 2), )

    
    line = property(__line.value, __line.set, None, None)

    _ElementMap.update({
        __line.name() : __line
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
    _XSDLocation = pyxb.utils.utility.Location('/Users/blb/Downloads/regrws-rnc/CustomerPayload.xsd', 69, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.string
    
    # Attribute number uses Python identifier number
    __number = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'number'), 'number', '__httpwww_arin_netregrwscorev1_CTD_ANON_4_number', pyxb.binding.datatypes.integer, required=True)
    __number._DeclarationLocation = pyxb.utils.utility.Location('/Users/blb/Downloads/regrws-rnc/CustomerPayload.xsd', 72, 10)
    __number._UseLocation = pyxb.utils.utility.Location('/Users/blb/Downloads/regrws-rnc/CustomerPayload.xsd', 72, 10)
    
    number = property(__number.value, __number.set, None, None)

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __number.name() : __number
    })



city = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'city'), pyxb.binding.datatypes.string, location=pyxb.utils.utility.Location('/Users/blb/Downloads/regrws-rnc/CustomerPayload.xsd', 21, 2))
Namespace.addCategoryObject('elementBinding', city.name().localName(), city)

handle = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'handle'), pyxb.binding.datatypes.string, location=pyxb.utils.utility.Location('/Users/blb/Downloads/regrws-rnc/CustomerPayload.xsd', 33, 2))
Namespace.addCategoryObject('elementBinding', handle.name().localName(), handle)

customerName = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'customerName'), pyxb.binding.datatypes.string, location=pyxb.utils.utility.Location('/Users/blb/Downloads/regrws-rnc/CustomerPayload.xsd', 34, 2))
Namespace.addCategoryObject('elementBinding', customerName.name().localName(), customerName)

parentOrgHandle = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'parentOrgHandle'), pyxb.binding.datatypes.string, location=pyxb.utils.utility.Location('/Users/blb/Downloads/regrws-rnc/CustomerPayload.xsd', 35, 2))
Namespace.addCategoryObject('elementBinding', parentOrgHandle.name().localName(), parentOrgHandle)

postalCode = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'postalCode'), pyxb.binding.datatypes.string, location=pyxb.utils.utility.Location('/Users/blb/Downloads/regrws-rnc/CustomerPayload.xsd', 36, 2))
Namespace.addCategoryObject('elementBinding', postalCode.name().localName(), postalCode)

privateCustomer = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'privateCustomer'), pyxb.binding.datatypes.boolean, location=pyxb.utils.utility.Location('/Users/blb/Downloads/regrws-rnc/CustomerPayload.xsd', 37, 2))
Namespace.addCategoryObject('elementBinding', privateCustomer.name().localName(), privateCustomer)

registrationDate = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'registrationDate'), pyxb.binding.datatypes.string, location=pyxb.utils.utility.Location('/Users/blb/Downloads/regrws-rnc/CustomerPayload.xsd', 45, 2))
Namespace.addCategoryObject('elementBinding', registrationDate.name().localName(), registrationDate)

iso3166_2 = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'iso3166-2'), pyxb.binding.datatypes.string, location=pyxb.utils.utility.Location('/Users/blb/Downloads/regrws-rnc/CustomerPayload.xsd', 46, 2))
Namespace.addCategoryObject('elementBinding', iso3166_2.name().localName(), iso3166_2)

code2 = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'code2'), pyxb.binding.datatypes.string, location=pyxb.utils.utility.Location('/Users/blb/Downloads/regrws-rnc/CustomerPayload.xsd', 59, 2))
Namespace.addCategoryObject('elementBinding', code2.name().localName(), code2)

code3 = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'code3'), pyxb.binding.datatypes.string, location=pyxb.utils.utility.Location('/Users/blb/Downloads/regrws-rnc/CustomerPayload.xsd', 60, 2))
Namespace.addCategoryObject('elementBinding', code3.name().localName(), code3)

name = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'name'), pyxb.binding.datatypes.string, location=pyxb.utils.utility.Location('/Users/blb/Downloads/regrws-rnc/CustomerPayload.xsd', 61, 2))
Namespace.addCategoryObject('elementBinding', name.name().localName(), name)

e164 = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'e164'), pyxb.binding.datatypes.string, location=pyxb.utils.utility.Location('/Users/blb/Downloads/regrws-rnc/CustomerPayload.xsd', 62, 2))
Namespace.addCategoryObject('elementBinding', e164.name().localName(), e164)

customer = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'customer'), CTD_ANON, location=pyxb.utils.utility.Location('/Users/blb/Downloads/regrws-rnc/CustomerPayload.xsd', 3, 2))
Namespace.addCategoryObject('elementBinding', customer.name().localName(), customer)

iso3166_1 = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'iso3166-1'), CTD_ANON_, location=pyxb.utils.utility.Location('/Users/blb/Downloads/regrws-rnc/CustomerPayload.xsd', 22, 2))
Namespace.addCategoryObject('elementBinding', iso3166_1.name().localName(), iso3166_1)

comment = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'comment'), CTD_ANON_2, location=pyxb.utils.utility.Location('/Users/blb/Downloads/regrws-rnc/CustomerPayload.xsd', 38, 2))
Namespace.addCategoryObject('elementBinding', comment.name().localName(), comment)

streetAddress = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'streetAddress'), CTD_ANON_3, location=pyxb.utils.utility.Location('/Users/blb/Downloads/regrws-rnc/CustomerPayload.xsd', 47, 2))
Namespace.addCategoryObject('elementBinding', streetAddress.name().localName(), streetAddress)

line = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'line'), CTD_ANON_4, location=pyxb.utils.utility.Location('/Users/blb/Downloads/regrws-rnc/CustomerPayload.xsd', 68, 2))
Namespace.addCategoryObject('elementBinding', line.name().localName(), line)



CTD_ANON._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'city'), pyxb.binding.datatypes.string, scope=CTD_ANON, location=pyxb.utils.utility.Location('/Users/blb/Downloads/regrws-rnc/CustomerPayload.xsd', 21, 2)))

CTD_ANON._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'iso3166-1'), CTD_ANON_, scope=CTD_ANON, location=pyxb.utils.utility.Location('/Users/blb/Downloads/regrws-rnc/CustomerPayload.xsd', 22, 2)))

CTD_ANON._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'handle'), pyxb.binding.datatypes.string, scope=CTD_ANON, location=pyxb.utils.utility.Location('/Users/blb/Downloads/regrws-rnc/CustomerPayload.xsd', 33, 2)))

CTD_ANON._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'customerName'), pyxb.binding.datatypes.string, scope=CTD_ANON, location=pyxb.utils.utility.Location('/Users/blb/Downloads/regrws-rnc/CustomerPayload.xsd', 34, 2)))

CTD_ANON._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'parentOrgHandle'), pyxb.binding.datatypes.string, scope=CTD_ANON, location=pyxb.utils.utility.Location('/Users/blb/Downloads/regrws-rnc/CustomerPayload.xsd', 35, 2)))

CTD_ANON._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'postalCode'), pyxb.binding.datatypes.string, scope=CTD_ANON, location=pyxb.utils.utility.Location('/Users/blb/Downloads/regrws-rnc/CustomerPayload.xsd', 36, 2)))

CTD_ANON._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'privateCustomer'), pyxb.binding.datatypes.boolean, scope=CTD_ANON, location=pyxb.utils.utility.Location('/Users/blb/Downloads/regrws-rnc/CustomerPayload.xsd', 37, 2)))

CTD_ANON._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'comment'), CTD_ANON_2, scope=CTD_ANON, location=pyxb.utils.utility.Location('/Users/blb/Downloads/regrws-rnc/CustomerPayload.xsd', 38, 2)))

CTD_ANON._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'registrationDate'), pyxb.binding.datatypes.string, scope=CTD_ANON, location=pyxb.utils.utility.Location('/Users/blb/Downloads/regrws-rnc/CustomerPayload.xsd', 45, 2)))

CTD_ANON._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'iso3166-2'), pyxb.binding.datatypes.string, scope=CTD_ANON, location=pyxb.utils.utility.Location('/Users/blb/Downloads/regrws-rnc/CustomerPayload.xsd', 46, 2)))

CTD_ANON._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'streetAddress'), CTD_ANON_3, scope=CTD_ANON, location=pyxb.utils.utility.Location('/Users/blb/Downloads/regrws-rnc/CustomerPayload.xsd', 47, 2)))

def _BuildAutomaton ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton
    del _BuildAutomaton
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location('/Users/blb/Downloads/regrws-rnc/CustomerPayload.xsd', 5, 6))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'city')), pyxb.utils.utility.Location('/Users/blb/Downloads/regrws-rnc/CustomerPayload.xsd', 6, 8))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'iso3166-1')), pyxb.utils.utility.Location('/Users/blb/Downloads/regrws-rnc/CustomerPayload.xsd', 7, 8))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'handle')), pyxb.utils.utility.Location('/Users/blb/Downloads/regrws-rnc/CustomerPayload.xsd', 8, 8))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'customerName')), pyxb.utils.utility.Location('/Users/blb/Downloads/regrws-rnc/CustomerPayload.xsd', 9, 8))
    st_3 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'parentOrgHandle')), pyxb.utils.utility.Location('/Users/blb/Downloads/regrws-rnc/CustomerPayload.xsd', 10, 8))
    st_4 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'postalCode')), pyxb.utils.utility.Location('/Users/blb/Downloads/regrws-rnc/CustomerPayload.xsd', 11, 8))
    st_5 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'privateCustomer')), pyxb.utils.utility.Location('/Users/blb/Downloads/regrws-rnc/CustomerPayload.xsd', 12, 8))
    st_6 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_6)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'comment')), pyxb.utils.utility.Location('/Users/blb/Downloads/regrws-rnc/CustomerPayload.xsd', 13, 8))
    st_7 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_7)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'registrationDate')), pyxb.utils.utility.Location('/Users/blb/Downloads/regrws-rnc/CustomerPayload.xsd', 14, 8))
    st_8 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_8)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'iso3166-2')), pyxb.utils.utility.Location('/Users/blb/Downloads/regrws-rnc/CustomerPayload.xsd', 15, 8))
    st_9 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_9)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'streetAddress')), pyxb.utils.utility.Location('/Users/blb/Downloads/regrws-rnc/CustomerPayload.xsd', 16, 8))
    st_10 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_10)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.WildcardUse(pyxb.binding.content.Wildcard(process_contents=pyxb.binding.content.Wildcard.PC_skip, namespace_constraint=pyxb.binding.content.Wildcard.NC_any), pyxb.utils.utility.Location('/Users/blb/Downloads/regrws-rnc/CustomerPayload.xsd', 56, 6))
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




CTD_ANON_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'code2'), pyxb.binding.datatypes.string, scope=CTD_ANON_, location=pyxb.utils.utility.Location('/Users/blb/Downloads/regrws-rnc/CustomerPayload.xsd', 59, 2)))

CTD_ANON_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'code3'), pyxb.binding.datatypes.string, scope=CTD_ANON_, location=pyxb.utils.utility.Location('/Users/blb/Downloads/regrws-rnc/CustomerPayload.xsd', 60, 2)))

CTD_ANON_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'name'), pyxb.binding.datatypes.string, scope=CTD_ANON_, location=pyxb.utils.utility.Location('/Users/blb/Downloads/regrws-rnc/CustomerPayload.xsd', 61, 2)))

CTD_ANON_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'e164'), pyxb.binding.datatypes.string, scope=CTD_ANON_, location=pyxb.utils.utility.Location('/Users/blb/Downloads/regrws-rnc/CustomerPayload.xsd', 62, 2)))

def _BuildAutomaton_ ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_
    del _BuildAutomaton_
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location('/Users/blb/Downloads/regrws-rnc/CustomerPayload.xsd', 24, 6))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'code2')), pyxb.utils.utility.Location('/Users/blb/Downloads/regrws-rnc/CustomerPayload.xsd', 25, 8))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'code3')), pyxb.utils.utility.Location('/Users/blb/Downloads/regrws-rnc/CustomerPayload.xsd', 26, 8))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'name')), pyxb.utils.utility.Location('/Users/blb/Downloads/regrws-rnc/CustomerPayload.xsd', 27, 8))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'e164')), pyxb.utils.utility.Location('/Users/blb/Downloads/regrws-rnc/CustomerPayload.xsd', 28, 8))
    st_3 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.WildcardUse(pyxb.binding.content.Wildcard(process_contents=pyxb.binding.content.Wildcard.PC_skip, namespace_constraint=pyxb.binding.content.Wildcard.NC_any), pyxb.utils.utility.Location('/Users/blb/Downloads/regrws-rnc/CustomerPayload.xsd', 65, 6))
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
CTD_ANON_._Automaton = _BuildAutomaton_()




CTD_ANON_2._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'line'), CTD_ANON_4, scope=CTD_ANON_2, location=pyxb.utils.utility.Location('/Users/blb/Downloads/regrws-rnc/CustomerPayload.xsd', 68, 2)))

def _BuildAutomaton_2 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_2
    del _BuildAutomaton_2
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location('/Users/blb/Downloads/regrws-rnc/CustomerPayload.xsd', 41, 8))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_2._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'line')), pyxb.utils.utility.Location('/Users/blb/Downloads/regrws-rnc/CustomerPayload.xsd', 41, 8))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
CTD_ANON_2._Automaton = _BuildAutomaton_2()




CTD_ANON_3._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'line'), CTD_ANON_4, scope=CTD_ANON_3, location=pyxb.utils.utility.Location('/Users/blb/Downloads/regrws-rnc/CustomerPayload.xsd', 68, 2)))

def _BuildAutomaton_3 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_3
    del _BuildAutomaton_3
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location('/Users/blb/Downloads/regrws-rnc/CustomerPayload.xsd', 50, 8))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_3._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'line')), pyxb.utils.utility.Location('/Users/blb/Downloads/regrws-rnc/CustomerPayload.xsd', 50, 8))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
CTD_ANON_3._Automaton = _BuildAutomaton_3()

