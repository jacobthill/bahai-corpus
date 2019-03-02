### Dates

If a source mentions a date, it should be tagged as <date when="2001">The year 2001</date>. For more examples, see https://www.tei-c.org/release/doc/tei-p5-doc/en/html/examples-date.html

### Events

If a source mentions an historical event this should be recorded. The event id should always be referenced and the type specified as event (which simply means that this string of text is referring to an event) (e.g. <rs key="unique-id” type=“event”></rs>). Note: prophecies should not be tagged as 'event'. They have their own 'prophecy' tag.

### People

If a source mentions a person this should be recorded. The event id should always be referenced and the type specified as person (which simply means that this string of text is referring to a person) (e.g. <rs key="unique-id" type=“person”></rs>).

### Places

If a source mentions a place this should be recorded. The event id should always be referenced and the type specified as place (which simply means that this string of text is referring to a place) (e.g. <rs rkey="unique-id" type=“place”></rs>). Non-literal places should be recorded as well. 

### Prayers

Prayers should be marked as such, even when contained in a larger document that is not a prayer.

### Prophecies

If a source mentions an event that has not yet happened at the time of writing this should be recorded. The event id should always be referenced and the type specified as prophecy (which simply means that this string of text is referring to a prophecy) (e.g. <rs key="unique-id" type=“prophecy”></rs>). This will distinguish prophecies from historical events thereby avoiding errors when using events for dating tablets.

### Text Reuse

Bahá'u'lláh usually does not explicitly cite His quotes, so rather than using <cit>, create a bibliographic record in a listBibl in the teiHeader, and in the text encode it as: 
<quote source="#bibl-123"><!-- quoted text --></quote>


### Works

If a source mentions a work this should be recorded. The event id should always be referenced and the type specified as work (which simply means that this string of text is referring to another work) (e.g. <rs key="unique-id" type=“work”></rs>).


