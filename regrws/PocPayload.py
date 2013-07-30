# ./PocPayload.py
# -*- coding: utf-8 -*-
# PyXB bindings for NM:514f13e3f1b2b4088cde1fa16b1c0c6121fb4d3d
# Generated 2013-07-11 15:17:45.817816 by PyXB version 1.2.2
# Namespace http://www.arin.net/regrws/core/v1

import pyxb
import pyxb.binding
import pyxb.binding.saxer
import StringIO
import pyxb.utils.utility
import pyxb.utils.domutils
import sys

# Unique identifier for bindings created at the same time
_GenerationUID = pyxb.utils.utility.UniqueIdentifier('urn:uuid:91220c73-ea5e-11e2-a210-10ddb19be936')

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
    _XSDLocation = pyxb.utils.utility.Location('/Users/blb/Downloads/regrws-rnc/PocPayload.xsd', 54, 4)
    _Documentation = None
STD_ANON._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=STD_ANON, enum_prefix=None)
STD_ANON.PERSON = STD_ANON._CF_enumeration.addEnumeration(unicode_value=u'PERSON', tag=u'PERSON')
STD_ANON.ROLE = STD_ANON._CF_enumeration.addEnumeration(unicode_value=u'ROLE', tag=u'ROLE')
STD_ANON._InitializeFacetMap(STD_ANON._CF_enumeration)

# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/Users/blb/Downloads/regrws-rnc/PocPayload.xsd', 4, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.arin.net/regrws/core/v1}extension uses Python identifier extension
    __extension = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'extension'), 'extension', '__httpwww_arin_netregrwscorev1_CTD_ANON_httpwww_arin_netregrwscorev1extension', True, pyxb.utils.utility.Location('/Users/blb/Downloads/regrws-rnc/PocPayload.xsd', 36, 2), )

    
    extension = property(__extension.value, __extension.set, None, None)

    
    # Element {http://www.arin.net/regrws/core/v1}number uses Python identifier number
    __number = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'number'), 'number', '__httpwww_arin_netregrwscorev1_CTD_ANON_httpwww_arin_netregrwscorev1number', True, pyxb.utils.utility.Location('/Users/blb/Downloads/regrws-rnc/PocPayload.xsd', 37, 2), )

    
    number = property(__number.value, __number.set, None, None)

    
    # Element {http://www.arin.net/regrws/core/v1}type uses Python identifier type
    __type = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'type'), 'type', '__httpwww_arin_netregrwscorev1_CTD_ANON_httpwww_arin_netregrwscorev1type', True, pyxb.utils.utility.Location('/Users/blb/Downloads/regrws-rnc/PocPayload.xsd', 38, 2), )

    
    type = property(__type.value, __type.set, None, None)

    _HasWildcardElement = True
    _ElementMap.update({
        __extension.name() : __extension,
        __number.name() : __number,
        __type.name() : __type
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
    _XSDLocation = pyxb.utils.utility.Location('/Users/blb/Downloads/regrws-rnc/PocPayload.xsd', 14, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.arin.net/regrws/core/v1}city uses Python identifier city
    __city = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'city'), 'city', '__httpwww_arin_netregrwscorev1_CTD_ANON__httpwww_arin_netregrwscorev1city', True, pyxb.utils.utility.Location('/Users/blb/Downloads/regrws-rnc/PocPayload.xsd', 51, 2), )

    
    city = property(__city.value, __city.set, None, None)

    
    # Element {http://www.arin.net/regrws/core/v1}companyName uses Python identifier companyName
    __companyName = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'companyName'), 'companyName', '__httpwww_arin_netregrwscorev1_CTD_ANON__httpwww_arin_netregrwscorev1companyName', True, pyxb.utils.utility.Location('/Users/blb/Downloads/regrws-rnc/PocPayload.xsd', 52, 2), )

    
    companyName = property(__companyName.value, __companyName.set, None, None)

    
    # Element {http://www.arin.net/regrws/core/v1}contactType uses Python identifier contactType
    __contactType = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'contactType'), 'contactType', '__httpwww_arin_netregrwscorev1_CTD_ANON__httpwww_arin_netregrwscorev1contactType', True, pyxb.utils.utility.Location('/Users/blb/Downloads/regrws-rnc/PocPayload.xsd', 53, 2), )

    
    contactType = property(__contactType.value, __contactType.set, None, None)

    
    # Element {http://www.arin.net/regrws/core/v1}iso3166-1 uses Python identifier iso3166_1
    __iso3166_1 = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'iso3166-1'), 'iso3166_1', '__httpwww_arin_netregrwscorev1_CTD_ANON__httpwww_arin_netregrwscorev1iso3166_1', True, pyxb.utils.utility.Location('/Users/blb/Downloads/regrws-rnc/PocPayload.xsd', 61, 2), )

    
    iso3166_1 = property(__iso3166_1.value, __iso3166_1.set, None, None)

    
    # Element {http://www.arin.net/regrws/core/v1}emails uses Python identifier emails
    __emails = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'emails'), 'emails', '__httpwww_arin_netregrwscorev1_CTD_ANON__httpwww_arin_netregrwscorev1emails', True, pyxb.utils.utility.Location('/Users/blb/Downloads/regrws-rnc/PocPayload.xsd', 72, 2), )

    
    emails = property(__emails.value, __emails.set, None, None)

    
    # Element {http://www.arin.net/regrws/core/v1}firstName uses Python identifier firstName
    __firstName = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'firstName'), 'firstName', '__httpwww_arin_netregrwscorev1_CTD_ANON__httpwww_arin_netregrwscorev1firstName', True, pyxb.utils.utility.Location('/Users/blb/Downloads/regrws-rnc/PocPayload.xsd', 79, 2), )

    
    firstName = property(__firstName.value, __firstName.set, None, None)

    
    # Element {http://www.arin.net/regrws/core/v1}lastModified uses Python identifier lastModified
    __lastModified = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'lastModified'), 'lastModified', '__httpwww_arin_netregrwscorev1_CTD_ANON__httpwww_arin_netregrwscorev1lastModified', True, pyxb.utils.utility.Location('/Users/blb/Downloads/regrws-rnc/PocPayload.xsd', 80, 2), )

    
    lastModified = property(__lastModified.value, __lastModified.set, None, None)

    
    # Element {http://www.arin.net/regrws/core/v1}lastName uses Python identifier lastName
    __lastName = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'lastName'), 'lastName', '__httpwww_arin_netregrwscorev1_CTD_ANON__httpwww_arin_netregrwscorev1lastName', True, pyxb.utils.utility.Location('/Users/blb/Downloads/regrws-rnc/PocPayload.xsd', 81, 2), )

    
    lastName = property(__lastName.value, __lastName.set, None, None)

    
    # Element {http://www.arin.net/regrws/core/v1}middleName uses Python identifier middleName
    __middleName = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'middleName'), 'middleName', '__httpwww_arin_netregrwscorev1_CTD_ANON__httpwww_arin_netregrwscorev1middleName', True, pyxb.utils.utility.Location('/Users/blb/Downloads/regrws-rnc/PocPayload.xsd', 82, 2), )

    
    middleName = property(__middleName.value, __middleName.set, None, None)

    
    # Element {http://www.arin.net/regrws/core/v1}phones uses Python identifier phones
    __phones = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'phones'), 'phones', '__httpwww_arin_netregrwscorev1_CTD_ANON__httpwww_arin_netregrwscorev1phones', True, pyxb.utils.utility.Location('/Users/blb/Downloads/regrws-rnc/PocPayload.xsd', 83, 2), )

    
    phones = property(__phones.value, __phones.set, None, None)

    
    # Element {http://www.arin.net/regrws/core/v1}handle uses Python identifier handle
    __handle = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'handle'), 'handle', '__httpwww_arin_netregrwscorev1_CTD_ANON__httpwww_arin_netregrwscorev1handle', True, pyxb.utils.utility.Location('/Users/blb/Downloads/regrws-rnc/PocPayload.xsd', 90, 2), )

    
    handle = property(__handle.value, __handle.set, None, None)

    
    # Element {http://www.arin.net/regrws/core/v1}postalCode uses Python identifier postalCode
    __postalCode = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'postalCode'), 'postalCode', '__httpwww_arin_netregrwscorev1_CTD_ANON__httpwww_arin_netregrwscorev1postalCode', True, pyxb.utils.utility.Location('/Users/blb/Downloads/regrws-rnc/PocPayload.xsd', 91, 2), )

    
    postalCode = property(__postalCode.value, __postalCode.set, None, None)

    
    # Element {http://www.arin.net/regrws/core/v1}comment uses Python identifier comment
    __comment = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'comment'), 'comment', '__httpwww_arin_netregrwscorev1_CTD_ANON__httpwww_arin_netregrwscorev1comment', True, pyxb.utils.utility.Location('/Users/blb/Downloads/regrws-rnc/PocPayload.xsd', 92, 2), )

    
    comment = property(__comment.value, __comment.set, None, None)

    
    # Element {http://www.arin.net/regrws/core/v1}registrationDate uses Python identifier registrationDate
    __registrationDate = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'registrationDate'), 'registrationDate', '__httpwww_arin_netregrwscorev1_CTD_ANON__httpwww_arin_netregrwscorev1registrationDate', True, pyxb.utils.utility.Location('/Users/blb/Downloads/regrws-rnc/PocPayload.xsd', 99, 2), )

    
    registrationDate = property(__registrationDate.value, __registrationDate.set, None, None)

    
    # Element {http://www.arin.net/regrws/core/v1}iso3166-2 uses Python identifier iso3166_2
    __iso3166_2 = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'iso3166-2'), 'iso3166_2', '__httpwww_arin_netregrwscorev1_CTD_ANON__httpwww_arin_netregrwscorev1iso3166_2', True, pyxb.utils.utility.Location('/Users/blb/Downloads/regrws-rnc/PocPayload.xsd', 100, 2), )

    
    iso3166_2 = property(__iso3166_2.value, __iso3166_2.set, None, None)

    
    # Element {http://www.arin.net/regrws/core/v1}streetAddress uses Python identifier streetAddress
    __streetAddress = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'streetAddress'), 'streetAddress', '__httpwww_arin_netregrwscorev1_CTD_ANON__httpwww_arin_netregrwscorev1streetAddress', True, pyxb.utils.utility.Location('/Users/blb/Downloads/regrws-rnc/PocPayload.xsd', 101, 2), )

    
    streetAddress = property(__streetAddress.value, __streetAddress.set, None, None)

    _HasWildcardElement = True
    _ElementMap.update({
        __city.name() : __city,
        __companyName.name() : __companyName,
        __contactType.name() : __contactType,
        __iso3166_1.name() : __iso3166_1,
        __emails.name() : __emails,
        __firstName.name() : __firstName,
        __lastModified.name() : __lastModified,
        __lastName.name() : __lastName,
        __middleName.name() : __middleName,
        __phones.name() : __phones,
        __handle.name() : __handle,
        __postalCode.name() : __postalCode,
        __comment.name() : __comment,
        __registrationDate.name() : __registrationDate,
        __iso3166_2.name() : __iso3166_2,
        __streetAddress.name() : __streetAddress
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
    _XSDLocation = pyxb.utils.utility.Location('/Users/blb/Downloads/regrws-rnc/PocPayload.xsd', 39, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.arin.net/regrws/core/v1}description uses Python identifier description
    __description = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'description'), 'description', '__httpwww_arin_netregrwscorev1_CTD_ANON_2_httpwww_arin_netregrwscorev1description', True, pyxb.utils.utility.Location('/Users/blb/Downloads/regrws-rnc/PocPayload.xsd', 113, 2), )

    
    description = property(__description.value, __description.set, None, None)

    
    # Element {http://www.arin.net/regrws/core/v1}code uses Python identifier code
    __code = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'code'), 'code', '__httpwww_arin_netregrwscorev1_CTD_ANON_2_httpwww_arin_netregrwscorev1code', True, pyxb.utils.utility.Location('/Users/blb/Downloads/regrws-rnc/PocPayload.xsd', 114, 2), )

    
    code = property(__code.value, __code.set, None, None)

    _ElementMap.update({
        __description.name() : __description,
        __code.name() : __code
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
    _XSDLocation = pyxb.utils.utility.Location('/Users/blb/Downloads/regrws-rnc/PocPayload.xsd', 62, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.arin.net/regrws/core/v1}code2 uses Python identifier code2
    __code2 = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'code2'), 'code2', '__httpwww_arin_netregrwscorev1_CTD_ANON_3_httpwww_arin_netregrwscorev1code2', True, pyxb.utils.utility.Location('/Users/blb/Downloads/regrws-rnc/PocPayload.xsd', 120, 2), )

    
    code2 = property(__code2.value, __code2.set, None, None)

    
    # Element {http://www.arin.net/regrws/core/v1}code3 uses Python identifier code3
    __code3 = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'code3'), 'code3', '__httpwww_arin_netregrwscorev1_CTD_ANON_3_httpwww_arin_netregrwscorev1code3', True, pyxb.utils.utility.Location('/Users/blb/Downloads/regrws-rnc/PocPayload.xsd', 121, 2), )

    
    code3 = property(__code3.value, __code3.set, None, None)

    
    # Element {http://www.arin.net/regrws/core/v1}name uses Python identifier name
    __name = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'name'), 'name', '__httpwww_arin_netregrwscorev1_CTD_ANON_3_httpwww_arin_netregrwscorev1name', True, pyxb.utils.utility.Location('/Users/blb/Downloads/regrws-rnc/PocPayload.xsd', 122, 2), )

    
    name = property(__name.value, __name.set, None, None)

    
    # Element {http://www.arin.net/regrws/core/v1}e164 uses Python identifier e164
    __e164 = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'e164'), 'e164', '__httpwww_arin_netregrwscorev1_CTD_ANON_3_httpwww_arin_netregrwscorev1e164', True, pyxb.utils.utility.Location('/Users/blb/Downloads/regrws-rnc/PocPayload.xsd', 123, 2), )

    
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
class CTD_ANON_4 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/Users/blb/Downloads/regrws-rnc/PocPayload.xsd', 73, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.arin.net/regrws/core/v1}email uses Python identifier email
    __email = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'email'), 'email', '__httpwww_arin_netregrwscorev1_CTD_ANON_4_httpwww_arin_netregrwscorev1email', True, pyxb.utils.utility.Location('/Users/blb/Downloads/regrws-rnc/PocPayload.xsd', 129, 2), )

    
    email = property(__email.value, __email.set, None, None)

    _ElementMap.update({
        __email.name() : __email
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
    _XSDLocation = pyxb.utils.utility.Location('/Users/blb/Downloads/regrws-rnc/PocPayload.xsd', 84, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.arin.net/regrws/core/v1}phone uses Python identifier phone
    __phone = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'phone'), 'phone', '__httpwww_arin_netregrwscorev1_CTD_ANON_5_httpwww_arin_netregrwscorev1phone', True, pyxb.utils.utility.Location('/Users/blb/Downloads/regrws-rnc/PocPayload.xsd', 3, 2), )

    
    phone = property(__phone.value, __phone.set, None, None)

    _ElementMap.update({
        __phone.name() : __phone
    })
    _AttributeMap.update({
        
    })



# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_6 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/Users/blb/Downloads/regrws-rnc/PocPayload.xsd', 93, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.arin.net/regrws/core/v1}line uses Python identifier line
    __line = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'line'), 'line', '__httpwww_arin_netregrwscorev1_CTD_ANON_6_httpwww_arin_netregrwscorev1line', True, pyxb.utils.utility.Location('/Users/blb/Downloads/regrws-rnc/PocPayload.xsd', 130, 2), )

    
    line = property(__line.value, __line.set, None, None)

    _ElementMap.update({
        __line.name() : __line
    })
    _AttributeMap.update({
        
    })



# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_7 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/Users/blb/Downloads/regrws-rnc/PocPayload.xsd', 102, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.arin.net/regrws/core/v1}line uses Python identifier line
    __line = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'line'), 'line', '__httpwww_arin_netregrwscorev1_CTD_ANON_7_httpwww_arin_netregrwscorev1line', True, pyxb.utils.utility.Location('/Users/blb/Downloads/regrws-rnc/PocPayload.xsd', 130, 2), )

    
    line = property(__line.value, __line.set, None, None)

    _ElementMap.update({
        __line.name() : __line
    })
    _AttributeMap.update({
        
    })



# Complex type [anonymous] with content type SIMPLE
class CTD_ANON_8 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type SIMPLE"""
    _TypeDefinition = pyxb.binding.datatypes.string
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/Users/blb/Downloads/regrws-rnc/PocPayload.xsd', 131, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.string
    
    # Attribute number uses Python identifier number
    __number = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'number'), 'number', '__httpwww_arin_netregrwscorev1_CTD_ANON_8_number', pyxb.binding.datatypes.integer, required=True)
    __number._DeclarationLocation = pyxb.utils.utility.Location('/Users/blb/Downloads/regrws-rnc/PocPayload.xsd', 134, 10)
    __number._UseLocation = pyxb.utils.utility.Location('/Users/blb/Downloads/regrws-rnc/PocPayload.xsd', 134, 10)
    
    number = property(__number.value, __number.set, None, None)

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __number.name() : __number
    })



extension = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'extension'), pyxb.binding.datatypes.string, location=pyxb.utils.utility.Location('/Users/blb/Downloads/regrws-rnc/PocPayload.xsd', 36, 2))
Namespace.addCategoryObject('elementBinding', extension.name().localName(), extension)

number = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'number'), pyxb.binding.datatypes.string, location=pyxb.utils.utility.Location('/Users/blb/Downloads/regrws-rnc/PocPayload.xsd', 37, 2))
Namespace.addCategoryObject('elementBinding', number.name().localName(), number)

city = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'city'), pyxb.binding.datatypes.string, location=pyxb.utils.utility.Location('/Users/blb/Downloads/regrws-rnc/PocPayload.xsd', 51, 2))
Namespace.addCategoryObject('elementBinding', city.name().localName(), city)

companyName = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'companyName'), pyxb.binding.datatypes.string, location=pyxb.utils.utility.Location('/Users/blb/Downloads/regrws-rnc/PocPayload.xsd', 52, 2))
Namespace.addCategoryObject('elementBinding', companyName.name().localName(), companyName)

firstName = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'firstName'), pyxb.binding.datatypes.string, location=pyxb.utils.utility.Location('/Users/blb/Downloads/regrws-rnc/PocPayload.xsd', 79, 2))
Namespace.addCategoryObject('elementBinding', firstName.name().localName(), firstName)

lastModified = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'lastModified'), pyxb.binding.datatypes.string, location=pyxb.utils.utility.Location('/Users/blb/Downloads/regrws-rnc/PocPayload.xsd', 80, 2))
Namespace.addCategoryObject('elementBinding', lastModified.name().localName(), lastModified)

lastName = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'lastName'), pyxb.binding.datatypes.string, location=pyxb.utils.utility.Location('/Users/blb/Downloads/regrws-rnc/PocPayload.xsd', 81, 2))
Namespace.addCategoryObject('elementBinding', lastName.name().localName(), lastName)

middleName = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'middleName'), pyxb.binding.datatypes.string, location=pyxb.utils.utility.Location('/Users/blb/Downloads/regrws-rnc/PocPayload.xsd', 82, 2))
Namespace.addCategoryObject('elementBinding', middleName.name().localName(), middleName)

handle = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'handle'), pyxb.binding.datatypes.string, location=pyxb.utils.utility.Location('/Users/blb/Downloads/regrws-rnc/PocPayload.xsd', 90, 2))
Namespace.addCategoryObject('elementBinding', handle.name().localName(), handle)

postalCode = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'postalCode'), pyxb.binding.datatypes.string, location=pyxb.utils.utility.Location('/Users/blb/Downloads/regrws-rnc/PocPayload.xsd', 91, 2))
Namespace.addCategoryObject('elementBinding', postalCode.name().localName(), postalCode)

registrationDate = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'registrationDate'), pyxb.binding.datatypes.string, location=pyxb.utils.utility.Location('/Users/blb/Downloads/regrws-rnc/PocPayload.xsd', 99, 2))
Namespace.addCategoryObject('elementBinding', registrationDate.name().localName(), registrationDate)

iso3166_2 = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'iso3166-2'), pyxb.binding.datatypes.string, location=pyxb.utils.utility.Location('/Users/blb/Downloads/regrws-rnc/PocPayload.xsd', 100, 2))
Namespace.addCategoryObject('elementBinding', iso3166_2.name().localName(), iso3166_2)

description = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'description'), pyxb.binding.datatypes.string, location=pyxb.utils.utility.Location('/Users/blb/Downloads/regrws-rnc/PocPayload.xsd', 113, 2))
Namespace.addCategoryObject('elementBinding', description.name().localName(), description)

code = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'code'), pyxb.binding.datatypes.string, location=pyxb.utils.utility.Location('/Users/blb/Downloads/regrws-rnc/PocPayload.xsd', 114, 2))
Namespace.addCategoryObject('elementBinding', code.name().localName(), code)

code2 = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'code2'), pyxb.binding.datatypes.string, location=pyxb.utils.utility.Location('/Users/blb/Downloads/regrws-rnc/PocPayload.xsd', 120, 2))
Namespace.addCategoryObject('elementBinding', code2.name().localName(), code2)

code3 = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'code3'), pyxb.binding.datatypes.string, location=pyxb.utils.utility.Location('/Users/blb/Downloads/regrws-rnc/PocPayload.xsd', 121, 2))
Namespace.addCategoryObject('elementBinding', code3.name().localName(), code3)

name = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'name'), pyxb.binding.datatypes.string, location=pyxb.utils.utility.Location('/Users/blb/Downloads/regrws-rnc/PocPayload.xsd', 122, 2))
Namespace.addCategoryObject('elementBinding', name.name().localName(), name)

e164 = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'e164'), pyxb.binding.datatypes.string, location=pyxb.utils.utility.Location('/Users/blb/Downloads/regrws-rnc/PocPayload.xsd', 123, 2))
Namespace.addCategoryObject('elementBinding', e164.name().localName(), e164)

email = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'email'), pyxb.binding.datatypes.string, location=pyxb.utils.utility.Location('/Users/blb/Downloads/regrws-rnc/PocPayload.xsd', 129, 2))
Namespace.addCategoryObject('elementBinding', email.name().localName(), email)

phone = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'phone'), CTD_ANON, location=pyxb.utils.utility.Location('/Users/blb/Downloads/regrws-rnc/PocPayload.xsd', 3, 2))
Namespace.addCategoryObject('elementBinding', phone.name().localName(), phone)

poc = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'poc'), CTD_ANON_, location=pyxb.utils.utility.Location('/Users/blb/Downloads/regrws-rnc/PocPayload.xsd', 13, 2))
Namespace.addCategoryObject('elementBinding', poc.name().localName(), poc)

type = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'type'), CTD_ANON_2, location=pyxb.utils.utility.Location('/Users/blb/Downloads/regrws-rnc/PocPayload.xsd', 38, 2))
Namespace.addCategoryObject('elementBinding', type.name().localName(), type)

contactType = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'contactType'), STD_ANON, location=pyxb.utils.utility.Location('/Users/blb/Downloads/regrws-rnc/PocPayload.xsd', 53, 2))
Namespace.addCategoryObject('elementBinding', contactType.name().localName(), contactType)

iso3166_1 = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'iso3166-1'), CTD_ANON_3, location=pyxb.utils.utility.Location('/Users/blb/Downloads/regrws-rnc/PocPayload.xsd', 61, 2))
Namespace.addCategoryObject('elementBinding', iso3166_1.name().localName(), iso3166_1)

emails = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'emails'), CTD_ANON_4, location=pyxb.utils.utility.Location('/Users/blb/Downloads/regrws-rnc/PocPayload.xsd', 72, 2))
Namespace.addCategoryObject('elementBinding', emails.name().localName(), emails)

phones = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'phones'), CTD_ANON_5, location=pyxb.utils.utility.Location('/Users/blb/Downloads/regrws-rnc/PocPayload.xsd', 83, 2))
Namespace.addCategoryObject('elementBinding', phones.name().localName(), phones)

comment = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'comment'), CTD_ANON_6, location=pyxb.utils.utility.Location('/Users/blb/Downloads/regrws-rnc/PocPayload.xsd', 92, 2))
Namespace.addCategoryObject('elementBinding', comment.name().localName(), comment)

streetAddress = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'streetAddress'), CTD_ANON_7, location=pyxb.utils.utility.Location('/Users/blb/Downloads/regrws-rnc/PocPayload.xsd', 101, 2))
Namespace.addCategoryObject('elementBinding', streetAddress.name().localName(), streetAddress)

line = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'line'), CTD_ANON_8, location=pyxb.utils.utility.Location('/Users/blb/Downloads/regrws-rnc/PocPayload.xsd', 130, 2))
Namespace.addCategoryObject('elementBinding', line.name().localName(), line)



CTD_ANON._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'extension'), pyxb.binding.datatypes.string, scope=CTD_ANON, location=pyxb.utils.utility.Location('/Users/blb/Downloads/regrws-rnc/PocPayload.xsd', 36, 2)))

CTD_ANON._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'number'), pyxb.binding.datatypes.string, scope=CTD_ANON, location=pyxb.utils.utility.Location('/Users/blb/Downloads/regrws-rnc/PocPayload.xsd', 37, 2)))

CTD_ANON._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'type'), CTD_ANON_2, scope=CTD_ANON, location=pyxb.utils.utility.Location('/Users/blb/Downloads/regrws-rnc/PocPayload.xsd', 38, 2)))

def _BuildAutomaton ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton
    del _BuildAutomaton
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location('/Users/blb/Downloads/regrws-rnc/PocPayload.xsd', 5, 6))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'extension')), pyxb.utils.utility.Location('/Users/blb/Downloads/regrws-rnc/PocPayload.xsd', 6, 8))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'number')), pyxb.utils.utility.Location('/Users/blb/Downloads/regrws-rnc/PocPayload.xsd', 7, 8))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'type')), pyxb.utils.utility.Location('/Users/blb/Downloads/regrws-rnc/PocPayload.xsd', 8, 8))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.WildcardUse(pyxb.binding.content.Wildcard(process_contents=pyxb.binding.content.Wildcard.PC_skip, namespace_constraint=pyxb.binding.content.Wildcard.NC_any), pyxb.utils.utility.Location('/Users/blb/Downloads/regrws-rnc/PocPayload.xsd', 48, 6))
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




CTD_ANON_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'city'), pyxb.binding.datatypes.string, scope=CTD_ANON_, location=pyxb.utils.utility.Location('/Users/blb/Downloads/regrws-rnc/PocPayload.xsd', 51, 2)))

CTD_ANON_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'companyName'), pyxb.binding.datatypes.string, scope=CTD_ANON_, location=pyxb.utils.utility.Location('/Users/blb/Downloads/regrws-rnc/PocPayload.xsd', 52, 2)))

CTD_ANON_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'contactType'), STD_ANON, scope=CTD_ANON_, location=pyxb.utils.utility.Location('/Users/blb/Downloads/regrws-rnc/PocPayload.xsd', 53, 2)))

CTD_ANON_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'iso3166-1'), CTD_ANON_3, scope=CTD_ANON_, location=pyxb.utils.utility.Location('/Users/blb/Downloads/regrws-rnc/PocPayload.xsd', 61, 2)))

CTD_ANON_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'emails'), CTD_ANON_4, scope=CTD_ANON_, location=pyxb.utils.utility.Location('/Users/blb/Downloads/regrws-rnc/PocPayload.xsd', 72, 2)))

CTD_ANON_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'firstName'), pyxb.binding.datatypes.string, scope=CTD_ANON_, location=pyxb.utils.utility.Location('/Users/blb/Downloads/regrws-rnc/PocPayload.xsd', 79, 2)))

CTD_ANON_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'lastModified'), pyxb.binding.datatypes.string, scope=CTD_ANON_, location=pyxb.utils.utility.Location('/Users/blb/Downloads/regrws-rnc/PocPayload.xsd', 80, 2)))

CTD_ANON_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'lastName'), pyxb.binding.datatypes.string, scope=CTD_ANON_, location=pyxb.utils.utility.Location('/Users/blb/Downloads/regrws-rnc/PocPayload.xsd', 81, 2)))

CTD_ANON_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'middleName'), pyxb.binding.datatypes.string, scope=CTD_ANON_, location=pyxb.utils.utility.Location('/Users/blb/Downloads/regrws-rnc/PocPayload.xsd', 82, 2)))

CTD_ANON_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'phones'), CTD_ANON_5, scope=CTD_ANON_, location=pyxb.utils.utility.Location('/Users/blb/Downloads/regrws-rnc/PocPayload.xsd', 83, 2)))

CTD_ANON_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'handle'), pyxb.binding.datatypes.string, scope=CTD_ANON_, location=pyxb.utils.utility.Location('/Users/blb/Downloads/regrws-rnc/PocPayload.xsd', 90, 2)))

CTD_ANON_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'postalCode'), pyxb.binding.datatypes.string, scope=CTD_ANON_, location=pyxb.utils.utility.Location('/Users/blb/Downloads/regrws-rnc/PocPayload.xsd', 91, 2)))

CTD_ANON_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'comment'), CTD_ANON_6, scope=CTD_ANON_, location=pyxb.utils.utility.Location('/Users/blb/Downloads/regrws-rnc/PocPayload.xsd', 92, 2)))

CTD_ANON_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'registrationDate'), pyxb.binding.datatypes.string, scope=CTD_ANON_, location=pyxb.utils.utility.Location('/Users/blb/Downloads/regrws-rnc/PocPayload.xsd', 99, 2)))

CTD_ANON_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'iso3166-2'), pyxb.binding.datatypes.string, scope=CTD_ANON_, location=pyxb.utils.utility.Location('/Users/blb/Downloads/regrws-rnc/PocPayload.xsd', 100, 2)))

CTD_ANON_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'streetAddress'), CTD_ANON_7, scope=CTD_ANON_, location=pyxb.utils.utility.Location('/Users/blb/Downloads/regrws-rnc/PocPayload.xsd', 101, 2)))

def _BuildAutomaton_ ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_
    del _BuildAutomaton_
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location('/Users/blb/Downloads/regrws-rnc/PocPayload.xsd', 15, 6))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'city')), pyxb.utils.utility.Location('/Users/blb/Downloads/regrws-rnc/PocPayload.xsd', 16, 8))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'companyName')), pyxb.utils.utility.Location('/Users/blb/Downloads/regrws-rnc/PocPayload.xsd', 17, 8))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'contactType')), pyxb.utils.utility.Location('/Users/blb/Downloads/regrws-rnc/PocPayload.xsd', 18, 8))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'iso3166-1')), pyxb.utils.utility.Location('/Users/blb/Downloads/regrws-rnc/PocPayload.xsd', 19, 8))
    st_3 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'emails')), pyxb.utils.utility.Location('/Users/blb/Downloads/regrws-rnc/PocPayload.xsd', 20, 8))
    st_4 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'firstName')), pyxb.utils.utility.Location('/Users/blb/Downloads/regrws-rnc/PocPayload.xsd', 21, 8))
    st_5 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'lastModified')), pyxb.utils.utility.Location('/Users/blb/Downloads/regrws-rnc/PocPayload.xsd', 22, 8))
    st_6 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_6)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'lastName')), pyxb.utils.utility.Location('/Users/blb/Downloads/regrws-rnc/PocPayload.xsd', 23, 8))
    st_7 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_7)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'middleName')), pyxb.utils.utility.Location('/Users/blb/Downloads/regrws-rnc/PocPayload.xsd', 24, 8))
    st_8 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_8)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'phones')), pyxb.utils.utility.Location('/Users/blb/Downloads/regrws-rnc/PocPayload.xsd', 25, 8))
    st_9 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_9)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'handle')), pyxb.utils.utility.Location('/Users/blb/Downloads/regrws-rnc/PocPayload.xsd', 26, 8))
    st_10 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_10)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'postalCode')), pyxb.utils.utility.Location('/Users/blb/Downloads/regrws-rnc/PocPayload.xsd', 27, 8))
    st_11 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_11)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'comment')), pyxb.utils.utility.Location('/Users/blb/Downloads/regrws-rnc/PocPayload.xsd', 28, 8))
    st_12 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_12)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'registrationDate')), pyxb.utils.utility.Location('/Users/blb/Downloads/regrws-rnc/PocPayload.xsd', 29, 8))
    st_13 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_13)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'iso3166-2')), pyxb.utils.utility.Location('/Users/blb/Downloads/regrws-rnc/PocPayload.xsd', 30, 8))
    st_14 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_14)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'streetAddress')), pyxb.utils.utility.Location('/Users/blb/Downloads/regrws-rnc/PocPayload.xsd', 31, 8))
    st_15 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_15)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.WildcardUse(pyxb.binding.content.Wildcard(process_contents=pyxb.binding.content.Wildcard.PC_skip, namespace_constraint=pyxb.binding.content.Wildcard.NC_any), pyxb.utils.utility.Location('/Users/blb/Downloads/regrws-rnc/PocPayload.xsd', 110, 6))
    st_16 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_16)
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
    st_16._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
CTD_ANON_._Automaton = _BuildAutomaton_()




CTD_ANON_2._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'description'), pyxb.binding.datatypes.string, scope=CTD_ANON_2, location=pyxb.utils.utility.Location('/Users/blb/Downloads/regrws-rnc/PocPayload.xsd', 113, 2)))

CTD_ANON_2._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'code'), pyxb.binding.datatypes.string, scope=CTD_ANON_2, location=pyxb.utils.utility.Location('/Users/blb/Downloads/regrws-rnc/PocPayload.xsd', 114, 2)))

def _BuildAutomaton_2 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_2
    del _BuildAutomaton_2
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location('/Users/blb/Downloads/regrws-rnc/PocPayload.xsd', 40, 6))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_2._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'description')), pyxb.utils.utility.Location('/Users/blb/Downloads/regrws-rnc/PocPayload.xsd', 41, 8))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_2._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'code')), pyxb.utils.utility.Location('/Users/blb/Downloads/regrws-rnc/PocPayload.xsd', 42, 8))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
CTD_ANON_2._Automaton = _BuildAutomaton_2()




CTD_ANON_3._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'code2'), pyxb.binding.datatypes.string, scope=CTD_ANON_3, location=pyxb.utils.utility.Location('/Users/blb/Downloads/regrws-rnc/PocPayload.xsd', 120, 2)))

CTD_ANON_3._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'code3'), pyxb.binding.datatypes.string, scope=CTD_ANON_3, location=pyxb.utils.utility.Location('/Users/blb/Downloads/regrws-rnc/PocPayload.xsd', 121, 2)))

CTD_ANON_3._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'name'), pyxb.binding.datatypes.string, scope=CTD_ANON_3, location=pyxb.utils.utility.Location('/Users/blb/Downloads/regrws-rnc/PocPayload.xsd', 122, 2)))

CTD_ANON_3._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'e164'), pyxb.binding.datatypes.string, scope=CTD_ANON_3, location=pyxb.utils.utility.Location('/Users/blb/Downloads/regrws-rnc/PocPayload.xsd', 123, 2)))

def _BuildAutomaton_3 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_3
    del _BuildAutomaton_3
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location('/Users/blb/Downloads/regrws-rnc/PocPayload.xsd', 63, 6))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_3._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'code2')), pyxb.utils.utility.Location('/Users/blb/Downloads/regrws-rnc/PocPayload.xsd', 64, 8))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_3._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'code3')), pyxb.utils.utility.Location('/Users/blb/Downloads/regrws-rnc/PocPayload.xsd', 65, 8))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_3._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'name')), pyxb.utils.utility.Location('/Users/blb/Downloads/regrws-rnc/PocPayload.xsd', 66, 8))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_3._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'e164')), pyxb.utils.utility.Location('/Users/blb/Downloads/regrws-rnc/PocPayload.xsd', 67, 8))
    st_3 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.WildcardUse(pyxb.binding.content.Wildcard(process_contents=pyxb.binding.content.Wildcard.PC_skip, namespace_constraint=pyxb.binding.content.Wildcard.NC_any), pyxb.utils.utility.Location('/Users/blb/Downloads/regrws-rnc/PocPayload.xsd', 126, 6))
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
CTD_ANON_3._Automaton = _BuildAutomaton_3()




CTD_ANON_4._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'email'), pyxb.binding.datatypes.string, scope=CTD_ANON_4, location=pyxb.utils.utility.Location('/Users/blb/Downloads/regrws-rnc/PocPayload.xsd', 129, 2)))

def _BuildAutomaton_4 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_4
    del _BuildAutomaton_4
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location('/Users/blb/Downloads/regrws-rnc/PocPayload.xsd', 75, 8))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_4._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'email')), pyxb.utils.utility.Location('/Users/blb/Downloads/regrws-rnc/PocPayload.xsd', 75, 8))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
CTD_ANON_4._Automaton = _BuildAutomaton_4()




CTD_ANON_5._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'phone'), CTD_ANON, scope=CTD_ANON_5, location=pyxb.utils.utility.Location('/Users/blb/Downloads/regrws-rnc/PocPayload.xsd', 3, 2)))

def _BuildAutomaton_5 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_5
    del _BuildAutomaton_5
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location('/Users/blb/Downloads/regrws-rnc/PocPayload.xsd', 86, 8))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_5._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'phone')), pyxb.utils.utility.Location('/Users/blb/Downloads/regrws-rnc/PocPayload.xsd', 86, 8))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
CTD_ANON_5._Automaton = _BuildAutomaton_5()




CTD_ANON_6._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'line'), CTD_ANON_8, scope=CTD_ANON_6, location=pyxb.utils.utility.Location('/Users/blb/Downloads/regrws-rnc/PocPayload.xsd', 130, 2)))

def _BuildAutomaton_6 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_6
    del _BuildAutomaton_6
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location('/Users/blb/Downloads/regrws-rnc/PocPayload.xsd', 95, 8))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_6._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'line')), pyxb.utils.utility.Location('/Users/blb/Downloads/regrws-rnc/PocPayload.xsd', 95, 8))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
CTD_ANON_6._Automaton = _BuildAutomaton_6()




CTD_ANON_7._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'line'), CTD_ANON_8, scope=CTD_ANON_7, location=pyxb.utils.utility.Location('/Users/blb/Downloads/regrws-rnc/PocPayload.xsd', 130, 2)))

def _BuildAutomaton_7 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_7
    del _BuildAutomaton_7
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location('/Users/blb/Downloads/regrws-rnc/PocPayload.xsd', 104, 8))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_7._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'line')), pyxb.utils.utility.Location('/Users/blb/Downloads/regrws-rnc/PocPayload.xsd', 104, 8))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
CTD_ANON_7._Automaton = _BuildAutomaton_7()

